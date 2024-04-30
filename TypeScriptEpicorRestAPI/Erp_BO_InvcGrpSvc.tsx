import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.InvcGrpSvc
// Description: AR Invoice Group
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get InvcGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InvcGrps
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcGrpRow
   */  
export function get_InvcGrps(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InvcGrps
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.InvcGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InvcGrps(requestBody:Erp_Tablesets_InvcGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the InvcGrp item
   Description: Calls GetByID to retrieve the InvcGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.InvcGrpRow
   */  
export function get_InvcGrps_Company_GroupID(Company:string, GroupID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InvcGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps(" + Company + "," + GroupID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_InvcGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InvcGrp for the service
   Description: Calls UpdateExt to update InvcGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InvcGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InvcGrps_Company_GroupID(Company:string, GroupID:string, requestBody:Erp_Tablesets_InvcGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps(" + Company + "," + GroupID + ")", {
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
   Summary: Call UpdateExt to delete InvcGrp item
   Description: Call UpdateExt to delete InvcGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InvcGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InvcGrps_Company_GroupID(Company:string, GroupID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps(" + Company + "," + GroupID + ")", {
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
   Description: Get InvcGrpAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_InvcGrpAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcGrpAttchRow
   */  
export function get_InvcGrps_Company_GroupID_InvcGrpAttches(Company:string, GroupID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps(" + Company + "," + GroupID + ")/InvcGrpAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the InvcGrpAttch item
   Description: Calls GetByID to retrieve the InvcGrpAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcGrpAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.InvcGrpAttchRow
   */  
export function get_InvcGrps_Company_GroupID_InvcGrpAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InvcGrpAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrps(" + Company + "," + GroupID + ")/InvcGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_InvcGrpAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get InvcGrpAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_InvcGrpAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcGrpAttchRow
   */  
export function get_InvcGrpAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrpAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_InvcGrpAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.InvcGrpAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.InvcGrpAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InvcGrpAttches(requestBody:Erp_Tablesets_InvcGrpAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrpAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the InvcGrpAttch item
   Description: Calls GetByID to retrieve the InvcGrpAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_InvcGrpAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.InvcGrpAttchRow
   */  
export function get_InvcGrpAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_InvcGrpAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_InvcGrpAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update InvcGrpAttch for the service
   Description: Calls UpdateExt to update InvcGrpAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_InvcGrpAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.InvcGrpAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_InvcGrpAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, requestBody:Erp_Tablesets_InvcGrpAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete InvcGrpAttch item
   Description: Call UpdateExt to delete InvcGrpAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_InvcGrpAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_InvcGrpAttches_Company_GroupID_DrawingSeq(Company:string, GroupID:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/InvcGrpAttches(" + Company + "," + GroupID + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.InvcGrpListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseInvcGrp:string, whereClauseInvcGrpAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseInvcGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInvcGrp=" + whereClauseInvcGrp
   }
   if(typeof whereClauseInvcGrpAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseInvcGrpAttch=" + whereClauseInvcGrpAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method GetRowsUseLockSetting
   Description: Returns the InvcGrp dataset using the automatic group lock configuration setting.
   OperationID: GetRowsUseLockSetting
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsUseLockSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsUseLockSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsUseLockSetting(requestBody:GetRowsUseLockSetting_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsUseLockSetting_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetRowsUseLockSetting", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsUseLockSetting_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsBOEGrp
   Description: Validate if the group is used for Bill of Exchange.
   OperationID: IsBOEGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsBOEGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsBOEGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsBOEGrp(requestBody:IsBOEGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsBOEGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/IsBOEGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as IsBOEGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsLocked
   Description: Validate if the group is locked.
   OperationID: IsLocked
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsLocked(requestBody:IsLocked_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsLocked_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/IsLocked", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as IsLocked_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvcGrp
   Description: Sets the user lock on the Current group. This method also run GetByID..
   OperationID: GetInvcGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInvcGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvcGrp(requestBody:GetInvcGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInvcGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetInvcGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetInvcGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvcGrpForBOE
   Description: Sets the user lock on the Current group. This method also run GetByID.
Used for Bill of Exchange Entry
   OperationID: GetInvcGrpForBOE
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInvcGrpForBOE_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvcGrpForBOE_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvcGrpForBOE(requestBody:GetInvcGrpForBOE_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInvcGrpForBOE_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetInvcGrpForBOE", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetInvcGrpForBOE_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListForBOE
   Description: Sets the user lock on the Current group. This method also run GetByID..
   OperationID: GetListForBOE
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListForBOE_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForBOE_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForBOE(requestBody:GetListForBOE_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListForBOE_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetListForBOE", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListForBOE_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListForGUI
   Description: Get the list of groups for Taiwan GUI.
   OperationID: GetListForGUI
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListForGUI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListForGUI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListForGUI(requestBody:GetListForGUI_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListForGUI_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetListForGUI", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListForGUI_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRMACRREQGroup
   Description: This method should ONLY be called for RMA processing.  It creates a group
with a groupid of RMACRREQ.  This group cannot be updated.
   OperationID: GetRMACRREQGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRMACRREQGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRMACRREQGroup(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRMACRREQGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetRMACRREQGroup", {
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
         resolve(data as GetRMACRREQGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofApplyDate
   Description: This methods should be called to validate the new apply date entered by
the user.
   OperationID: OnChangeofApplyDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeofApplyDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofApplyDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofApplyDate(requestBody:OnChangeofApplyDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeofApplyDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/OnChangeofApplyDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeofApplyDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeofInvoiceDate
   Description: This methods should be called to validate the new invoice date entered by
the user.
   OperationID: OnChangeofInvoiceDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeofInvoiceDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeofInvoiceDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeofInvoiceDate(requestBody:OnChangeofInvoiceDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeofInvoiceDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/OnChangeofInvoiceDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeofInvoiceDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PostInvoices
   Description: Posts the invoices for a group.
   OperationID: PostInvoices
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PostInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostInvoices(requestBody:PostInvoices_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PostInvoices_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/PostInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PostInvoices_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrePostInvoices
   Description: This method should be called before Invoices for a group are posted. If the GL
is not interfaced the user will be asked to continue Y/N.  If they choose N,
the PostInvoices method should not be called.
   OperationID: PrePostInvoices
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PrePostInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrePostInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrePostInvoices(requestBody:PrePostInvoices_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PrePostInvoices_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/PrePostInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PrePostInvoices_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnlockGroup
   Description: Clears the lock of a group, only if the user of the current session is the same as the one locking the group.
This method update the database and refresh the group dataset with the information from the database.
   OperationID: UnlockGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnlockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlockGroup(requestBody:UnlockGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnlockGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/UnlockGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnlockGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LockGroup
   Description: Locks the groupID for the current user in session only if the group is not locked already
This method update the database and refresh the group dataset with the information from the database.
   OperationID: LockGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LockGroup(requestBody:LockGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LockGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/LockGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as LockGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateForBOE
   Description: Sets the user lock on the Current group. This method also run GetByID.
Used for Bill of Exchange Entry
   OperationID: UpdateForBOE
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateForBOE_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateForBOE_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateForBOE(requestBody:UpdateForBOE_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateForBOE_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/UpdateForBOE", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateForBOE_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckNewGroupIDForBOE
   Description: Verifies that group with specified group id could be an AR Bill Of Exchange Group.
   OperationID: CheckNewGroupIDForBOE
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckNewGroupIDForBOE_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckNewGroupIDForBOE_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckNewGroupIDForBOE(requestBody:CheckNewGroupIDForBOE_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckNewGroupIDForBOE_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/CheckNewGroupIDForBOE", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckNewGroupIDForBOE_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateNoLock
   Description: Update group without locking by ActiveUser
   OperationID: UpdateNoLock
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateNoLock(requestBody:UpdateNoLock_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateNoLock_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/UpdateNoLock", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateNoLock_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsNoLock
   Description: The wrapper method for GetRows. Retrieve groups ignoring Active User lock
   OperationID: GetRowsNoLock
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsNoLock(requestBody:GetRowsNoLock_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsNoLock_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetRowsNoLock", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsNoLock_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewInvcGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewInvcGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInvcGrp(requestBody:GetNewInvcGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewInvcGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetNewInvcGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewInvcGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewInvcGrpAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewInvcGrpAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewInvcGrpAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInvcGrpAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInvcGrpAttch(requestBody:GetNewInvcGrpAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewInvcGrpAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetNewInvcGrpAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewInvcGrpAttch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvcGrpSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcGrpAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcGrpListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_InvcGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_InvcGrpRow,
}

export interface Erp_Tablesets_InvcGrpAttchRow{
   "Company":string,
   "GroupID":string,
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

export interface Erp_Tablesets_InvcGrpListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   "GroupID":string,
      /**  Invoice date for all invoices within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on the InvoiceDate.  */  
   "InvoiceDate":string,
      /**  The user ID that created this batch.  */  
   "CreatedBy":string,
      /**  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  */  
   "FiscalYear":number,
      /**  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  */  
   "FiscalPeriod":number,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   "ActiveUserID":string,
      /**   Contains posting error messages. Possible messages are:
"Invoice with no detail",
 "Invalid G/L accounts"....  */  
   "PostErrorLog":string,
      /**  Field to lock the InvcGrp record while the Post Process is running.  */  
   "PostInProcess":boolean,
      /**  Indicates that the AutoPrintReady flag on all the Invoice Headers belonging to the Group will reflect automatically the value of the AutoPrintReady flag at the Group level.  */  
   "UpdateInvAutoPrint":boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Indicates if when Auto-Printing all Invoices in a Group, only the ones that have the EDIReady flag as true will be printed, or all of them. This flag is intended to Auto-Print the AR Invoice Form as an Outbound EDI Report.  */  
   "AutoPrintEDIOnly":boolean,
      /**  Apply date for all invoices within this batch.  Apply date is the date in which invoices will be applied to the gl books when posted.  */  
   "ApplyDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BOE Post  */  
   "BOEPost":string,
      /**  Is BOE  */  
   "IsBOE":boolean,
      /**  Flag to allow the user to post based on security.  */  
   "UserCanPostGroupFlag":boolean,
      /**  Flag to indicate whether the use can create a deposit.  */  
   "UserCanDeposit":boolean,
      /**  Total amount for invoices in this group.  */  
   "TotalInvAmt":number,
      /**  Indicates whether this dataset's row comes from Bill Of Exchange or not.  */  
   "FromBOE":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_InvcGrpRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   "GroupID":string,
      /**  Invoice date for all invoices within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on the InvoiceDate.  */  
   "InvoiceDate":string,
      /**  The user ID that created this batch.  */  
   "CreatedBy":string,
      /**  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  */  
   "FiscalYear":number,
      /**  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  */  
   "FiscalPeriod":number,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   "ActiveUserID":string,
      /**   Contains posting error messages. Possible messages are:
"Invoice with no detail",
 "Invalid G/L accounts"....  */  
   "PostErrorLog":string,
      /**  Field to lock the InvcGrp record while the Post Process is running.  */  
   "PostInProcess":boolean,
      /**  Indicates that the AutoPrintReady flag on all the Invoice Headers belonging to the Group will reflect automatically the value of the AutoPrintReady flag at the Group level.  */  
   "UpdateInvAutoPrint":boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   "AutoPrintReady":boolean,
      /**  Indicates if when Auto-Printing all Invoices in a Group, only the ones that have the EDIReady flag as true will be printed, or all of them. This flag is intended to Auto-Print the AR Invoice Form as an Outbound EDI Report.  */  
   "AutoPrintEDIOnly":boolean,
      /**  Apply date for all invoices within this batch.  Apply date is the date in which invoices will be applied to the gl books when posted.  */  
   "ApplyDate":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BOE Post  */  
   "BOEPost":string,
      /**  Is BOE  */  
   "IsBOE":boolean,
      /**  Cash Group ID  */  
   "CashGroupID":string,
      /**  PECollectionMode  */  
   "PECollectionMode":number,
      /**  PECollectionCustNum  */  
   "PECollectionCustNum":number,
      /**  Indicates whether this dataset's row comes from Bill Of Exchange or not.  */  
   "FromBOE":boolean,
      /**  is invcGrp locked in RvLock table.  */  
   "IsDocumentLocked":boolean,
      /**  locked means can not be posted. an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  Total amount for invoices in this group.  */  
   "TotalInvAmt":number,
      /**  Flag to indicate whether the use can create a deposit.  */  
   "UserCanDeposit":boolean,
      /**  Flag to allow the user to post based on security.  */  
   "UserCanPostGroupFlag":boolean,
      /**   Indicates if the check of invoices customers being in Collections needs to be done before the Post
(Used for Peru localization)  */  
   "ChkCollections":boolean,
   "RvJrnUID":number,
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
      @param GroupID
   */  
export interface CheckNewGroupIDForBOE_input{
   GroupID:string,
}

export interface CheckNewGroupIDForBOE_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   Message:string,
}
}

   /** Required : 
      @param groupID
   */  
export interface DeleteByID_input{
   groupID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_InvcGrpAttchRow{
   Company:string,
   GroupID:string,
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

export interface Erp_Tablesets_InvcGrpListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  Invoice date for all invoices within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on the InvoiceDate.  */  
   InvoiceDate:string,
      /**  The user ID that created this batch.  */  
   CreatedBy:string,
      /**  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  */  
   FiscalYear:number,
      /**  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  */  
   FiscalPeriod:number,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   ActiveUserID:string,
      /**   Contains posting error messages. Possible messages are:
"Invoice with no detail",
 "Invalid G/L accounts"....  */  
   PostErrorLog:string,
      /**  Field to lock the InvcGrp record while the Post Process is running.  */  
   PostInProcess:boolean,
      /**  Indicates that the AutoPrintReady flag on all the Invoice Headers belonging to the Group will reflect automatically the value of the AutoPrintReady flag at the Group level.  */  
   UpdateInvAutoPrint:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Indicates if when Auto-Printing all Invoices in a Group, only the ones that have the EDIReady flag as true will be printed, or all of them. This flag is intended to Auto-Print the AR Invoice Form as an Outbound EDI Report.  */  
   AutoPrintEDIOnly:boolean,
      /**  Apply date for all invoices within this batch.  Apply date is the date in which invoices will be applied to the gl books when posted.  */  
   ApplyDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BOE Post  */  
   BOEPost:string,
      /**  Is BOE  */  
   IsBOE:boolean,
      /**  Flag to allow the user to post based on security.  */  
   UserCanPostGroupFlag:boolean,
      /**  Flag to indicate whether the use can create a deposit.  */  
   UserCanDeposit:boolean,
      /**  Total amount for invoices in this group.  */  
   TotalInvAmt:number,
      /**  Indicates whether this dataset's row comes from Bill Of Exchange or not.  */  
   FromBOE:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcGrpListTableset{
   InvcGrpList:Erp_Tablesets_InvcGrpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InvcGrpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  Invoice date for all invoices within this batch. This date must be found in the Fiscal file. The Fiscal file provides the Fiscal Year and Period, which is defaulted based on the InvoiceDate.  */  
   InvoiceDate:string,
      /**  The user ID that created this batch.  */  
   CreatedBy:string,
      /**  Fiscal Year. This is defaulted based on the finding the Fiscal master for the corresponding InvoiceDate.  User can override this. This value is used as one of the defaults to the InvHead records. (see InvHead for usage).  */  
   FiscalYear:number,
      /**  A Fiscal period which provides one of the defaults to be used when creating invoices within this group. This field is defaulted based on finding the Fiscal master which contains the corresponding  InvoiceDate period. (See InvcHead.FiscalPeriod for usage)  */  
   FiscalPeriod:number,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   ActiveUserID:string,
      /**   Contains posting error messages. Possible messages are:
"Invoice with no detail",
 "Invalid G/L accounts"....  */  
   PostErrorLog:string,
      /**  Field to lock the InvcGrp record while the Post Process is running.  */  
   PostInProcess:boolean,
      /**  Indicates that the AutoPrintReady flag on all the Invoice Headers belonging to the Group will reflect automatically the value of the AutoPrintReady flag at the Group level.  */  
   UpdateInvAutoPrint:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Indicates if when Auto-Printing all Invoices in a Group, only the ones that have the EDIReady flag as true will be printed, or all of them. This flag is intended to Auto-Print the AR Invoice Form as an Outbound EDI Report.  */  
   AutoPrintEDIOnly:boolean,
      /**  Apply date for all invoices within this batch.  Apply date is the date in which invoices will be applied to the gl books when posted.  */  
   ApplyDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BOE Post  */  
   BOEPost:string,
      /**  Is BOE  */  
   IsBOE:boolean,
      /**  Cash Group ID  */  
   CashGroupID:string,
      /**  PECollectionMode  */  
   PECollectionMode:number,
      /**  PECollectionCustNum  */  
   PECollectionCustNum:number,
      /**  Indicates whether this dataset's row comes from Bill Of Exchange or not.  */  
   FromBOE:boolean,
      /**  is invcGrp locked in RvLock table.  */  
   IsDocumentLocked:boolean,
      /**  locked means can not be posted. an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  Total amount for invoices in this group.  */  
   TotalInvAmt:number,
      /**  Flag to indicate whether the use can create a deposit.  */  
   UserCanDeposit:boolean,
      /**  Flag to allow the user to post based on security.  */  
   UserCanPostGroupFlag:boolean,
      /**   Indicates if the check of invoices customers being in Collections needs to be done before the Post
(Used for Peru localization)  */  
   ChkCollections:boolean,
   RvJrnUID:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcGrpTableset{
   InvcGrp:Erp_Tablesets_InvcGrpRow[],
   InvcGrpAttch:Erp_Tablesets_InvcGrpAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtInvcGrpTableset{
   InvcGrp:Erp_Tablesets_InvcGrpRow[],
   InvcGrpAttch:Erp_Tablesets_InvcGrpAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param groupID
   */  
export interface GetByID_input{
   groupID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_InvcGrpTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_InvcGrpTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_InvcGrpTableset[],
}

   /** Required : 
      @param inGroupID
      @param ds
   */  
export interface GetInvcGrpForBOE_input{
      /**  Group ID.  */  
   inGroupID:string,
   ds:Erp_Tablesets_InvcGrpTableset[],
}

export interface GetInvcGrpForBOE_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvcGrpTableset,
}
}

   /** Required : 
      @param groupID
      @param ds
   */  
export interface GetInvcGrp_input{
      /**  Group ID.  */  
   groupID:string,
   ds:Erp_Tablesets_InvcGrpTableset[],
}

export interface GetInvcGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvcGrpTableset,
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetListForBOE_input{
      /**  whereClause  */  
   whereClause:string,
      /**  pageSize  */  
   pageSize:number,
      /**  absolutePage  */  
   absolutePage:number,
}

export interface GetListForBOE_output{
   returnObj:Erp_Tablesets_InvcGrpListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClause
      @param tranDocTypeID
      @param startDate
      @param endDate
      @param pageSize
      @param absolutePage
   */  
export interface GetListForGUI_input{
      /**  whereClause  */  
   whereClause:string,
      /**  tranDocTypeID  */  
   tranDocTypeID:string,
      /**  startDate  */  
   startDate:string,
      /**  endDate  */  
   endDate:string,
      /**  pageSize  */  
   pageSize:number,
      /**  absolutePage  */  
   absolutePage:number,
}

export interface GetListForGUI_output{
   returnObj:Erp_Tablesets_InvcGrpListTableset[],
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
   returnObj:Erp_Tablesets_InvcGrpListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param groupID
   */  
export interface GetNewInvcGrpAttch_input{
   ds:Erp_Tablesets_InvcGrpTableset[],
   groupID:string,
}

export interface GetNewInvcGrpAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvcGrpTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewInvcGrp_input{
   ds:Erp_Tablesets_InvcGrpTableset[],
}

export interface GetNewInvcGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvcGrpTableset,
}
}

export interface GetRMACRREQGroup_output{
   returnObj:Erp_Tablesets_InvcGrpTableset[],
}

   /** Required : 
      @param whereClauseInvcGrp
      @param whereClauseInvcGrpAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsNoLock_input{
   whereClauseInvcGrp:string,
   whereClauseInvcGrpAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsNoLock_output{
   returnObj:Erp_Tablesets_InvcGrpTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseInvcGrp
      @param whereClauseInvcGrpAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsUseLockSetting_input{
      /**  InvcGrp where clause  */  
   whereClauseInvcGrp:string,
      /**  Attachment where clause  */  
   whereClauseInvcGrpAttch:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetRowsUseLockSetting_output{
   returnObj:Erp_Tablesets_InvcGrpTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseInvcGrp
      @param whereClauseInvcGrpAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseInvcGrp:string,
   whereClauseInvcGrpAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_InvcGrpTableset[],
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
      @param groupID
   */  
export interface IsBOEGrp_input{
      /**  Group ID.  */  
   groupID:string,
}

export interface IsBOEGrp_output{
   returnObj:boolean,
}

   /** Required : 
      @param groupID
   */  
export interface IsLocked_input{
      /**  Group ID to check if is locked.  */  
   groupID:string,
}

export interface IsLocked_output{
      /**  True if group is locked, otherwise false.  */  
   returnObj:boolean,
}

   /** Required : 
      @param groupID
      @param ds
   */  
export interface LockGroup_input{
      /**  Group ID to lock  */  
   groupID:string,
   ds:Erp_Tablesets_InvcGrpTableset[],
}

export interface LockGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvcGrpTableset,
}
}

   /** Required : 
      @param groupID
      @param newApplyDate
      @param ds
   */  
export interface OnChangeofApplyDate_input{
      /**  Group ID.  */  
   groupID:string,
      /**  New Apply Date.  */  
   newApplyDate:string,
   ds:Erp_Tablesets_InvcGrpTableset[],
}

export interface OnChangeofApplyDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvcGrpTableset,
}
}

   /** Required : 
      @param groupID
      @param newInvoiceDate
      @param ds
   */  
export interface OnChangeofInvoiceDate_input{
      /**  Group ID.  */  
   groupID:string,
      /**  New invoice date.  */  
   newInvoiceDate:string,
   ds:Erp_Tablesets_InvcGrpTableset[],
}

export interface OnChangeofInvoiceDate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvcGrpTableset,
}
}

   /** Required : 
      @param groupID
   */  
export interface PostInvoices_input{
      /**  Group ID.  */  
   groupID:string,
}

export interface PostInvoices_output{
parameters : {
      /**  output parameters  */  
   invoicesGenerated:string,
   errorMessage:string,
   legalNumberMessage:string,
}
}

   /** Required : 
      @param ipTCOnline
      @param ds
   */  
export interface PrePostInvoices_input{
      /**  Tax Connect status.  */  
   ipTCOnline:boolean,
   ds:Erp_Tablesets_InvcGrpTableset[],
}

export interface PrePostInvoices_output{
parameters : {
      /**  output parameters  */  
   gLMessage:string,
   gLWarning:string,
   collectionsWarning:string,
   currencyWarning:string,
   needsUserInput:boolean,
   ds:Erp_Tablesets_InvcGrpTableset,
}
}

   /** Required : 
      @param priorGroupID
      @param ds
   */  
export interface UnlockGroup_input{
      /**  Prior Group ID.  */  
   priorGroupID:string,
   ds:Erp_Tablesets_InvcGrpTableset[],
}

export interface UnlockGroup_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvcGrpTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtInvcGrpTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtInvcGrpTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateForBOE_input{
   ds:Erp_Tablesets_InvcGrpTableset[],
}

export interface UpdateForBOE_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvcGrpTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateNoLock_input{
   ds:Erp_Tablesets_InvcGrpTableset[],
}

export interface UpdateNoLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvcGrpTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_InvcGrpTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvcGrpTableset,
}
}

