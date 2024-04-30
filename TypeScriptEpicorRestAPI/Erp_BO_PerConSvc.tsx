import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PerConSvc
// Description: Handles the Person Contact business object.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get PerCons items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PerCons
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConRow
   */  
export function get_PerCons(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PerCons
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerConRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PerConRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PerCons(requestBody:Erp_Tablesets_PerConRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PerCon item
   Description: Calls GetByID to retrieve the PerCon item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerCon
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerConID Desc: PerConID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PerConRow
   */  
export function get_PerCons_Company_PerConID(Company:string, PerConID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PerConRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PerConRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PerCon for the service
   Description: Calls UpdateExt to update PerCon. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PerCon
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerConID Desc: PerConID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerConRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PerCons_Company_PerConID(Company:string, PerConID:string, requestBody:Erp_Tablesets_PerConRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")", {
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
   Summary: Call UpdateExt to delete PerCon item
   Description: Call UpdateExt to delete PerCon item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PerCon
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerConID Desc: PerConID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PerCons_Company_PerConID(Company:string, PerConID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")", {
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
   Description: Get PerConLnks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PerConLnks1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerConID Desc: PerConID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConLnkRow
   */  
export function get_PerCons_Company_PerConID_PerConLnks(Company:string, PerConID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConLnkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")/PerConLnks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConLnkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PerConLnk item
   Description: Calls GetByID to retrieve the PerConLnk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerConLnk1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerConID Desc: PerConID   Required: True
      @param ContextLink Desc: ContextLink   Required: True   Allow empty value : True
      @param LinkSysRowID Desc: LinkSysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PerConLnkRow
   */  
export function get_PerCons_Company_PerConID_PerConLnks_Company_PerConID_ContextLink_LinkSysRowID(Company:string, PerConID:string, ContextLink:string, LinkSysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PerConLnkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")/PerConLnks(" + Company + "," + PerConID + "," + ContextLink + "," + LinkSysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PerConLnkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PerConAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PerConAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerConID Desc: PerConID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConAttchRow
   */  
export function get_PerCons_Company_PerConID_PerConAttches(Company:string, PerConID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")/PerConAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PerConAttch item
   Description: Calls GetByID to retrieve the PerConAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerConAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerConID Desc: PerConID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PerConAttchRow
   */  
export function get_PerCons_Company_PerConID_PerConAttches_Company_PerConID_DrawingSeq(Company:string, PerConID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PerConAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerCons(" + Company + "," + PerConID + ")/PerConAttches(" + Company + "," + PerConID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PerConAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PerConLnks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PerConLnks
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConLnkRow
   */  
export function get_PerConLnks(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConLnkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConLnks", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConLnkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PerConLnks
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerConLnkRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PerConLnkRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PerConLnks(requestBody:Erp_Tablesets_PerConLnkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConLnks", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PerConLnk item
   Description: Calls GetByID to retrieve the PerConLnk item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerConLnk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerConID Desc: PerConID   Required: True
      @param ContextLink Desc: ContextLink   Required: True   Allow empty value : True
      @param LinkSysRowID Desc: LinkSysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PerConLnkRow
   */  
export function get_PerConLnks_Company_PerConID_ContextLink_LinkSysRowID(Company:string, PerConID:string, ContextLink:string, LinkSysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PerConLnkRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConLnks(" + Company + "," + PerConID + "," + ContextLink + "," + LinkSysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PerConLnkRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PerConLnk for the service
   Description: Calls UpdateExt to update PerConLnk. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PerConLnk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerConID Desc: PerConID   Required: True
      @param ContextLink Desc: ContextLink   Required: True   Allow empty value : True
      @param LinkSysRowID Desc: LinkSysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerConLnkRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PerConLnks_Company_PerConID_ContextLink_LinkSysRowID(Company:string, PerConID:string, ContextLink:string, LinkSysRowID:string, requestBody:Erp_Tablesets_PerConLnkRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConLnks(" + Company + "," + PerConID + "," + ContextLink + "," + LinkSysRowID + ")", {
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
   Summary: Call UpdateExt to delete PerConLnk item
   Description: Call UpdateExt to delete PerConLnk item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PerConLnk
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerConID Desc: PerConID   Required: True
      @param ContextLink Desc: ContextLink   Required: True   Allow empty value : True
      @param LinkSysRowID Desc: LinkSysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PerConLnks_Company_PerConID_ContextLink_LinkSysRowID(Company:string, PerConID:string, ContextLink:string, LinkSysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConLnks(" + Company + "," + PerConID + "," + ContextLink + "," + LinkSysRowID + ")", {
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
   Description: Get PerConAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PerConAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConAttchRow
   */  
export function get_PerConAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PerConAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PerConAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PerConAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PerConAttches(requestBody:Erp_Tablesets_PerConAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PerConAttch item
   Description: Calls GetByID to retrieve the PerConAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PerConAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerConID Desc: PerConID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PerConAttchRow
   */  
export function get_PerConAttches_Company_PerConID_DrawingSeq(Company:string, PerConID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PerConAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConAttches(" + Company + "," + PerConID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PerConAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PerConAttch for the service
   Description: Calls UpdateExt to update PerConAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PerConAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerConID Desc: PerConID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PerConAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PerConAttches_Company_PerConID_DrawingSeq(Company:string, PerConID:string, DrawingSeq:string, requestBody:Erp_Tablesets_PerConAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConAttches(" + Company + "," + PerConID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PerConAttch item
   Description: Call UpdateExt to delete PerConAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PerConAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PerConID Desc: PerConID   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PerConAttches_Company_PerConID_DrawingSeq(Company:string, PerConID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PerConAttches(" + Company + "," + PerConID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PerConListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePerCon:string, whereClausePerConAttch:string, whereClausePerConLnk:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePerCon!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePerCon=" + whereClausePerCon
   }
   if(typeof whereClausePerConAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePerConAttch=" + whereClausePerConAttch
   }
   if(typeof whereClausePerConLnk!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePerConLnk=" + whereClausePerConLnk
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(perConID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof perConID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "perConID=" + perConID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method GetClientFileName
   OperationID: GetClientFileName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetClientFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetClientFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetClientFileName(requestBody:GetClientFileName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetClientFileName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/GetClientFileName", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetClientFileName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPerConGlobalFields
   OperationID: GetPerConGlobalFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPerConGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPerConGlobalFields(requestBody:GetPerConGlobalFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPerConGlobalFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/GetPerConGlobalFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPerConGlobalFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeGlobalPerCon
   Description: Method to call when changing the GlobalPerCon on a PerCon.
   OperationID: ChangeGlobalPerCon
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeGlobalPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeGlobalPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeGlobalPerCon(requestBody:ChangeGlobalPerCon_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeGlobalPerCon_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/ChangeGlobalPerCon", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeGlobalPerCon_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePerConLnk
   OperationID: ChangePerConLnk
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePerConLnk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePerConLnk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePerConLnk(requestBody:ChangePerConLnk_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePerConLnk_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/ChangePerConLnk", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangePerConLnk_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDupPerCon
   Description: This method checks the Name, FirstName and LastName fields to see if there
are any duplicate contacts. A ListDataSet will be returned to the user
of any duplicates asking if the user wants to continue. Needs to be run
before Update on a NEW record only.
   OperationID: CheckDupPerCon
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDupPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDupPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDupPerCon(requestBody:CheckDupPerCon_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDupPerCon_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/CheckDupPerCon", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckDupPerCon_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DefaultName
   Description: This method populates the detail fields from PerCon.Name when targetName = "Detail".
When targetField = "Name", then the PerCon.Name is built from the detail fields.
   OperationID: DefaultName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DefaultName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DefaultName(requestBody:DefaultName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DefaultName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/DefaultName", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DefaultName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetGlbPerConList
   Description: This method returns the GlbPerCon dataset based on a delimited list of GlbPerConID values passed in.
   OperationID: GetGlbPerConList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetGlbPerConList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlbPerConList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetGlbPerConList(requestBody:GetGlbPerConList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetGlbPerConList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/GetGlbPerConList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetGlbPerConList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPerConForLink
   Description: This returns the PerCon dataset for linking.
   OperationID: GetPerConForLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPerConForLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConForLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPerConForLink(requestBody:GetPerConForLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPerConForLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/GetPerConForLink", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPerConForLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LinkGlbPerCon
   Description: This method performs the actual logic behind linking a PerCon. It is run after
the PreLinkGlbPerCon method which determines the PerConID to link to.
If the PerConID is for a PerCon that already exists, the GlbPerCon information is
translated and then copied to the PerConDataSet as an update.
If the PerConID is for a new PerCon, the GlbPerCon information is translated and then
copied to the PerConDataSet as an Add. Until the update method is run on PerCon record
the Link process is not completed.
   OperationID: LinkGlbPerCon
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LinkGlbPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LinkGlbPerCon(requestBody:LinkGlbPerCon_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LinkGlbPerCon_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/LinkGlbPerCon", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LinkGlbPerCon_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreLinkGlbPerCon
   Description: Linking a GlbPerCon record ties a global record to a new or existing PerCon record so
that any changes made to the GlbPerCon record in another company are automatically copied
to any linked PerCon's.
This method performs the pre link logic to check of okay to link or get the new PerConID
to create/link to. Will be run before LinkGlbPerCon which actually creates/updates a
PerCon record and will send the modified record back for update.  When the Link "button" is
originally selected, the LinkPerConID will be defaulted to the GlbPerConID field.  It will then
check to see if this PerConID is available for use. If available for use the system will return a
question asking the user if they want to use this number.  If the answer is no, then the user
either needs to select an existing PerConID to link to or enter a brand new number.  You will
run this method until the user answer is yes. Then the LinkGlbPerCon method is called.
   OperationID: PreLinkGlbPerCon
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreLinkGlbPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreLinkGlbPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreLinkGlbPerCon(requestBody:PreLinkGlbPerCon_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreLinkGlbPerCon_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/PreLinkGlbPerCon", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PreLinkGlbPerCon_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SkipGlbPerCon
   Description: This method performs the logic behind the skip option for GlbPerCon
Skip - sets the Skipped flag to true.
If the PerConID field is not 0 will error out
   OperationID: SkipGlbPerCon
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SkipGlbPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SkipGlbPerCon(requestBody:SkipGlbPerCon_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SkipGlbPerCon_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/SkipGlbPerCon", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SkipGlbPerCon_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnlinkGlbPerCon
   Description: This method performs the logic behind the unlink option for GlbPerCon
Unlink - clears the PerConID field in GlbPerCon.  Returns the PerCon DataSet
   OperationID: UnlinkGlbPerCon
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnlinkGlbPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlinkGlbPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlinkGlbPerCon(requestBody:UnlinkGlbPerCon_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnlinkGlbPerCon_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/UnlinkGlbPerCon", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnlinkGlbPerCon_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsPayrollManager
   OperationID: IsPayrollManager
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsPayrollManager_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsPayrollManager(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsPayrollManager_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/IsPayrollManager", {
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
         resolve(data as IsPayrollManager_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPerCon
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerCon
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPerCon_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerCon_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPerCon(requestBody:GetNewPerCon_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPerCon_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/GetNewPerCon", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPerCon_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPerConAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerConAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPerConAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerConAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPerConAttch(requestBody:GetNewPerConAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPerConAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/GetNewPerConAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPerConAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPerConLnk
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPerConLnk
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPerConLnk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPerConLnk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPerConLnk(requestBody:GetNewPerConLnk_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPerConLnk_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/GetNewPerConLnk", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPerConLnk_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PerConSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PerConAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PerConListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConLnkRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PerConLnkRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PerConRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PerConRow,
}

export interface Erp_Tablesets_PerConAttchRow{
   "Company":string,
   "PerConID":number,
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

export interface Erp_Tablesets_PerConListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**  Full name of the contact.  */  
   "Name":string,
      /**  Contact's first name.  */  
   "FirstName":string,
      /**  Contact's middle name.  */  
   "MiddleName":string,
      /**  Contact's last name.  */  
   "LastName":string,
      /**  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  */  
   "PRName":string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   "Func":string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   "FaxNum":string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   "PhoneNum":string,
      /**  The contact's email address.  */  
   "EMailAddress":string,
      /**  The contact's cell phone number.  */  
   "CellPhoneNum":string,
      /**  The contact's pager number.  */  
   "PagerNum":string,
      /**  The contact's home number.  */  
   "HomeNum":string,
      /**  The contact's alternate phone number.  */  
   "AltNum":string,
      /**  Contact's prefix.  */  
   "Prefix":string,
      /**  Contact's suffix.  */  
   "Suffix":string,
      /**  Contact's initials.  */  
   "Initials":string,
      /**  Contact's website.  */  
   "WebSite":string,
      /**  Contact's IM.  */  
   "IM":string,
      /**  Contact's Twitter.  */  
   "Twitter":string,
      /**  Contact's LinkedIn.  */  
   "LinkedIn":string,
      /**  Contact's FaceBook.  */  
   "FaceBook":string,
      /**  User defined Link 1.  */  
   "WebLink1":string,
      /**  User defined Link 2.  */  
   "WebLink2":string,
      /**  User defined Link 3.  */  
   "WebLink3":string,
      /**  User defined Link 4.  */  
   "WebLink4":string,
      /**  User defined Link 5.  */  
   "WebLink5":string,
      /**  Address line 1  */  
   "Address1":string,
      /**  Address line 2  */  
   "Address2":string,
      /**  Address line 3  */  
   "Address3":string,
      /**  City  */  
   "City":string,
      /**  State/Province  */  
   "State":string,
      /**  Zip/Postal Code  */  
   "Zip":string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  The Country.CountryNum value related to the SalesRep.Country value.  */  
   "CountryNum":number,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   "CorpName":string,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   "RoleCode":string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   "Comment":string,
      /**  Contact's title.  */  
   "ContactTitle":string,
      /**  The name of the person this contact reports to.  */  
   "ReportsTo":string,
      /**  Contact's payroll last name.  */  
   "PRLastName":string,
      /**  Contact's payroll first name.  */  
   "PRFirstName":string,
      /**  Contact's payroll middle name.  */  
   "PRMiddleName":string,
      /**  The System User ID.  */  
   "DcdUserID":string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   "PhotoFile":string,
      /**  Marks the PerCon as a global PerCon, available to be sent out to other companies.  */  
   "GlobalPerCon":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Logical column used for Create Selected Links action menu. Indicates that a PR Employee link should be created if it doesn't exist already.  */  
   "CrtPREmpLnk":boolean,
      /**  Logical column used for Create Selected Links action menu. Indicates that an Employee link should be created if it doesn't exist already.  */  
   "CrtEmpLnk":boolean,
      /**  Logical column used for Create Selected Links action menu. Indicates that a Buyer link should be created if it doesn't exist already.  */  
   "CrtBuyerLnk":boolean,
      /**  Logical column used for Create Selected Links action menu. Indicates that a Work Force link should be created if it doesn't exist already.  */  
   "CrtWFLnk":boolean,
      /**  Path to the photo file if it exists.  */  
   "PhotoFilePath":string,
      /**  Indicates if the PerCon is Global (master or linked)  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany and GlbPerConID that is linking to this PerCon.  */  
   "GlbLink":string,
   "EnableGlbLock":boolean,
   "EnableGlbPerCon":boolean,
      /**  A description of the role.  */  
   "RoleCodeRoleDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PerConLnkRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**   The table name and context that this PerConLnk is related to:
Customer(If related to CustCnt and CustCnt.ShipTonum = "")
Ship to(If related to CustCnt and CustCnt.ShipTonum <> "")
Supplier((If related to VendCnt and VendCnt.PurPoint = "")
Supplier PP((If related to VendCnt and VendCnt.PurPoint <> "")
Employee(If related to EmpBasic)
Work force (If related to SalesRep)
Buyer(If related to PurAgent)  */  
   "ContextLink":string,
      /**  The SysRowId of the linked table.  */  
   "LinkSysRowID":string,
      /**  Flag that indicates the primary link of the Person/Contact.  */  
   "PrimaryContext":boolean,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   "FaxNum":string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   "PhoneNum":string,
      /**  The contact's email address.  */  
   "EMailAddress":string,
      /**  The contact's cell phone number.  */  
   "CellPhoneNum":string,
      /**  The contact's pager number.  */  
   "PagerNum":string,
      /**  The contact's home number.  */  
   "HomeNum":string,
      /**  The contact's alternate phone number.  */  
   "AltNum":string,
      /**  Contact's website.  */  
   "WebSite":string,
      /**  Contact's IM.  */  
   "IM":string,
      /**  Contact's Twitter.  */  
   "Twitter":string,
      /**  Contact's LinkedIn.  */  
   "LinkedIn":string,
      /**  Contact's FaceBook.  */  
   "FaceBook":string,
      /**  User defined Link 1.  */  
   "WebLink1":string,
      /**  User defined Link 2.  */  
   "WebLink2":string,
      /**  User defined Link 3.  */  
   "WebLink3":string,
      /**  User defined Link 4.  */  
   "WebLink4":string,
      /**  User defined Link 5.  */  
   "WebLink5":string,
      /**  Address line 1  */  
   "Address1":string,
      /**  Address line 2  */  
   "Address2":string,
      /**  Address line 3  */  
   "Address3":string,
      /**  City  */  
   "City":string,
      /**  State/Province  */  
   "State":string,
      /**  Zip/Postal Code  */  
   "Zip":string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  The Country.CountryNum value related to the SalesRep.Country value.  */  
   "CountryNum":number,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   "CorpName":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Customer ID from Customer table.  */  
   "CustID":string,
      /**  Full name of the customer.  */  
   "CustName":string,
      /**  Number of the Ship To for the Customer Contact.  */  
   "ShipToNum":string,
      /**  Name of the customer contact's Ship To.  */  
   "ShipToName":string,
      /**  Name of the Customer Contact.  */  
   "CustContactName":string,
      /**  Vendor ID from the Vendor table.  */  
   "VendorID":string,
      /**  Name of the vendor.  */  
   "VendorName":string,
      /**  Purchase Point from the Vendor.  */  
   "PurPoint":string,
      /**  Name of the vendor's purchase point.  */  
   "PurPointName":string,
      /**  Name of the vendor's contact.  */  
   "VendorContactName":string,
      /**  The code of the sales representative, from the SalesRep table.  */  
   "SalesRepCode":string,
      /**  Name of the sales representative.  */  
   "SalesRepName":string,
      /**  Buyer ID from the PurAgent table.  */  
   "BuyerID":string,
      /**  Name of the buyer.  */  
   "BuyerName":string,
      /**  Employee ID from the EmpBasic table.  */  
   "EmpID":string,
      /**  Name of the employee.  */  
   "EmpName":string,
   "PREmpID":string,
   "PREmpName":string,
      /**  Shows the value of the Sync. Name flag in the linked record.  */  
   "SyncNameToPerCon":boolean,
      /**  Shows the value of the Sync. Address flag in the linked record.  */  
   "SyncAddressToPerCon":boolean,
      /**  Shows the value of the Sync. Phone flag in the linked record.  */  
   "SyncPhoneToPerCon":boolean,
      /**  Shows the value of the Sync. Email flag in the linked record.  */  
   "SyncEmailToPerCon":boolean,
      /**  Shows the value of the Sync. Links flag in the linked record.  */  
   "SyncLinksToPerCon":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PerConRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier for a PerCon record.  */  
   "PerConID":number,
      /**  Full name of the contact.  */  
   "Name":string,
      /**  Contact's first name.  */  
   "FirstName":string,
      /**  Contact's middle name.  */  
   "MiddleName":string,
      /**  Contact's last name.  */  
   "LastName":string,
      /**  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  */  
   "PRName":string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   "Func":string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   "FaxNum":string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   "PhoneNum":string,
      /**  The contact's email address.  */  
   "EMailAddress":string,
      /**  The contact's cell phone number.  */  
   "CellPhoneNum":string,
      /**  The contact's pager number.  */  
   "PagerNum":string,
      /**  The contact's home number.  */  
   "HomeNum":string,
      /**  The contact's alternate phone number.  */  
   "AltNum":string,
      /**  Contact's prefix.  */  
   "Prefix":string,
      /**  Contact's suffix.  */  
   "Suffix":string,
      /**  Contact's initials.  */  
   "Initials":string,
      /**  Contact's website.  */  
   "WebSite":string,
      /**  Contact's IM.  */  
   "IM":string,
      /**  Contact's Twitter.  */  
   "Twitter":string,
      /**  Contact's LinkedIn.  */  
   "LinkedIn":string,
      /**  Contact's FaceBook.  */  
   "FaceBook":string,
      /**  User defined Link 1.  */  
   "WebLink1":string,
      /**  User defined Link 2.  */  
   "WebLink2":string,
      /**  User defined Link 3.  */  
   "WebLink3":string,
      /**  User defined Link 4.  */  
   "WebLink4":string,
      /**  User defined Link 5.  */  
   "WebLink5":string,
      /**  Address line 1  */  
   "Address1":string,
      /**  Address line 2  */  
   "Address2":string,
      /**  Address line 3  */  
   "Address3":string,
      /**  City  */  
   "City":string,
      /**  State/Province  */  
   "State":string,
      /**  Zip/Postal Code  */  
   "Zip":string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   "Country":string,
      /**  The Country.CountryNum value related to the SalesRep.Country value.  */  
   "CountryNum":number,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   "CorpName":string,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   "RoleCode":string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   "Comment":string,
      /**  Contact's title.  */  
   "ContactTitle":string,
      /**  The name of the person this contact reports to.  */  
   "ReportsTo":string,
      /**  Contact's payroll last name.  */  
   "PRLastName":string,
      /**  Contact's payroll first name.  */  
   "PRFirstName":string,
      /**  Contact's payroll middle name.  */  
   "PRMiddleName":string,
      /**  The System User ID.  */  
   "DcdUserID":string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   "PhotoFile":string,
      /**  Marks the PerCon as a global PerCon, available to be sent out to other companies.  */  
   "GlobalPerCon":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Indicates if the record is linked from HCM  */  
   "HCMLinked":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  */  
   "IssuerPrsnIDCode":string,
      /**  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  */  
   "IssuerIDType":string,
      /**  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  */  
   "IssuerName":string,
      /**  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  */  
   "IssuerSurname":string,
      /**  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  */  
   "IssuerSerialNum":string,
      /**  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  */  
   "IssuerIDIssDate":string,
      /**  ImageID  */  
   "ImageID":string,
      /**  Logical column used for Create Selected Links action menu. Indicates that a Buyer link should be created if it doesn't exist already.  */  
   "CrtBuyerLnk":boolean,
      /**  Logical column used for Create Selected Links action menu. Indicates that an Employee link should be created if it doesn't exist already.  */  
   "CrtEmpLnk":boolean,
      /**  Logical column used for Create Selected Links action menu. Indicates that a PR Employee link should be created if it doesn't exist already.  */  
   "CrtPREmpLnk":boolean,
      /**  Logical column used for Create Selected Links action menu. Indicates that a Work Force link should be created if it doesn't exist already.  */  
   "CrtWFLnk":boolean,
   "EnableGlbLock":boolean,
   "EnableGlbPerCon":boolean,
      /**  Indicates if the PerCon is Global (master or linked)  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany and GlbPerConID that is linking to this PerCon.  */  
   "GlbLink":string,
      /**  Path to the photo file if it exists.  */  
   "PhotoFilePath":string,
   "EnableCreateBuyer":boolean,
   "EnableCreateEmployee":boolean,
   "EnableCreatePREmployee":boolean,
   "EnableCreateWorkForce":boolean,
   "BitFlag":number,
   "RoleCodeRoleDescription":string,
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
      @param ipGlobalPerCon
      @param ds
   */  
export interface ChangeGlobalPerCon_input{
      /**  The proposed GlobalPerCon value.  */  
   ipGlobalPerCon:boolean,
   ds:Erp_Tablesets_PerConTableset[],
}

export interface ChangeGlobalPerCon_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PerConTableset,
}
}

   /** Required : 
      @param ipNewPerConID
      @param ipPerConID
      @param ipContextLink
      @param ipLinkSysRowID
      @param ds
   */  
export interface ChangePerConLnk_input{
      /**  New PerConID.  */  
   ipNewPerConID:number,
      /**  Current PerConID.  */  
   ipPerConID:number,
      /**  ContextLink.  */  
   ipContextLink:string,
      /**  LinkSysRowID.  */  
   ipLinkSysRowID:string,
   ds:Erp_Tablesets_PerConTableset[],
}

export interface ChangePerConLnk_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PerConTableset,
}
}

   /** Required : 
      @param vName
      @param vEmail
      @param vPhone
      @param vSysRowID
   */  
export interface CheckDupPerCon_input{
      /**  The name of the contact.  */  
   vName:string,
   vEmail:string,
   vPhone:string,
      /**  SysRowID field of the PerCon record.  */  
   vSysRowID:string,
}

export interface CheckDupPerCon_output{
   returnObj:Erp_Tablesets_PerConListTableset[],
}

   /** Required : 
      @param targetField
      @param perConID
      @param ds
   */  
export interface DefaultName_input{
      /**  Indicates which fields to populate either "Detail" or "Name"  */  
   targetField:string,
      /**  PerCon.PerConID  */  
   perConID:number,
   ds:Erp_Tablesets_PerConTableset[],
}

export interface DefaultName_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PerConTableset,
}
}

   /** Required : 
      @param perConID
   */  
export interface DeleteByID_input{
   perConID:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GlbPerConRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Full name of the contact.  */  
   Name:string,
      /**  Contact's first name.  */  
   FirstName:string,
      /**  Contact's middle name.  */  
   MiddleName:string,
      /**  Contact's last name.  */  
   LastName:string,
      /**  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  */  
   PRName:string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   Func:string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   FaxNum:string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  The contact's email address.  */  
   EMailAddress:string,
      /**  The contact's cell phone number.  */  
   CellPhoneNum:string,
      /**  The contact's pager number.  */  
   PagerNum:string,
      /**  The contact's home number.  */  
   HomeNum:string,
      /**  The contact's alternate phone number.  */  
   AltNum:string,
      /**  Contact's prefix.  */  
   Prefix:string,
      /**  Contact's suffix.  */  
   Suffix:string,
      /**  Contact's initials.  */  
   Initials:string,
      /**  Contact's website.  */  
   WebSite:string,
      /**  Contact's IM.  */  
   IM:string,
      /**  Contact's Twitter.  */  
   Twitter:string,
      /**  Contact's LinkedIn.  */  
   LinkedIn:string,
      /**  Contact's FaceBook.  */  
   FaceBook:string,
      /**  User defined Link 1.  */  
   WebLink1:string,
      /**  User defined Link 2.  */  
   WebLink2:string,
      /**  User defined Link 3.  */  
   WebLink3:string,
      /**  User defined Link 4.  */  
   WebLink4:string,
      /**  User defined Link 5.  */  
   WebLink5:string,
      /**  Address line 1  */  
   Address1:string,
      /**  Address line 2  */  
   Address2:string,
      /**  Address line 3  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  State/Province  */  
   State:string,
      /**  Zip/Postal Code  */  
   Zip:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  The Country.CountryNum value related to the SalesRep.Country value.  */  
   CountryNum:number,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   CorpName:string,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   RoleCode:string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   Comment:string,
      /**  Contact's title.  */  
   ContactTitle:string,
      /**  The name of the person this contact reports to.  */  
   ReportsTo:string,
      /**  Contact's payroll last name.  */  
   PRLastName:string,
      /**  Contact's payroll first name.  */  
   PRFirstName:string,
      /**  Contact's payroll middle name.  */  
   PRMiddleName:string,
      /**  The System User ID.  */  
   DcdUserID:string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   PhotoFile:string,
      /**  Owner Company Identifier.  */  
   GlbCompany:string,
      /**  The Owner's PerConID field identifies the PerCon and is used as the primary key.  */  
   GlbPerConID:number,
      /**  Original Owner Company Identifier. - NOT CURRENTLY IN USE  */  
   OldCompany:string,
      /**  The Original Owner's PerConID field identifies the PerCon and is used as the primary key.   NOT CURRENTLY IN USE  */  
   OldPerConID:number,
      /**  Indicates if the user chose to skip this record when linking global PerCon's.  The user can come back at a later time and choose to link a skipped PerCon if they need to.  */  
   Skipped:boolean,
      /**  Marks the PerCon as a global PerCon, available to be sent out to other companies.  */  
   GlobalPerCon:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Full name of the contact. A descriptive Name assigned by the parent company user to uniquely identify the PerCon record.  */  
   GlbName:string,
   HCMLinked:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ImageID  */  
   ImageID:string,
      /**  Indicates if the PerCon is Global (master or linked)  */  
   GlbFlag:boolean,
   LinkName:string,
   LinkPerConID:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbPerConTableset{
   GlbPerCon:Erp_Tablesets_GlbPerConRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PerConAttchRow{
   Company:string,
   PerConID:number,
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

export interface Erp_Tablesets_PerConListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Full name of the contact.  */  
   Name:string,
      /**  Contact's first name.  */  
   FirstName:string,
      /**  Contact's middle name.  */  
   MiddleName:string,
      /**  Contact's last name.  */  
   LastName:string,
      /**  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  */  
   PRName:string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   Func:string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   FaxNum:string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  The contact's email address.  */  
   EMailAddress:string,
      /**  The contact's cell phone number.  */  
   CellPhoneNum:string,
      /**  The contact's pager number.  */  
   PagerNum:string,
      /**  The contact's home number.  */  
   HomeNum:string,
      /**  The contact's alternate phone number.  */  
   AltNum:string,
      /**  Contact's prefix.  */  
   Prefix:string,
      /**  Contact's suffix.  */  
   Suffix:string,
      /**  Contact's initials.  */  
   Initials:string,
      /**  Contact's website.  */  
   WebSite:string,
      /**  Contact's IM.  */  
   IM:string,
      /**  Contact's Twitter.  */  
   Twitter:string,
      /**  Contact's LinkedIn.  */  
   LinkedIn:string,
      /**  Contact's FaceBook.  */  
   FaceBook:string,
      /**  User defined Link 1.  */  
   WebLink1:string,
      /**  User defined Link 2.  */  
   WebLink2:string,
      /**  User defined Link 3.  */  
   WebLink3:string,
      /**  User defined Link 4.  */  
   WebLink4:string,
      /**  User defined Link 5.  */  
   WebLink5:string,
      /**  Address line 1  */  
   Address1:string,
      /**  Address line 2  */  
   Address2:string,
      /**  Address line 3  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  State/Province  */  
   State:string,
      /**  Zip/Postal Code  */  
   Zip:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  The Country.CountryNum value related to the SalesRep.Country value.  */  
   CountryNum:number,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   CorpName:string,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   RoleCode:string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   Comment:string,
      /**  Contact's title.  */  
   ContactTitle:string,
      /**  The name of the person this contact reports to.  */  
   ReportsTo:string,
      /**  Contact's payroll last name.  */  
   PRLastName:string,
      /**  Contact's payroll first name.  */  
   PRFirstName:string,
      /**  Contact's payroll middle name.  */  
   PRMiddleName:string,
      /**  The System User ID.  */  
   DcdUserID:string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   PhotoFile:string,
      /**  Marks the PerCon as a global PerCon, available to be sent out to other companies.  */  
   GlobalPerCon:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Logical column used for Create Selected Links action menu. Indicates that a PR Employee link should be created if it doesn't exist already.  */  
   CrtPREmpLnk:boolean,
      /**  Logical column used for Create Selected Links action menu. Indicates that an Employee link should be created if it doesn't exist already.  */  
   CrtEmpLnk:boolean,
      /**  Logical column used for Create Selected Links action menu. Indicates that a Buyer link should be created if it doesn't exist already.  */  
   CrtBuyerLnk:boolean,
      /**  Logical column used for Create Selected Links action menu. Indicates that a Work Force link should be created if it doesn't exist already.  */  
   CrtWFLnk:boolean,
      /**  Path to the photo file if it exists.  */  
   PhotoFilePath:string,
      /**  Indicates if the PerCon is Global (master or linked)  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany and GlbPerConID that is linking to this PerCon.  */  
   GlbLink:string,
   EnableGlbLock:boolean,
   EnableGlbPerCon:boolean,
      /**  A description of the role.  */  
   RoleCodeRoleDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PerConListTableset{
   PerConList:Erp_Tablesets_PerConListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PerConLnkRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**   The table name and context that this PerConLnk is related to:
Customer(If related to CustCnt and CustCnt.ShipTonum = "")
Ship to(If related to CustCnt and CustCnt.ShipTonum <> "")
Supplier((If related to VendCnt and VendCnt.PurPoint = "")
Supplier PP((If related to VendCnt and VendCnt.PurPoint <> "")
Employee(If related to EmpBasic)
Work force (If related to SalesRep)
Buyer(If related to PurAgent)  */  
   ContextLink:string,
      /**  The SysRowId of the linked table.  */  
   LinkSysRowID:string,
      /**  Flag that indicates the primary link of the Person/Contact.  */  
   PrimaryContext:boolean,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   FaxNum:string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  The contact's email address.  */  
   EMailAddress:string,
      /**  The contact's cell phone number.  */  
   CellPhoneNum:string,
      /**  The contact's pager number.  */  
   PagerNum:string,
      /**  The contact's home number.  */  
   HomeNum:string,
      /**  The contact's alternate phone number.  */  
   AltNum:string,
      /**  Contact's website.  */  
   WebSite:string,
      /**  Contact's IM.  */  
   IM:string,
      /**  Contact's Twitter.  */  
   Twitter:string,
      /**  Contact's LinkedIn.  */  
   LinkedIn:string,
      /**  Contact's FaceBook.  */  
   FaceBook:string,
      /**  User defined Link 1.  */  
   WebLink1:string,
      /**  User defined Link 2.  */  
   WebLink2:string,
      /**  User defined Link 3.  */  
   WebLink3:string,
      /**  User defined Link 4.  */  
   WebLink4:string,
      /**  User defined Link 5.  */  
   WebLink5:string,
      /**  Address line 1  */  
   Address1:string,
      /**  Address line 2  */  
   Address2:string,
      /**  Address line 3  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  State/Province  */  
   State:string,
      /**  Zip/Postal Code  */  
   Zip:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  The Country.CountryNum value related to the SalesRep.Country value.  */  
   CountryNum:number,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   CorpName:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Customer ID from Customer table.  */  
   CustID:string,
      /**  Full name of the customer.  */  
   CustName:string,
      /**  Number of the Ship To for the Customer Contact.  */  
   ShipToNum:string,
      /**  Name of the customer contact's Ship To.  */  
   ShipToName:string,
      /**  Name of the Customer Contact.  */  
   CustContactName:string,
      /**  Vendor ID from the Vendor table.  */  
   VendorID:string,
      /**  Name of the vendor.  */  
   VendorName:string,
      /**  Purchase Point from the Vendor.  */  
   PurPoint:string,
      /**  Name of the vendor's purchase point.  */  
   PurPointName:string,
      /**  Name of the vendor's contact.  */  
   VendorContactName:string,
      /**  The code of the sales representative, from the SalesRep table.  */  
   SalesRepCode:string,
      /**  Name of the sales representative.  */  
   SalesRepName:string,
      /**  Buyer ID from the PurAgent table.  */  
   BuyerID:string,
      /**  Name of the buyer.  */  
   BuyerName:string,
      /**  Employee ID from the EmpBasic table.  */  
   EmpID:string,
      /**  Name of the employee.  */  
   EmpName:string,
   PREmpID:string,
   PREmpName:string,
      /**  Shows the value of the Sync. Name flag in the linked record.  */  
   SyncNameToPerCon:boolean,
      /**  Shows the value of the Sync. Address flag in the linked record.  */  
   SyncAddressToPerCon:boolean,
      /**  Shows the value of the Sync. Phone flag in the linked record.  */  
   SyncPhoneToPerCon:boolean,
      /**  Shows the value of the Sync. Email flag in the linked record.  */  
   SyncEmailToPerCon:boolean,
      /**  Shows the value of the Sync. Links flag in the linked record.  */  
   SyncLinksToPerCon:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PerConRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Full name of the contact.  */  
   Name:string,
      /**  Contact's first name.  */  
   FirstName:string,
      /**  Contact's middle name.  */  
   MiddleName:string,
      /**  Contact's last name.  */  
   LastName:string,
      /**  Name used by Payroll - defaults to FullName - link this field to the name field in Empbasic and in the future to PREmpMas.  */  
   PRName:string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   Func:string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   FaxNum:string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  The contact's email address.  */  
   EMailAddress:string,
      /**  The contact's cell phone number.  */  
   CellPhoneNum:string,
      /**  The contact's pager number.  */  
   PagerNum:string,
      /**  The contact's home number.  */  
   HomeNum:string,
      /**  The contact's alternate phone number.  */  
   AltNum:string,
      /**  Contact's prefix.  */  
   Prefix:string,
      /**  Contact's suffix.  */  
   Suffix:string,
      /**  Contact's initials.  */  
   Initials:string,
      /**  Contact's website.  */  
   WebSite:string,
      /**  Contact's IM.  */  
   IM:string,
      /**  Contact's Twitter.  */  
   Twitter:string,
      /**  Contact's LinkedIn.  */  
   LinkedIn:string,
      /**  Contact's FaceBook.  */  
   FaceBook:string,
      /**  User defined Link 1.  */  
   WebLink1:string,
      /**  User defined Link 2.  */  
   WebLink2:string,
      /**  User defined Link 3.  */  
   WebLink3:string,
      /**  User defined Link 4.  */  
   WebLink4:string,
      /**  User defined Link 5.  */  
   WebLink5:string,
      /**  Address line 1  */  
   Address1:string,
      /**  Address line 2  */  
   Address2:string,
      /**  Address line 3  */  
   Address3:string,
      /**  City  */  
   City:string,
      /**  State/Province  */  
   State:string,
      /**  Zip/Postal Code  */  
   Zip:string,
      /**  Country is used as part of the mailing address. It can be left blank.  */  
   Country:string,
      /**  The Country.CountryNum value related to the SalesRep.Country value.  */  
   CountryNum:number,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   CorpName:string,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   RoleCode:string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   Comment:string,
      /**  Contact's title.  */  
   ContactTitle:string,
      /**  The name of the person this contact reports to.  */  
   ReportsTo:string,
      /**  Contact's payroll last name.  */  
   PRLastName:string,
      /**  Contact's payroll first name.  */  
   PRFirstName:string,
      /**  Contact's payroll middle name.  */  
   PRMiddleName:string,
      /**  The System User ID.  */  
   DcdUserID:string,
      /**  Name of file that contains the employee's photo image.  This can be blank (no photo available).  Employee photos are stored in the following directory structure ManufacturingSystem\Emphoto\(Company ID). directory  */  
   PhotoFile:string,
      /**  Marks the PerCon as a global PerCon, available to be sent out to other companies.  */  
   GlobalPerCon:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Indicates if the record is linked from HCM  */  
   HCMLinked:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  */  
   IssuerPrsnIDCode:string,
      /**  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  */  
   IssuerIDType:string,
      /**  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  */  
   IssuerName:string,
      /**  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  */  
   IssuerSurname:string,
      /**  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  */  
   IssuerSerialNum:string,
      /**  Used in Romania CSF - Additional info for printing on invoice, such as Name & Surname, Personal ID code, ID type & serial number, date of ID issuance.  */  
   IssuerIDIssDate:string,
      /**  ImageID  */  
   ImageID:string,
      /**  Logical column used for Create Selected Links action menu. Indicates that a Buyer link should be created if it doesn't exist already.  */  
   CrtBuyerLnk:boolean,
      /**  Logical column used for Create Selected Links action menu. Indicates that an Employee link should be created if it doesn't exist already.  */  
   CrtEmpLnk:boolean,
      /**  Logical column used for Create Selected Links action menu. Indicates that a PR Employee link should be created if it doesn't exist already.  */  
   CrtPREmpLnk:boolean,
      /**  Logical column used for Create Selected Links action menu. Indicates that a Work Force link should be created if it doesn't exist already.  */  
   CrtWFLnk:boolean,
   EnableGlbLock:boolean,
   EnableGlbPerCon:boolean,
      /**  Indicates if the PerCon is Global (master or linked)  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany and GlbPerConID that is linking to this PerCon.  */  
   GlbLink:string,
      /**  Path to the photo file if it exists.  */  
   PhotoFilePath:string,
   EnableCreateBuyer:boolean,
   EnableCreateEmployee:boolean,
   EnableCreatePREmployee:boolean,
   EnableCreateWorkForce:boolean,
   BitFlag:number,
   RoleCodeRoleDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PerConTableset{
   PerCon:Erp_Tablesets_PerConRow[],
   PerConAttch:Erp_Tablesets_PerConAttchRow[],
   PerConLnk:Erp_Tablesets_PerConLnkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPerConTableset{
   PerCon:Erp_Tablesets_PerConRow[],
   PerConAttch:Erp_Tablesets_PerConAttchRow[],
   PerConLnk:Erp_Tablesets_PerConLnkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param perConID
   */  
export interface GetByID_input{
   perConID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PerConTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PerConTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PerConTableset[],
}

   /** Required : 
      @param IP_ServerFileName
   */  
export interface GetClientFileName_input{
   IP_ServerFileName:string,
}

export interface GetClientFileName_output{
   returnObj:string,
}

   /** Required : 
      @param glbPerConIDList
   */  
export interface GetGlbPerConList_input{
      /**  Delimited list of GlbPerConID values  */  
   glbPerConIDList:string,
}

export interface GetGlbPerConList_output{
   returnObj:Erp_Tablesets_GlbPerConTableset[],
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
   returnObj:Erp_Tablesets_PerConListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param perConID
   */  
export interface GetNewPerConAttch_input{
   ds:Erp_Tablesets_PerConTableset[],
   perConID:number,
}

export interface GetNewPerConAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PerConTableset,
}
}

   /** Required : 
      @param ds
      @param perConID
      @param contextLink
   */  
export interface GetNewPerConLnk_input{
   ds:Erp_Tablesets_PerConTableset[],
   perConID:number,
   contextLink:string,
}

export interface GetNewPerConLnk_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PerConTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPerCon_input{
   ds:Erp_Tablesets_PerConTableset[],
}

export interface GetNewPerCon_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PerConTableset,
}
}

   /** Required : 
      @param ipPerConID
   */  
export interface GetPerConForLink_input{
      /**  Global PerConID field on the GlbPerCon record to link  */  
   ipPerConID:number,
}

export interface GetPerConForLink_output{
   returnObj:Erp_Tablesets_PerConTableset[],
}

   /** Required : 
      @param PerConID
      @param GlobalLock
   */  
export interface GetPerConGlobalFields_input{
   PerConID:number,
   GlobalLock:boolean,
}

export interface GetPerConGlobalFields_output{
   returnObj:string,
}

   /** Required : 
      @param whereClausePerCon
      @param whereClausePerConAttch
      @param whereClausePerConLnk
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePerCon:string,
   whereClausePerConAttch:string,
   whereClausePerConLnk:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PerConTableset[],
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

export interface IsPayrollManager_output{
   returnObj:boolean,
}

   /** Required : 
      @param glbCompany
      @param glbPerConID
      @param GlbPerConDS
      @param ds1
   */  
export interface LinkGlbPerCon_input{
      /**  Global Company field on the GlbPerCon record to link  */  
   glbCompany:string,
      /**  Global PerConID field on the GlbPerCon record to link  */  
   glbPerConID:number,
   GlbPerConDS:Erp_Tablesets_GlbPerConTableset[],
   ds1:Erp_Tablesets_PerConTableset[],
}

export interface LinkGlbPerCon_output{
parameters : {
      /**  output parameters  */  
   ds1:Erp_Tablesets_PerConTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbPerConID
      @param checkDuplicate
      @param ds
   */  
export interface PreLinkGlbPerCon_input{
      /**  Global Company field on the GlbPerCon record to link  */  
   glbCompany:string,
      /**  Global PerConID field on the GlbPerCon record to link  */  
   glbPerConID:number,
      /**  checkDuplicate  */  
   checkDuplicate:boolean,
   ds:Erp_Tablesets_GlbPerConTableset[],
}

export interface PreLinkGlbPerCon_output{
   returnObj:Erp_Tablesets_PerConListTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbPerConTableset,
   vMessage:string,
}
}

   /** Required : 
      @param glbCompany
      @param glbPerConID
      @param ds
   */  
export interface SkipGlbPerCon_input{
      /**  Global Company field on the GlbPerCon record to skip  */  
   glbCompany:string,
      /**  Global PerConID field on the GlbPerCon record to skip  */  
   glbPerConID:number,
   ds:Erp_Tablesets_GlbPerConTableset[],
}

export interface SkipGlbPerCon_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbPerConTableset,
}
}

   /** Required : 
      @param glbCompany
      @param glbPerConID
      @param ds
   */  
export interface UnlinkGlbPerCon_input{
      /**  Global Company field on the GlbPerCon record to unlink  */  
   glbCompany:string,
      /**  Global PerConID field on the GlbPerCon record to unlink  */  
   glbPerConID:number,
   ds:Erp_Tablesets_GlbPerConTableset[],
}

export interface UnlinkGlbPerCon_output{
   returnObj:Erp_Tablesets_PerConTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbPerConTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPerConTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPerConTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PerConTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PerConTableset,
}
}

