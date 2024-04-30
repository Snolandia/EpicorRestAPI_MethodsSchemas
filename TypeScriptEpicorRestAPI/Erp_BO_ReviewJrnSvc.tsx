import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ReviewJrnSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get ReviewJrns items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReviewJrns
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnRow
   */  
export function get_ReviewJrns(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReviewJrns
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RvJrnRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RvJrnRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReviewJrns(requestBody:Erp_Tablesets_RvJrnRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ReviewJrn item
   Description: Calls GetByID to retrieve the ReviewJrn item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReviewJrn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RvJrnRow
   */  
export function get_ReviewJrns_Company_RvJrnUID(Company:string, RvJrnUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RvJrnRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns(" + Company + "," + RvJrnUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RvJrnRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ReviewJrn for the service
   Description: Calls UpdateExt to update ReviewJrn. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReviewJrn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RvJrnRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ReviewJrns_Company_RvJrnUID(Company:string, RvJrnUID:string, requestBody:Erp_Tablesets_RvJrnRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns(" + Company + "," + RvJrnUID + ")", {
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
   Summary: Call UpdateExt to delete ReviewJrn item
   Description: Call UpdateExt to delete ReviewJrn item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReviewJrn
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ReviewJrns_Company_RvJrnUID(Company:string, RvJrnUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns(" + Company + "," + RvJrnUID + ")", {
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
   Description: Get RvJrnTrs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RvJrnTrs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrRow
   */  
export function get_ReviewJrns_Company_RvJrnUID_RvJrnTrs(Company:string, RvJrnUID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns(" + Company + "," + RvJrnUID + ")/RvJrnTrs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RvJrnTr item
   Description: Calls GetByID to retrieve the RvJrnTr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTr1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RvJrnTrRow
   */  
export function get_ReviewJrns_Company_RvJrnUID_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID(Company:string, RvJrnUID:string, RvJrnTrUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RvJrnTrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ReviewJrns(" + Company + "," + RvJrnUID + ")/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RvJrnTrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RvJrnTrs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RvJrnTrs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrRow
   */  
export function get_RvJrnTrs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RvJrnTrs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RvJrnTrRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RvJrnTrRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RvJrnTrs(requestBody:Erp_Tablesets_RvJrnTrRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RvJrnTr item
   Description: Calls GetByID to retrieve the RvJrnTr item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RvJrnTrRow
   */  
export function get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID(Company:string, RvJrnUID:string, RvJrnTrUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RvJrnTrRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RvJrnTrRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RvJrnTr for the service
   Description: Calls UpdateExt to update RvJrnTr. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RvJrnTr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RvJrnTrRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID(Company:string, RvJrnUID:string, RvJrnTrUID:string, requestBody:Erp_Tablesets_RvJrnTrRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")", {
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
   Summary: Call UpdateExt to delete RvJrnTr item
   Description: Call UpdateExt to delete RvJrnTr item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RvJrnTr
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID(Company:string, RvJrnUID:string, RvJrnTrUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")", {
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
   Description: Get RvJrnTrDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RvJrnTrDtls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrDtlRow
   */  
export function get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtls(Company:string, RvJrnUID:string, RvJrnTrUID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")/RvJrnTrDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RvJrnTrDtl item
   Description: Calls GetByID to retrieve the RvJrnTrDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTrDtl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param RvJrnTrDtlUID Desc: RvJrnTrDtlUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RvJrnTrDtlRow
   */  
export function get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtls_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtlUID(Company:string, RvJrnUID:string, RvJrnTrUID:string, RvJrnTrDtlUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RvJrnTrDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")/RvJrnTrDtls(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + RvJrnTrDtlUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RvJrnTrDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get RvJrnTrTreeLeaves items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RvJrnTrTreeLeaves1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrTreeLeafRow
   */  
export function get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID_RvJrnTrTreeLeaves(Company:string, RvJrnUID:string, RvJrnTrUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrTreeLeafRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")/RvJrnTrTreeLeaves", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrTreeLeafRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RvJrnTrTreeLeaf item
   Description: Calls GetByID to retrieve the RvJrnTrTreeLeaf item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTrTreeLeaf1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RvJrnTrTreeLeafRow
   */  
export function get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID_RvJrnTrTreeLeaves_SysRowID(Company:string, RvJrnUID:string, RvJrnTrUID:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RvJrnTrTreeLeafRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")/RvJrnTrTreeLeaves(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RvJrnTrTreeLeafRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get WErrors items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_WErrors1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WErrorRow
   */  
export function get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID_WErrors(Company:string, RvJrnUID:string, RvJrnTrUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WErrorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")/WErrors", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WErrorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the WError item
   Description: Calls GetByID to retrieve the WError item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WError1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param ErrorUID Desc: ErrorUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.WErrorRow
   */  
export function get_RvJrnTrs_Company_RvJrnUID_RvJrnTrUID_WErrors_Company_RvJrnUID_RvJrnTrUID_ErrorUID(Company:string, RvJrnUID:string, RvJrnTrUID:string, ErrorUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WErrorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrs(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + ")/WErrors(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + ErrorUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_WErrorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RvJrnTrDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RvJrnTrDtls
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrDtlRow
   */  
export function get_RvJrnTrDtls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RvJrnTrDtls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RvJrnTrDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RvJrnTrDtls(requestBody:Erp_Tablesets_RvJrnTrDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RvJrnTrDtl item
   Description: Calls GetByID to retrieve the RvJrnTrDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTrDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param RvJrnTrDtlUID Desc: RvJrnTrDtlUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RvJrnTrDtlRow
   */  
export function get_RvJrnTrDtls_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtlUID(Company:string, RvJrnUID:string, RvJrnTrUID:string, RvJrnTrDtlUID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RvJrnTrDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + RvJrnTrDtlUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RvJrnTrDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RvJrnTrDtl for the service
   Description: Calls UpdateExt to update RvJrnTrDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RvJrnTrDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param RvJrnTrDtlUID Desc: RvJrnTrDtlUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RvJrnTrDtls_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtlUID(Company:string, RvJrnUID:string, RvJrnTrUID:string, RvJrnTrDtlUID:string, requestBody:Erp_Tablesets_RvJrnTrDtlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + RvJrnTrDtlUID + ")", {
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
   Summary: Call UpdateExt to delete RvJrnTrDtl item
   Description: Call UpdateExt to delete RvJrnTrDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RvJrnTrDtl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param RvJrnTrDtlUID Desc: RvJrnTrDtlUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RvJrnTrDtls_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtlUID(Company:string, RvJrnUID:string, RvJrnTrUID:string, RvJrnTrDtlUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + RvJrnTrDtlUID + ")", {
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
   Description: Get RvJrnTrDtlRefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RvJrnTrDtlRefs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param RvJrnTrDtlUID Desc: RvJrnTrDtlUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrDtlRefRow
   */  
export function get_RvJrnTrDtls_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtlUID_RvJrnTrDtlRefs(Company:string, RvJrnUID:string, RvJrnTrUID:string, RvJrnTrDtlUID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrDtlRefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + RvJrnTrDtlUID + ")/RvJrnTrDtlRefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrDtlRefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RvJrnTrDtlRef item
   Description: Calls GetByID to retrieve the RvJrnTrDtlRef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTrDtlRef1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param RvJrnTrDtlUID Desc: RvJrnTrDtlUID   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RvJrnTrDtlRefRow
   */  
export function get_RvJrnTrDtls_Company_RvJrnUID_RvJrnTrUID_RvJrnTrDtlUID_RvJrnTrDtlRefs_SysRowID(Company:string, RvJrnUID:string, RvJrnTrUID:string, RvJrnTrDtlUID:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RvJrnTrDtlRefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtls(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + RvJrnTrDtlUID + ")/RvJrnTrDtlRefs(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RvJrnTrDtlRefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RvJrnTrDtlRefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RvJrnTrDtlRefs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrDtlRefRow
   */  
export function get_RvJrnTrDtlRefs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrDtlRefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtlRefs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrDtlRefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RvJrnTrDtlRefs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RvJrnTrDtlRefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RvJrnTrDtlRefs(requestBody:Erp_Tablesets_RvJrnTrDtlRefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtlRefs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RvJrnTrDtlRef item
   Description: Calls GetByID to retrieve the RvJrnTrDtlRef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTrDtlRef
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RvJrnTrDtlRefRow
   */  
export function get_RvJrnTrDtlRefs_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RvJrnTrDtlRefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtlRefs(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RvJrnTrDtlRefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RvJrnTrDtlRef for the service
   Description: Calls UpdateExt to update RvJrnTrDtlRef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RvJrnTrDtlRef
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RvJrnTrDtlRefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RvJrnTrDtlRefs_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_RvJrnTrDtlRefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtlRefs(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete RvJrnTrDtlRef item
   Description: Call UpdateExt to delete RvJrnTrDtlRef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RvJrnTrDtlRef
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RvJrnTrDtlRefs_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrDtlRefs(" + SysRowID + ")", {
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
   Description: Get RvJrnTrTreeLeaves items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RvJrnTrTreeLeaves
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnTrTreeLeafRow
   */  
export function get_RvJrnTrTreeLeaves(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrTreeLeafRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrTreeLeaves", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrTreeLeafRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RvJrnTrTreeLeaves
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RvJrnTrTreeLeafRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.RvJrnTrTreeLeafRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RvJrnTrTreeLeaves(requestBody:Erp_Tablesets_RvJrnTrTreeLeafRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrTreeLeaves", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the RvJrnTrTreeLeaf item
   Description: Calls GetByID to retrieve the RvJrnTrTreeLeaf item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RvJrnTrTreeLeaf
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.RvJrnTrTreeLeafRow
   */  
export function get_RvJrnTrTreeLeaves_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_RvJrnTrTreeLeafRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrTreeLeaves(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_RvJrnTrTreeLeafRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RvJrnTrTreeLeaf for the service
   Description: Calls UpdateExt to update RvJrnTrTreeLeaf. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RvJrnTrTreeLeaf
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.RvJrnTrTreeLeafRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RvJrnTrTreeLeaves_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_RvJrnTrTreeLeafRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrTreeLeaves(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete RvJrnTrTreeLeaf item
   Description: Call UpdateExt to delete RvJrnTrTreeLeaf item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RvJrnTrTreeLeaf
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RvJrnTrTreeLeaves_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RvJrnTrTreeLeaves(" + SysRowID + ")", {
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
   Description: Get WErrors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_WErrors
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.WErrorRow
   */  
export function get_WErrors(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WErrorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/WErrors", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WErrorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_WErrors
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.WErrorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.WErrorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_WErrors(requestBody:Erp_Tablesets_WErrorRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/WErrors", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the WError item
   Description: Calls GetByID to retrieve the WError item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_WError
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param ErrorUID Desc: ErrorUID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.WErrorRow
   */  
export function get_WErrors_Company_RvJrnUID_RvJrnTrUID_ErrorUID(Company:string, RvJrnUID:string, RvJrnTrUID:string, ErrorUID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_WErrorRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/WErrors(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + ErrorUID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_WErrorRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update WError for the service
   Description: Calls UpdateExt to update WError. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_WError
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param ErrorUID Desc: ErrorUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.WErrorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_WErrors_Company_RvJrnUID_RvJrnTrUID_ErrorUID(Company:string, RvJrnUID:string, RvJrnTrUID:string, ErrorUID:string, requestBody:Erp_Tablesets_WErrorRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/WErrors(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + ErrorUID + ")", {
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
   Summary: Call UpdateExt to delete WError item
   Description: Call UpdateExt to delete WError item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_WError
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RvJrnUID Desc: RvJrnUID   Required: True
      @param RvJrnTrUID Desc: RvJrnTrUID   Required: True
      @param ErrorUID Desc: ErrorUID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_WErrors_Company_RvJrnUID_RvJrnTrUID_ErrorUID(Company:string, RvJrnUID:string, RvJrnTrUID:string, ErrorUID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/WErrors(" + Company + "," + RvJrnUID + "," + RvJrnTrUID + "," + ErrorUID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RvJrnListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnListRow)
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
export function get_GetRows(whereClauseRvJrn:string, whereClauseRvJrnTr:string, whereClauseRvJrnTrDtl:string, whereClauseRvJrnTrDtlRef:string, whereClauseRvJrnTrTreeLeaf:string, whereClauseWError:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseRvJrn!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRvJrn=" + whereClauseRvJrn
   }
   if(typeof whereClauseRvJrnTr!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRvJrnTr=" + whereClauseRvJrnTr
   }
   if(typeof whereClauseRvJrnTrDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRvJrnTrDtl=" + whereClauseRvJrnTrDtl
   }
   if(typeof whereClauseRvJrnTrDtlRef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRvJrnTrDtlRef=" + whereClauseRvJrnTrDtlRef
   }
   if(typeof whereClauseRvJrnTrTreeLeaf!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRvJrnTrTreeLeaf=" + whereClauseRvJrnTrTreeLeaf
   }
   if(typeof whereClauseWError!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseWError=" + whereClauseWError
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(rvJrnUID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof rvJrnUID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rvJrnUID=" + rvJrnUID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method GetJournalHeader
   OperationID: GetJournalHeader
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetJournalHeader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJournalHeader_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJournalHeader(requestBody:GetJournalHeader_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetJournalHeader_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetJournalHeader", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetJournalHeader_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetJournalTreeLeaf
   Description: This method populates RvJrnTrDtl datatable in reference ReviewJrnTableset dataset.
It depends on ipRvJrnTrUID, ipTreeLeafUID (Leef Node number) and Leef records limit (1000 by the default).
   OperationID: GetJournalTreeLeaf
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetJournalTreeLeaf_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetJournalTreeLeaf_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetJournalTreeLeaf(requestBody:GetJournalTreeLeaf_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetJournalTreeLeaf_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetJournalTreeLeaf", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetJournalTreeLeaf_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RestoreTmpJournalLine
   OperationID: RestoreTmpJournalLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RestoreTmpJournalLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RestoreTmpJournalLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RestoreTmpJournalLine(requestBody:RestoreTmpJournalLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RestoreTmpJournalLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/RestoreTmpJournalLine", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RestoreTmpJournalLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExcludeFromList
   Description: Exclude journals from the list with do not conform search criteria.
   OperationID: ExcludeFromList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExcludeFromList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExcludeFromList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExcludeFromList(requestBody:ExcludeFromList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExcludeFromList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ExcludeFromList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExcludeFromList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRefTypeList
   Description: Get list of reference types.
   OperationID: GetRefTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRefTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRefTypeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRefTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetRefTypeList", {
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
         resolve(data as GetRefTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessJournal
   Description: Confirm or cancel journal entry.
   OperationID: ProcessJournal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessJournal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessJournal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessJournal(requestBody:ProcessJournal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessJournal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/ProcessJournal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ProcessJournal_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLockRecords
   Description: Populates Lock records list. Based on RvLock table (ABTUID = '').
   OperationID: GetLockRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLockRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLockRecords(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLockRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetLockRecords", {
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
         resolve(data as GetLockRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteRvLockRecords
   Description: This method removed selected RvLock records with child related lockings from the database
   OperationID: DeleteRvLockRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteRvLockRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRvLockRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteRvLockRecords(requestBody:DeleteRvLockRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteRvLockRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/DeleteRvLockRecords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteRvLockRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TransValidate
   Description: Validate Transactions for current journal.
   OperationID: TransValidate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/TransValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TransValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TransValidate(requestBody:TransValidate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<TransValidate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/TransValidate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as TransValidate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: GetCodeDescList
   OperationID: GetCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:GetCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetCodeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsWithGroupCheck
   Description: The extended method for retireving rows with additional filter by Group
   OperationID: GetRowsWithGroupCheck
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsWithGroupCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsWithGroupCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsWithGroupCheck(requestBody:GetRowsWithGroupCheck_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsWithGroupCheck_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetRowsWithGroupCheck", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsWithGroupCheck_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRvJrn
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRvJrn
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRvJrn_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRvJrn_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRvJrn(requestBody:GetNewRvJrn_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRvJrn_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetNewRvJrn", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRvJrn_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRvJrnTr
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRvJrnTr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRvJrnTr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRvJrnTr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRvJrnTr(requestBody:GetNewRvJrnTr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRvJrnTr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetNewRvJrnTr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRvJrnTr_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRvJrnTrDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRvJrnTrDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRvJrnTrDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRvJrnTrDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRvJrnTrDtl(requestBody:GetNewRvJrnTrDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRvJrnTrDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetNewRvJrnTrDtl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewRvJrnTrDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewWError
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewWError
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewWError_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewWError_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewWError(requestBody:GetNewWError_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewWError_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetNewWError", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewWError_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReviewJrnSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RvJrnListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RvJrnRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrDtlRefRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RvJrnTrDtlRefRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RvJrnTrDtlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RvJrnTrRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RvJrnTrTreeLeafRow{
   "odatametadata":string,
   "value":Erp_Tablesets_RvJrnTrTreeLeafRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_WErrorRow{
   "odatametadata":string,
   "value":Erp_Tablesets_WErrorRow,
}

export interface Erp_Tablesets_RvJrnListRow{
      /**  Review Journal unique ID.  */  
   "RvJrnUID":number,
      /**  Journal Entry Date  */  
   "JeDate":string,
      /**  True if transaction is valid.  */  
   "IsValid":boolean,
      /**  Posting Mode.  */  
   "PostingMode":string,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   "SourceModule":string,
      /**  User unique ID.  */  
   "UserUID":string,
      /**  Change date.  */  
   "ChangeDate":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Date that this transaction was posted to the G/L files.  */  
   "PostedDate":string,
      /**  Review date  */  
   "RvDate":string,
      /**  Identifies the review journal entry as a simulation transaction that is not going to be posted to the general ledger.  Yes indicates the transaction is a simulated transaction.  No indicates the transaction is a general ledger transaction.  */  
   "Simulation":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Error flag.  */  
   "HasErr":boolean,
      /**   Flag shows that Review Journal is locked.
0 - Not Locked
1 - Posting - Transaction is still on posting process
2 - Aborted - Posting process was finished abnormally and should be cancelled by user  */  
   "IsLcked":number,
      /**  Text value of IsLcked field  */  
   "LockStatus":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RvJrnRow{
      /**  Review Journal unique ID.  */  
   "RvJrnUID":number,
      /**  Journal Entry Date  */  
   "JeDate":string,
      /**  True if transaction is valid.  */  
   "IsValid":boolean,
      /**  Posting Mode.  */  
   "PostingMode":string,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   "SourceModule":string,
      /**  User unique ID.  */  
   "UserUID":string,
      /**  Change date.  */  
   "ChangeDate":string,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Date that this transaction was posted to the G/L files.  */  
   "PostedDate":string,
      /**  Review date  */  
   "RvDate":string,
      /**  Identifies the review journal entry as a simulation transaction that is not going to be posted to the general ledger.  Yes indicates the transaction is a simulated transaction.  No indicates the transaction is a general ledger transaction.  */  
   "Simulation":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Error flag.  */  
   "HasErr":boolean,
      /**   Flag shows that Review Journal is locked.
0 - Not Locked
1 - Posting - Transaction is still on posting process
2 - Aborted - Posting process was finished abnormally and should be cancelled by user  */  
   "IsLcked":number,
      /**  Text value of IsLcked field  */  
   "LockStatus":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RvJrnTrDtlRefRow{
      /**  Reference to RvJrn.  */  
   "RvJrnUID":number,
      /**  Reference to RvJrnTr.  */  
   "RvJrnTrUID":number,
      /**  Reference to RvJrnTrDtl.  */  
   "RvJrnTrDtlUID":number,
      /**  Reference code.  */  
   "RefCode":string,
      /**  Reference UID.  */  
   "RefUID":number,
      /**  Reference value.  */  
   "RefValue":string,
      /**  Line can be summarized.  */  
   "IsSummarize":boolean,
   "Company":string,
      /**  ParentLine  */  
   "ParentLine":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RvJrnTrDtlRow{
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
      /**  External Segment Value 1  */  
   "ExtSegValue1":string,
      /**  Ext Segment Value 2  */  
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
      /**  if yes, the balance records are not updated for the GLJrnDtl even if the GL Account resolves to a valid GL Balance Account.  */  
   "SkipBalances":boolean,
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
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
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
      /**   P = derived from Period Balance records via Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations  */  
   "SrcType":string,
      /**  Review Journal Transaction Detail unique ID.  */  
   "RvJrnTrDtlUID":number,
      /**  Review Journal Transaction Table unique ID.  */  
   "RvJrnTrUID":number,
      /**  Review Journal unique ID.  */  
   "RvJrnUID":number,
      /**  Technical identifier.  */  
   "BRuleUID":number,
      /**  True if transaction is summarized.  */  
   "IsSummarize":boolean,
      /**  Reference unique ID.  */  
   "RefUID":number,
      /**  Change date.  */  
   "ChangeDate":string,
      /**  CloseFiscalPeriod  */  
   "CloseFiscalPeriod":number,
      /**  Tran Seq  */  
   "TranSeq":number,
      /**  Credit Amount.  */  
   "CreditAmount":number,
      /**  Debit Amount.  */  
   "DebitAmount":number,
      /**  Book Credit Amount  */  
   "BookCreditAmount":number,
      /**  Book Debit Amount  */  
   "BookDebitAmount":number,
      /**  ParentLine  */  
   "ParentLine":number,
      /**  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  */  
   "ParentRUID":string,
      /**  if has reverse line  */  
   "HasReverseLine":boolean,
      /**  This is the last allocation stamp to affect this GLJrnDtl.  */  
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
      /**  External GL Account, from Main COA of External Company (GLBGLAccount)  */  
   "ExtGLAccount":string,
      /**  External COA, should be MAin COA from External Company (GLBCOA)  */  
   "ExtCOACode":string,
      /**  Used to create a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports.  */  
   "CorrAccUID":number,
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
      /**  The Internal CustNum that ties back to the Customer master file.  */  
   "CustNum":number,
      /**  SourcePlant  */  
   "SourcePlant":string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   "ExtSysType":string,
      /**  URL for drill back to an integrated external system  */  
   "ExtSysURL":string,
   "BookCurrencyCode":string,
   "DebitCreditLine":string,
      /**  Debit Amount flag.  */  
   "IsDebitAmount":boolean,
      /**  Line Amount.  */  
   "LineAmount":number,
      /**  Show Yes if it is Red Storno transaction  */  
   "RedStorno":boolean,
      /**  Statistical Amount. UI display value.  */  
   "StatAmount":number,
      /**  TreeLeafUID  */  
   "TreeLeafUID":number,
   "BitFlag":number,
   "CurrencyCodeCurrencyID":string,
   "CurrencyCodeDocumentDesc":string,
   "CurrencyCodeCurrSymbol":string,
   "CurrencyCodeCurrName":string,
   "CurrencyCodeCurrDesc":string,
   "GLAccountDesc":string,
   "GLGLAcctDisp":string,
   "GLGLShortAcct":string,
   "JournalCodeJrnlDescription":string,
   "LinkToBookingRuleDisplayName":string,
   "RvTranGLCGLAcctContext":string,
   "RvTranGLCKey6":string,
   "RvTranGLCKey5":string,
   "RvTranGLCKey3":string,
   "RvTranGLCRelatedToFile":string,
   "RvTranGLCKey2":string,
   "RvTranGLCKey1":string,
   "RvTranGLCKey4":string,
   "RvTranGLCSysGLControlType":string,
   "StatUOMStatUOMDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RvJrnTrRow{
      /**  Review Journal Transaction Table unique ID.  */  
   "RvJrnTrUID":number,
      /**  Review Journal unique ID.  */  
   "RvJrnUID":number,
      /**  BookID  */  
   "BookID":string,
      /**  True if transaction is valid.  */  
   "IsValid":boolean,
      /**  True if transaction is reverse.  */  
   "IsReverse":boolean,
      /**  Transaction number.  */  
   "TranNum":number,
      /**  Legal number.  */  
   "LegalNum":number,
      /**  Description.  */  
   "Description":string,
      /**  Credit Amount.  */  
   "CreditAmount":number,
      /**  Debit Amount.  */  
   "DebitAmount":number,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   "JournalCode":string,
      /**  User unique ID.  */  
   "UserUID":string,
      /**  Change date.  */  
   "ChangeDate":string,
      /**  Fiscal year that entry applies to.  */  
   "FiscalYear":number,
      /**  Fiscal period that this journal entry applies to.  */  
   "FiscalPeriod":number,
      /**  Code of Chart of Account  */  
   "COACode":string,
      /**  Book Credit Amount  */  
   "BookCreditAmount":number,
      /**  Book Debit Amount  */  
   "BookDebitAmount":number,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Date for this journal transaction entry.  */  
   "JEDate":string,
      /**  Date that this transaction was posted to the G/L files.  */  
   "PostedDate":string,
      /**  Account transaction revision UID. Technical identifier.  */  
   "ACTRevisionUID":number,
      /**  Account transaction type UID. Technical identifier. Reference to an account transaction type.  */  
   "ACTTypeUID":number,
      /**  ABTUID,guid  */  
   "ABTUID":string,
      /**  Identifies the review journal entry as a simulation transaction that is not going to be posted to the general ledger.  Yes indicates the transaction is a simulated transaction.  No indicates the transaction is a general ledger transaction.  */  
   "Simulation":boolean,
      /**  Statistical UOM code.  */  
   "StatUOMCode":string,
      /**  This field shows the Total Debit statistical amount.  */  
   "DebitStatAmt":number,
      /**  This field shows the Total Credit statistical amount.  */  
   "CreditStatAmt":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Error flag.  */  
   "HasErr":boolean,
      /**  Flag to show book using special font.  */  
   "MarkBook":boolean,
      /**  Balance Amount.  */  
   "BalanceAmount":number,
   "BookCurrencyCode":string,
   "BitFlag":number,
   "ActRevisionRevisionCode":string,
   "ActTypeDisplayName":string,
   "BookCurrencyCode_":string,
   "BookDescription":string,
   "JournalCodeJrnlDescription":string,
   "StatUOMStatUOMDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_RvJrnTrTreeLeafRow{
   "BookID":string,
      /**  Company  */  
   "Company":string,
      /**  Description  */  
   "Description":string,
      /**  RvJrnTrUID  */  
   "RvJrnTrUID":number,
      /**  RvJrnUID  */  
   "RvJrnUID":number,
      /**  TreeLeafUID  */  
   "TreeLeafUID":number,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_WErrorRow{
      /**  Error unique ID.  */  
   "ErrorUID":number,
      /**  Review Journal Transaction Table unique ID.  */  
   "RvJrnTrUID":number,
      /**  Description.  */  
   "Description":string,
      /**  True if record represents error.  */  
   "IsError":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  Review Journal unique ID.  */  
   "RvJrnUID":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  1 - Warning/Error was added during creation of transaction line. Cannot be revalidated in Review Journal. 0 - Warning/Error can be revalidated in Review Journal.  */  
   "Persistent":boolean,
   "ErrKind":string,
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
      @param rvJrnUID
   */  
export interface DeleteByID_input{
   rvJrnUID:number,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param ds
   */  
export interface DeleteRvLockRecords_input{
   ds:Erp_Tablesets_RvLockTableset[],
}

export interface DeleteRvLockRecords_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_RvLockTableset,
}
}

export interface Erp_Tablesets_ReviewJrnTableset{
   RvJrn:Erp_Tablesets_RvJrnRow[],
   RvJrnTr:Erp_Tablesets_RvJrnTrRow[],
   RvJrnTrDtl:Erp_Tablesets_RvJrnTrDtlRow[],
   RvJrnTrDtlRef:Erp_Tablesets_RvJrnTrDtlRefRow[],
   RvJrnTrTreeLeaf:Erp_Tablesets_RvJrnTrTreeLeafRow[],
   WError:Erp_Tablesets_WErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RvJrnListRow{
      /**  Review Journal unique ID.  */  
   RvJrnUID:number,
      /**  Journal Entry Date  */  
   JeDate:string,
      /**  True if transaction is valid.  */  
   IsValid:boolean,
      /**  Posting Mode.  */  
   PostingMode:string,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   SourceModule:string,
      /**  User unique ID.  */  
   UserUID:string,
      /**  Change date.  */  
   ChangeDate:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Date that this transaction was posted to the G/L files.  */  
   PostedDate:string,
      /**  Review date  */  
   RvDate:string,
      /**  Identifies the review journal entry as a simulation transaction that is not going to be posted to the general ledger.  Yes indicates the transaction is a simulated transaction.  No indicates the transaction is a general ledger transaction.  */  
   Simulation:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Error flag.  */  
   HasErr:boolean,
      /**   Flag shows that Review Journal is locked.
0 - Not Locked
1 - Posting - Transaction is still on posting process
2 - Aborted - Posting process was finished abnormally and should be cancelled by user  */  
   IsLcked:number,
      /**  Text value of IsLcked field  */  
   LockStatus:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RvJrnListTableset{
   RvJrnList:Erp_Tablesets_RvJrnListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_RvJrnRow{
      /**  Review Journal unique ID.  */  
   RvJrnUID:number,
      /**  Journal Entry Date  */  
   JeDate:string,
      /**  True if transaction is valid.  */  
   IsValid:boolean,
      /**  Posting Mode.  */  
   PostingMode:string,
      /**   Indicates the module that created this journal entry.  This is assigned by the system.
Values can be; AR, AP, GL, PR.  */  
   SourceModule:string,
      /**  User unique ID.  */  
   UserUID:string,
      /**  Change date.  */  
   ChangeDate:string,
      /**  Company Identifier.  */  
   Company:string,
      /**  Date that this transaction was posted to the G/L files.  */  
   PostedDate:string,
      /**  Review date  */  
   RvDate:string,
      /**  Identifies the review journal entry as a simulation transaction that is not going to be posted to the general ledger.  Yes indicates the transaction is a simulated transaction.  No indicates the transaction is a general ledger transaction.  */  
   Simulation:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Error flag.  */  
   HasErr:boolean,
      /**   Flag shows that Review Journal is locked.
0 - Not Locked
1 - Posting - Transaction is still on posting process
2 - Aborted - Posting process was finished abnormally and should be cancelled by user  */  
   IsLcked:number,
      /**  Text value of IsLcked field  */  
   LockStatus:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RvJrnTrDtlRefRow{
      /**  Reference to RvJrn.  */  
   RvJrnUID:number,
      /**  Reference to RvJrnTr.  */  
   RvJrnTrUID:number,
      /**  Reference to RvJrnTrDtl.  */  
   RvJrnTrDtlUID:number,
      /**  Reference code.  */  
   RefCode:string,
      /**  Reference UID.  */  
   RefUID:number,
      /**  Reference value.  */  
   RefValue:string,
      /**  Line can be summarized.  */  
   IsSummarize:boolean,
   Company:string,
      /**  ParentLine  */  
   ParentLine:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RvJrnTrDtlRow{
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
      /**  External Segment Value 1  */  
   ExtSegValue1:string,
      /**  Ext Segment Value 2  */  
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
      /**  if yes, the balance records are not updated for the GLJrnDtl even if the GL Account resolves to a valid GL Balance Account.  */  
   SkipBalances:boolean,
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
      /**  Internal system calcualted sequence number not inteneded for external use.  */  
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
      /**   P = derived from Period Balance records via Periodic Consolidation.
C = derived from GLJrnDtl via Continuous Consolidation.
A = derived from Advanced Allocations  */  
   SrcType:string,
      /**  Review Journal Transaction Detail unique ID.  */  
   RvJrnTrDtlUID:number,
      /**  Review Journal Transaction Table unique ID.  */  
   RvJrnTrUID:number,
      /**  Review Journal unique ID.  */  
   RvJrnUID:number,
      /**  Technical identifier.  */  
   BRuleUID:number,
      /**  True if transaction is summarized.  */  
   IsSummarize:boolean,
      /**  Reference unique ID.  */  
   RefUID:number,
      /**  Change date.  */  
   ChangeDate:string,
      /**  CloseFiscalPeriod  */  
   CloseFiscalPeriod:number,
      /**  Tran Seq  */  
   TranSeq:number,
      /**  Credit Amount.  */  
   CreditAmount:number,
      /**  Debit Amount.  */  
   DebitAmount:number,
      /**  Book Credit Amount  */  
   BookCreditAmount:number,
      /**  Book Debit Amount  */  
   BookDebitAmount:number,
      /**  ParentLine  */  
   ParentLine:number,
      /**  If the current line is reversal, then this field is used for link with original journal line. It equals SysRowID of original line.  */  
   ParentRUID:string,
      /**  if has reverse line  */  
   HasReverseLine:boolean,
      /**  This is the last allocation stamp to affect this GLJrnDtl.  */  
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
      /**  External GL Account, from Main COA of External Company (GLBGLAccount)  */  
   ExtGLAccount:string,
      /**  External COA, should be MAin COA from External Company (GLBCOA)  */  
   ExtCOACode:string,
      /**  Used to create a pair of journal details balancing each other, each detail in the pair should reference the other one. This allows to show correspondence of accounts in reports.  */  
   CorrAccUID:number,
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
      /**  The Internal CustNum that ties back to the Customer master file.  */  
   CustNum:number,
      /**  SourcePlant  */  
   SourcePlant:string,
      /**  Used for integrations - system type for URL specified in ExtSysURL - B = BisTrack / L = LumberTrack / F = FiberTrack / blank = Building Supply  */  
   ExtSysType:string,
      /**  URL for drill back to an integrated external system  */  
   ExtSysURL:string,
   BookCurrencyCode:string,
   DebitCreditLine:string,
      /**  Debit Amount flag.  */  
   IsDebitAmount:boolean,
      /**  Line Amount.  */  
   LineAmount:number,
      /**  Show Yes if it is Red Storno transaction  */  
   RedStorno:boolean,
      /**  Statistical Amount. UI display value.  */  
   StatAmount:number,
      /**  TreeLeafUID  */  
   TreeLeafUID:number,
   BitFlag:number,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrDesc:string,
   GLAccountDesc:string,
   GLGLAcctDisp:string,
   GLGLShortAcct:string,
   JournalCodeJrnlDescription:string,
   LinkToBookingRuleDisplayName:string,
   RvTranGLCGLAcctContext:string,
   RvTranGLCKey6:string,
   RvTranGLCKey5:string,
   RvTranGLCKey3:string,
   RvTranGLCRelatedToFile:string,
   RvTranGLCKey2:string,
   RvTranGLCKey1:string,
   RvTranGLCKey4:string,
   RvTranGLCSysGLControlType:string,
   StatUOMStatUOMDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RvJrnTrRow{
      /**  Review Journal Transaction Table unique ID.  */  
   RvJrnTrUID:number,
      /**  Review Journal unique ID.  */  
   RvJrnUID:number,
      /**  BookID  */  
   BookID:string,
      /**  True if transaction is valid.  */  
   IsValid:boolean,
      /**  True if transaction is reverse.  */  
   IsReverse:boolean,
      /**  Transaction number.  */  
   TranNum:number,
      /**  Legal number.  */  
   LegalNum:number,
      /**  Description.  */  
   Description:string,
      /**  Credit Amount.  */  
   CreditAmount:number,
      /**  Debit Amount.  */  
   DebitAmount:number,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  User unique ID.  */  
   UserUID:string,
      /**  Change date.  */  
   ChangeDate:string,
      /**  Fiscal year that entry applies to.  */  
   FiscalYear:number,
      /**  Fiscal period that this journal entry applies to.  */  
   FiscalPeriod:number,
      /**  Code of Chart of Account  */  
   COACode:string,
      /**  Book Credit Amount  */  
   BookCreditAmount:number,
      /**  Book Debit Amount  */  
   BookDebitAmount:number,
      /**  Company Identifier.  */  
   Company:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Date for this journal transaction entry.  */  
   JEDate:string,
      /**  Date that this transaction was posted to the G/L files.  */  
   PostedDate:string,
      /**  Account transaction revision UID. Technical identifier.  */  
   ACTRevisionUID:number,
      /**  Account transaction type UID. Technical identifier. Reference to an account transaction type.  */  
   ACTTypeUID:number,
      /**  ABTUID,guid  */  
   ABTUID:string,
      /**  Identifies the review journal entry as a simulation transaction that is not going to be posted to the general ledger.  Yes indicates the transaction is a simulated transaction.  No indicates the transaction is a general ledger transaction.  */  
   Simulation:boolean,
      /**  Statistical UOM code.  */  
   StatUOMCode:string,
      /**  This field shows the Total Debit statistical amount.  */  
   DebitStatAmt:number,
      /**  This field shows the Total Credit statistical amount.  */  
   CreditStatAmt:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Error flag.  */  
   HasErr:boolean,
      /**  Flag to show book using special font.  */  
   MarkBook:boolean,
      /**  Balance Amount.  */  
   BalanceAmount:number,
   BookCurrencyCode:string,
   BitFlag:number,
   ActRevisionRevisionCode:string,
   ActTypeDisplayName:string,
   BookCurrencyCode_:string,
   BookDescription:string,
   JournalCodeJrnlDescription:string,
   StatUOMStatUOMDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RvJrnTrTreeLeafRow{
   BookID:string,
      /**  Company  */  
   Company:string,
      /**  Description  */  
   Description:string,
      /**  RvJrnTrUID  */  
   RvJrnTrUID:number,
      /**  RvJrnUID  */  
   RvJrnUID:number,
      /**  TreeLeafUID  */  
   TreeLeafUID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RvLockRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Identifies the master file to which the record is related to.  */  
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
      /**  Date when document has been locked  */  
   LockDate:string,
      /**  Time when document has been locked  */  
   LockTime:number,
      /**  User ID that locked this document.  */  
   LockedBy:string,
      /**  Reference to Review Journal UID.  */  
   RvJrnUID:number,
      /**  Show Status of locked document. Can be "Posting" - if the document has been sent to Posting, "Reviewing" - if the document has not been posted and transaction left in review Journal.  */  
   LockStatus:string,
      /**  Reference to ABT, that is used in posting  */  
   ABTUID:string,
      /**  GlbABTUID  */  
   GlbABTUID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SysTaskNum  */  
   SysTaskNum:number,
   ReleaseRvLockFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_RvLockTableset{
   RvLock:Erp_Tablesets_RvLockRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtReviewJrnTableset{
   RvJrn:Erp_Tablesets_RvJrnRow[],
   RvJrnTr:Erp_Tablesets_RvJrnTrRow[],
   RvJrnTrDtl:Erp_Tablesets_RvJrnTrDtlRow[],
   RvJrnTrDtlRef:Erp_Tablesets_RvJrnTrDtlRefRow[],
   RvJrnTrTreeLeaf:Erp_Tablesets_RvJrnTrTreeLeafRow[],
   WError:Erp_Tablesets_WErrorRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_WErrorRow{
      /**  Error unique ID.  */  
   ErrorUID:number,
      /**  Review Journal Transaction Table unique ID.  */  
   RvJrnTrUID:number,
      /**  Description.  */  
   Description:string,
      /**  True if record represents error.  */  
   IsError:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  Review Journal unique ID.  */  
   RvJrnUID:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  1 - Warning/Error was added during creation of transaction line. Cannot be revalidated in Review Journal. 0 - Warning/Error can be revalidated in Review Journal.  */  
   Persistent:boolean,
   ErrKind:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param intRvJrnUID
      @param intACTTypeUID
      @param strGroupID
   */  
export interface ExcludeFromList_input{
      /**  Journal number  */  
   intRvJrnUID:number,
      /**  Search criteria for RvJrnTr table  */  
   intACTTypeUID:number,
      /**  Search criteria for RvJrnTrDtl table  */  
   strGroupID:string,
}

export interface ExcludeFromList_output{
parameters : {
      /**  output parameters  */  
   lExclude:boolean,
}
}

   /** Required : 
      @param rvJrnUID
   */  
export interface GetByID_input{
   rvJrnUID:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_ReviewJrnTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_ReviewJrnTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_ReviewJrnTableset[],
}

   /** Required : 
      @param systemCode
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
      /**  systemCode  */  
   systemCode:string,
      /**  tableName  */  
   tableName:string,
      /**  fieldName  */  
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param ipRvJrnUID
      @param ipRecLimitPerTr
      @param ds
   */  
export interface GetJournalHeader_input{
      /**  RvJrnUID  */  
   ipRvJrnUID:number,
      /**  RecLimitPerTr  */  
   ipRecLimitPerTr:number,
   ds:Erp_Tablesets_ReviewJrnTableset[],
}

export interface GetJournalHeader_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReviewJrnTableset,
}
}

   /** Required : 
      @param ipRvJrnUID
      @param ipRvJrnTrUID
      @param ipBookID
      @param ipTreeLeafUID
      @param ipRecLimitPerTr
      @param ds
   */  
export interface GetJournalTreeLeaf_input{
      /**  RvJrnUID  */  
   ipRvJrnUID:number,
      /**  RvJrnTrUID  */  
   ipRvJrnTrUID:number,
      /**  BookID  */  
   ipBookID:string,
      /**  TreeLeafUID  */  
   ipTreeLeafUID:number,
      /**  RecLimitPerTr  */  
   ipRecLimitPerTr:number,
   ds:Erp_Tablesets_ReviewJrnTableset[],
}

export interface GetJournalTreeLeaf_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReviewJrnTableset,
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
   returnObj:Erp_Tablesets_RvJrnListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetLockRecords_output{
   returnObj:Erp_Tablesets_RvLockTableset[],
}

   /** Required : 
      @param ds
      @param rvJrnUID
      @param rvJrnTrUID
   */  
export interface GetNewRvJrnTrDtl_input{
   ds:Erp_Tablesets_ReviewJrnTableset[],
   rvJrnUID:number,
   rvJrnTrUID:number,
}

export interface GetNewRvJrnTrDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReviewJrnTableset,
}
}

   /** Required : 
      @param ds
      @param rvJrnUID
   */  
export interface GetNewRvJrnTr_input{
   ds:Erp_Tablesets_ReviewJrnTableset[],
   rvJrnUID:number,
}

export interface GetNewRvJrnTr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReviewJrnTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewRvJrn_input{
   ds:Erp_Tablesets_ReviewJrnTableset[],
}

export interface GetNewRvJrn_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReviewJrnTableset,
}
}

   /** Required : 
      @param ds
      @param rvJrnUID
      @param rvJrnTrUID
   */  
export interface GetNewWError_input{
   ds:Erp_Tablesets_ReviewJrnTableset[],
   rvJrnUID:number,
   rvJrnTrUID:number,
}

export interface GetNewWError_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReviewJrnTableset,
}
}

export interface GetRefTypeList_output{
parameters : {
      /**  output parameters  */  
   strList:string,
}
}

   /** Required : 
      @param whereClauseRvJrn
      @param whereClauseRvJrnTr
      @param whereClauseRvJrnTrDtl
      @param whereClauseRvJrnTrDtlRef
      @param whereClauseRvJrnTrTreeLeaf
      @param whereClauseWError
      @param groupID
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsWithGroupCheck_input{
   whereClauseRvJrn:string,
   whereClauseRvJrnTr:string,
   whereClauseRvJrnTrDtl:string,
   whereClauseRvJrnTrDtlRef:string,
   whereClauseRvJrnTrTreeLeaf:string,
   whereClauseWError:string,
      /**  The group ID  */  
   groupID:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsWithGroupCheck_output{
   returnObj:Erp_Tablesets_ReviewJrnTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseRvJrn
      @param whereClauseRvJrnTr
      @param whereClauseRvJrnTrDtl
      @param whereClauseRvJrnTrDtlRef
      @param whereClauseRvJrnTrTreeLeaf
      @param whereClauseWError
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseRvJrn:string,
   whereClauseRvJrnTr:string,
   whereClauseRvJrnTrDtl:string,
   whereClauseRvJrnTrDtlRef:string,
   whereClauseRvJrnTrTreeLeaf:string,
   whereClauseWError:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_ReviewJrnTableset[],
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
      @param bConfirm
      @param inrvJrnUID
   */  
export interface ProcessJournal_input{
      /**  True if confirm  */  
   bConfirm:boolean,
      /**  journal number  */  
   inrvJrnUID:number,
}

export interface ProcessJournal_output{
}

   /** Required : 
      @param ipRvJrnUID
      @param ipRvJrnTrUID
      @param ipBookID
      @param ipTreeLeafUID
      @param ds
   */  
export interface RestoreTmpJournalLine_input{
      /**  RvJrnUID  */  
   ipRvJrnUID:number,
      /**  RvJrnTrUID  */  
   ipRvJrnTrUID:number,
      /**  BookID  */  
   ipBookID:string,
      /**  TreeLeafUID  */  
   ipTreeLeafUID:number,
   ds:Erp_Tablesets_ReviewJrnTableset[],
}

export interface RestoreTmpJournalLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReviewJrnTableset,
}
}

   /** Required : 
      @param rvJrnUID
   */  
export interface TransValidate_input{
      /**  journal number  */  
   rvJrnUID:number,
}

export interface TransValidate_output{
parameters : {
      /**  output parameters  */  
   isValid:boolean,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtReviewJrnTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtReviewJrnTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_ReviewJrnTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReviewJrnTableset,
}
}

