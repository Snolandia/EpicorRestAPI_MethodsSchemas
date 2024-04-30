import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.ZDataTableSvc
// Description: The ZDataTable service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get ZDataTables items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZDataTables
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZDataTableRow
   */  
export function get_ZDataTables(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZDataTables
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZDataTableRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ZDataTableRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ZDataTables(requestBody:Ice_Tablesets_ZDataTableRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ZDataTable item
   Description: Calls GetByID to retrieve the ZDataTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZDataTable
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ZDataTableRow
   */  
export function get_ZDataTables_SystemCode_DataTableID(SystemCode:string, DataTableID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ZDataTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_ZDataTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ZDataTable for the service
   Description: Calls UpdateExt to update ZDataTable. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZDataTable
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZDataTableRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ZDataTables_SystemCode_DataTableID(SystemCode:string, DataTableID:string, requestBody:Ice_Tablesets_ZDataTableRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")", {
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
   Summary: Call UpdateExt to delete ZDataTable item
   Description: Call UpdateExt to delete ZDataTable item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZDataTable
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ZDataTables_SystemCode_DataTableID(SystemCode:string, DataTableID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")", {
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
   Description: Get ZLookupLinks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZLookupLinks1
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZLookupLinkRow
   */  
export function get_ZDataTables_SystemCode_DataTableID_ZLookupLinks(SystemCode:string, DataTableID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLookupLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")/ZLookupLinks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLookupLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ZLookupLink item
   Description: Calls GetByID to retrieve the ZLookupLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZLookupLink1
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LookupID Desc: LookupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ZLookupLinkRow
   */  
export function get_ZDataTables_SystemCode_DataTableID_ZLookupLinks_SystemCode_DataTableID_LookupID(SystemCode:string, DataTableID:string, LookupID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ZLookupLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_ZLookupLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ZDataFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZDataFields1
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZDataFieldRow
   */  
export function get_ZDataTables_SystemCode_DataTableID_ZDataFields(SystemCode:string, DataTableID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")/ZDataFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ZDataField item
   Description: Calls GetByID to retrieve the ZDataField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZDataField1
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ZDataFieldRow
   */  
export function get_ZDataTables_SystemCode_DataTableID_ZDataFields_SystemCode_DataTableID_FieldName(SystemCode:string, DataTableID:string, FieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ZDataFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")/ZDataFields(" + SystemCode + "," + DataTableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_ZDataFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ZKeys items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZKeys1
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZKeyRow
   */  
export function get_ZDataTables_SystemCode_DataTableID_ZKeys(SystemCode:string, DataTableID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZKeyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")/ZKeys", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZKeyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ZKey item
   Description: Calls GetByID to retrieve the ZKey item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZKey1
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param KeyID Desc: KeyID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ZKeyRow
   */  
export function get_ZDataTables_SystemCode_DataTableID_ZKeys_SystemCode_DataTableID_KeyID(SystemCode:string, DataTableID:string, KeyID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ZKeyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataTables(" + SystemCode + "," + DataTableID + ")/ZKeys(" + SystemCode + "," + DataTableID + "," + KeyID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_ZKeyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ZLookupLinks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZLookupLinks
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZLookupLinkRow
   */  
export function get_ZLookupLinks(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLookupLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLookupLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZLookupLinks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZLookupLinkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ZLookupLinkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ZLookupLinks(requestBody:Ice_Tablesets_ZLookupLinkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ZLookupLink item
   Description: Calls GetByID to retrieve the ZLookupLink item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZLookupLink
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LookupID Desc: LookupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ZLookupLinkRow
   */  
export function get_ZLookupLinks_SystemCode_DataTableID_LookupID(SystemCode:string, DataTableID:string, LookupID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ZLookupLinkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_ZLookupLinkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ZLookupLink for the service
   Description: Calls UpdateExt to update ZLookupLink. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZLookupLink
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LookupID Desc: LookupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZLookupLinkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ZLookupLinks_SystemCode_DataTableID_LookupID(SystemCode:string, DataTableID:string, LookupID:string, requestBody:Ice_Tablesets_ZLookupLinkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")", {
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
   Summary: Call UpdateExt to delete ZLookupLink item
   Description: Call UpdateExt to delete ZLookupLink item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZLookupLink
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LookupID Desc: LookupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ZLookupLinks_SystemCode_DataTableID_LookupID(SystemCode:string, DataTableID:string, LookupID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")", {
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
   Description: Get ZLinkColumns items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZLinkColumns1
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LookupID Desc: LookupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZLinkColumnRow
   */  
export function get_ZLookupLinks_SystemCode_DataTableID_LookupID_ZLinkColumns(SystemCode:string, DataTableID:string, LookupID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLinkColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")/ZLinkColumns", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLinkColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ZLinkColumn item
   Description: Calls GetByID to retrieve the ZLinkColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZLinkColumn1
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LookupID Desc: LookupID   Required: True   Allow empty value : True
      @param LinkID Desc: LinkID   Required: True   Allow empty value : True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ZLinkColumnRow
   */  
export function get_ZLookupLinks_SystemCode_DataTableID_LookupID_ZLinkColumns_SystemCode_DataTableID_LinkID_SysRowID(SystemCode:string, DataTableID:string, LookupID:string, LinkID:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ZLinkColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")/ZLinkColumns(" + SystemCode + "," + DataTableID + "," + LinkID + "," + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_ZLinkColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ZLookupFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZLookupFields1
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LookupID Desc: LookupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZLookupFieldRow
   */  
export function get_ZLookupLinks_SystemCode_DataTableID_LookupID_ZLookupFields(SystemCode:string, DataTableID:string, LookupID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLookupFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")/ZLookupFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLookupFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ZLookupField item
   Description: Calls GetByID to retrieve the ZLookupField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZLookupField1
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LookupID Desc: LookupID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ZLookupFieldRow
   */  
export function get_ZLookupLinks_SystemCode_DataTableID_LookupID_ZLookupFields_SystemCode_DataTableID_LookupID_Seq(SystemCode:string, DataTableID:string, LookupID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ZLookupFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupLinks(" + SystemCode + "," + DataTableID + "," + LookupID + ")/ZLookupFields(" + SystemCode + "," + DataTableID + "," + LookupID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_ZLookupFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ZLinkColumns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZLinkColumns
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZLinkColumnRow
   */  
export function get_ZLinkColumns(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLinkColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLinkColumns", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLinkColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZLinkColumns
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZLinkColumnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ZLinkColumnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ZLinkColumns(requestBody:Ice_Tablesets_ZLinkColumnRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLinkColumns", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ZLinkColumn item
   Description: Calls GetByID to retrieve the ZLinkColumn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZLinkColumn
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LinkID Desc: LinkID   Required: True   Allow empty value : True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ZLinkColumnRow
   */  
export function get_ZLinkColumns_SystemCode_DataTableID_LinkID_SysRowID(SystemCode:string, DataTableID:string, LinkID:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ZLinkColumnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLinkColumns(" + SystemCode + "," + DataTableID + "," + LinkID + "," + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_ZLinkColumnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ZLinkColumn for the service
   Description: Calls UpdateExt to update ZLinkColumn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZLinkColumn
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LinkID Desc: LinkID   Required: True   Allow empty value : True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZLinkColumnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ZLinkColumns_SystemCode_DataTableID_LinkID_SysRowID(SystemCode:string, DataTableID:string, LinkID:string, SysRowID:string, requestBody:Ice_Tablesets_ZLinkColumnRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLinkColumns(" + SystemCode + "," + DataTableID + "," + LinkID + "," + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete ZLinkColumn item
   Description: Call UpdateExt to delete ZLinkColumn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZLinkColumn
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LinkID Desc: LinkID   Required: True   Allow empty value : True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ZLinkColumns_SystemCode_DataTableID_LinkID_SysRowID(SystemCode:string, DataTableID:string, LinkID:string, SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLinkColumns(" + SystemCode + "," + DataTableID + "," + LinkID + "," + SysRowID + ")", {
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
   Description: Get ZLookupFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZLookupFields
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZLookupFieldRow
   */  
export function get_ZLookupFields(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLookupFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLookupFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZLookupFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZLookupFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ZLookupFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ZLookupFields(requestBody:Ice_Tablesets_ZLookupFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ZLookupField item
   Description: Calls GetByID to retrieve the ZLookupField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZLookupField
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LookupID Desc: LookupID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ZLookupFieldRow
   */  
export function get_ZLookupFields_SystemCode_DataTableID_LookupID_Seq(SystemCode:string, DataTableID:string, LookupID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ZLookupFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupFields(" + SystemCode + "," + DataTableID + "," + LookupID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_ZLookupFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ZLookupField for the service
   Description: Calls UpdateExt to update ZLookupField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZLookupField
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LookupID Desc: LookupID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZLookupFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ZLookupFields_SystemCode_DataTableID_LookupID_Seq(SystemCode:string, DataTableID:string, LookupID:string, Seq:string, requestBody:Ice_Tablesets_ZLookupFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupFields(" + SystemCode + "," + DataTableID + "," + LookupID + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete ZLookupField item
   Description: Call UpdateExt to delete ZLookupField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZLookupField
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param LookupID Desc: LookupID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ZLookupFields_SystemCode_DataTableID_LookupID_Seq(SystemCode:string, DataTableID:string, LookupID:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZLookupFields(" + SystemCode + "," + DataTableID + "," + LookupID + "," + Seq + ")", {
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
   Description: Get ZDataFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZDataFields
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZDataFieldRow
   */  
export function get_ZDataFields(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZDataFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZDataFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ZDataFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ZDataFields(requestBody:Ice_Tablesets_ZDataFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ZDataField item
   Description: Calls GetByID to retrieve the ZDataField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZDataField
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ZDataFieldRow
   */  
export function get_ZDataFields_SystemCode_DataTableID_FieldName(SystemCode:string, DataTableID:string, FieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ZDataFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataFields(" + SystemCode + "," + DataTableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_ZDataFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ZDataField for the service
   Description: Calls UpdateExt to update ZDataField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZDataField
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZDataFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ZDataFields_SystemCode_DataTableID_FieldName(SystemCode:string, DataTableID:string, FieldName:string, requestBody:Ice_Tablesets_ZDataFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataFields(" + SystemCode + "," + DataTableID + "," + FieldName + ")", {
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
   Summary: Call UpdateExt to delete ZDataField item
   Description: Call UpdateExt to delete ZDataField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZDataField
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ZDataFields_SystemCode_DataTableID_FieldName(SystemCode:string, DataTableID:string, FieldName:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZDataFields(" + SystemCode + "," + DataTableID + "," + FieldName + ")", {
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
   Description: Get ZKeys items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZKeys
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZKeyRow
   */  
export function get_ZKeys(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZKeyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZKeyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZKeys
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZKeyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ZKeyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ZKeys(requestBody:Ice_Tablesets_ZKeyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ZKey item
   Description: Calls GetByID to retrieve the ZKey item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZKey
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param KeyID Desc: KeyID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ZKeyRow
   */  
export function get_ZKeys_SystemCode_DataTableID_KeyID(SystemCode:string, DataTableID:string, KeyID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ZKeyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys(" + SystemCode + "," + DataTableID + "," + KeyID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_ZKeyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ZKey for the service
   Description: Calls UpdateExt to update ZKey. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZKey
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param KeyID Desc: KeyID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZKeyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ZKeys_SystemCode_DataTableID_KeyID(SystemCode:string, DataTableID:string, KeyID:string, requestBody:Ice_Tablesets_ZKeyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys(" + SystemCode + "," + DataTableID + "," + KeyID + ")", {
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
   Summary: Call UpdateExt to delete ZKey item
   Description: Call UpdateExt to delete ZKey item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZKey
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param KeyID Desc: KeyID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ZKeys_SystemCode_DataTableID_KeyID(SystemCode:string, DataTableID:string, KeyID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys(" + SystemCode + "," + DataTableID + "," + KeyID + ")", {
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
   Description: Get ZKeyFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ZKeyFields1
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param KeyID Desc: KeyID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZKeyFieldRow
   */  
export function get_ZKeys_SystemCode_DataTableID_KeyID_ZKeyFields(SystemCode:string, DataTableID:string, KeyID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZKeyFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys(" + SystemCode + "," + DataTableID + "," + KeyID + ")/ZKeyFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZKeyFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ZKeyField item
   Description: Calls GetByID to retrieve the ZKeyField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZKeyField1
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param KeyID Desc: KeyID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ZKeyFieldRow
   */  
export function get_ZKeys_SystemCode_DataTableID_KeyID_ZKeyFields_SystemCode_DataTableID_KeyID_Seq(SystemCode:string, DataTableID:string, KeyID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ZKeyFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeys(" + SystemCode + "," + DataTableID + "," + KeyID + ")/ZKeyFields(" + SystemCode + "," + DataTableID + "," + KeyID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_ZKeyFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ZKeyFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ZKeyFields
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZKeyFieldRow
   */  
export function get_ZKeyFields(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZKeyFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeyFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZKeyFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ZKeyFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ZKeyFieldRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ZKeyFieldRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ZKeyFields(requestBody:Ice_Tablesets_ZKeyFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeyFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ZKeyField item
   Description: Calls GetByID to retrieve the ZKeyField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ZKeyField
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param KeyID Desc: KeyID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ZKeyFieldRow
   */  
export function get_ZKeyFields_SystemCode_DataTableID_KeyID_Seq(SystemCode:string, DataTableID:string, KeyID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ZKeyFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeyFields(" + SystemCode + "," + DataTableID + "," + KeyID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_ZKeyFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ZKeyField for the service
   Description: Calls UpdateExt to update ZKeyField. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ZKeyField
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param KeyID Desc: KeyID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ZKeyFieldRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ZKeyFields_SystemCode_DataTableID_KeyID_Seq(SystemCode:string, DataTableID:string, KeyID:string, Seq:string, requestBody:Ice_Tablesets_ZKeyFieldRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeyFields(" + SystemCode + "," + DataTableID + "," + KeyID + "," + Seq + ")", {
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
   Summary: Call UpdateExt to delete ZKeyField item
   Description: Call UpdateExt to delete ZKeyField item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ZKeyField
      @param SystemCode Desc: SystemCode   Required: True   Allow empty value : True
      @param DataTableID Desc: DataTableID   Required: True   Allow empty value : True
      @param KeyID Desc: KeyID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ZKeyFields_SystemCode_DataTableID_KeyID_Seq(SystemCode:string, DataTableID:string, KeyID:string, Seq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ZKeyFields(" + SystemCode + "," + DataTableID + "," + KeyID + "," + Seq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ZDataTableListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataTableListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataTableListRow)
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
export function get_GetRows(whereClauseZDataTable:string, whereClauseZLookupLink:string, whereClauseZLinkColumn:string, whereClauseZLookupField:string, whereClauseZDataField:string, whereClauseZKey:string, whereClauseZKeyField:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseZDataTable!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseZDataTable=" + whereClauseZDataTable
   }
   if(typeof whereClauseZLookupLink!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseZLookupLink=" + whereClauseZLookupLink
   }
   if(typeof whereClauseZLinkColumn!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseZLinkColumn=" + whereClauseZLinkColumn
   }
   if(typeof whereClauseZLookupField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseZLookupField=" + whereClauseZLookupField
   }
   if(typeof whereClauseZDataField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseZDataField=" + whereClauseZDataField
   }
   if(typeof whereClauseZKey!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseZKey=" + whereClauseZKey
   }
   if(typeof whereClauseZKeyField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseZKeyField=" + whereClauseZKeyField
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(systemCode:string, dataTableID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof systemCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "systemCode=" + systemCode
   }
   if(typeof dataTableID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "dataTableID=" + dataTableID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method ChangeLikeDataFieldName
   Description: This method should be invoked when the LikeFieldName changes.
   OperationID: ChangeLikeDataFieldName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeLikeDataFieldName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLikeDataFieldName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLikeDataFieldName(requestBody:ChangeLikeDataFieldName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeLikeDataFieldName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ChangeLikeDataFieldName", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeLikeDataFieldName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetKeyFields
   Description: Get key fields.
   OperationID: GetKeyFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetKeyFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKeyFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetKeyFields(requestBody:GetKeyFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetKeyFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetKeyFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetKeyFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetKeys
   Description: Get key fields for table
   OperationID: GetKeys
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetKeys_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetKeys_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetKeys(requestBody:GetKeys_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetKeys_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetKeys", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetKeys_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateGuid
   Description: Validate the GUID
   OperationID: ValidateGuid
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateGuid_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGuid_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateGuid(requestBody:ValidateGuid_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateGuid_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ValidateGuid", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateGuid_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateNFormatString
   Description: Get the formated string
   OperationID: ValidateNFormatString
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateNFormatString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNFormatString_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateNFormatString(requestBody:ValidateNFormatString_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateNFormatString_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ValidateNFormatString", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateNFormatString_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateNFormatNumber
   Description: Get the formated number
   OperationID: ValidateNFormatNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateNFormatNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNFormatNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateNFormatNumber(requestBody:ValidateNFormatNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateNFormatNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ValidateNFormatNumber", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateNFormatNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Synchronize
   Description: Synchronize one table
   OperationID: Synchronize
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Synchronize_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Synchronize_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Synchronize(requestBody:Synchronize_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Synchronize_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/Synchronize", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Synchronize_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SynchronizeClass
   Description: Synchronize all the tables of a class
   OperationID: SynchronizeClass
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SynchronizeClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SynchronizeClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SynchronizeClass(requestBody:SynchronizeClass_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SynchronizeClass_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/SynchronizeClass", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SynchronizeClass_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HasDBTable
   Description: Checks if DB table exists in database
   OperationID: HasDBTable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HasDBTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasDBTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HasDBTable(requestBody:HasDBTable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HasDBTable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/HasDBTable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as HasDBTable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HasZDataTable
   Description: Checks if DB table exists in database
   OperationID: HasZDataTable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HasZDataTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasZDataTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HasZDataTable(requestBody:HasZDataTable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HasZDataTable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/HasZDataTable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as HasZDataTable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExtendedTableSyncInfo
   Description: Get extended table sync information.
   OperationID: GetExtendedTableSyncInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetExtendedTableSyncInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExtendedTableSyncInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExtendedTableSyncInfo(requestBody:GetExtendedTableSyncInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetExtendedTableSyncInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetExtendedTableSyncInfo", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetExtendedTableSyncInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetExtendedTableSyncDetailsMessage
   Description: Get extended table sync information.
   OperationID: GetExtendedTableSyncDetailsMessage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetExtendedTableSyncDetailsMessage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExtendedTableSyncDetailsMessage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetExtendedTableSyncDetailsMessage(requestBody:GetExtendedTableSyncDetailsMessage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetExtendedTableSyncDetailsMessage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetExtendedTableSyncDetailsMessage", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetExtendedTableSyncDetailsMessage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CanModifyUDFieldFormat
   Description: Check if UD Field Format can be modified
   OperationID: CanModifyUDFieldFormat
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CanModifyUDFieldFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CanModifyUDFieldFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CanModifyUDFieldFormat(requestBody:CanModifyUDFieldFormat_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CanModifyUDFieldFormat_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/CanModifyUDFieldFormat", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CanModifyUDFieldFormat_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClassicFieldName
   Description: Check if UD Field Name is the classic fieldName
   OperationID: ClassicFieldName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ClassicFieldName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClassicFieldName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClassicFieldName(requestBody:ClassicFieldName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ClassicFieldName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/ClassicFieldName", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ClassicFieldName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewZDataTable
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZDataTable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewZDataTable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZDataTable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewZDataTable(requestBody:GetNewZDataTable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewZDataTable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetNewZDataTable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewZDataTable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewZLookupLink
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZLookupLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewZLookupLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZLookupLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewZLookupLink(requestBody:GetNewZLookupLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewZLookupLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetNewZLookupLink", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewZLookupLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewZLinkColumn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZLinkColumn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewZLinkColumn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZLinkColumn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewZLinkColumn(requestBody:GetNewZLinkColumn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewZLinkColumn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetNewZLinkColumn", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewZLinkColumn_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewZLookupField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZLookupField
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewZLookupField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZLookupField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewZLookupField(requestBody:GetNewZLookupField_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewZLookupField_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetNewZLookupField", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewZLookupField_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewZDataField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZDataField
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewZDataField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZDataField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewZDataField(requestBody:GetNewZDataField_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewZDataField_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetNewZDataField", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewZDataField_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewZKey
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZKey
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewZKey_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZKey_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewZKey(requestBody:GetNewZKey_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewZKey_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetNewZKey", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewZKey_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewZKeyField
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewZKeyField
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewZKeyField_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewZKeyField_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewZKeyField(requestBody:GetNewZKeyField_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewZKeyField_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetNewZKeyField", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewZKeyField_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ZDataTableSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataFieldRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ZDataFieldRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataTableListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ZDataTableListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZDataTableRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ZDataTableRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZKeyFieldRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ZKeyFieldRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZKeyRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ZKeyRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLinkColumnRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ZLinkColumnRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLookupFieldRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ZLookupFieldRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ZLookupLinkRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ZLookupLinkRow,
}

export interface Ice_Tablesets_ZDataFieldRow{
      /**  SystemCode  */  
   "SystemCode":string,
      /**  DataTable ID  */  
   "DataTableID":string,
      /**  Field Name  */  
   "FieldName":string,
      /**  Sequence  */  
   "Seq":number,
      /**  Database Table Name  */  
   "DBTableName":string,
      /**  Data Type  */  
   "DataType":string,
      /**  Required  */  
   "Required":boolean,
      /**  Read Only  */  
   "ReadOnly":boolean,
      /**  Description  */  
   "Description":string,
      /**  External  */  
   "External":boolean,
      /**  Formula  */  
   "Formula":string,
      /**  Included  */  
   "Included":boolean,
      /**  Field Format  */  
   "FieldFormat":string,
      /**  Field Scale  */  
   "FieldScale":number,
      /**  Field Label  */  
   "FieldLabel":string,
      /**  Initial Value  */  
   "InitialValue":string,
      /**  Indicates Data Field is a Description Field  */  
   "IsDescriptionField":boolean,
      /**  LikeDataFieldSystemCode  */  
   "LikeDataFieldSystemCode":string,
      /**  TableID to use with LikeField  */  
   "LikeDataFieldTableID":string,
      /**  A delimited list of the modules required by this object.  */  
   "RequiredModules":string,
      /**  Contains the characters that are used as delimiters for when building a list from values of this data field. So during data entry we should validate none of these charater is in the value of this data field.  */  
   "Delimiters":string,
      /**  Code and Description value list  */  
   "CodeDescriptionList":string,
      /**  Like Data Fiel Name reference  */  
   "LikeDataFieldName":string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   "SystemFlag":boolean,
      /**  Indicates Data Field is a Currency code column  */  
   "CurrencyCodeColumn":string,
      /**  Currency Type  */  
   "CurrencyType":string,
      /**  Currency Source  */  
   "CurrencySource":string,
      /**   Further defines the Business use of the Field
Valid values are "Currency,Quantity,UOM"  */  
   "BizType":string,
      /**  UDLikeDataFieldSystemCode  */  
   "UDLikeDataFieldSystemCode":string,
      /**  TableID to use with LikeField  */  
   "UDLikeDataFieldTableID":string,
      /**  User Defined Extended Property Like Data Field Name.  */  
   "UDLikeDataFieldName":string,
      /**  User Defined Extended Property Field Property  */  
   "UDFieldFormat":string,
      /**  User Defined Extended Property Field Label  */  
   "UDFieldLabel":string,
      /**  User Defined Extended Property Initial Value  */  
   "UDInitialValue":string,
      /**  User Defined Extended Property Required flag  */  
   "UDRequired":boolean,
      /**  User Defined Extended Property Read Only flag  */  
   "UDReadOnly":boolean,
      /**  User Defined Extended Property Currency code column flag  */  
   "UDCurrencyCodeColumn":string,
      /**  User Defined Extended Property Currency Type  */  
   "UDCurrencyType":string,
      /**  User Defined Extended Property currency Source  */  
   "UDCurrencySource":string,
      /**  UDPredictiveSearchID  */  
   "UDPredictiveSearchID":string,
      /**  CGCCode  */  
   "CGCCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  CausesOnChange  */  
   "CausesOnChange":boolean,
   "DefaultFieldScale":number,
   "DefaultFormat":string,
   "DefaultInitValue":string,
   "DefaultLabel":string,
      /**  DelimiterCheck  */  
   "DelimiterCheck":boolean,
   "EffectiveCurrencySource":string,
   "EffectiveCurrencyType":string,
   "LinkedColumn":string,
      /**  UD Code Type  */  
   "UDCodeType":string,
      /**  UD Linked Column  */  
   "UDLinkedColumn":string,
      /**  UD UOM Column  */  
   "UDUomColumn":string,
   "UomColumn":string,
      /**  Zone Baq ID  */  
   "ZoneBAQ":string,
      /**  Allow Zone Search When control is Empty  */  
   "ZoneSearchOnEmptyControl":boolean,
   "Company":string,
   "IsHidden":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ZDataTableListRow{
      /**  SystemCode  */  
   "SystemCode":string,
      /**  DataTable ID  */  
   "DataTableID":string,
      /**  Description  */  
   "Description":string,
      /**  SchemaName  */  
   "SchemaName":string,
      /**  Database TableName  */  
   "DBTableName":string,
      /**  Where Clause  */  
   "WhereClause":string,
      /**  If yes then this table is restricted by accessiable sales territories  */  
   "RestrictedByTer":boolean,
      /**  If yes then this table is restricted by accessiable Sites  */  
   "RestrictedByPlant":boolean,
      /**   DB = Database, TT = Temp Table, RP = Report Parameter, PP = Process Parameter. This value can be used for filtering table searches, controling sensitivity of fields, and controlling references by datasets.
Field sensitivity rules based on this value are  */  
   "TableType":string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   "SystemFlag":boolean,
      /**  A descriptive label for the table that the system may use in the construction of a message. Ex: Can not delete one or more "Bill of Lading" records exist.  Where Bill of Lading is the label. Which is much better that use the table name "BOLHead".  */  
   "TableLabel":string,
      /**  Identifier value the system will use when creating Change Log records for this specific table (ChgLog.Indentifier)  ChgLogID must be the same for a set of related tables. For example: Customer, ShipTo, CustBillTo, CustCnt, are all related and will have a ChgLogID = "Customer".  TIP: Using the tablename of the highest level parent table as the ChgLogID may avoid   accidental duplication.  */  
   "ChgLogID":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ZDataTableRow{
      /**  SystemCode  */  
   "SystemCode":string,
      /**  DataTable ID  */  
   "DataTableID":string,
      /**  Description  */  
   "Description":string,
      /**  SchemaName  */  
   "SchemaName":string,
      /**  Database TableName  */  
   "DBTableName":string,
      /**  Where Clause  */  
   "WhereClause":string,
      /**  If yes then this table is restricted by accessiable sales territories  */  
   "RestrictedByTer":boolean,
      /**  If yes then this table is restricted by accessiable Sites  */  
   "RestrictedByPlant":boolean,
      /**  controls the behavior of  object designer field synchronization with the db schema. When set True, the synch process will bring in all the DB fields from a DB table into the zDataFields table. When set to False, the synch process will only update the fields that are currently in the zDataFields table.  */  
   "FullSync":boolean,
      /**   DB = Database, TT = Temp Table, RP = Report Parameter, PP = Process Parameter. This value can be used for filtering table searches, controling sensitivity of fields, and controlling references by datasets.
Field sensitivity rules based on this value are  */  
   "TableType":string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   "SystemFlag":boolean,
      /**  A descriptive label for the table that the system may use in the construction of a message. Ex: Can not delete one or more "Bill of Lading" records exist.  Where Bill of Lading is the label. Which is much better that use the table name "BOLHead".  */  
   "TableLabel":string,
      /**  Identifier value the system will use when creating Change Log records for this specific table (ChgLog.Indentifier)  ChgLogID must be the same for a set of related tables. For example: Customer, ShipTo, CustBillTo, CustCnt, are all related and will have a ChgLogID = "Customer".  TIP: Using the tablename of the highest level parent table as the ChgLogID may avoid   accidental duplication.  */  
   "ChgLogID":string,
      /**  BO Used to Update Table  */  
   "BOUpdate":string,
      /**  BO Method used for Update  */  
   "UpdateMethod":string,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  Interface  */  
   "Interface":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ZKeyFieldRow{
      /**  SystemCode  */  
   "SystemCode":string,
      /**  DataTable ID  */  
   "DataTableID":string,
      /**  Key ID  */  
   "KeyID":string,
      /**  Sequence  */  
   "Seq":number,
      /**  Field Name  */  
   "FieldName":string,
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

export interface Ice_Tablesets_ZKeyRow{
      /**  SystemCode  */  
   "SystemCode":string,
      /**  DataTable ID  */  
   "DataTableID":string,
      /**  Key ID  */  
   "KeyID":string,
      /**  Description  */  
   "Description":string,
      /**  Primary Key  */  
   "IsPrimaryKey":boolean,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   "SystemFlag":boolean,
      /**  External Key  */  
   "External":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ZLinkColumnRow{
      /**  SystemCode  */  
   "SystemCode":string,
      /**  DataTable ID  */  
   "DataTableID":string,
      /**  Link ID  */  
   "LinkID":string,
      /**  Field Name  */  
   "FieldName":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  LinkColName  */  
   "LinkColName":string,
   "BitFlag":number,
   "ZLookupLinkForeignDataTableID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ZLookupFieldRow{
      /**  SystemCode  */  
   "SystemCode":string,
      /**  DataTable ID  */  
   "DataTableID":string,
      /**  LookUp ID  */  
   "LookupID":string,
      /**  Sequence  */  
   "Seq":number,
      /**  Field Name  */  
   "FieldName":string,
      /**  Constant Field indicator  */  
   "IsConst":boolean,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "ForeignFieldName":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ZLookupLinkRow{
      /**  SystemCode  */  
   "SystemCode":string,
      /**  DataTable ID  */  
   "DataTableID":string,
      /**  LookUp ID  */  
   "LookupID":string,
      /**  ForeignSystemCode  */  
   "ForeignSystemCode":string,
      /**  Foreign DataTable ID  */  
   "ForeignDataTableID":string,
      /**  Key ID  */  
   "KeyID":string,
      /**  Description  */  
   "Description":string,
      /**  Validation Required  */  
   "ValidationRequired":boolean,
      /**  Extra validation  */  
   "ValidationPhraseEx":string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   "SystemFlag":boolean,
      /**  Indicating this lookup link is not used for pulling the IsDisplayField  to the master table but for checking referential integraty.  */  
   "ValidationOnly":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
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
      @param ts
   */  
export interface CanModifyUDFieldFormat_input{
   ts:Ice_Tablesets_ZDataTableTableset[],
}

export interface CanModifyUDFieldFormat_output{
      /**  True if can be modified  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   message:string,
}
}

   /** Required : 
      @param systemCode
      @param dataTableID
      @param fieldName
      @param dbTableName
      @param external
      @param likeDataFieldSystemCode
      @param likeDataFieldTableID
      @param likeDataFieldName
   */  
export interface ChangeLikeDataFieldName_input{
   systemCode:string,
   dataTableID:string,
   fieldName:string,
   dbTableName:string,
   external:boolean,
   likeDataFieldSystemCode:string,
   likeDataFieldTableID:string,
   likeDataFieldName:string,
}

export interface ChangeLikeDataFieldName_output{
parameters : {
      /**  output parameters  */  
   defaultFormat:string,
   defaultLabel:string,
   defaultInitValue:string,
   defaultFieldScale:number,
}
}

   /** Required : 
      @param fieldName
   */  
export interface ClassicFieldName_input{
      /**  data (only need the field row)  */  
   fieldName:string,
}

export interface ClassicFieldName_output{
      /**  True if can be modified  */  
   returnObj:boolean,
}

   /** Required : 
      @param systemCode
      @param dataTableID
   */  
export interface DeleteByID_input{
   systemCode:string,
   dataTableID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param systemCode
      @param dataTableID
   */  
export interface GetByID_input{
   systemCode:string,
   dataTableID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_ZDataTableTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_ZDataTableTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_ZDataTableTableset[],
}

   /** Required : 
      @param schemaName
      @param tableName
   */  
export interface GetExtendedTableSyncDetailsMessage_input{
      /**  Schema name (Ice, Erp)  */  
   schemaName:string,
      /**  table name (e.g. Tip_UD)  */  
   tableName:string,
}

export interface GetExtendedTableSyncDetailsMessage_output{
      /**  True if everything is in sync  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   dbExists:boolean,
   zDataSynced:boolean,
   dataModelSynced:boolean,
   syncMessage:string,
}
}

   /** Required : 
      @param schemaName
      @param tableName
   */  
export interface GetExtendedTableSyncInfo_input{
      /**  Schema name (Ice, Erp)  */  
   schemaName:string,
      /**  table name (e.g. Tip_UD)  */  
   tableName:string,
}

export interface GetExtendedTableSyncInfo_output{
      /**  True if everything is in sync  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   dbExists:boolean,
   zDataSynced:boolean,
   dataModelSynced:boolean,
}
}

   /** Required : 
      @param systemCode
      @param dataTableID
      @param keyID
   */  
export interface GetKeyFields_input{
   systemCode:string,
      /**  Table ID  */  
   dataTableID:string,
      /**  Proposed KeyID  */  
   keyID:string,
}

export interface GetKeyFields_output{
   returnObj:Ice_Tablesets_ZDataTableTableset[],
}

   /** Required : 
      @param systemCode
      @param dataTableID
   */  
export interface GetKeys_input{
   systemCode:string,
      /**  Table ID  */  
   dataTableID:string,
}

export interface GetKeys_output{
   returnObj:Ice_Tablesets_ZDataTableTableset[],
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
   returnObj:Ice_Tablesets_ZDataTableListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param systemCode
      @param dataTableID
   */  
export interface GetNewZDataField_input{
   ds:Ice_Tablesets_ZDataTableTableset[],
   systemCode:string,
   dataTableID:string,
}

export interface GetNewZDataField_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ZDataTableTableset,
}
}

   /** Required : 
      @param ds
      @param systemCode
   */  
export interface GetNewZDataTable_input{
   ds:Ice_Tablesets_ZDataTableTableset[],
   systemCode:string,
}

export interface GetNewZDataTable_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ZDataTableTableset,
}
}

   /** Required : 
      @param ds
      @param systemCode
      @param dataTableID
      @param keyID
   */  
export interface GetNewZKeyField_input{
   ds:Ice_Tablesets_ZDataTableTableset[],
   systemCode:string,
   dataTableID:string,
   keyID:string,
}

export interface GetNewZKeyField_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ZDataTableTableset,
}
}

   /** Required : 
      @param ds
      @param systemCode
      @param dataTableID
   */  
export interface GetNewZKey_input{
   ds:Ice_Tablesets_ZDataTableTableset[],
   systemCode:string,
   dataTableID:string,
}

export interface GetNewZKey_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ZDataTableTableset,
}
}

   /** Required : 
      @param ds
      @param systemCode
      @param dataTableID
      @param linkID
   */  
export interface GetNewZLinkColumn_input{
   ds:Ice_Tablesets_ZDataTableTableset[],
   systemCode:string,
   dataTableID:string,
   linkID:string,
}

export interface GetNewZLinkColumn_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ZDataTableTableset,
}
}

   /** Required : 
      @param ds
      @param systemCode
      @param dataTableID
      @param lookupID
   */  
export interface GetNewZLookupField_input{
   ds:Ice_Tablesets_ZDataTableTableset[],
   systemCode:string,
   dataTableID:string,
   lookupID:string,
}

export interface GetNewZLookupField_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ZDataTableTableset,
}
}

   /** Required : 
      @param ds
      @param systemCode
      @param dataTableID
   */  
export interface GetNewZLookupLink_input{
   ds:Ice_Tablesets_ZDataTableTableset[],
   systemCode:string,
   dataTableID:string,
}

export interface GetNewZLookupLink_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ZDataTableTableset,
}
}

   /** Required : 
      @param whereClauseZDataTable
      @param whereClauseZLookupLink
      @param whereClauseZLinkColumn
      @param whereClauseZLookupField
      @param whereClauseZDataField
      @param whereClauseZKey
      @param whereClauseZKeyField
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseZDataTable:string,
   whereClauseZLookupLink:string,
   whereClauseZLinkColumn:string,
   whereClauseZLookupField:string,
   whereClauseZDataField:string,
   whereClauseZKey:string,
   whereClauseZKeyField:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_ZDataTableTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param schemaName
      @param tableName
   */  
export interface HasDBTable_input{
      /**  Schema name (Ice, Erp)  */  
   schemaName:string,
      /**  table name (e.g. Tip_UD)  */  
   tableName:string,
}

export interface HasDBTable_output{
      /**  True if exists  */  
   returnObj:boolean,
}

   /** Required : 
      @param schemaName
      @param tableName
   */  
export interface HasZDataTable_input{
      /**  Schema name (Ice, Erp)  */  
   schemaName:string,
      /**  table name (e.g. Tip_UD)  */  
   tableName:string,
}

export interface HasZDataTable_output{
      /**  True if exists  */  
   returnObj:boolean,
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

export interface Ice_Tablesets_UpdExtZDataTableTableset{
   ZDataTable:Ice_Tablesets_ZDataTableRow[],
   ZLookupLink:Ice_Tablesets_ZLookupLinkRow[],
   ZLinkColumn:Ice_Tablesets_ZLinkColumnRow[],
   ZLookupField:Ice_Tablesets_ZLookupFieldRow[],
   ZDataField:Ice_Tablesets_ZDataFieldRow[],
   ZKey:Ice_Tablesets_ZKeyRow[],
   ZKeyField:Ice_Tablesets_ZKeyFieldRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ZDataFieldRow{
      /**  SystemCode  */  
   SystemCode:string,
      /**  DataTable ID  */  
   DataTableID:string,
      /**  Field Name  */  
   FieldName:string,
      /**  Sequence  */  
   Seq:number,
      /**  Database Table Name  */  
   DBTableName:string,
      /**  Data Type  */  
   DataType:string,
      /**  Required  */  
   Required:boolean,
      /**  Read Only  */  
   ReadOnly:boolean,
      /**  Description  */  
   Description:string,
      /**  External  */  
   External:boolean,
      /**  Formula  */  
   Formula:string,
      /**  Included  */  
   Included:boolean,
      /**  Field Format  */  
   FieldFormat:string,
      /**  Field Scale  */  
   FieldScale:number,
      /**  Field Label  */  
   FieldLabel:string,
      /**  Initial Value  */  
   InitialValue:string,
      /**  Indicates Data Field is a Description Field  */  
   IsDescriptionField:boolean,
      /**  LikeDataFieldSystemCode  */  
   LikeDataFieldSystemCode:string,
      /**  TableID to use with LikeField  */  
   LikeDataFieldTableID:string,
      /**  A delimited list of the modules required by this object.  */  
   RequiredModules:string,
      /**  Contains the characters that are used as delimiters for when building a list from values of this data field. So during data entry we should validate none of these charater is in the value of this data field.  */  
   Delimiters:string,
      /**  Code and Description value list  */  
   CodeDescriptionList:string,
      /**  Like Data Fiel Name reference  */  
   LikeDataFieldName:string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  Indicates Data Field is a Currency code column  */  
   CurrencyCodeColumn:string,
      /**  Currency Type  */  
   CurrencyType:string,
      /**  Currency Source  */  
   CurrencySource:string,
      /**   Further defines the Business use of the Field
Valid values are "Currency,Quantity,UOM"  */  
   BizType:string,
      /**  UDLikeDataFieldSystemCode  */  
   UDLikeDataFieldSystemCode:string,
      /**  TableID to use with LikeField  */  
   UDLikeDataFieldTableID:string,
      /**  User Defined Extended Property Like Data Field Name.  */  
   UDLikeDataFieldName:string,
      /**  User Defined Extended Property Field Property  */  
   UDFieldFormat:string,
      /**  User Defined Extended Property Field Label  */  
   UDFieldLabel:string,
      /**  User Defined Extended Property Initial Value  */  
   UDInitialValue:string,
      /**  User Defined Extended Property Required flag  */  
   UDRequired:boolean,
      /**  User Defined Extended Property Read Only flag  */  
   UDReadOnly:boolean,
      /**  User Defined Extended Property Currency code column flag  */  
   UDCurrencyCodeColumn:string,
      /**  User Defined Extended Property Currency Type  */  
   UDCurrencyType:string,
      /**  User Defined Extended Property currency Source  */  
   UDCurrencySource:string,
      /**  UDPredictiveSearchID  */  
   UDPredictiveSearchID:string,
      /**  CGCCode  */  
   CGCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CausesOnChange  */  
   CausesOnChange:boolean,
   DefaultFieldScale:number,
   DefaultFormat:string,
   DefaultInitValue:string,
   DefaultLabel:string,
      /**  DelimiterCheck  */  
   DelimiterCheck:boolean,
   EffectiveCurrencySource:string,
   EffectiveCurrencyType:string,
   LinkedColumn:string,
      /**  UD Code Type  */  
   UDCodeType:string,
      /**  UD Linked Column  */  
   UDLinkedColumn:string,
      /**  UD UOM Column  */  
   UDUomColumn:string,
   UomColumn:string,
      /**  Zone Baq ID  */  
   ZoneBAQ:string,
      /**  Allow Zone Search When control is Empty  */  
   ZoneSearchOnEmptyControl:boolean,
   Company:string,
   IsHidden:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ZDataTableListRow{
      /**  SystemCode  */  
   SystemCode:string,
      /**  DataTable ID  */  
   DataTableID:string,
      /**  Description  */  
   Description:string,
      /**  SchemaName  */  
   SchemaName:string,
      /**  Database TableName  */  
   DBTableName:string,
      /**  Where Clause  */  
   WhereClause:string,
      /**  If yes then this table is restricted by accessiable sales territories  */  
   RestrictedByTer:boolean,
      /**  If yes then this table is restricted by accessiable Sites  */  
   RestrictedByPlant:boolean,
      /**   DB = Database, TT = Temp Table, RP = Report Parameter, PP = Process Parameter. This value can be used for filtering table searches, controling sensitivity of fields, and controlling references by datasets.
Field sensitivity rules based on this value are  */  
   TableType:string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  A descriptive label for the table that the system may use in the construction of a message. Ex: Can not delete one or more "Bill of Lading" records exist.  Where Bill of Lading is the label. Which is much better that use the table name "BOLHead".  */  
   TableLabel:string,
      /**  Identifier value the system will use when creating Change Log records for this specific table (ChgLog.Indentifier)  ChgLogID must be the same for a set of related tables. For example: Customer, ShipTo, CustBillTo, CustCnt, are all related and will have a ChgLogID = "Customer".  TIP: Using the tablename of the highest level parent table as the ChgLogID may avoid   accidental duplication.  */  
   ChgLogID:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ZDataTableListTableset{
   ZDataTableList:Ice_Tablesets_ZDataTableListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ZDataTableRow{
      /**  SystemCode  */  
   SystemCode:string,
      /**  DataTable ID  */  
   DataTableID:string,
      /**  Description  */  
   Description:string,
      /**  SchemaName  */  
   SchemaName:string,
      /**  Database TableName  */  
   DBTableName:string,
      /**  Where Clause  */  
   WhereClause:string,
      /**  If yes then this table is restricted by accessiable sales territories  */  
   RestrictedByTer:boolean,
      /**  If yes then this table is restricted by accessiable Sites  */  
   RestrictedByPlant:boolean,
      /**  controls the behavior of  object designer field synchronization with the db schema. When set True, the synch process will bring in all the DB fields from a DB table into the zDataFields table. When set to False, the synch process will only update the fields that are currently in the zDataFields table.  */  
   FullSync:boolean,
      /**   DB = Database, TT = Temp Table, RP = Report Parameter, PP = Process Parameter. This value can be used for filtering table searches, controling sensitivity of fields, and controlling references by datasets.
Field sensitivity rules based on this value are  */  
   TableType:string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  A descriptive label for the table that the system may use in the construction of a message. Ex: Can not delete one or more "Bill of Lading" records exist.  Where Bill of Lading is the label. Which is much better that use the table name "BOLHead".  */  
   TableLabel:string,
      /**  Identifier value the system will use when creating Change Log records for this specific table (ChgLog.Indentifier)  ChgLogID must be the same for a set of related tables. For example: Customer, ShipTo, CustBillTo, CustCnt, are all related and will have a ChgLogID = "Customer".  TIP: Using the tablename of the highest level parent table as the ChgLogID may avoid   accidental duplication.  */  
   ChgLogID:string,
      /**  BO Used to Update Table  */  
   BOUpdate:string,
      /**  BO Method used for Update  */  
   UpdateMethod:string,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  Interface  */  
   Interface:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ZDataTableTableset{
   ZDataTable:Ice_Tablesets_ZDataTableRow[],
   ZLookupLink:Ice_Tablesets_ZLookupLinkRow[],
   ZLinkColumn:Ice_Tablesets_ZLinkColumnRow[],
   ZLookupField:Ice_Tablesets_ZLookupFieldRow[],
   ZDataField:Ice_Tablesets_ZDataFieldRow[],
   ZKey:Ice_Tablesets_ZKeyRow[],
   ZKeyField:Ice_Tablesets_ZKeyFieldRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ZKeyFieldRow{
      /**  SystemCode  */  
   SystemCode:string,
      /**  DataTable ID  */  
   DataTableID:string,
      /**  Key ID  */  
   KeyID:string,
      /**  Sequence  */  
   Seq:number,
      /**  Field Name  */  
   FieldName:string,
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

export interface Ice_Tablesets_ZKeyRow{
      /**  SystemCode  */  
   SystemCode:string,
      /**  DataTable ID  */  
   DataTableID:string,
      /**  Key ID  */  
   KeyID:string,
      /**  Description  */  
   Description:string,
      /**  Primary Key  */  
   IsPrimaryKey:boolean,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  External Key  */  
   External:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ZLinkColumnRow{
      /**  SystemCode  */  
   SystemCode:string,
      /**  DataTable ID  */  
   DataTableID:string,
      /**  Link ID  */  
   LinkID:string,
      /**  Field Name  */  
   FieldName:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  LinkColName  */  
   LinkColName:string,
   BitFlag:number,
   ZLookupLinkForeignDataTableID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ZLookupFieldRow{
      /**  SystemCode  */  
   SystemCode:string,
      /**  DataTable ID  */  
   DataTableID:string,
      /**  LookUp ID  */  
   LookupID:string,
      /**  Sequence  */  
   Seq:number,
      /**  Field Name  */  
   FieldName:string,
      /**  Constant Field indicator  */  
   IsConst:boolean,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   ForeignFieldName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ZLookupLinkRow{
      /**  SystemCode  */  
   SystemCode:string,
      /**  DataTable ID  */  
   DataTableID:string,
      /**  LookUp ID  */  
   LookupID:string,
      /**  ForeignSystemCode  */  
   ForeignSystemCode:string,
      /**  Foreign DataTable ID  */  
   ForeignDataTableID:string,
      /**  Key ID  */  
   KeyID:string,
      /**  Description  */  
   Description:string,
      /**  Validation Required  */  
   ValidationRequired:boolean,
      /**  Extra validation  */  
   ValidationPhraseEx:string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  Indicating this lookup link is not used for pulling the IsDisplayField  to the master table but for checking referential integraty.  */  
   ValidationOnly:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param systemCode
      @param className
   */  
export interface SynchronizeClass_input{
      /**  System code  */  
   systemCode:string,
      /**  Class name  */  
   className:string,
}

export interface SynchronizeClass_output{
}

   /** Required : 
      @param systemCode
      @param dataTableID
   */  
export interface Synchronize_input{
   systemCode:string,
      /**  Table ID  */  
   dataTableID:string,
}

export interface Synchronize_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtZDataTableTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtZDataTableTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_ZDataTableTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ZDataTableTableset,
}
}

   /** Required : 
      @param inputValue
   */  
export interface ValidateGuid_input{
   inputValue:string,
}

export interface ValidateGuid_output{
      /**  The formated Guid  */  
   returnObj:string,
}

   /** Required : 
      @param inputValue
      @param format
      @param dataType
   */  
export interface ValidateNFormatNumber_input{
   inputValue:string,
   format:string,
   dataType:string,
}

export interface ValidateNFormatNumber_output{
      /**  The formated Number  */  
   returnObj:string,
parameters : {
      /**  output parameters  */  
   inputValue:string,
}
}

   /** Required : 
      @param format
      @param inputValue
   */  
export interface ValidateNFormatString_input{
   format:string,
   inputValue:string,
}

export interface ValidateNFormatString_output{
      /**  The formated String  */  
   returnObj:string,
}

