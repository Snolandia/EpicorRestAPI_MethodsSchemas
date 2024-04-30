import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.AssetImpairSvc
// Description: Fixed Asset Impairment
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get AssetImpairs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AssetImpairs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAImpairmentRow
   */  
export function get_AssetImpairs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AssetImpairs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAImpairmentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.FAImpairmentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssetImpairs(requestBody:Erp_Tablesets_FAImpairmentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the AssetImpair item
   Description: Calls GetByID to retrieve the AssetImpair item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AssetImpair
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param ImpairNum Desc: ImpairNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FAImpairmentRow
   */  
export function get_AssetImpairs_Company_AssetNum_ImpairNum(Company:string, AssetNum:string, ImpairNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAImpairmentRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs(" + Company + "," + AssetNum + "," + ImpairNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_FAImpairmentRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AssetImpair for the service
   Description: Calls UpdateExt to update AssetImpair. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AssetImpair
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param ImpairNum Desc: ImpairNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAImpairmentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AssetImpairs_Company_AssetNum_ImpairNum(Company:string, AssetNum:string, ImpairNum:string, requestBody:Erp_Tablesets_FAImpairmentRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs(" + Company + "," + AssetNum + "," + ImpairNum + ")", {
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
   Summary: Call UpdateExt to delete AssetImpair item
   Description: Call UpdateExt to delete AssetImpair item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AssetImpair
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param ImpairNum Desc: ImpairNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AssetImpairs_Company_AssetNum_ImpairNum(Company:string, AssetNum:string, ImpairNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs(" + Company + "," + AssetNum + "," + ImpairNum + ")", {
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
   Description: Get FAImpairmentAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FAImpairmentAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param ImpairNum Desc: ImpairNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAImpairmentAttchRow
   */  
export function get_AssetImpairs_Company_AssetNum_ImpairNum_FAImpairmentAttches(Company:string, AssetNum:string, ImpairNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs(" + Company + "," + AssetNum + "," + ImpairNum + ")/FAImpairmentAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FAImpairmentAttch item
   Description: Calls GetByID to retrieve the FAImpairmentAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAImpairmentAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param ImpairNum Desc: ImpairNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FAImpairmentAttchRow
   */  
export function get_AssetImpairs_Company_AssetNum_ImpairNum_FAImpairmentAttches_Company_AssetNum_ImpairNum_DrawingSeq(Company:string, AssetNum:string, ImpairNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAImpairmentAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/AssetImpairs(" + Company + "," + AssetNum + "," + ImpairNum + ")/FAImpairmentAttches(" + Company + "," + AssetNum + "," + ImpairNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_FAImpairmentAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FAImpairmentAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAImpairmentAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAImpairmentAttchRow
   */  
export function get_FAImpairmentAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/FAImpairmentAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAImpairmentAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAImpairmentAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.FAImpairmentAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FAImpairmentAttches(requestBody:Erp_Tablesets_FAImpairmentAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/FAImpairmentAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the FAImpairmentAttch item
   Description: Calls GetByID to retrieve the FAImpairmentAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAImpairmentAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param ImpairNum Desc: ImpairNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FAImpairmentAttchRow
   */  
export function get_FAImpairmentAttches_Company_AssetNum_ImpairNum_DrawingSeq(Company:string, AssetNum:string, ImpairNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAImpairmentAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/FAImpairmentAttches(" + Company + "," + AssetNum + "," + ImpairNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_FAImpairmentAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FAImpairmentAttch for the service
   Description: Calls UpdateExt to update FAImpairmentAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAImpairmentAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param ImpairNum Desc: ImpairNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAImpairmentAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FAImpairmentAttches_Company_AssetNum_ImpairNum_DrawingSeq(Company:string, AssetNum:string, ImpairNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_FAImpairmentAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/FAImpairmentAttches(" + Company + "," + AssetNum + "," + ImpairNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete FAImpairmentAttch item
   Description: Call UpdateExt to delete FAImpairmentAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAImpairmentAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param ImpairNum Desc: ImpairNum   Required: True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FAImpairmentAttches_Company_AssetNum_ImpairNum_DrawingSeq(Company:string, AssetNum:string, ImpairNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/FAImpairmentAttches(" + Company + "," + AssetNum + "," + ImpairNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAImpairmentListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentListRow)
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
export function get_GetRows(whereClauseFAImpairment:string, whereClauseFAImpairmentAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFAImpairment!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFAImpairment=" + whereClauseFAImpairment
   }
   if(typeof whereClauseFAImpairmentAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFAImpairmentAttch=" + whereClauseFAImpairmentAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(assetNum:string, impairNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof assetNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "assetNum=" + assetNum
   }
   if(typeof impairNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "impairNum=" + impairNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method CheckAssetTransactions
   Description: Checks if there are any transactions for this Asset marked as Ready To Post
   OperationID: CheckAssetTransactions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckAssetTransactions_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAssetTransactions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAssetTransactions(requestBody:CheckAssetTransactions_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckAssetTransactions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/CheckAssetTransactions", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckAssetTransactions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearReadyToPost
   Description: Clears Ready To Post flag on Asset transactions with SysRowID different from the one provided
   OperationID: ClearReadyToPost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ClearReadyToPost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearReadyToPost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearReadyToPost(requestBody:ClearReadyToPost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ClearReadyToPost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/ClearReadyToPost", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ClearReadyToPost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeImpairmentCost
   Description: Method to call when changing the impairment cost.
   OperationID: ChangeImpairmentCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeImpairmentCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeImpairmentCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeImpairmentCost(requestBody:ChangeImpairmentCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeImpairmentCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/ChangeImpairmentCost", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeImpairmentCost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckAssetDepRecalcNeeded
   Description: Check if the asset or any of its registers requires depreciation calculation
   OperationID: CheckAssetDepRecalcNeeded
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckAssetDepRecalcNeeded_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAssetDepRecalcNeeded_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAssetDepRecalcNeeded(requestBody:CheckAssetDepRecalcNeeded_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckAssetDepRecalcNeeded_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/CheckAssetDepRecalcNeeded", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckAssetDepRecalcNeeded_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFAImpairment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAImpairment
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFAImpairment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAImpairment_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFAImpairment(requestBody:GetNewFAImpairment_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFAImpairment_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/GetNewFAImpairment", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewFAImpairment_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFAImpairmentAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAImpairmentAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFAImpairmentAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAImpairmentAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFAImpairmentAttch(requestBody:GetNewFAImpairmentAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFAImpairmentAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/GetNewFAImpairmentAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewFAImpairmentAttch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.AssetImpairSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAImpairmentAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAImpairmentListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAImpairmentRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAImpairmentRow,
}

export interface Erp_Tablesets_FAImpairmentAttchRow{
   "Company":string,
   "AssetNum":string,
   "ImpairNum":number,
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

export interface Erp_Tablesets_FAImpairmentListRow{
      /**  Company of the Addition.  */  
   "Company":string,
      /**  Asset number of the Addition.  */  
   "AssetNum":string,
      /**  Unique number to identify the Impairment of an asset.  */  
   "ImpairNum":number,
      /**  Description of the Impairment.  */  
   "Description":string,
      /**  The Impairment Date that will be used to get the exchange rate.  */  
   "ApplyDate":string,
      /**  Flag to indicat that the impairment is allowed to be posted to the GL.  */  
   "ReadyToPost":boolean,
      /**  Flag to indicate that the impairment is posted to the GL. After posting modification of the impairment is not allowed.  */  
   "Posted":boolean,
      /**  Posting date of the impairment to the GL.  */  
   "PostDate":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier of the currency rate group.  */  
   "RateGrpCode":string,
      /**  The impairment cost recorded against the asset.  */  
   "ImpairmentCost":number,
      /**  The impairment cost recorded against the asset in the currency specified.  */  
   "DocImpairmentCost":number,
      /**  Reporting currency value of the Impairment Cost.  */  
   "Rpt1ImpairmentCost":number,
      /**  Reporting currency value of the Impairment Cost.  */  
   "Rpt2ImpairmentCost":number,
      /**  Reporting currency value of the Impairment Cost.  */  
   "Rpt3ImpairmentCost":number,
      /**  The addition is posted by the user.  */  
   "PostedBy":string,
      /**  The fiscal year of posting of the addition to the GL.  */  
   "FiscalYear":number,
      /**  The fiscal period of posting of the addition to the GL.  */  
   "FiscalPeriod":number,
      /**  Fiscal year suffix  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The GL journal to which the impairment is posted.  */  
   "JournalCode":string,
      /**  The GL journal number to which the impairment is posted.  */  
   "JournalNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "RvJrnUID":number,
      /**  Shows if this impairment transaction is blocked in RvLock.  */  
   "IsLocked":boolean,
      /**  Locked means the entry can not be updated or deleted: the impairment is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "BaseCurrCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "BaseCurrCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "BaseCurrDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "BaseCurrCurrName":string,
      /**  Description of the currency  */  
   "BaseCurrCurrDesc":string,
      /**  Description of the currency  */  
   "CurrencyCurrDesc":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "CurrencyDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrencyCurrName":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrencyCurrSymbol":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyCurrencyID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FAImpairmentRow{
      /**  Company of the Addition.  */  
   "Company":string,
      /**  Asset number of the Addition.  */  
   "AssetNum":string,
      /**  Unique number to identify the Impairment of an asset.  */  
   "ImpairNum":number,
      /**  Description of the Impairment.  */  
   "Description":string,
      /**  The Impairment Date that will be used to get the exchange rate.  */  
   "ApplyDate":string,
      /**  Flag to indicat that the impairment is allowed to be posted to the GL.  */  
   "ReadyToPost":boolean,
      /**  Flag to indicate that the impairment is posted to the GL. After posting modification of the impairment is not allowed.  */  
   "Posted":boolean,
      /**  Posting date of the impairment to the GL.  */  
   "PostDate":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier of the currency rate group.  */  
   "RateGrpCode":string,
      /**  The impairment cost recorded against the asset.  */  
   "ImpairmentCost":number,
      /**  The impairment cost recorded against the asset in the currency specified.  */  
   "DocImpairmentCost":number,
      /**  Reporting currency value of the Impairment Cost.  */  
   "Rpt1ImpairmentCost":number,
      /**  Reporting currency value of the Impairment Cost.  */  
   "Rpt2ImpairmentCost":number,
      /**  Reporting currency value of the Impairment Cost.  */  
   "Rpt3ImpairmentCost":number,
      /**  The addition is posted by the user.  */  
   "PostedBy":string,
      /**  The fiscal year of posting of the addition to the GL.  */  
   "FiscalYear":number,
      /**  The fiscal period of posting of the addition to the GL.  */  
   "FiscalPeriod":number,
      /**  Fiscal year suffix  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The GL journal to which the impairment is posted.  */  
   "JournalCode":string,
      /**  The GL journal number to which the impairment is posted.  */  
   "JournalNum":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates that the transaction is reflected in FAsset costs.  */  
   "HdrCostRecorded":boolean,
      /**  List of Asset Registers in which the transaction is reflected.  */  
   "RecordedRegList":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
   "RvJrnUID":number,
      /**  Shows if this impairment transaction is blocked in RvLock.  */  
   "IsLocked":boolean,
      /**  Locked means the entry can not be updated or deleted: the impairment is already in review journal or in posting process.  */  
   "LockStatus":string,
   "BitFlag":number,
   "BaseCurrCurrDesc":string,
   "BaseCurrCurrencyID":string,
   "BaseCurrCurrName":string,
   "BaseCurrCurrSymbol":string,
   "BaseCurrDocumentDesc":string,
   "CurrencyCurrDesc":string,
   "CurrencyCurrSymbol":string,
   "CurrencyCurrencyID":string,
   "CurrencyCurrName":string,
   "CurrencyDocumentDesc":string,
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
      @param ProposedImpairCost
      @param BaseOrDoc
      @param ds
   */  
export interface ChangeImpairmentCost_input{
      /**  The proposed impairment cost  */  
   ProposedImpairCost:number,
      /**  The field type - base or doc  */  
   BaseOrDoc:string,
   ds:Erp_Tablesets_AssetImpairTableset[],
}

export interface ChangeImpairmentCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetImpairTableset,
}
}

   /** Required : 
      @param assetNum
   */  
export interface CheckAssetDepRecalcNeeded_input{
      /**  Asset ID  */  
   assetNum:string,
}

export interface CheckAssetDepRecalcNeeded_output{
      /**  true if depreciation calculation is required  */  
   returnObj:boolean,
}

   /** Required : 
      @param assetNum
      @param sysRowID
   */  
export interface CheckAssetTransactions_input{
      /**  Asset ID  */  
   assetNum:string,
      /**  SysRowID to be excluded from search  */  
   sysRowID:string,
}

export interface CheckAssetTransactions_output{
      /**  If transaction found: Warning message offering to clear Ready To Post flag; otherwise: an empty string  */  
   returnObj:string,
}

   /** Required : 
      @param assetNum
      @param sysRowID
   */  
export interface ClearReadyToPost_input{
      /**  Asset ID  */  
   assetNum:string,
      /**  SysRowID to be excluded from search  */  
   sysRowID:string,
}

export interface ClearReadyToPost_output{
}

   /** Required : 
      @param assetNum
      @param impairNum
   */  
export interface DeleteByID_input{
   assetNum:string,
   impairNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_AssetImpairTableset{
   FAImpairment:Erp_Tablesets_FAImpairmentRow[],
   FAImpairmentAttch:Erp_Tablesets_FAImpairmentAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FAImpairmentAttchRow{
   Company:string,
   AssetNum:string,
   ImpairNum:number,
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

export interface Erp_Tablesets_FAImpairmentListRow{
      /**  Company of the Addition.  */  
   Company:string,
      /**  Asset number of the Addition.  */  
   AssetNum:string,
      /**  Unique number to identify the Impairment of an asset.  */  
   ImpairNum:number,
      /**  Description of the Impairment.  */  
   Description:string,
      /**  The Impairment Date that will be used to get the exchange rate.  */  
   ApplyDate:string,
      /**  Flag to indicat that the impairment is allowed to be posted to the GL.  */  
   ReadyToPost:boolean,
      /**  Flag to indicate that the impairment is posted to the GL. After posting modification of the impairment is not allowed.  */  
   Posted:boolean,
      /**  Posting date of the impairment to the GL.  */  
   PostDate:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier of the currency rate group.  */  
   RateGrpCode:string,
      /**  The impairment cost recorded against the asset.  */  
   ImpairmentCost:number,
      /**  The impairment cost recorded against the asset in the currency specified.  */  
   DocImpairmentCost:number,
      /**  Reporting currency value of the Impairment Cost.  */  
   Rpt1ImpairmentCost:number,
      /**  Reporting currency value of the Impairment Cost.  */  
   Rpt2ImpairmentCost:number,
      /**  Reporting currency value of the Impairment Cost.  */  
   Rpt3ImpairmentCost:number,
      /**  The addition is posted by the user.  */  
   PostedBy:string,
      /**  The fiscal year of posting of the addition to the GL.  */  
   FiscalYear:number,
      /**  The fiscal period of posting of the addition to the GL.  */  
   FiscalPeriod:number,
      /**  Fiscal year suffix  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The GL journal to which the impairment is posted.  */  
   JournalCode:string,
      /**  The GL journal number to which the impairment is posted.  */  
   JournalNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   RvJrnUID:number,
      /**  Shows if this impairment transaction is blocked in RvLock.  */  
   IsLocked:boolean,
      /**  Locked means the entry can not be updated or deleted: the impairment is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   BaseCurrCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   BaseCurrCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   BaseCurrDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   BaseCurrCurrName:string,
      /**  Description of the currency  */  
   BaseCurrCurrDesc:string,
      /**  Description of the currency  */  
   CurrencyCurrDesc:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   CurrencyDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrencyCurrName:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrencyCurrSymbol:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyCurrencyID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FAImpairmentListTableset{
   FAImpairmentList:Erp_Tablesets_FAImpairmentListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FAImpairmentRow{
      /**  Company of the Addition.  */  
   Company:string,
      /**  Asset number of the Addition.  */  
   AssetNum:string,
      /**  Unique number to identify the Impairment of an asset.  */  
   ImpairNum:number,
      /**  Description of the Impairment.  */  
   Description:string,
      /**  The Impairment Date that will be used to get the exchange rate.  */  
   ApplyDate:string,
      /**  Flag to indicat that the impairment is allowed to be posted to the GL.  */  
   ReadyToPost:boolean,
      /**  Flag to indicate that the impairment is posted to the GL. After posting modification of the impairment is not allowed.  */  
   Posted:boolean,
      /**  Posting date of the impairment to the GL.  */  
   PostDate:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier of the currency rate group.  */  
   RateGrpCode:string,
      /**  The impairment cost recorded against the asset.  */  
   ImpairmentCost:number,
      /**  The impairment cost recorded against the asset in the currency specified.  */  
   DocImpairmentCost:number,
      /**  Reporting currency value of the Impairment Cost.  */  
   Rpt1ImpairmentCost:number,
      /**  Reporting currency value of the Impairment Cost.  */  
   Rpt2ImpairmentCost:number,
      /**  Reporting currency value of the Impairment Cost.  */  
   Rpt3ImpairmentCost:number,
      /**  The addition is posted by the user.  */  
   PostedBy:string,
      /**  The fiscal year of posting of the addition to the GL.  */  
   FiscalYear:number,
      /**  The fiscal period of posting of the addition to the GL.  */  
   FiscalPeriod:number,
      /**  Fiscal year suffix  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The GL journal to which the impairment is posted.  */  
   JournalCode:string,
      /**  The GL journal number to which the impairment is posted.  */  
   JournalNum:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates that the transaction is reflected in FAsset costs.  */  
   HdrCostRecorded:boolean,
      /**  List of Asset Registers in which the transaction is reflected.  */  
   RecordedRegList:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
   RvJrnUID:number,
      /**  Shows if this impairment transaction is blocked in RvLock.  */  
   IsLocked:boolean,
      /**  Locked means the entry can not be updated or deleted: the impairment is already in review journal or in posting process.  */  
   LockStatus:string,
   BitFlag:number,
   BaseCurrCurrDesc:string,
   BaseCurrCurrencyID:string,
   BaseCurrCurrName:string,
   BaseCurrCurrSymbol:string,
   BaseCurrDocumentDesc:string,
   CurrencyCurrDesc:string,
   CurrencyCurrSymbol:string,
   CurrencyCurrencyID:string,
   CurrencyCurrName:string,
   CurrencyDocumentDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtAssetImpairTableset{
   FAImpairment:Erp_Tablesets_FAImpairmentRow[],
   FAImpairmentAttch:Erp_Tablesets_FAImpairmentAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param assetNum
      @param impairNum
   */  
export interface GetByID_input{
   assetNum:string,
   impairNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_AssetImpairTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_AssetImpairTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_AssetImpairTableset[],
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
   returnObj:Erp_Tablesets_FAImpairmentListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param assetNum
      @param impairNum
   */  
export interface GetNewFAImpairmentAttch_input{
   ds:Erp_Tablesets_AssetImpairTableset[],
   assetNum:string,
   impairNum:number,
}

export interface GetNewFAImpairmentAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetImpairTableset,
}
}

   /** Required : 
      @param ds
      @param assetNum
   */  
export interface GetNewFAImpairment_input{
   ds:Erp_Tablesets_AssetImpairTableset[],
   assetNum:string,
}

export interface GetNewFAImpairment_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetImpairTableset,
}
}

   /** Required : 
      @param whereClauseFAImpairment
      @param whereClauseFAImpairmentAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFAImpairment:string,
   whereClauseFAImpairmentAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_AssetImpairTableset[],
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
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtAssetImpairTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtAssetImpairTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_AssetImpairTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AssetImpairTableset,
}
}

