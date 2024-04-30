import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.RptDataDefSvc
// Description: Business Logic (create/update/delete...) for Report Data Definitions
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get RptDataDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptDataDefs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptDataDefRow
   */  
export function get_RptDataDefs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataDefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptDataDefs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptDataDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptDataDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptDataDefs(requestBody:Ice_Tablesets_RptDataDefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataDefs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptDataDef item
   Description: Calls GetByID to retrieve the RptDataDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptDataDef
      @param RptDefID Desc: RptDefID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptDataDefRow
   */  
export function get_RptDataDefs_RptDefID(RptDefID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptDataDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataDefs(" + RptDefID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptDataDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptDataDef for the service
   Description: Calls UpdateExt to update RptDataDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptDataDef
      @param RptDefID Desc: RptDefID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptDataDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptDataDefs_RptDefID(RptDefID:string, requestBody:Ice_Tablesets_RptDataDefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataDefs(" + RptDefID + ")", {
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
   Summary: Call UpdateExt to delete RptDataDef item
   Description: Call UpdateExt to delete RptDataDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptDataDef
      @param RptDefID Desc: RptDefID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptDataDefs_RptDefID(RptDefID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataDefs(" + RptDefID + ")", {
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
   Description: Get RptTables items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptTables
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptTableRow
   */  
export function get_RptTables(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptTables
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptTables(requestBody:Ice_Tablesets_RptTableRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptTable item
   Description: Calls GetByID to retrieve the RptTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptTable
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptTableRow
   */  
export function get_RptTables_RptDefID_RptTableID(RptDefID:string, RptTableID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptTable for the service
   Description: Calls UpdateExt to update RptTable. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptTable
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptTables_RptDefID_RptTableID(RptDefID:string, RptTableID:string, requestBody:Ice_Tablesets_RptTableRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")", {
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
   Summary: Call UpdateExt to delete RptTable item
   Description: Call UpdateExt to delete RptTable item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptTable
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptTables_RptDefID_RptTableID(RptDefID:string, RptTableID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")", {
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
   Description: Get RptCalcFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptCalcFields1
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCalcFieldRow
   */  
export function get_RptTables_RptDefID_RptTableID_RptCalcFields(RptDefID:string, RptTableID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCalcFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptCalcFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCalcFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RptCalcField item
   Description: Calls GetByID to retrieve the RptCalcField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCalcField1
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptCalcFieldRow
   */  
export function get_RptTables_RptDefID_RptTableID_RptCalcFields_RptDefID_RptTableID_SystemCode_ZDataTableID_FieldName(RptDefID:string, RptTableID:string, SystemCode:string, ZDataTableID:string, FieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptCalcFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptCalcFields(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptCalcFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RptExcludes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptExcludes1
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptExcludeRow
   */  
export function get_RptTables_RptDefID_RptTableID_RptExcludes(RptDefID:string, RptTableID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptExcludeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptExcludes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptExcludeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RptExclude item
   Description: Calls GetByID to retrieve the RptExclude item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptExclude1
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param ZFieldName Desc: ZFieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptExcludeRow
   */  
export function get_RptTables_RptDefID_RptTableID_RptExcludes_RptDefID_RptTableID_SystemCode_ZDataTableID_ZFieldName(RptDefID:string, RptTableID:string, SystemCode:string, ZDataTableID:string, ZFieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptExcludeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptExcludes(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + ZFieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptExcludeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RptLinkTables items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptLinkTables1
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptLinkTableRow
   */  
export function get_RptTables_RptDefID_RptTableID_RptLinkTables(RptDefID:string, RptTableID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLinkTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptLinkTables", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLinkTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RptLinkTable item
   Description: Calls GetByID to retrieve the RptLinkTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptLinkTable1
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param RptLinkID Desc: RptLinkID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param ZLookupID Desc: ZLookupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptLinkTableRow
   */  
export function get_RptTables_RptDefID_RptTableID_RptLinkTables_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID(RptDefID:string, RptTableID:string, RptLinkID:string, SystemCode:string, ZDataTableID:string, ZLookupID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptLinkTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptLinkTables(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptLinkTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RptWhereItems items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptWhereItems1
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptWhereItemRow
   */  
export function get_RptTables_RptDefID_RptTableID_RptWhereItems(RptDefID:string, RptTableID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptWhereItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptWhereItems", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptWhereItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RptWhereItem item
   Description: Calls GetByID to retrieve the RptWhereItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptWhereItem1
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptWhereItemRow
   */  
export function get_RptTables_RptDefID_RptTableID_RptWhereItems_RptDefID_RptTableID_SystemCode_ZDataTableID_Seq(RptDefID:string, RptTableID:string, SystemCode:string, ZDataTableID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptWhereItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptTables(" + RptDefID + "," + RptTableID + ")/RptWhereItems(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptWhereItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RptCalcFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptCalcFields
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCalcFieldRow
   */  
export function get_RptCalcFields(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCalcFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCalcFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCalcFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptCalcFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptCalcFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptCalcFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptCalcFields(requestBody:Ice_Tablesets_RptCalcFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCalcFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptCalcField item
   Description: Calls GetByID to retrieve the RptCalcField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCalcField
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptCalcFieldRow
   */  
export function get_RptCalcFields_RptDefID_RptTableID_SystemCode_ZDataTableID_FieldName(RptDefID:string, RptTableID:string, SystemCode:string, ZDataTableID:string, FieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptCalcFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCalcFields(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptCalcFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptCalcField for the service
   Description: Calls UpdateExt to update RptCalcField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptCalcField
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptCalcFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptCalcFields_RptDefID_RptTableID_SystemCode_ZDataTableID_FieldName(RptDefID:string, RptTableID:string, SystemCode:string, ZDataTableID:string, FieldName:string, requestBody:Ice_Tablesets_RptCalcFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCalcFields(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + FieldName + ")", {
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
   Summary: Call UpdateExt to delete RptCalcField item
   Description: Call UpdateExt to delete RptCalcField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptCalcField
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptCalcFields_RptDefID_RptTableID_SystemCode_ZDataTableID_FieldName(RptDefID:string, RptTableID:string, SystemCode:string, ZDataTableID:string, FieldName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCalcFields(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + FieldName + ")", {
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
   Description: Get RptExcludes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptExcludes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptExcludeRow
   */  
export function get_RptExcludes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptExcludeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptExcludes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptExcludeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptExcludes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptExcludeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptExcludeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptExcludes(requestBody:Ice_Tablesets_RptExcludeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptExcludes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptExclude item
   Description: Calls GetByID to retrieve the RptExclude item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptExclude
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param ZFieldName Desc: ZFieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptExcludeRow
   */  
export function get_RptExcludes_RptDefID_RptTableID_SystemCode_ZDataTableID_ZFieldName(RptDefID:string, RptTableID:string, SystemCode:string, ZDataTableID:string, ZFieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptExcludeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptExcludes(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + ZFieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptExcludeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptExclude for the service
   Description: Calls UpdateExt to update RptExclude. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptExclude
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param ZFieldName Desc: ZFieldName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptExcludeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptExcludes_RptDefID_RptTableID_SystemCode_ZDataTableID_ZFieldName(RptDefID:string, RptTableID:string, SystemCode:string, ZDataTableID:string, ZFieldName:string, requestBody:Ice_Tablesets_RptExcludeRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptExcludes(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + ZFieldName + ")", {
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
   Summary: Call UpdateExt to delete RptExclude item
   Description: Call UpdateExt to delete RptExclude item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptExclude
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param ZFieldName Desc: ZFieldName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptExcludes_RptDefID_RptTableID_SystemCode_ZDataTableID_ZFieldName(RptDefID:string, RptTableID:string, SystemCode:string, ZDataTableID:string, ZFieldName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptExcludes(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + ZFieldName + ")", {
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
   Description: Get RptLinkTables items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptLinkTables
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptLinkTableRow
   */  
export function get_RptLinkTables(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLinkTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLinkTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptLinkTables
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptLinkTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptLinkTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptLinkTables(requestBody:Ice_Tablesets_RptLinkTableRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptLinkTable item
   Description: Calls GetByID to retrieve the RptLinkTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptLinkTable
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param RptLinkID Desc: RptLinkID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param ZLookupID Desc: ZLookupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptLinkTableRow
   */  
export function get_RptLinkTables_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID(RptDefID:string, RptTableID:string, RptLinkID:string, SystemCode:string, ZDataTableID:string, ZLookupID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptLinkTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptLinkTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptLinkTable for the service
   Description: Calls UpdateExt to update RptLinkTable. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptLinkTable
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param RptLinkID Desc: RptLinkID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param ZLookupID Desc: ZLookupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptLinkTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptLinkTables_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID(RptDefID:string, RptTableID:string, RptLinkID:string, SystemCode:string, ZDataTableID:string, ZLookupID:string, requestBody:Ice_Tablesets_RptLinkTableRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + ")", {
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
   Summary: Call UpdateExt to delete RptLinkTable item
   Description: Call UpdateExt to delete RptLinkTable item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptLinkTable
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param RptLinkID Desc: RptLinkID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param ZLookupID Desc: ZLookupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptLinkTables_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID(RptDefID:string, RptTableID:string, RptLinkID:string, SystemCode:string, ZDataTableID:string, ZLookupID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + ")", {
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
   Description: Get RptLinkFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptLinkFields1
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param RptLinkID Desc: RptLinkID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param ZLookupID Desc: ZLookupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptLinkFieldRow
   */  
export function get_RptLinkTables_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID_RptLinkFields(RptDefID:string, RptTableID:string, RptLinkID:string, SystemCode:string, ZDataTableID:string, ZLookupID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLinkFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + ")/RptLinkFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLinkFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RptLinkField item
   Description: Calls GetByID to retrieve the RptLinkField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptLinkField1
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param RptLinkID Desc: RptLinkID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param ZLookupID Desc: ZLookupID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptLinkFieldRow
   */  
export function get_RptLinkTables_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID_RptLinkFields_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID_FieldName(RptDefID:string, RptTableID:string, RptLinkID:string, SystemCode:string, ZDataTableID:string, ZLookupID:string, FieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptLinkFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkTables(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + ")/RptLinkFields(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptLinkFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RptLinkFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptLinkFields
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptLinkFieldRow
   */  
export function get_RptLinkFields(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLinkFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLinkFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptLinkFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptLinkFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptLinkFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptLinkFields(requestBody:Ice_Tablesets_RptLinkFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptLinkField item
   Description: Calls GetByID to retrieve the RptLinkField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptLinkField
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param RptLinkID Desc: RptLinkID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param ZLookupID Desc: ZLookupID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptLinkFieldRow
   */  
export function get_RptLinkFields_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID_FieldName(RptDefID:string, RptTableID:string, RptLinkID:string, SystemCode:string, ZDataTableID:string, ZLookupID:string, FieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptLinkFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkFields(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptLinkFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptLinkField for the service
   Description: Calls UpdateExt to update RptLinkField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptLinkField
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param RptLinkID Desc: RptLinkID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param ZLookupID Desc: ZLookupID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptLinkFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptLinkFields_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID_FieldName(RptDefID:string, RptTableID:string, RptLinkID:string, SystemCode:string, ZDataTableID:string, ZLookupID:string, FieldName:string, requestBody:Ice_Tablesets_RptLinkFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkFields(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + "," + FieldName + ")", {
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
   Summary: Call UpdateExt to delete RptLinkField item
   Description: Call UpdateExt to delete RptLinkField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptLinkField
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param RptLinkID Desc: RptLinkID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param ZLookupID Desc: ZLookupID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptLinkFields_RptDefID_RptTableID_RptLinkID_SystemCode_ZDataTableID_ZLookupID_FieldName(RptDefID:string, RptTableID:string, RptLinkID:string, SystemCode:string, ZDataTableID:string, ZLookupID:string, FieldName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLinkFields(" + RptDefID + "," + RptTableID + "," + RptLinkID + "," + SystemCode + "," + ZDataTableID + "," + ZLookupID + "," + FieldName + ")", {
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
   Description: Get RptWhereItems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptWhereItems
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptWhereItemRow
   */  
export function get_RptWhereItems(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptWhereItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptWhereItems", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptWhereItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptWhereItems
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptWhereItemRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptWhereItemRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptWhereItems(requestBody:Ice_Tablesets_RptWhereItemRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptWhereItems", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptWhereItem item
   Description: Calls GetByID to retrieve the RptWhereItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptWhereItem
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptWhereItemRow
   */  
export function get_RptWhereItems_RptDefID_RptTableID_SystemCode_ZDataTableID_Seq(RptDefID:string, RptTableID:string, SystemCode:string, ZDataTableID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptWhereItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptWhereItems(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptWhereItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptWhereItem for the service
   Description: Calls UpdateExt to update RptWhereItem. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptWhereItem
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptWhereItemRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptWhereItems_RptDefID_RptTableID_SystemCode_ZDataTableID_Seq(RptDefID:string, RptTableID:string, SystemCode:string, ZDataTableID:string, Seq:string, requestBody:Ice_Tablesets_RptWhereItemRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptWhereItems(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete RptWhereItem item
   Description: Call UpdateExt to delete RptWhereItem item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptWhereItem
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param ZDataTableID Desc: ZDataTableID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptWhereItems_RptDefID_RptTableID_SystemCode_ZDataTableID_Seq(RptDefID:string, RptTableID:string, SystemCode:string, ZDataTableID:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptWhereItems(" + RptDefID + "," + RptTableID + "," + SystemCode + "," + ZDataTableID + "," + Seq + ")", {
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
   Description: Get RptCriteriaSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptCriteriaSets
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCriteriaSetRow
   */  
export function get_RptCriteriaSets(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaSets", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptCriteriaSets
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptCriteriaSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptCriteriaSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptCriteriaSets(requestBody:Ice_Tablesets_RptCriteriaSetRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaSets", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptCriteriaSet item
   Description: Calls GetByID to retrieve the RptCriteriaSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCriteriaSet
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptCriteriaSetRow
   */  
export function get_RptCriteriaSets_RptDefID_RptCriteriaSetID(RptDefID:string, RptCriteriaSetID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptCriteriaSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaSets(" + RptDefID + "," + RptCriteriaSetID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptCriteriaSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptCriteriaSet for the service
   Description: Calls UpdateExt to update RptCriteriaSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptCriteriaSet
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptCriteriaSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptCriteriaSets_RptDefID_RptCriteriaSetID(RptDefID:string, RptCriteriaSetID:string, requestBody:Ice_Tablesets_RptCriteriaSetRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaSets(" + RptDefID + "," + RptCriteriaSetID + ")", {
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
   Summary: Call UpdateExt to delete RptCriteriaSet item
   Description: Call UpdateExt to delete RptCriteriaSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptCriteriaSet
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptCriteriaSets_RptDefID_RptCriteriaSetID(RptDefID:string, RptCriteriaSetID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaSets(" + RptDefID + "," + RptCriteriaSetID + ")", {
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
   Description: Get RptCriteriaFilters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptCriteriaFilters
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCriteriaFilterRow
   */  
export function get_RptCriteriaFilters(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaFilters", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptCriteriaFilters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptCriteriaFilterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptCriteriaFilterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptCriteriaFilters(requestBody:Ice_Tablesets_RptCriteriaFilterRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaFilters", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptCriteriaFilter item
   Description: Calls GetByID to retrieve the RptCriteriaFilter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCriteriaFilter
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param FilterID Desc: FilterID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptCriteriaFilterRow
   */  
export function get_RptCriteriaFilters_RptDefID_RptCriteriaSetID_FilterID(RptDefID:string, RptCriteriaSetID:string, FilterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptCriteriaFilterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaFilters(" + RptDefID + "," + RptCriteriaSetID + "," + FilterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptCriteriaFilterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptCriteriaFilter for the service
   Description: Calls UpdateExt to update RptCriteriaFilter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptCriteriaFilter
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param FilterID Desc: FilterID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptCriteriaFilterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptCriteriaFilters_RptDefID_RptCriteriaSetID_FilterID(RptDefID:string, RptCriteriaSetID:string, FilterID:string, requestBody:Ice_Tablesets_RptCriteriaFilterRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaFilters(" + RptDefID + "," + RptCriteriaSetID + "," + FilterID + ")", {
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
   Summary: Call UpdateExt to delete RptCriteriaFilter item
   Description: Call UpdateExt to delete RptCriteriaFilter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptCriteriaFilter
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param FilterID Desc: FilterID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptCriteriaFilters_RptDefID_RptCriteriaSetID_FilterID(RptDefID:string, RptCriteriaSetID:string, FilterID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaFilters(" + RptDefID + "," + RptCriteriaSetID + "," + FilterID + ")", {
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
   Description: Get RptCriteriaMappings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptCriteriaMappings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCriteriaMappingRow
   */  
export function get_RptCriteriaMappings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaMappingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaMappings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaMappingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptCriteriaMappings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptCriteriaMappingRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptCriteriaMappingRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptCriteriaMappings(requestBody:Ice_Tablesets_RptCriteriaMappingRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaMappings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptCriteriaMapping item
   Description: Calls GetByID to retrieve the RptCriteriaMapping item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCriteriaMapping
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptCriteriaMappingRow
   */  
export function get_RptCriteriaMappings_RptDefID_RptCriteriaSetID_RptTableID_ParameterID(RptDefID:string, RptCriteriaSetID:string, RptTableID:string, ParameterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptCriteriaMappingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaMappings(" + RptDefID + "," + RptCriteriaSetID + "," + RptTableID + "," + ParameterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptCriteriaMappingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptCriteriaMapping for the service
   Description: Calls UpdateExt to update RptCriteriaMapping. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptCriteriaMapping
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptCriteriaMappingRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptCriteriaMappings_RptDefID_RptCriteriaSetID_RptTableID_ParameterID(RptDefID:string, RptCriteriaSetID:string, RptTableID:string, ParameterID:string, requestBody:Ice_Tablesets_RptCriteriaMappingRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaMappings(" + RptDefID + "," + RptCriteriaSetID + "," + RptTableID + "," + ParameterID + ")", {
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
   Summary: Call UpdateExt to delete RptCriteriaMapping item
   Description: Call UpdateExt to delete RptCriteriaMapping item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptCriteriaMapping
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptCriteriaMappings_RptDefID_RptCriteriaSetID_RptTableID_ParameterID(RptDefID:string, RptCriteriaSetID:string, RptTableID:string, ParameterID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaMappings(" + RptDefID + "," + RptCriteriaSetID + "," + RptTableID + "," + ParameterID + ")", {
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
   Description: Get RptCriteriaPrompts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptCriteriaPrompts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCriteriaPromptRow
   */  
export function get_RptCriteriaPrompts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaPromptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPrompts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaPromptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptCriteriaPrompts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptCriteriaPromptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptCriteriaPromptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptCriteriaPrompts(requestBody:Ice_Tablesets_RptCriteriaPromptRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPrompts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptCriteriaPrompt item
   Description: Calls GetByID to retrieve the RptCriteriaPrompt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCriteriaPrompt
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param PromptID Desc: PromptID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptCriteriaPromptRow
   */  
export function get_RptCriteriaPrompts_RptDefID_RptCriteriaSetID_PromptID(RptDefID:string, RptCriteriaSetID:string, PromptID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptCriteriaPromptRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPrompts(" + RptDefID + "," + RptCriteriaSetID + "," + PromptID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptCriteriaPromptRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptCriteriaPrompt for the service
   Description: Calls UpdateExt to update RptCriteriaPrompt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptCriteriaPrompt
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param PromptID Desc: PromptID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptCriteriaPromptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptCriteriaPrompts_RptDefID_RptCriteriaSetID_PromptID(RptDefID:string, RptCriteriaSetID:string, PromptID:string, requestBody:Ice_Tablesets_RptCriteriaPromptRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPrompts(" + RptDefID + "," + RptCriteriaSetID + "," + PromptID + ")", {
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
   Summary: Call UpdateExt to delete RptCriteriaPrompt item
   Description: Call UpdateExt to delete RptCriteriaPrompt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptCriteriaPrompt
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param PromptID Desc: PromptID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptCriteriaPrompts_RptDefID_RptCriteriaSetID_PromptID(RptDefID:string, RptCriteriaSetID:string, PromptID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPrompts(" + RptDefID + "," + RptCriteriaSetID + "," + PromptID + ")", {
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
   Description: Get RptCriteriaPromptValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptCriteriaPromptValues
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptCriteriaPromptValueRow
   */  
export function get_RptCriteriaPromptValues(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaPromptValueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPromptValues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaPromptValueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptCriteriaPromptValues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptCriteriaPromptValueRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptCriteriaPromptValueRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptCriteriaPromptValues(requestBody:Ice_Tablesets_RptCriteriaPromptValueRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPromptValues", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptCriteriaPromptValue item
   Description: Calls GetByID to retrieve the RptCriteriaPromptValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptCriteriaPromptValue
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param PromptID Desc: PromptID   Required: True
      @param ItemID Desc: ItemID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptCriteriaPromptValueRow
   */  
export function get_RptCriteriaPromptValues_RptDefID_RptCriteriaSetID_PromptID_ItemID(RptDefID:string, RptCriteriaSetID:string, PromptID:string, ItemID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptCriteriaPromptValueRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPromptValues(" + RptDefID + "," + RptCriteriaSetID + "," + PromptID + "," + ItemID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptCriteriaPromptValueRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptCriteriaPromptValue for the service
   Description: Calls UpdateExt to update RptCriteriaPromptValue. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptCriteriaPromptValue
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param PromptID Desc: PromptID   Required: True
      @param ItemID Desc: ItemID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptCriteriaPromptValueRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptCriteriaPromptValues_RptDefID_RptCriteriaSetID_PromptID_ItemID(RptDefID:string, RptCriteriaSetID:string, PromptID:string, ItemID:string, requestBody:Ice_Tablesets_RptCriteriaPromptValueRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPromptValues(" + RptDefID + "," + RptCriteriaSetID + "," + PromptID + "," + ItemID + ")", {
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
   Summary: Call UpdateExt to delete RptCriteriaPromptValue item
   Description: Call UpdateExt to delete RptCriteriaPromptValue item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptCriteriaPromptValue
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param PromptID Desc: PromptID   Required: True
      @param ItemID Desc: ItemID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptCriteriaPromptValues_RptDefID_RptCriteriaSetID_PromptID_ItemID(RptDefID:string, RptCriteriaSetID:string, PromptID:string, ItemID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptCriteriaPromptValues(" + RptDefID + "," + RptCriteriaSetID + "," + PromptID + "," + ItemID + ")", {
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
   Description: Get RptRelations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptRelations
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptRelationRow
   */  
export function get_RptRelations(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptRelationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptRelationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptRelations
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptRelationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptRelationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptRelations(requestBody:Ice_Tablesets_RptRelationRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptRelation item
   Description: Calls GetByID to retrieve the RptRelation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptRelation
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptRelationRow
   */  
export function get_RptRelations_RptDefID_RelationID(RptDefID:string, RelationID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptRelationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations(" + RptDefID + "," + RelationID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptRelationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptRelation for the service
   Description: Calls UpdateExt to update RptRelation. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptRelation
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptRelationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptRelations_RptDefID_RelationID(RptDefID:string, RelationID:string, requestBody:Ice_Tablesets_RptRelationRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations(" + RptDefID + "," + RelationID + ")", {
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
   Summary: Call UpdateExt to delete RptRelation item
   Description: Call UpdateExt to delete RptRelation item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptRelation
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptRelations_RptDefID_RelationID(RptDefID:string, RelationID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations(" + RptDefID + "," + RelationID + ")", {
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
   Description: Get RptRelationFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptRelationFields1
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptRelationFieldRow
   */  
export function get_RptRelations_RptDefID_RelationID_RptRelationFields(RptDefID:string, RelationID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptRelationFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations(" + RptDefID + "," + RelationID + ")/RptRelationFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptRelationFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RptRelationField item
   Description: Calls GetByID to retrieve the RptRelationField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptRelationField1
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptRelationFieldRow
   */  
export function get_RptRelations_RptDefID_RelationID_RptRelationFields_RptDefID_RelationID_Seq(RptDefID:string, RelationID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptRelationFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelations(" + RptDefID + "," + RelationID + ")/RptRelationFields(" + RptDefID + "," + RelationID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptRelationFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RptRelationFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptRelationFields
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptRelationFieldRow
   */  
export function get_RptRelationFields(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptRelationFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelationFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptRelationFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptRelationFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptRelationFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptRelationFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptRelationFields(requestBody:Ice_Tablesets_RptRelationFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelationFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptRelationField item
   Description: Calls GetByID to retrieve the RptRelationField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptRelationField
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptRelationFieldRow
   */  
export function get_RptRelationFields_RptDefID_RelationID_Seq(RptDefID:string, RelationID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptRelationFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelationFields(" + RptDefID + "," + RelationID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptRelationFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptRelationField for the service
   Description: Calls UpdateExt to update RptRelationField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptRelationField
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptRelationFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptRelationFields_RptDefID_RelationID_Seq(RptDefID:string, RelationID:string, Seq:string, requestBody:Ice_Tablesets_RptRelationFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelationFields(" + RptDefID + "," + RelationID + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete RptRelationField item
   Description: Call UpdateExt to delete RptRelationField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptRelationField
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptRelationFields_RptDefID_RelationID_Seq(RptDefID:string, RelationID:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptRelationFields(" + RptDefID + "," + RelationID + "," + Seq + ")", {
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
   Description: Get RptLiterals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptLiterals
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptLiteralsRow
   */  
export function get_RptLiterals(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLiteralsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLiterals", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLiteralsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptLiterals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptLiteralsRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptLiteralsRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptLiterals(requestBody:Ice_Tablesets_RptLiteralsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLiterals", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptLiteral item
   Description: Calls GetByID to retrieve the RptLiteral item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptLiteral
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param LiteralName Desc: LiteralName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptLiteralsRow
   */  
export function get_RptLiterals_RptDefID_LiteralName(RptDefID:string, LiteralName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptLiteralsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLiterals(" + RptDefID + "," + LiteralName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptLiteralsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptLiteral for the service
   Description: Calls UpdateExt to update RptLiteral. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptLiteral
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param LiteralName Desc: LiteralName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptLiteralsRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptLiterals_RptDefID_LiteralName(RptDefID:string, LiteralName:string, requestBody:Ice_Tablesets_RptLiteralsRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLiterals(" + RptDefID + "," + LiteralName + ")", {
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
   Summary: Call UpdateExt to delete RptLiteral item
   Description: Call UpdateExt to delete RptLiteral item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptLiteral
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param LiteralName Desc: LiteralName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptLiterals_RptDefID_LiteralName(RptDefID:string, LiteralName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptLiterals(" + RptDefID + "," + LiteralName + ")", {
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
   Description: Get RptDataSourceFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptDataSourceFields
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptDataSourceFieldRow
   */  
export function get_RptDataSourceFields(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataSourceFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataSourceFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptDataSourceFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptDataSourceFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptDataSourceFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptDataSourceFields(requestBody:Ice_Tablesets_RptDataSourceFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptDataSourceField item
   Description: Calls GetByID to retrieve the RptDataSourceField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptDataSourceField
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptDataSourceFieldRow
   */  
export function get_RptDataSourceFields_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptDataSourceFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceFields(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptDataSourceFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptDataSourceField for the service
   Description: Calls UpdateExt to update RptDataSourceField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptDataSourceField
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptDataSourceFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptDataSourceFields_SysRowID(SysRowID:string, requestBody:Ice_Tablesets_RptDataSourceFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceFields(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete RptDataSourceField item
   Description: Call UpdateExt to delete RptDataSourceField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptDataSourceField
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptDataSourceFields_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceFields(" + SysRowID + ")", {
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
   Description: Get RptDataSourceParameters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptDataSourceParameters
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptDataSourceParameterRow
   */  
export function get_RptDataSourceParameters(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataSourceParameterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceParameters", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataSourceParameterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptDataSourceParameters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptDataSourceParameterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptDataSourceParameterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptDataSourceParameters(requestBody:Ice_Tablesets_RptDataSourceParameterRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceParameters", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RptDataSourceParameter item
   Description: Calls GetByID to retrieve the RptDataSourceParameter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptDataSourceParameter
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptDataSourceParameterRow
   */  
export function get_RptDataSourceParameters_RptDefID_RptCriteriaSetID_RptTableID_ParameterID(RptDefID:string, RptCriteriaSetID:string, RptTableID:string, ParameterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptDataSourceParameterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceParameters(" + RptDefID + "," + RptCriteriaSetID + "," + RptTableID + "," + ParameterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_RptDataSourceParameterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptDataSourceParameter for the service
   Description: Calls UpdateExt to update RptDataSourceParameter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptDataSourceParameter
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptDataSourceParameterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptDataSourceParameters_RptDefID_RptCriteriaSetID_RptTableID_ParameterID(RptDefID:string, RptCriteriaSetID:string, RptTableID:string, ParameterID:string, requestBody:Ice_Tablesets_RptDataSourceParameterRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceParameters(" + RptDefID + "," + RptCriteriaSetID + "," + RptTableID + "," + ParameterID + ")", {
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
   Summary: Call UpdateExt to delete RptDataSourceParameter item
   Description: Call UpdateExt to delete RptDataSourceParameter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptDataSourceParameter
      @param RptDefID Desc: RptDefID   Required: True   Allow empty value : True
      @param RptCriteriaSetID Desc: RptCriteriaSetID   Required: True   Allow empty value : True
      @param RptTableID Desc: RptTableID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptDataSourceParameters_RptDefID_RptCriteriaSetID_RptTableID_ParameterID(RptDefID:string, RptCriteriaSetID:string, RptTableID:string, ParameterID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/RptDataSourceParameters(" + RptDefID + "," + RptCriteriaSetID + "," + RptTableID + "," + ParameterID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptDataDefListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataDefListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataDefListRow)
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
export function get_GetRows(whereClauseRptDataDef:string, whereClauseRptTable:string, whereClauseRptCalcField:string, whereClauseRptExclude:string, whereClauseRptLinkTable:string, whereClauseRptLinkField:string, whereClauseRptWhereItem:string, whereClauseRptCriteriaSet:string, whereClauseRptCriteriaFilter:string, whereClauseRptCriteriaMapping:string, whereClauseRptCriteriaPrompt:string, whereClauseRptCriteriaPromptValue:string, whereClauseRptRelation:string, whereClauseRptRelationField:string, whereClauseRptLiterals:string, whereClauseRptDataSourceField:string, whereClauseRptDataSourceParameter:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRptDataDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptDataDef=" + whereClauseRptDataDef
   }
   if(typeof whereClauseRptTable!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptTable=" + whereClauseRptTable
   }
   if(typeof whereClauseRptCalcField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptCalcField=" + whereClauseRptCalcField
   }
   if(typeof whereClauseRptExclude!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptExclude=" + whereClauseRptExclude
   }
   if(typeof whereClauseRptLinkTable!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptLinkTable=" + whereClauseRptLinkTable
   }
   if(typeof whereClauseRptLinkField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptLinkField=" + whereClauseRptLinkField
   }
   if(typeof whereClauseRptWhereItem!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptWhereItem=" + whereClauseRptWhereItem
   }
   if(typeof whereClauseRptCriteriaSet!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptCriteriaSet=" + whereClauseRptCriteriaSet
   }
   if(typeof whereClauseRptCriteriaFilter!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptCriteriaFilter=" + whereClauseRptCriteriaFilter
   }
   if(typeof whereClauseRptCriteriaMapping!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptCriteriaMapping=" + whereClauseRptCriteriaMapping
   }
   if(typeof whereClauseRptCriteriaPrompt!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptCriteriaPrompt=" + whereClauseRptCriteriaPrompt
   }
   if(typeof whereClauseRptCriteriaPromptValue!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptCriteriaPromptValue=" + whereClauseRptCriteriaPromptValue
   }
   if(typeof whereClauseRptRelation!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptRelation=" + whereClauseRptRelation
   }
   if(typeof whereClauseRptRelationField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptRelationField=" + whereClauseRptRelationField
   }
   if(typeof whereClauseRptLiterals!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptLiterals=" + whereClauseRptLiterals
   }
   if(typeof whereClauseRptDataSourceField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptDataSourceField=" + whereClauseRptDataSourceField
   }
   if(typeof whereClauseRptDataSourceParameter!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptDataSourceParameter=" + whereClauseRptDataSourceParameter
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(rptDefID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof rptDefID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rptDefID=" + rptDefID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method CreateRptCriteriaPromptsforSelected
   Description: Create Report Criteria Prompts for each Report Mapping record selected.
   OperationID: CreateRptCriteriaPromptsforSelected
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateRptCriteriaPromptsforSelected_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateRptCriteriaPromptsforSelected_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateRptCriteriaPromptsforSelected(requestBody:CreateRptCriteriaPromptsforSelected_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateRptCriteriaPromptsforSelected_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/CreateRptCriteriaPromptsforSelected", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateRptCriteriaPromptsforSelected_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DoesExistsRptCriteriaMappingbyRptTableID
   Description: Check if exists RptCriteriaMapping records for a Report Data Source
   OperationID: DoesExistsRptCriteriaMappingbyRptTableID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DoesExistsRptCriteriaMappingbyRptTableID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoesExistsRptCriteriaMappingbyRptTableID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DoesExistsRptCriteriaMappingbyRptTableID(requestBody:DoesExistsRptCriteriaMappingbyRptTableID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DoesExistsRptCriteriaMappingbyRptTableID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/DoesExistsRptCriteriaMappingbyRptTableID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DoesExistsRptCriteriaMappingbyRptTableID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRelationColumnList
   Description: Get column list when building report relation between parent and child tables
   OperationID: GetRelationColumnList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRelationColumnList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRelationColumnList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRelationColumnList(requestBody:GetRelationColumnList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRelationColumnList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetRelationColumnList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRelationColumnList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetColumnTypeList
   Description: Column types list
   OperationID: Get_GetColumnTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetColumnTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetColumnTypeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetColumnTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetColumnTypeList", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetColumnTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMappingTypeList
   Description: Mapping types list
   OperationID: Get_GetMappingTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMappingTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetMappingTypeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMappingTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetMappingTypeList", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetMappingTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEditorTypeList
   Description: Editor types list
   OperationID: Get_GetEditorTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetEditorTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetEditorTypeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetEditorTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetEditorTypeList", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetEditorTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDataFromList
   Description: Get values for Data From dropdown
   OperationID: GetDataFromList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataFromList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDataFromList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetDataFromList", {
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
         resolve(data as GetDataFromList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCriteriaMappingFPList
   Description: Get list of controls according mapping type
   OperationID: Get_GetCriteriaMappingFPList
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCriteriaMappingFPList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetCriteriaMappingFPList(rptDefID:string, rptCriteriaSetID:string, mappingType:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof rptDefID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rptDefID=" + rptDefID
   }
   if(typeof rptCriteriaSetID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rptCriteriaSetID=" + rptCriteriaSetID
   }
   if(typeof mappingType!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "mappingType=" + mappingType
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCriteriaMappingFPList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetCriteriaMappingFPList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetCriteriaMappingFPList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteAllCriteriaSets
   Description: Delete all criteria sets for a report data definition.
   OperationID: DeleteAllCriteriaSets
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteAllCriteriaSets_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAllCriteriaSets_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteAllCriteriaSets(requestBody:DeleteAllCriteriaSets_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteAllCriteriaSets_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/DeleteAllCriteriaSets", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteAllCriteriaSets_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetEICalculators
   Description: Get Electronic Interface Calculator Names in tilde-separated string.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetEICalculators", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method DoesRptExist
   Description: Check to see if report exists.
   OperationID: DoesRptExist
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DoesRptExist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoesRptExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DoesRptExist(requestBody:DoesRptExist_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DoesRptExist_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/DoesRptExist", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DoesRptExist_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DoesRptCriteriaSetExists
   Description: check to see if report criteria set already exists.
   OperationID: DoesRptCriteriaSetExists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DoesRptCriteriaSetExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoesRptCriteriaSetExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DoesRptCriteriaSetExists(requestBody:DoesRptCriteriaSetExists_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DoesRptCriteriaSetExists_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/DoesRptCriteriaSetExists", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DoesRptCriteriaSetExists_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DuplicateRpt
   Description: To create a new report data definition by duplicating from another.
Typically this is used to duplicate a system report definition so that it can be modified.
   OperationID: DuplicateRpt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DuplicateRpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateRpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateRpt(requestBody:DuplicateRpt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DuplicateRpt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/DuplicateRpt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DuplicateRpt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DuplicateRptCriteriaSet
   Description: Create a new report criteria set by duplicating from another.
   OperationID: DuplicateRptCriteriaSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DuplicateRptCriteriaSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DuplicateRptCriteriaSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DuplicateRptCriteriaSet(requestBody:DuplicateRptCriteriaSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DuplicateRptCriteriaSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/DuplicateRptCriteriaSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DuplicateRptCriteriaSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDataDefUsedTables
   Description: Returns a DataSet with a list of tables and their fields in use on a Report Data Definition given a Report Definition ID.
   OperationID: GetDataDefUsedTables
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDataDefUsedTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataDefUsedTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataDefUsedTables(requestBody:GetDataDefUsedTables_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDataDefUsedTables_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetDataDefUsedTables", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDataDefUsedTables_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOperatorList
   Description: Gets the Operator List to compare FieldName against a constant or another field
   OperationID: GetOperatorList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetOperatorList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOperatorList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOperatorList(requestBody:GetOperatorList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetOperatorList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetOperatorList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetOperatorList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRptDataDefList
   Description: Gets the Report Data Definition List for a specific ReportID
   OperationID: GetRptDataDefList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRptDataDefList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRptDataDefList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRptDataDefList(requestBody:GetRptDataDefList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRptDataDefList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetRptDataDefList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRptDataDefList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportReport
   Description: Exports the report.
   OperationID: ExportReport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportReport(requestBody:ExportReport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportReport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/ExportReport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExportReport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportReportEx
   Description: Export the report with given name
   OperationID: ExportReportEx
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportReportEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReportEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportReportEx(requestBody:ExportReportEx_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportReportEx_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/ExportReportEx", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExportReportEx_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportReport
   Description: Imports the report.
   OperationID: ImportReport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportReport(requestBody:ImportReport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportReport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/ImportReport", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportReport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportReportEx
   Description: Imports the report by given filename (with path).
   OperationID: ImportReportEx
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportReportEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReportEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportReportEx(requestBody:ImportReportEx_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportReportEx_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/ImportReportEx", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportReportEx_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFieldsUsedByReportTable
   Description: Returns a DataSet with a list of fields (including calculated fields) in use on a Report table within a Report Data Definition.
   OperationID: GetFieldsUsedByReportTable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFieldsUsedByReportTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldsUsedByReportTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFieldsUsedByReportTable(requestBody:GetFieldsUsedByReportTable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFieldsUsedByReportTable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetFieldsUsedByReportTable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetFieldsUsedByReportTable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptTableEx
   Description: Create new Rpt source (table, BAQ, EI) by sourceType, wrapper to GetNewRptTable
   OperationID: GetNewRptTableEx
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptTableEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptTableEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptTableEx(requestBody:GetNewRptTableEx_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptTableEx_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptTableEx", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptTableEx_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetFieldType
   Description: Get the data type of a data field.
   OperationID: GetFieldType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetFieldType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFieldType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetFieldType(requestBody:GetFieldType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetFieldType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetFieldType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetFieldType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDataSourceType
   Description: Get DataSource Type for the RptTable record.
   OperationID: GetDataSourceType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDataSourceType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDataSourceType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDataSourceType(requestBody:GetDataSourceType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDataSourceType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetDataSourceType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDataSourceType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeQueryID
   OperationID: OnChangeQueryID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeQueryID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeQueryID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeQueryID(requestBody:OnChangeQueryID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeQueryID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/OnChangeQueryID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeQueryID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReportDataSchema
   Description: Gets the schema for the report data.
   OperationID: GetReportDataSchema
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetReportDataSchema_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportDataSchema_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportDataSchema(requestBody:GetReportDataSchema_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReportDataSchema_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetReportDataSchema", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetReportDataSchema_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReportDataSchemaTablesAndFields
   Description: Gets the schema for the report data in a tableset to usable in REST calls.
   OperationID: GetReportDataSchemaTablesAndFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetReportDataSchemaTablesAndFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportDataSchemaTablesAndFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportDataSchemaTablesAndFields(requestBody:GetReportDataSchemaTablesAndFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReportDataSchemaTablesAndFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetReportDataSchemaTablesAndFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetReportDataSchemaTablesAndFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBreakTableList
   Description: Get break table list (for report style combo box)
   OperationID: GetBreakTableList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBreakTableList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBreakTableList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBreakTableList(requestBody:GetBreakTableList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBreakTableList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetBreakTableList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBreakTableList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPromptsAndFiltersForRptCriteriaSet
   Description: Returns the Prompts and Filters for the given Report Data Definition and Report Criteria Set.
   OperationID: GetPromptsAndFiltersForRptCriteriaSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPromptsAndFiltersForRptCriteriaSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPromptsAndFiltersForRptCriteriaSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPromptsAndFiltersForRptCriteriaSet(requestBody:GetPromptsAndFiltersForRptCriteriaSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPromptsAndFiltersForRptCriteriaSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetPromptsAndFiltersForRptCriteriaSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPromptsAndFiltersForRptCriteriaSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTokenList
   Description: Returns a comma separated list of valid tokens for the given data type.
   OperationID: GetTokenList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTokenList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTokenList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTokenList(requestBody:GetTokenList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTokenList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetTokenList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetTokenList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportElectronicInterface
   Description: Export electronic interfaces as a DataSet.
   OperationID: ExportElectronicInterface
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportElectronicInterface_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportElectronicInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportElectronicInterface(requestBody:ExportElectronicInterface_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportElectronicInterface_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/ExportElectronicInterface", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExportElectronicInterface_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportElectronicInterface
   Description: Import electronic interfaces from a DataSet.
   OperationID: ImportElectronicInterface
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportElectronicInterface_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportElectronicInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportElectronicInterface(requestBody:ImportElectronicInterface_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportElectronicInterface_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/ImportElectronicInterface", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportElectronicInterface_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteElectronicInterface
   Description: Delete an electronic interface.
   OperationID: DeleteElectronicInterface
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteElectronicInterface_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteElectronicInterface_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteElectronicInterface(requestBody:DeleteElectronicInterface_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteElectronicInterface_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/DeleteElectronicInterface", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteElectronicInterface_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetElectronicInterfaceList
   Description: Calls the ERP Extension if present and returns a list of Electronic Interfaces.
   OperationID: GetElectronicInterfaceList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetElectronicInterfaceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetElectronicInterfaceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetElectronicInterfaceList(requestBody:GetElectronicInterfaceList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetElectronicInterfaceList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetElectronicInterfaceList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetElectronicInterfaceList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDropDownPromptDisplayOrder
   Description: Change display order value from a source drop down prompt item to a target one and vice versa.
   OperationID: ChangeDropDownPromptDisplayOrder
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDropDownPromptDisplayOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDropDownPromptDisplayOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDropDownPromptDisplayOrder(requestBody:ChangeDropDownPromptDisplayOrder_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDropDownPromptDisplayOrder_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/ChangeDropDownPromptDisplayOrder", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDropDownPromptDisplayOrder_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDropDownPromptRows
   Description: Get Drop down prompt rows.
   OperationID: GetDropDownPromptRows
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDropDownPromptRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDropDownPromptRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDropDownPromptRows(requestBody:GetDropDownPromptRows_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDropDownPromptRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetDropDownPromptRows", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDropDownPromptRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateBAQDataSource
   Description: Validates the BAQ data source is able to current company, throw en exception where exists any BAQ record not founded.
   OperationID: ValidateBAQDataSource
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateBAQDataSource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateBAQDataSource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateBAQDataSource(requestBody:ValidateBAQDataSource_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateBAQDataSource_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/ValidateBAQDataSource", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateBAQDataSource_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateRptLabels
   Description: Validates that the number of labels does not exceed a maximum of 800 for system reports and 1020 for custom (non-system) reports.
   OperationID: ValidateRptLabels
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateRptLabels_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateRptLabels_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateRptLabels(requestBody:ValidateRptLabels_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateRptLabels_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/ValidateRptLabels", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateRptLabels_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSelectLinkTables
   Description: Get list of tables available for RptLinkTable selection
   OperationID: GetSelectLinkTables
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSelectLinkTables_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectLinkTables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectLinkTables(requestBody:GetSelectLinkTables_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSelectLinkTables_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetSelectLinkTables", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetSelectLinkTables_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptDataDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptDataDef
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptDataDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptDataDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptDataDef(requestBody:GetNewRptDataDef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptDataDef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptDataDef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptDataDef_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptTable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptTable(requestBody:GetNewRptTable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptTable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptTable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptTable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptCalcField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptCalcField
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptCalcField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptCalcField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptCalcField(requestBody:GetNewRptCalcField_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptCalcField_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptCalcField", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptCalcField_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptExclude
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptExclude
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptExclude_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptExclude_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptExclude(requestBody:GetNewRptExclude_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptExclude_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptExclude", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptExclude_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptLinkTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptLinkTable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptLinkTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptLinkTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptLinkTable(requestBody:GetNewRptLinkTable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptLinkTable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptLinkTable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptLinkTable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptLinkField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptLinkField
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptLinkField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptLinkField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptLinkField(requestBody:GetNewRptLinkField_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptLinkField_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptLinkField", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptLinkField_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptWhereItem
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptWhereItem
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptWhereItem_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptWhereItem_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptWhereItem(requestBody:GetNewRptWhereItem_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptWhereItem_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptWhereItem", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptWhereItem_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptCriteriaSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptCriteriaSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptCriteriaSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptCriteriaSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptCriteriaSet(requestBody:GetNewRptCriteriaSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptCriteriaSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptCriteriaSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptCriteriaSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptCriteriaFilter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptCriteriaFilter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptCriteriaFilter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptCriteriaFilter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptCriteriaFilter(requestBody:GetNewRptCriteriaFilter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptCriteriaFilter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptCriteriaFilter", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptCriteriaFilter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptCriteriaMapping
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptCriteriaMapping
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptCriteriaMapping_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptCriteriaMapping_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptCriteriaMapping(requestBody:GetNewRptCriteriaMapping_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptCriteriaMapping_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptCriteriaMapping", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptCriteriaMapping_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptCriteriaPrompt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptCriteriaPrompt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptCriteriaPrompt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptCriteriaPrompt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptCriteriaPrompt(requestBody:GetNewRptCriteriaPrompt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptCriteriaPrompt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptCriteriaPrompt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptCriteriaPrompt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptCriteriaPromptValue
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptCriteriaPromptValue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptCriteriaPromptValue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptCriteriaPromptValue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptCriteriaPromptValue(requestBody:GetNewRptCriteriaPromptValue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptCriteriaPromptValue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptCriteriaPromptValue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptCriteriaPromptValue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptRelation
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptRelation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptRelation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptRelation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptRelation(requestBody:GetNewRptRelation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptRelation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptRelation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptRelation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptRelationField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptRelationField
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptRelationField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptRelationField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptRelationField(requestBody:GetNewRptRelationField_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptRelationField_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptRelationField", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptRelationField_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptLiterals
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptLiterals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptLiterals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptLiterals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptLiterals(requestBody:GetNewRptLiterals_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptLiterals_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetNewRptLiterals", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRptLiterals_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.RptDataDefSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCalcFieldRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptCalcFieldRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaFilterRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptCriteriaFilterRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaMappingRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptCriteriaMappingRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaPromptRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptCriteriaPromptRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaPromptValueRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptCriteriaPromptValueRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptCriteriaSetRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptCriteriaSetRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataDefListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptDataDefListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataDefRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptDataDefRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataSourceFieldRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptDataSourceFieldRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptDataSourceParameterRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptDataSourceParameterRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptExcludeRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptExcludeRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLinkFieldRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptLinkFieldRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLinkTableRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptLinkTableRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptLiteralsRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptLiteralsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptRelationFieldRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptRelationFieldRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptRelationRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptRelationRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptTableRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptTableRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptWhereItemRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptWhereItemRow,
}

export interface Ice_Tablesets_RptCalcFieldRow{
      /**  Report Data Definition ID  */  
   "RptDefID":string,
      /**  Report Table ID  */  
   "RptTableID":string,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   "ZDataTableID":string,
      /**  Name for Calculated Field.  When output to XML they will be written as Calc-fieldname in order to avoid conflicts with other fields in the table.  */  
   "FieldName":string,
      /**  Field Label  */  
   "FieldLabel":string,
      /**  Character, Date, Integer, Decimal, Logical  */  
   "DataType":string,
      /**  Field Format  */  
   "FieldFormat":string,
      /**  Field Length  */  
   "FieldLength":number,
      /**  Field Precision  */  
   "FieldPrecision":number,
      /**  Decimal Currency Dependent  */  
   "DecimalCurDepended":boolean,
      /**  Value Type: G - General, C - Cost, P - Price  */  
   "DecimalValueType":string,
      /**  Currency type: O - Own/Base Currency, G - Global Currency, D - Currency from Document  */  
   "DecimalCurrencyType":string,
      /**  Decimal Currency code  */  
   "DecimalCurCodeField":string,
      /**  Further defines the Business use of the Field  */  
   "BizType":string,
      /**  Field Name from zdatatable  */  
   "ZFieldName":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  */  
   "DataSourceType":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptCriteriaFilterRow{
      /**  Company  */  
   "Company":string,
      /**  RptDefID  */  
   "RptDefID":string,
      /**  RptCriteriaSetID  */  
   "RptCriteriaSetID":string,
      /**  FilterID  */  
   "FilterID":number,
      /**  FilterName  */  
   "FilterName":string,
      /**  AdapterName  */  
   "AdapterName":string,
      /**  LookupField  */  
   "LookupField":string,
      /**  FilterLabel  */  
   "FilterLabel":string,
      /**  TabLabel  */  
   "TabLabel":string,
      /**  DataType  */  
   "DataType":string,
      /**  EpiGuid  */  
   "EpiGuid":string,
      /**  DisplayOrder  */  
   "DisplayOrder":number,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptCriteriaMappingRow{
      /**  Company  */  
   "Company":string,
      /**  RptDefID  */  
   "RptDefID":string,
      /**  RptCriteriaSetID  */  
   "RptCriteriaSetID":string,
      /**  RptTableID  */  
   "RptTableID":string,
      /**  ParameterID  */  
   "ParameterID":string,
      /**  PromptID  */  
   "PromptID":number,
      /**  FilterID  */  
   "FilterID":number,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptCriteriaPromptRow{
      /**  Company  */  
   "Company":string,
      /**  RptDefID  */  
   "RptDefID":string,
      /**  RptCriteriaSetID  */  
   "RptCriteriaSetID":string,
      /**  PromptID  */  
   "PromptID":number,
      /**  PromptName  */  
   "PromptName":string,
      /**  DataType  */  
   "DataType":string,
      /**  Label  */  
   "Label":string,
      /**  DefaultValue  */  
   "DefaultValue":string,
      /**  EpiGuid  */  
   "EpiGuid":string,
      /**  IsConstant  */  
   "IsConstant":boolean,
      /**  ConstantValue  */  
   "ConstantValue":string,
      /**  IsVisible  */  
   "IsVisible":boolean,
      /**  DisplayOrder  */  
   "DisplayOrder":number,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  EditorType  */  
   "EditorType":string,
      /**  DataFrom  */  
   "DataFrom":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  DisplayColumn  */  
   "DisplayColumn":string,
      /**  ValueColumn  */  
   "ValueColumn":string,
      /**  EFTHeadCompany  */  
   "EFTHeadCompany":string,
      /**  EFTHeadUID  */  
   "EFTHeadUID":number,
      /**  Use an empty string on this column, instead of null.  */  
   "IsEmptyString":boolean,
   "EIName":string,
   "EIDescription":string,
   "DefaultValueInt":number,
   "DefaultValueNum":number,
   "DefaultValueDatetime":string,
   "IsDynamic":boolean,
   "DefaultValueBit":boolean,
   "ConstantValueBit":boolean,
   "ConstantValueDatetime":string,
   "ConstantValueNum":number,
   "ConstantValueInt":number,
   "UseTypedValues":boolean,
   "DefaultValueDatetimeDynamic":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptCriteriaPromptValueRow{
      /**  Company  */  
   "Company":string,
      /**  RptDefID  */  
   "RptDefID":string,
      /**  RptCriteriaSetID  */  
   "RptCriteriaSetID":string,
      /**  PromptID  */  
   "PromptID":number,
      /**  ItemID  */  
   "ItemID":number,
      /**  ItemValue  */  
   "ItemValue":string,
      /**  ItemDescription  */  
   "ItemDescription":string,
      /**  DisplayOrder  */  
   "DisplayOrder":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptCriteriaSetRow{
      /**  Company  */  
   "Company":string,
      /**  RptDefID  */  
   "RptDefID":string,
      /**  RptCriteriaSetID  */  
   "RptCriteriaSetID":string,
      /**  Description  */  
   "Description":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  IsDefault  */  
   "IsDefault":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptDataDefListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Report Data Definition ID  */  
   "RptDefID":string,
      /**  Report Data Definition Description  */  
   "RptDescription":string,
      /**   Indicates if this is a base system report data defintion. System report data defintions  can not be modified by users. This defintion corresponds to the base report programs (@ Crystal.rpt)
If the user requires modification they can make a duplicate and make the necessary changes to that version.  */  
   "SystemRpt":boolean,
      /**  The Report Type similar to the one set in the Report Styles, that will help to identify which report type is this data definition intended for.  */  
   "RptTypeID":string,
      /**  Used to identify which data definition was used for duplication.  */  
   "DuplicateOf":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Flag to indicate Dynamic Report  */  
   "DynamicReport":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptDataDefRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Report Data Definition ID  */  
   "RptDefID":string,
      /**  Report Data Definition Description  */  
   "RptDescription":string,
      /**   Indicates if this is a base system report data defintion. System report data defintions  can not be modified by users. This defintion corresponds to the base report programs (@ Crystal.rpt)
If the user requires modification they can make a duplicate and make the necessary changes to that version.  */  
   "SystemRpt":boolean,
      /**  The Report Type similar to the one set in the Report Styles, that will help to identify which report type is this data definition intended for.  */  
   "RptTypeID":string,
      /**  Used to identify which data definition was used for duplication.  */  
   "DuplicateOf":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  PrimaryTable  */  
   "PrimaryTable":string,
      /**  PrimaryKey1  */  
   "PrimaryKey1":string,
      /**  PrimaryKey2  */  
   "PrimaryKey2":string,
      /**  UseMultipleCriteria  */  
   "UseMultipleCriteria":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptDataSourceFieldRow{
   "FieldName":string,
   "QueryID":string,
      /**  Database Table Name  */  
   "DBTableName":string,
      /**  Database Field Name  */  
   "DBFieldName":string,
      /**  DataType  */  
   "DataType":string,
      /**  Like Data Field Name  */  
   "LikeDataFieldName":string,
      /**  Field Label  */  
   "FieldLabel":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptDataSourceParameterRow{
      /**  RptDefID  */  
   "RptDefID":string,
      /**  RptCriteriaSetID  */  
   "RptCriteriaSetID":string,
      /**  RptTableID  */  
   "RptTableID":string,
      /**  ParameterID  */  
   "ParameterID":string,
      /**  PromptID  */  
   "PromptID":number,
      /**  FilterID  */  
   "FilterID":number,
      /**  Data source type.  */  
   "Type":string,
      /**  Parameter data type.  */  
   "ParamDataType":string,
      /**  Flag to inditate if parameter is mandatory or not.  */  
   "IsMandatory":boolean,
   "SkipIfEmpty":boolean,
      /**  Shows control type related to parameter: Prompt or Filter.  */  
   "ControlType":string,
   "ControlName":string,
   "ControlDataType":string,
   "QueryEI":string,
   "SysRevID":number,
   "Selection":boolean,
      /**  Control type in the source of the parameter.  */  
   "SourceControlType":string,
   "ControlNameDesc":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptExcludeRow{
      /**  Report Data Definition ID  */  
   "RptDefID":string,
      /**  Report Table ID  */  
   "RptTableID":string,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   "ZDataTableID":string,
      /**  zField Name  */  
   "ZFieldName":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ExcludeColumn  */  
   "ExcludeColumn":boolean,
      /**  ExcludeLabel  */  
   "ExcludeLabel":boolean,
      /**  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  */  
   "DataSourceType":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptLinkFieldRow{
      /**  Report Data Definition ID  */  
   "RptDefID":string,
      /**  Report Table ID  */  
   "RptTableID":string,
      /**  Report Link ID  */  
   "RptLinkID":string,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   "ZDataTableID":string,
      /**  Foreign Key component of ZLookupLink. ZLookUpLink  defines the Foreign Tables related to the RptTable.ZDataTable.  ZLookupLinkField defines the fields needed to link to it.  */  
   "ZLookupID":string,
      /**  field name of the database table. DB Table is defined by  ZDataTable.DBTableName.  */  
   "FieldName":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptLinkTableRow{
      /**  Report Data Definition ID  */  
   "RptDefID":string,
      /**  Report Table ID  */  
   "RptTableID":string,
      /**  Report Link ID  */  
   "RptLinkID":string,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   "ZDataTableID":string,
      /**  Foreign Key component of ZLookupLink. ZLookUpLink  defines the Foreign Tables related to the RptTable.ZDataTable.  ZLookupLinkField defines the fields needed to link to it.  */  
   "ZLookupID":string,
      /**  Description  */  
   "Description":string,
      /**  Key ID  */  
   "KeyID":string,
      /**  Foreign Report Table ID  */  
   "ForeignRptTableID":string,
      /**  Foreign zTable ID  */  
   "ForeignZTableID":string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  */  
   "DataSourceType":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptLiteralsRow{
      /**  Report Data Definition ID  */  
   "RptDefID":string,
      /**  Literal Name  */  
   "LiteralName":string,
      /**  Literal Value  */  
   "LiteralValue":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptRelationFieldRow{
      /**  Report Data Definition ID  */  
   "RptDefID":string,
      /**  Report Relation ID  */  
   "RelationID":string,
      /**  Sequence  */  
   "Seq":number,
      /**  Parent Field Name  */  
   "ParentFieldName":string,
      /**  Child Field Name  */  
   "ChildFieldName":string,
      /**  Operator to use for relation between Parent and Child fields.  */  
   "CompOp":string,
      /**  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  */  
   "IsConst":boolean,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptRelationRow{
      /**  Report Data Definition ID  */  
   "RptDefID":string,
      /**  Report Relation ID  */  
   "RelationID":string,
      /**  Parent Report Table ID  */  
   "ParentRptTableID":string,
      /**  ChildRptTableID  */  
   "ChildRptTableID":string,
      /**  Key ID  */  
   "KeyID":string,
      /**  Description  */  
   "Description":string,
      /**  Valid values are "each", "first", and "last".  */  
   "WhichItem":string,
      /**  "Outer" = outer-join, "" = inner-join  */  
   "JoinType":string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Sequence Order to dump Relationships on the EDI Flat files.  */  
   "SeqOrder":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptTableRow{
      /**  Report Data Definition ID  */  
   "RptDefID":string,
      /**  ID for the Table in this report.  Usually this would be the same as the ZDataTableID, which is usually the same as the db table name. Allows us to have the data from the same physical table defined more than once in the report.  Example would be spliting the OrderMsc into something like OrderHeadMsc and OrderDtlMsc.  */  
   "RptTableID":string,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   "ZDataTableID":string,
      /**  Sequence Control  */  
   "SeqControl":number,
      /**  Parent Report Table ID  */  
   "ParentRptTableID":string,
      /**   Indicates if this is the Primary table of the generated Report Dataset.
Primary table defintions have an additional field, "RptLanguageID". 
The RptLanguageID field is used to link to the RptLabel table.
The RptLabel is not a database table,  it contains the translations for the literals and is present
only in the generated Report Dataset.  */  
   "PrimaryTable":boolean,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  IsSystemTable  */  
   "IsSystemTable":boolean,
      /**  QueryID  */  
   "QueryID":string,
      /**  EFTHeadCompany  */  
   "EFTHeadCompany":string,
      /**  EFTHeadUID  */  
   "EFTHeadUID":number,
      /**  DB Table Type  */  
   "TableType":string,
      /**  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  */  
   "DataSourceType":string,
      /**  Data Source Description  */  
   "DataSourceDescription":string,
      /**  Data Source Name  */  
   "DataSourceName":string,
      /**  True when data source is valid and available for current company and user, otherwise is false.  */  
   "IsValidDataSource":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptWhereItemRow{
      /**  Report Data Definition ID  */  
   "RptDefID":string,
      /**  ID for the Table in this report.  Usually this would be the same as the ZDataTableID, which is usually the same as the db table name. Allows us to have the data from the same physical table defined more than once in the report.  Example would be spliting the OrderMsc into something like OrderHeadMsc and OrderDtlMsc.  */  
   "RptTableID":string,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   "ZDataTableID":string,
      /**  Sequence  */  
   "Seq":number,
      /**  Field Name  */  
   "FieldName":string,
      /**  Operator to use for relation between left value and right value.  */  
   "CompOp":string,
      /**  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  */  
   "IsConst":boolean,
      /**  To Table ID  */  
   "ToTableID":string,
      /**  ToSystemCode  */  
   "ToSystemCode":string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   "ToZTableID":string,
      /**  To Field Name  */  
   "ToFieldName":string,
      /**  And / Or  */  
   "AndOr":string,
      /**  Negative indicator  */  
   "Neg":boolean,
      /**  The constant value that will be used to compare against the selected field  */  
   "RValue":string,
      /**  Number of Left Parenthesis  */  
   "NumLeftP":number,
      /**  Number of Right Parenthesis  */  
   "NumRightP":number,
      /**  Parent Sequence  */  
   "ParentSeq":number,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "FromToday":boolean,
   "FromTodayValue":number,
   "LeftP":string,
   "RightP":string,
   "RValueDate":string,
   "RValueNumber":number,
      /**  Constanst value caracter field  */  
   "RValueChar":string,
      /**  Constant value Boolean  */  
   "RValueBool":boolean,
      /**  Constant Value Integer  */  
   "RValueInt":number,
      /**  Field Type  */  
   "FieldType":string,
      /**  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  */  
   "DataSourceType":string,
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
      @param ds
      @param rptDefID
      @param rptCriteriaSetID
      @param promptID
      @param sourceItemID
      @param targetItemID
   */  
export interface ChangeDropDownPromptDisplayOrder_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
      /**  Report definition identifier  */  
   rptDefID:string,
      /**  Criteria Set identifier  */  
   rptCriteriaSetID:string,
      /**  Prompt identifier  */  
   promptID:number,
      /**  Source item ID to change Display Order field  */  
   sourceItemID:number,
      /**  Target item ID to change Display order field  */  
   targetItemID:number,
}

export interface ChangeDropDownPromptDisplayOrder_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param anyRptCriteriaPromptCrated
   */  
export interface CreateRptCriteriaPromptsforSelected_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   anyRptCriteriaPromptCrated:boolean,
}

export interface CreateRptCriteriaPromptsforSelected_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
   anyRptCriteriaPromptCrated:boolean,
}
}

   /** Required : 
      @param ds
      @param rptDefID
   */  
export interface DeleteAllCriteriaSets_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
}

export interface DeleteAllCriteriaSets_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param rptDefID
   */  
export interface DeleteByID_input{
   rptDefID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param companyID
      @param eftHeadUID
   */  
export interface DeleteElectronicInterface_input{
   companyID:string,
   eftHeadUID:number,
}

export interface DeleteElectronicInterface_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param rptDefID
      @param rptTableID
   */  
export interface DoesExistsRptCriteriaMappingbyRptTableID_input{
   rptDefID:string,
   rptTableID:string,
}

export interface DoesExistsRptCriteriaMappingbyRptTableID_output{
   returnObj:boolean,
}

   /** Required : 
      @param rptDefID
      @param rptCriteriaSetID
   */  
export interface DoesRptCriteriaSetExists_input{
      /**  The report definition identifier.  */  
   rptDefID:string,
      /**  ID for the new report criteria set.  */  
   rptCriteriaSetID:string,
}

export interface DoesRptCriteriaSetExists_output{
   returnObj:boolean,
}

   /** Required : 
      @param rptDefID
   */  
export interface DoesRptExist_input{
      /**  ID for the new report.  */  
   rptDefID:string,
}

export interface DoesRptExist_output{
      /**  `true` if the report exists.  */  
   returnObj:boolean,
}

   /** Required : 
      @param sourceRptDefID
      @param sourceRptCriteriaSetID
      @param targetRptCriteriaSetID
      @param targetCriteriaDescription
   */  
export interface DuplicateRptCriteriaSet_input{
      /**  ID of report which contains the criteria set that will be duplicated.  */  
   sourceRptDefID:string,
      /**  ID of criteria set that will be duplicated.  */  
   sourceRptCriteriaSetID:string,
      /**  ID for the new criteria set.  */  
   targetRptCriteriaSetID:string,
      /**  >Description that will be used for the new criteria set.
            if blank, the source description will be used.  */  
   targetCriteriaDescription:string,
}

export interface DuplicateRptCriteriaSet_output{
   returnObj:Ice_Tablesets_RptDataDefTableset[],
}

   /** Required : 
      @param sourceRptDefID
      @param targetRptDefID
      @param targetRptDescription
   */  
export interface DuplicateRpt_input{
      /**  Id of report that will be duplicated.  */  
   sourceRptDefID:string,
      /**  ID for the new report.  */  
   targetRptDefID:string,
      /**  Description that will be used for the new report.
            if blank, the source description will be used.  */  
   targetRptDescription:string,
}

export interface DuplicateRpt_output{
   returnObj:Ice_Tablesets_RptDataDefTableset[],
}

   /** Required : 
      @param companyID
      @param eftHeadUID
   */  
export interface ExportElectronicInterface_input{
   companyID:string,
   eftHeadUID:number,
}

export interface ExportElectronicInterface_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param rptDefId
      @param exportFileName
   */  
export interface ExportReportEx_input{
      /**  The RptDataDefId to export  */  
   rptDefId:string,
      /**  The name of the file to be created  */  
   exportFileName:string,
}

export interface ExportReportEx_output{
}

   /** Required : 
      @param rptDefId
   */  
export interface ExportReport_input{
      /**  The RptDefId to export.  */  
   rptDefId:string,
}

export interface ExportReport_output{
      /**  The export data.  */  
   returnObj:string,
}

   /** Required : 
      @param rptDefID
   */  
export interface GetBreakTableList_input{
      /**  RptDefID value.  */  
   rptDefID:string,
}

export interface GetBreakTableList_output{
   returnObj:Ice_Tablesets_BreakTableListTableset[],
}

   /** Required : 
      @param rptDefID
   */  
export interface GetByID_input{
   rptDefID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_RptDataDefTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_RptDataDefTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_RptDataDefTableset[],
}

export interface GetColumnTypeList_output{
   returnObj:string,
}

   /** Required : 
      @param rptDefID
      @param rptCriteriaSetID
      @param mappingType
   */  
export interface GetCriteriaMappingFPList_input{
   rptDefID:string,
   rptCriteriaSetID:string,
   mappingType:string,
}

export interface GetCriteriaMappingFPList_output{
   returnObj:Ice_Tablesets_RptCriteriaMappingFPListTableset[],
}

   /** Required : 
      @param rptDefID
      @param onlyDBTables
   */  
export interface GetDataDefUsedTables_input{
      /**  Report Definition ID  */  
   rptDefID:string,
      /**  Return Only DataBase Tables  */  
   onlyDBTables:boolean,
}

export interface GetDataDefUsedTables_output{
   returnObj:Ice_Tablesets_DefUsedTablesTableset[],
}

export interface GetDataFromList_output{
   returnObj:string,
}

   /** Required : 
      @param ds
      @param rptDefID
      @param rptTableID
   */  
export interface GetDataSourceType_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
   rptTableID:string,
}

export interface GetDataSourceType_output{
   returnObj:string,
}

   /** Required : 
      @param rptDefID
      @param rptCriteriaSetID
      @param promptID
   */  
export interface GetDropDownPromptRows_input{
      /**  Report definition identifier.  */  
   rptDefID:string,
      /**  Criteria set identifier.  */  
   rptCriteriaSetID:string,
      /**  Prompt identifier.  */  
   promptID:number,
}

export interface GetDropDownPromptRows_output{
      /**  Down prompt rows in a Data table.  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param eFTHeadCompany
      @param eFTHeadUID
   */  
export interface GetEICalculators_input{
   eFTHeadCompany:string,
   eFTHeadUID:number,
}

export interface GetEICalculators_output{
   returnObj:string,
}

export interface GetEditorTypeList_output{
   returnObj:string,
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetElectronicInterfaceList_input{
      /**  The where clause.  */  
   whereClause:string,
      /**  Size of the page.  */  
   pageSize:number,
      /**  The absolute page.  */  
   absolutePage:number,
}

export interface GetElectronicInterfaceList_output{
   returnObj:Ice_Tablesets_ElectronicInterfacesListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param systemCode
      @param dataTableID
      @param fieldName
   */  
export interface GetFieldType_input{
   systemCode:string,
   dataTableID:string,
   fieldName:string,
}

export interface GetFieldType_output{
   returnObj:string,
}

   /** Required : 
      @param rptDefID
      @param reportTable
      @param systemCode
      @param zDataTableID
   */  
export interface GetFieldsUsedByReportTable_input{
      /**  Report Definition ID  */  
   rptDefID:string,
      /**  Report table used on the data definition  */  
   reportTable:string,
      /**  System code of the report table  */  
   systemCode:string,
      /**  ZDatatableID of the report table  */  
   zDataTableID:string,
}

export interface GetFieldsUsedByReportTable_output{
   returnObj:Ice_Tablesets_DefUsedTablesTableset[],
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
   returnObj:Ice_Tablesets_RptDataDefListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetMappingTypeList_output{
   returnObj:string,
}

   /** Required : 
      @param ds
      @param rptDefID
      @param rptTableID
      @param systemCode
      @param zdataTableID
   */  
export interface GetNewRptCalcField_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
   rptTableID:string,
   systemCode:string,
   zdataTableID:string,
}

export interface GetNewRptCalcField_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
      @param rptCriteriaSetID
   */  
export interface GetNewRptCriteriaFilter_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
   rptCriteriaSetID:string,
}

export interface GetNewRptCriteriaFilter_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
      @param rptCriteriaSetID
      @param rptTableID
   */  
export interface GetNewRptCriteriaMapping_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
   rptCriteriaSetID:string,
   rptTableID:string,
}

export interface GetNewRptCriteriaMapping_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
      @param rptCriteriaSetID
      @param promptID
   */  
export interface GetNewRptCriteriaPromptValue_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
   rptCriteriaSetID:string,
   promptID:number,
}

export interface GetNewRptCriteriaPromptValue_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
      @param rptCriteriaSetID
   */  
export interface GetNewRptCriteriaPrompt_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
   rptCriteriaSetID:string,
}

export interface GetNewRptCriteriaPrompt_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
   */  
export interface GetNewRptCriteriaSet_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
}

export interface GetNewRptCriteriaSet_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewRptDataDef_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
}

export interface GetNewRptDataDef_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
      @param rptTableID
      @param systemCode
      @param zdataTableID
   */  
export interface GetNewRptExclude_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
   rptTableID:string,
   systemCode:string,
   zdataTableID:string,
}

export interface GetNewRptExclude_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
      @param rptTableID
      @param rptLinkID
      @param systemCode
      @param zdataTableID
      @param zlookupID
   */  
export interface GetNewRptLinkField_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
   rptTableID:string,
   rptLinkID:string,
   systemCode:string,
   zdataTableID:string,
   zlookupID:string,
}

export interface GetNewRptLinkField_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
      @param rptTableID
      @param rptLinkID
      @param systemCode
      @param zdataTableID
   */  
export interface GetNewRptLinkTable_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
   rptTableID:string,
   rptLinkID:string,
   systemCode:string,
   zdataTableID:string,
}

export interface GetNewRptLinkTable_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
   */  
export interface GetNewRptLiterals_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
}

export interface GetNewRptLiterals_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
      @param relationID
   */  
export interface GetNewRptRelationField_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
   relationID:string,
}

export interface GetNewRptRelationField_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
   */  
export interface GetNewRptRelation_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
}

export interface GetNewRptRelation_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
      @param dataSourceType
   */  
export interface GetNewRptTableEx_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
   dataSourceType:string,
}

export interface GetNewRptTableEx_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
   */  
export interface GetNewRptTable_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
}

export interface GetNewRptTable_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param ds
      @param rptDefID
      @param rptTableID
      @param systemCode
      @param zdataTableID
   */  
export interface GetNewRptWhereItem_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   rptDefID:string,
   rptTableID:string,
   systemCode:string,
   zdataTableID:string,
}

export interface GetNewRptWhereItem_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param fieldType
   */  
export interface GetOperatorList_input{
      /**  Field Data-Type  */  
   fieldType:string,
}

export interface GetOperatorList_output{
parameters : {
      /**  output parameters  */  
   operatorList:string,
}
}

   /** Required : 
      @param rptDataDef
      @param rptCriteriaSetID
   */  
export interface GetPromptsAndFiltersForRptCriteriaSet_input{
      /**  Report Data Definition Identifier.  */  
   rptDataDef:string,
      /**  Report Criteria Set Identifier.  */  
   rptCriteriaSetID:string,
}

export interface GetPromptsAndFiltersForRptCriteriaSet_output{
   returnObj:Ice_Tablesets_RptCriteriaDataTableset[],
}

   /** Required : 
      @param rptDefID
      @param childRptTableID
      @param parentRptTableID
   */  
export interface GetRelationColumnList_input{
   rptDefID:string,
   childRptTableID:string,
   parentRptTableID:string,
}

export interface GetRelationColumnList_output{
   returnObj:Ice_Tablesets_RelationColumnListTableset[],
}

   /** Required : 
      @param rptDefId
   */  
export interface GetReportDataSchemaTablesAndFields_input{
      /**  The RptDefID value.  */  
   rptDefId:string,
}

export interface GetReportDataSchemaTablesAndFields_output{
   returnObj:Ice_Tablesets_DefUsedTablesTableset[],
}

   /** Required : 
      @param rptDefId
   */  
export interface GetReportDataSchema_input{
      /**  The RptDefID value.  */  
   rptDefId:string,
}

export interface GetReportDataSchema_output{
      /**  The schema for the report data.  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param whereClauseRptDataDef
      @param whereClauseRptTable
      @param whereClauseRptCalcField
      @param whereClauseRptExclude
      @param whereClauseRptLinkTable
      @param whereClauseRptLinkField
      @param whereClauseRptWhereItem
      @param whereClauseRptCriteriaSet
      @param whereClauseRptCriteriaFilter
      @param whereClauseRptCriteriaMapping
      @param whereClauseRptCriteriaPrompt
      @param whereClauseRptCriteriaPromptValue
      @param whereClauseRptRelation
      @param whereClauseRptRelationField
      @param whereClauseRptLiterals
      @param whereClauseRptDataSourceField
      @param whereClauseRptDataSourceParameter
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRptDataDef:string,
   whereClauseRptTable:string,
   whereClauseRptCalcField:string,
   whereClauseRptExclude:string,
   whereClauseRptLinkTable:string,
   whereClauseRptLinkField:string,
   whereClauseRptWhereItem:string,
   whereClauseRptCriteriaSet:string,
   whereClauseRptCriteriaFilter:string,
   whereClauseRptCriteriaMapping:string,
   whereClauseRptCriteriaPrompt:string,
   whereClauseRptCriteriaPromptValue:string,
   whereClauseRptRelation:string,
   whereClauseRptRelationField:string,
   whereClauseRptLiterals:string,
   whereClauseRptDataSourceField:string,
   whereClauseRptDataSourceParameter:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_RptDataDefTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param WhereClause
      @param ReportID
      @param PageSize
      @param AbsolutePage
   */  
export interface GetRptDataDefList_input{
      /**  Where clause.  */  
   WhereClause:string,
      /**  ReportID.  */  
   ReportID:string,
      /**  Page size.  */  
   PageSize:number,
      /**  Absolute page.  */  
   AbsolutePage:number,
}

export interface GetRptDataDefList_output{
   returnObj:Ice_Tablesets_RptDataDefListTableset[],
parameters : {
      /**  output parameters  */  
   MorePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetSelectLinkTables_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
}

export interface GetSelectLinkTables_output{
   returnObj:Ice_Tablesets_SelectLinkDataTableset[],
}

   /** Required : 
      @param tokenDataType
   */  
export interface GetTokenList_input{
      /**  Type of token for which you want the list of valid values.
            Valid Types are; Date, FiscalPeriod, FiscalYear  */  
   tokenDataType:string,
}

export interface GetTokenList_output{
   returnObj:string,
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

export interface Ice_Tablesets_BreakTableListTableset{
   BreakTable:Ice_Tablesets_BreakTableRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_BreakTableRow{
      /**  Report definition ID  */  
   RptDefID:string,
      /**  Table name  */  
   RptTableID:string,
      /**  System Code  */  
   SystemCode:string,
   ZDataTableID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DefUsedFieldsRow{
      /**  Name of field used by the Data Definition  */  
   FieldName:string,
      /**  Name of table used by the Data Defintion  */  
   TableName:string,
      /**  Field type (character, date, decimal, integer, logical)  */  
   DataType:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DefUsedTablesRow{
      /**  Name of table used by the Data Defintion  */  
   TableName:string,
      /**  Indicates the type of table (DB, TT, RPT).  */  
   TableType:string,
      /**  Flag indicating if this is a Link Table.  */  
   LinkTable:boolean,
   Sequence:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DefUsedTablesTableset{
   DefUsedTables:Ice_Tablesets_DefUsedTablesRow[],
   DefUsedFields:Ice_Tablesets_DefUsedFieldsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ElectronicInterfaceListRow{
      /**  From ERP.EFTHeadUID  */  
   EFTHeadUID:number,
      /**  ERP.EFTHead/Name  */  
   Name:string,
      /**  ERP.EFTHead/Description  */  
   Description:string,
      /**  ERP.EFTHead/Type  */  
   Type:number,
      /**  ERP.EFTHead/Company  */  
   Company:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ElectronicInterfacesListTableset{
   ElectronicInterfaceList:Ice_Tablesets_ElectronicInterfaceListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_RelationColumnListRow{
   ColumnName:string,
   TableName:string,
   IsParentTableColumn:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RelationColumnListTableset{
   RelationColumnList:Ice_Tablesets_RelationColumnListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_RptCalcFieldRow{
      /**  Report Data Definition ID  */  
   RptDefID:string,
      /**  Report Table ID  */  
   RptTableID:string,
      /**  SystemCode  */  
   SystemCode:string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   ZDataTableID:string,
      /**  Name for Calculated Field.  When output to XML they will be written as Calc-fieldname in order to avoid conflicts with other fields in the table.  */  
   FieldName:string,
      /**  Field Label  */  
   FieldLabel:string,
      /**  Character, Date, Integer, Decimal, Logical  */  
   DataType:string,
      /**  Field Format  */  
   FieldFormat:string,
      /**  Field Length  */  
   FieldLength:number,
      /**  Field Precision  */  
   FieldPrecision:number,
      /**  Decimal Currency Dependent  */  
   DecimalCurDepended:boolean,
      /**  Value Type: G - General, C - Cost, P - Price  */  
   DecimalValueType:string,
      /**  Currency type: O - Own/Base Currency, G - Global Currency, D - Currency from Document  */  
   DecimalCurrencyType:string,
      /**  Decimal Currency code  */  
   DecimalCurCodeField:string,
      /**  Further defines the Business use of the Field  */  
   BizType:string,
      /**  Field Name from zdatatable  */  
   ZFieldName:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  */  
   DataSourceType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptCriteriaDataTableset{
   RptDataDef:Ice_Tablesets_RptDataDefRow[],
   RptCriteriaFilter:Ice_Tablesets_RptCriteriaFilterRow[],
   RptCriteriaPrompt:Ice_Tablesets_RptCriteriaPromptRow[],
   RptCriteriaSet:Ice_Tablesets_RptCriteriaSetRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_RptCriteriaFilterRow{
      /**  Company  */  
   Company:string,
      /**  RptDefID  */  
   RptDefID:string,
      /**  RptCriteriaSetID  */  
   RptCriteriaSetID:string,
      /**  FilterID  */  
   FilterID:number,
      /**  FilterName  */  
   FilterName:string,
      /**  AdapterName  */  
   AdapterName:string,
      /**  LookupField  */  
   LookupField:string,
      /**  FilterLabel  */  
   FilterLabel:string,
      /**  TabLabel  */  
   TabLabel:string,
      /**  DataType  */  
   DataType:string,
      /**  EpiGuid  */  
   EpiGuid:string,
      /**  DisplayOrder  */  
   DisplayOrder:number,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptCriteriaMappingFPListRow{
   ID:string,
   Name:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptCriteriaMappingFPListTableset{
   RptCriteriaMappingFPList:Ice_Tablesets_RptCriteriaMappingFPListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_RptCriteriaMappingRow{
      /**  Company  */  
   Company:string,
      /**  RptDefID  */  
   RptDefID:string,
      /**  RptCriteriaSetID  */  
   RptCriteriaSetID:string,
      /**  RptTableID  */  
   RptTableID:string,
      /**  ParameterID  */  
   ParameterID:string,
      /**  PromptID  */  
   PromptID:number,
      /**  FilterID  */  
   FilterID:number,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptCriteriaPromptRow{
      /**  Company  */  
   Company:string,
      /**  RptDefID  */  
   RptDefID:string,
      /**  RptCriteriaSetID  */  
   RptCriteriaSetID:string,
      /**  PromptID  */  
   PromptID:number,
      /**  PromptName  */  
   PromptName:string,
      /**  DataType  */  
   DataType:string,
      /**  Label  */  
   Label:string,
      /**  DefaultValue  */  
   DefaultValue:string,
      /**  EpiGuid  */  
   EpiGuid:string,
      /**  IsConstant  */  
   IsConstant:boolean,
      /**  ConstantValue  */  
   ConstantValue:string,
      /**  IsVisible  */  
   IsVisible:boolean,
      /**  DisplayOrder  */  
   DisplayOrder:number,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  EditorType  */  
   EditorType:string,
      /**  DataFrom  */  
   DataFrom:string,
      /**  QueryID  */  
   QueryID:string,
      /**  DisplayColumn  */  
   DisplayColumn:string,
      /**  ValueColumn  */  
   ValueColumn:string,
      /**  EFTHeadCompany  */  
   EFTHeadCompany:string,
      /**  EFTHeadUID  */  
   EFTHeadUID:number,
      /**  Use an empty string on this column, instead of null.  */  
   IsEmptyString:boolean,
   EIName:string,
   EIDescription:string,
   DefaultValueInt:number,
   DefaultValueNum:number,
   DefaultValueDatetime:string,
   IsDynamic:boolean,
   DefaultValueBit:boolean,
   ConstantValueBit:boolean,
   ConstantValueDatetime:string,
   ConstantValueNum:number,
   ConstantValueInt:number,
   UseTypedValues:boolean,
   DefaultValueDatetimeDynamic:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptCriteriaPromptValueRow{
      /**  Company  */  
   Company:string,
      /**  RptDefID  */  
   RptDefID:string,
      /**  RptCriteriaSetID  */  
   RptCriteriaSetID:string,
      /**  PromptID  */  
   PromptID:number,
      /**  ItemID  */  
   ItemID:number,
      /**  ItemValue  */  
   ItemValue:string,
      /**  ItemDescription  */  
   ItemDescription:string,
      /**  DisplayOrder  */  
   DisplayOrder:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptCriteriaSetRow{
      /**  Company  */  
   Company:string,
      /**  RptDefID  */  
   RptDefID:string,
      /**  RptCriteriaSetID  */  
   RptCriteriaSetID:string,
      /**  Description  */  
   Description:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  IsDefault  */  
   IsDefault:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptDataDefListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Report Data Definition ID  */  
   RptDefID:string,
      /**  Report Data Definition Description  */  
   RptDescription:string,
      /**   Indicates if this is a base system report data defintion. System report data defintions  can not be modified by users. This defintion corresponds to the base report programs (@ Crystal.rpt)
If the user requires modification they can make a duplicate and make the necessary changes to that version.  */  
   SystemRpt:boolean,
      /**  The Report Type similar to the one set in the Report Styles, that will help to identify which report type is this data definition intended for.  */  
   RptTypeID:string,
      /**  Used to identify which data definition was used for duplication.  */  
   DuplicateOf:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Flag to indicate Dynamic Report  */  
   DynamicReport:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptDataDefListTableset{
   RptDataDefList:Ice_Tablesets_RptDataDefListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_RptDataDefRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Report Data Definition ID  */  
   RptDefID:string,
      /**  Report Data Definition Description  */  
   RptDescription:string,
      /**   Indicates if this is a base system report data defintion. System report data defintions  can not be modified by users. This defintion corresponds to the base report programs (@ Crystal.rpt)
If the user requires modification they can make a duplicate and make the necessary changes to that version.  */  
   SystemRpt:boolean,
      /**  The Report Type similar to the one set in the Report Styles, that will help to identify which report type is this data definition intended for.  */  
   RptTypeID:string,
      /**  Used to identify which data definition was used for duplication.  */  
   DuplicateOf:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  PrimaryTable  */  
   PrimaryTable:string,
      /**  PrimaryKey1  */  
   PrimaryKey1:string,
      /**  PrimaryKey2  */  
   PrimaryKey2:string,
      /**  UseMultipleCriteria  */  
   UseMultipleCriteria:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptDataDefTableset{
   RptDataDef:Ice_Tablesets_RptDataDefRow[],
   RptTable:Ice_Tablesets_RptTableRow[],
   RptCalcField:Ice_Tablesets_RptCalcFieldRow[],
   RptExclude:Ice_Tablesets_RptExcludeRow[],
   RptLinkTable:Ice_Tablesets_RptLinkTableRow[],
   RptLinkField:Ice_Tablesets_RptLinkFieldRow[],
   RptWhereItem:Ice_Tablesets_RptWhereItemRow[],
   RptCriteriaSet:Ice_Tablesets_RptCriteriaSetRow[],
   RptCriteriaFilter:Ice_Tablesets_RptCriteriaFilterRow[],
   RptCriteriaMapping:Ice_Tablesets_RptCriteriaMappingRow[],
   RptCriteriaPrompt:Ice_Tablesets_RptCriteriaPromptRow[],
   RptCriteriaPromptValue:Ice_Tablesets_RptCriteriaPromptValueRow[],
   RptRelation:Ice_Tablesets_RptRelationRow[],
   RptRelationField:Ice_Tablesets_RptRelationFieldRow[],
   RptLiterals:Ice_Tablesets_RptLiteralsRow[],
   RptDataSourceField:Ice_Tablesets_RptDataSourceFieldRow[],
   RptDataSourceParameter:Ice_Tablesets_RptDataSourceParameterRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_RptDataSourceFieldRow{
   FieldName:string,
   QueryID:string,
      /**  Database Table Name  */  
   DBTableName:string,
      /**  Database Field Name  */  
   DBFieldName:string,
      /**  DataType  */  
   DataType:string,
      /**  Like Data Field Name  */  
   LikeDataFieldName:string,
      /**  Field Label  */  
   FieldLabel:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptDataSourceParameterRow{
      /**  RptDefID  */  
   RptDefID:string,
      /**  RptCriteriaSetID  */  
   RptCriteriaSetID:string,
      /**  RptTableID  */  
   RptTableID:string,
      /**  ParameterID  */  
   ParameterID:string,
      /**  PromptID  */  
   PromptID:number,
      /**  FilterID  */  
   FilterID:number,
      /**  Data source type.  */  
   Type:string,
      /**  Parameter data type.  */  
   ParamDataType:string,
      /**  Flag to inditate if parameter is mandatory or not.  */  
   IsMandatory:boolean,
   SkipIfEmpty:boolean,
      /**  Shows control type related to parameter: Prompt or Filter.  */  
   ControlType:string,
   ControlName:string,
   ControlDataType:string,
   QueryEI:string,
   SysRevID:number,
   Selection:boolean,
      /**  Control type in the source of the parameter.  */  
   SourceControlType:string,
   ControlNameDesc:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptExcludeRow{
      /**  Report Data Definition ID  */  
   RptDefID:string,
      /**  Report Table ID  */  
   RptTableID:string,
      /**  SystemCode  */  
   SystemCode:string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   ZDataTableID:string,
      /**  zField Name  */  
   ZFieldName:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ExcludeColumn  */  
   ExcludeColumn:boolean,
      /**  ExcludeLabel  */  
   ExcludeLabel:boolean,
      /**  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  */  
   DataSourceType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptLinkFieldRow{
      /**  Report Data Definition ID  */  
   RptDefID:string,
      /**  Report Table ID  */  
   RptTableID:string,
      /**  Report Link ID  */  
   RptLinkID:string,
      /**  SystemCode  */  
   SystemCode:string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   ZDataTableID:string,
      /**  Foreign Key component of ZLookupLink. ZLookUpLink  defines the Foreign Tables related to the RptTable.ZDataTable.  ZLookupLinkField defines the fields needed to link to it.  */  
   ZLookupID:string,
      /**  field name of the database table. DB Table is defined by  ZDataTable.DBTableName.  */  
   FieldName:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptLinkTableRow{
      /**  Report Data Definition ID  */  
   RptDefID:string,
      /**  Report Table ID  */  
   RptTableID:string,
      /**  Report Link ID  */  
   RptLinkID:string,
      /**  SystemCode  */  
   SystemCode:string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   ZDataTableID:string,
      /**  Foreign Key component of ZLookupLink. ZLookUpLink  defines the Foreign Tables related to the RptTable.ZDataTable.  ZLookupLinkField defines the fields needed to link to it.  */  
   ZLookupID:string,
      /**  Description  */  
   Description:string,
      /**  Key ID  */  
   KeyID:string,
      /**  Foreign Report Table ID  */  
   ForeignRptTableID:string,
      /**  Foreign zTable ID  */  
   ForeignZTableID:string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  */  
   DataSourceType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptLiteralsRow{
      /**  Report Data Definition ID  */  
   RptDefID:string,
      /**  Literal Name  */  
   LiteralName:string,
      /**  Literal Value  */  
   LiteralValue:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptRelationFieldRow{
      /**  Report Data Definition ID  */  
   RptDefID:string,
      /**  Report Relation ID  */  
   RelationID:string,
      /**  Sequence  */  
   Seq:number,
      /**  Parent Field Name  */  
   ParentFieldName:string,
      /**  Child Field Name  */  
   ChildFieldName:string,
      /**  Operator to use for relation between Parent and Child fields.  */  
   CompOp:string,
      /**  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  */  
   IsConst:boolean,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptRelationRow{
      /**  Report Data Definition ID  */  
   RptDefID:string,
      /**  Report Relation ID  */  
   RelationID:string,
      /**  Parent Report Table ID  */  
   ParentRptTableID:string,
      /**  ChildRptTableID  */  
   ChildRptTableID:string,
      /**  Key ID  */  
   KeyID:string,
      /**  Description  */  
   Description:string,
      /**  Valid values are "each", "first", and "last".  */  
   WhichItem:string,
      /**  "Outer" = outer-join, "" = inner-join  */  
   JoinType:string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Sequence Order to dump Relationships on the EDI Flat files.  */  
   SeqOrder:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptTableRow{
      /**  Report Data Definition ID  */  
   RptDefID:string,
      /**  ID for the Table in this report.  Usually this would be the same as the ZDataTableID, which is usually the same as the db table name. Allows us to have the data from the same physical table defined more than once in the report.  Example would be spliting the OrderMsc into something like OrderHeadMsc and OrderDtlMsc.  */  
   RptTableID:string,
      /**  SystemCode  */  
   SystemCode:string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   ZDataTableID:string,
      /**  Sequence Control  */  
   SeqControl:number,
      /**  Parent Report Table ID  */  
   ParentRptTableID:string,
      /**   Indicates if this is the Primary table of the generated Report Dataset.
Primary table defintions have an additional field, "RptLanguageID". 
The RptLanguageID field is used to link to the RptLabel table.
The RptLabel is not a database table,  it contains the translations for the literals and is present
only in the generated Report Dataset.  */  
   PrimaryTable:boolean,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  IsSystemTable  */  
   IsSystemTable:boolean,
      /**  QueryID  */  
   QueryID:string,
      /**  EFTHeadCompany  */  
   EFTHeadCompany:string,
      /**  EFTHeadUID  */  
   EFTHeadUID:number,
      /**  DB Table Type  */  
   TableType:string,
      /**  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  */  
   DataSourceType:string,
      /**  Data Source Description  */  
   DataSourceDescription:string,
      /**  Data Source Name  */  
   DataSourceName:string,
      /**  True when data source is valid and available for current company and user, otherwise is false.  */  
   IsValidDataSource:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_RptWhereItemRow{
      /**  Report Data Definition ID  */  
   RptDefID:string,
      /**  ID for the Table in this report.  Usually this would be the same as the ZDataTableID, which is usually the same as the db table name. Allows us to have the data from the same physical table defined more than once in the report.  Example would be spliting the OrderMsc into something like OrderHeadMsc and OrderDtlMsc.  */  
   RptTableID:string,
      /**  SystemCode  */  
   SystemCode:string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   ZDataTableID:string,
      /**  Sequence  */  
   Seq:number,
      /**  Field Name  */  
   FieldName:string,
      /**  Operator to use for relation between left value and right value.  */  
   CompOp:string,
      /**  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  */  
   IsConst:boolean,
      /**  To Table ID  */  
   ToTableID:string,
      /**  ToSystemCode  */  
   ToSystemCode:string,
      /**  Foreign key to ZDataTable, which has the reference to the actual DB TableName. This is Mandatory and must be valid.  */  
   ToZTableID:string,
      /**  To Field Name  */  
   ToFieldName:string,
      /**  And / Or  */  
   AndOr:string,
      /**  Negative indicator  */  
   Neg:boolean,
      /**  The constant value that will be used to compare against the selected field  */  
   RValue:string,
      /**  Number of Left Parenthesis  */  
   NumLeftP:number,
      /**  Number of Right Parenthesis  */  
   NumRightP:number,
      /**  Parent Sequence  */  
   ParentSeq:number,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   FromToday:boolean,
   FromTodayValue:number,
   LeftP:string,
   RightP:string,
   RValueDate:string,
   RValueNumber:number,
      /**  Constanst value caracter field  */  
   RValueChar:string,
      /**  Constant value Boolean  */  
   RValueBool:boolean,
      /**  Constant Value Integer  */  
   RValueInt:number,
      /**  Field Type  */  
   FieldType:string,
      /**  Field required existing in child view tables of "RptTable" table to work with EpiDataView.StaticFilter  */  
   DataSourceType:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SelectLinkDataTableset{
   SelectLinkTable:Ice_Tablesets_SelectLinkTableRow[],
   SelectLinkField:Ice_Tablesets_SelectLinkFieldRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_SelectLinkFieldRow{
   FieldName:string,
   LookupID:string,
   RowSelected:boolean,
   RptTableID:string,
   SystemCode:string,
   ZDataTableID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_SelectLinkTableRow{
      /**  Lookup ID from ZLookupLink  */  
   LookupID:string,
   RowSelected:boolean,
   RptTableID:string,
   SystemCode:string,
   ZDataTableID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UpdExtRptDataDefTableset{
   RptDataDef:Ice_Tablesets_RptDataDefRow[],
   RptTable:Ice_Tablesets_RptTableRow[],
   RptCalcField:Ice_Tablesets_RptCalcFieldRow[],
   RptExclude:Ice_Tablesets_RptExcludeRow[],
   RptLinkTable:Ice_Tablesets_RptLinkTableRow[],
   RptLinkField:Ice_Tablesets_RptLinkFieldRow[],
   RptWhereItem:Ice_Tablesets_RptWhereItemRow[],
   RptCriteriaSet:Ice_Tablesets_RptCriteriaSetRow[],
   RptCriteriaFilter:Ice_Tablesets_RptCriteriaFilterRow[],
   RptCriteriaMapping:Ice_Tablesets_RptCriteriaMappingRow[],
   RptCriteriaPrompt:Ice_Tablesets_RptCriteriaPromptRow[],
   RptCriteriaPromptValue:Ice_Tablesets_RptCriteriaPromptValueRow[],
   RptRelation:Ice_Tablesets_RptRelationRow[],
   RptRelationField:Ice_Tablesets_RptRelationFieldRow[],
   RptLiterals:Ice_Tablesets_RptLiteralsRow[],
   RptDataSourceField:Ice_Tablesets_RptDataSourceFieldRow[],
   RptDataSourceParameter:Ice_Tablesets_RptDataSourceParameterRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param version
      @param data
   */  
export interface ImportElectronicInterface_input{
   version:string,
   data:any,      //schema had no properties on an object.
}

export interface ImportElectronicInterface_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param importFileName
   */  
export interface ImportReportEx_input{
      /**  The file name with report data to import.  */  
   importFileName:string,
}

export interface ImportReportEx_output{
      /**  The RDDs name of imported file.  */  
   returnObj:string,
}

   /** Required : 
      @param reportData
   */  
export interface ImportReport_input{
      /**  The report data to import.  */  
   reportData:string,
}

export interface ImportReport_output{
      /**  The RDDs imported.  */  
   returnObj:string,
}

   /** Required : 
      @param ds
      @param queryID
   */  
export interface OnChangeQueryID_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
   queryID:string,
}

export interface OnChangeQueryID_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
   queryID:string,
   opMessage:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtRptDataDefTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtRptDataDefTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_RptDataDefTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_RptDataDefTableset,
}
}

   /** Required : 
      @param rptDefId
   */  
export interface ValidateBAQDataSource_input{
   rptDefId:string,
}

export interface ValidateBAQDataSource_output{
}

   /** Required : 
      @param rptDefId
   */  
export interface ValidateRptLabels_input{
   rptDefId:string,
}

export interface ValidateRptLabels_output{
}

