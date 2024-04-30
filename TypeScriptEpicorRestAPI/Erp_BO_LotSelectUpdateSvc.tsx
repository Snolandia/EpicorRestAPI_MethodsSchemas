import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.LotSelectUpdateSvc
// Description: Generic Lot Number Selection and Update Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get LotSelectUpdates items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LotSelectUpdates
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartLotRow
   */  
export function get_LotSelectUpdates(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LotSelectUpdates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartLotRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartLotRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LotSelectUpdates(requestBody:Erp_Tablesets_PartLotRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LotSelectUpdate item
   Description: Calls GetByID to retrieve the LotSelectUpdate item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LotSelectUpdate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartLotRow
   */  
export function get_LotSelectUpdates_Company_PartNum_LotNum(Company:string, PartNum:string, LotNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartLotRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates(" + Company + "," + PartNum + "," + LotNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PartLotRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LotSelectUpdate for the service
   Description: Calls UpdateExt to update LotSelectUpdate. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LotSelectUpdate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartLotRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LotSelectUpdates_Company_PartNum_LotNum(Company:string, PartNum:string, LotNum:string, requestBody:Erp_Tablesets_PartLotRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates(" + Company + "," + PartNum + "," + LotNum + ")", {
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
   Summary: Call UpdateExt to delete LotSelectUpdate item
   Description: Call UpdateExt to delete LotSelectUpdate item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LotSelectUpdate
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LotSelectUpdates_Company_PartNum_LotNum(Company:string, PartNum:string, LotNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates(" + Company + "," + PartNum + "," + LotNum + ")", {
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
   Description: Get PartLotAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartLotAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartLotAttchRow
   */  
export function get_LotSelectUpdates_Company_PartNum_LotNum_PartLotAttches(Company:string, PartNum:string, LotNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates(" + Company + "," + PartNum + "," + LotNum + ")/PartLotAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PartLotAttch item
   Description: Calls GetByID to retrieve the PartLotAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartLotAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartLotAttchRow
   */  
export function get_LotSelectUpdates_Company_PartNum_LotNum_PartLotAttches_Company_PartNum_LotNum_DrawingSeq(Company:string, PartNum:string, LotNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartLotAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/LotSelectUpdates(" + Company + "," + PartNum + "," + LotNum + ")/PartLotAttches(" + Company + "," + PartNum + "," + LotNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PartLotAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PartLotAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartLotAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartLotAttchRow
   */  
export function get_PartLotAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/PartLotAttches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartLotAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartLotAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartLotAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartLotAttches(requestBody:Erp_Tablesets_PartLotAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/PartLotAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PartLotAttch item
   Description: Calls GetByID to retrieve the PartLotAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartLotAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartLotAttchRow
   */  
export function get_PartLotAttches_Company_PartNum_LotNum_DrawingSeq(Company:string, PartNum:string, LotNum:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartLotAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/PartLotAttches(" + Company + "," + PartNum + "," + LotNum + "," + DrawingSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_PartLotAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartLotAttch for the service
   Description: Calls UpdateExt to update PartLotAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartLotAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartLotAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartLotAttches_Company_PartNum_LotNum_DrawingSeq(Company:string, PartNum:string, LotNum:string, DrawingSeq:string, requestBody:Erp_Tablesets_PartLotAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/PartLotAttches(" + Company + "," + PartNum + "," + LotNum + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PartLotAttch item
   Description: Call UpdateExt to delete PartLotAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartLotAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartLotAttches_Company_PartNum_LotNum_DrawingSeq(Company:string, PartNum:string, LotNum:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/PartLotAttches(" + Company + "," + PartNum + "," + LotNum + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartLotListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotListRow)
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
export function get_GetRows(whereClausePartLot:string, whereClausePartLotAttch:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartLot!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartLot=" + whereClausePartLot
   }
   if(typeof whereClausePartLotAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartLotAttch=" + whereClausePartLotAttch
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(partNum:string, lotNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof partNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "partNum=" + partNum
   }
   if(typeof lotNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "lotNum=" + lotNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method CheckDupLotNum
   Description: This method checks the Lot Number to see if there is any duplicate lot number used
by another part number.  A warning message will be returned to the user asking
if the user wants to continue creating a duplicate lot number.  This needs to be run
before Update method.  If the user answers yes to the question then the update method can be run.
   OperationID: CheckDupLotNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDupLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDupLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDupLotNum(requestBody:CheckDupLotNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDupLotNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/CheckDupLotNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckDupLotNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChkForNeedsLotAttrs
   Description: User can create a PartLot record on the fly if the user has CAN-MaintainLot permissions.
The record is created only if there is no PartLot recrod for pcLotNum and the user
has permissions.
   OperationID: ChkForNeedsLotAttrs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChkForNeedsLotAttrs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChkForNeedsLotAttrs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChkForNeedsLotAttrs(requestBody:ChkForNeedsLotAttrs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChkForNeedsLotAttrs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/ChkForNeedsLotAttrs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChkForNeedsLotAttrs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateNewLotNum
   Description: This method will generate a new lot number
   OperationID: GenerateNewLotNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateNewLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateNewLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateNewLotNum(requestBody:GenerateNewLotNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateNewLotNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/GenerateNewLotNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GenerateNewLotNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListByBinNum
   Description: This method finds lots for Parts by WarehouseCode and BinNum for PackOut Tab in CustShipEntry.
   OperationID: GetListByBinNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListByBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListByBinNum(requestBody:GetListByBinNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListByBinNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/GetListByBinNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListByBinNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListPartLot
   Description: This method finds lots for Parts by WarehouseCode and BinNum.
   OperationID: GetListPartLot
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListPartLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListPartLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListPartLot(requestBody:GetListPartLot_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListPartLot_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/GetListPartLot", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListPartLot_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListByWarehouse
   Description: This method finds lots for Parts by WarehouseCode.
   OperationID: GetListByWarehouse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListByWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListByWarehouse(requestBody:GetListByWarehouse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListByWarehouse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/GetListByWarehouse", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListByWarehouse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateLotAttributes
   Description: Validate the attributes information introduced by the user.
   OperationID: ValidateLotAttributes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateLotAttributes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLotAttributes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateLotAttributes(requestBody:ValidateLotAttributes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateLotAttributes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/ValidateLotAttributes", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateLotAttributes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateShippingDocumentsAttached
   Description: Validate if a Shipping Document was attached if Shipping Docs Available was marked as true
   OperationID: ValidateShippingDocumentsAttached
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateShippingDocumentsAttached_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateShippingDocumentsAttached_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateShippingDocumentsAttached(requestBody:ValidateShippingDocumentsAttached_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateShippingDocumentsAttached_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/ValidateShippingDocumentsAttached", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateShippingDocumentsAttached_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingRevisionNum
   OperationID: OnChangingRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:OnChangingRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/OnChangingRevisionNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartNum
   OperationID: OnChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:OnChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/OnChangePartNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAttributeSet
   OperationID: OnChangeAttributeSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAttributeSet(requestBody:OnChangeAttributeSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAttributeSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/OnChangeAttributeSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeAttributeSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartLot
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartLot
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartLot(requestBody:GetNewPartLot_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartLot_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/GetNewPartLot", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPartLot_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPartLotAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartLotAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartLotAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartLotAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartLotAttch(requestBody:GetNewPartLotAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartLotAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/GetNewPartLotAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPartLotAttch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LotSelectUpdateSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartLotAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartLotListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartLotRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartLotRow,
}

export interface Erp_Tablesets_PartLotAttchRow{
   "Company":string,
   "PartNum":string,
   "LotNum":string,
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

export interface Erp_Tablesets_PartLotListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part.  */  
   "PartNum":string,
      /**  Unique lot number for the part.  */  
   "LotNum":string,
      /**  Optional lot number description.  */  
   "PartLotDescription":string,
      /**  Indicates that there is still some of the lot on hand.  */  
   "OnHand":boolean,
      /**  Earliest date that the lot was referenced.  */  
   "FirstRefDate":string,
      /**  Latest date that the lot was referenced.  */  
   "LastRefDate":string,
      /**   Used only when costing method is by lot. Average Unit Labor Cost of the Part.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   "LotLaborCost":number,
      /**  Used only for lot costing method. Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the LaborCost for the formula for calculating average unit costs.  */  
   "LotBurdenCost":number,
      /**  Used only for costing by lot.  Average Material Unit cost.  maintained Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See LotLaborCost description for explanation of updating with the receipts cost.  */  
   "LotMaterialCost":number,
      /**  Used only when costing by lot. Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   "LotSubContCost":number,
      /**  Use only when lot t cosintg methid is used. Lot  Material Burden Unit cost. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   "LotMtlBurCost":number,
      /**  Determined by setting on Part.AttExpDt if required or tracked.  */  
   "ExpirationDate":string,
      /**  Required Shipping  Documents Available.A flag manually set by the user to indicate that the required documents for the Part/Lot are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Part/Lot.  If the Part.ShipDocReq = yes  then PartLot.ShipDocsA vail must = yes before the system will allow shipment of the Part/LotRequires DocManagement license.  */  
   "ShipDocAvail":boolean,
      /**  Determined by setting on Part.AttBatch if required or tracked.  */  
   "Batch":string,
      /**  Determined by setting on Part.AttMfgBatch if required or tracked.  */  
   "MfgBatch":string,
      /**  Determined by setting on Part.AttMfgLot if required or tracked.  */  
   "MfgLot":string,
      /**  Determined by setting on Part.AttHeat if required or tracked.  */  
   "HeatNum":string,
      /**  Determined by setting on Part.AttFirmware if required or tracked.  */  
   "FirmWare":string,
      /**  Determined by setting on Part.AttBeforeDt if required or tracked.  */  
   "BestBeforeDt":string,
      /**  Determined by setting on Part.AttMfgDt if required or tracked.  */  
   "MfgDt":string,
      /**  Determined by setting on Part.AttCureDt if required or tracked.  */  
   "CureDt":string,
      /**  Expire Date  */  
   "ExpireDt":string,
      /**   Used only when costing method is by LOT FIFO. FIFO Average Unit Labor Cost of the Part per Lot.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating a FIFO lot average cost the following logic is used.
 NEW AVG COST = sum of all (FIFO OnHandQty * FIFO costs)
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   "FIFOLotLaborCost":number,
      /**  Used only for lot FIFO costing method. FIFO Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOLotLaborCost for the formula for calculating average unit costs.  */  
   "FIFOLotBurdenCost":number,
      /**  Used only for costing by lot FIFO.  FIFO Average Material Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   "FIFOLotMaterialCost":number,
      /**  Used only when costing by lot FIFO. FIFO Average Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   "FIFOLotSubContCost":number,
      /**  Use only when lot FIFO costing method is used. FIFO Lot Average Material Burden Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   "FIFOLotMtlBurCost":number,
      /**   Malaysia Localization
LMW Commissioner of Oath's Number  */  
   "CSFLMWComOath":string,
      /**   Malaysia Localization
CJ5 Form Number  */  
   "CSFCJ5FormNbr":string,
      /**   Malaysia Localization
CJ5 Vessel Number  */  
   "CSFCJ5Vessel":string,
      /**   Malaysia Localization
The start date of CJ5 approved period  */  
   "CSFCJ5ApvlStart":string,
      /**   Malaysia Localization
The end date of CJ5 approved period  */  
   "CSFCJ5ApvlEnd":string,
      /**  Stores the number of the import document.  */  
   "ImportNum":string,
      /**  Stores the Country from which the document is imported.  */  
   "ImportedFrom":number,
      /**  Location description from which the document is imported.  */  
   "ImportedFromDesc":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Source of transaction  */  
   "TransactionSource":string,
   "ScrLotBurdenCost":number,
   "ScrLotLaborCost":number,
   "ScrLotMaterialCost":number,
   "ScrLotMtlBurCost":number,
   "ScrLotSubContCost":number,
      /**  Plant to which the lot belongs to  */  
   "Plant":string,
      /**  On Hand quantity for the part in the specified lot  */  
   "OnHandQty":number,
      /**   Malaysia localization         
Indicated if CSF fields are available  */  
   "CSFCJ5Avail":boolean,
      /**   Malaysia localization         
Indicates if LMW fields are available  */  
   "CSFLMWAvail":boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   "PartNumPricePerCode":string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   "PartNumTrackDimension":boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   "PartNumIUM":string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   "PartNumSalesUM":string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   "PartNumTrackLots":boolean,
      /**  Describes the Part.  */  
   "PartNumPartDescription":string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   "PartNumSellingFactor":number,
      /**  Indicates if this part is serial number tracked  */  
   "PartNumTrackSerialNum":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartLotRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The PartNum field identifies the Part.  */  
   "PartNum":string,
      /**  Unique lot number for the part.  */  
   "LotNum":string,
      /**  Optional lot number description.  */  
   "PartLotDescription":string,
      /**  Indicates that there is still some of the lot on hand.  */  
   "OnHand":boolean,
      /**  Earliest date that the lot was referenced.  */  
   "FirstRefDate":string,
      /**  Latest date that the lot was referenced.  */  
   "LastRefDate":string,
      /**   Used only when costing method is by lot. Average Unit Labor Cost of the Part.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   "LotLaborCost":number,
      /**  Used only for lot costing method. Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the LaborCost for the formula for calculating average unit costs.  */  
   "LotBurdenCost":number,
      /**  Used only for costing by lot.  Average Material Unit cost.  maintained Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See LotLaborCost description for explanation of updating with the receipts cost.  */  
   "LotMaterialCost":number,
      /**  Used only when costing by lot. Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   "LotSubContCost":number,
      /**  Use only when lot t cosintg methid is used. Lot  Material Burden Unit cost. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   "LotMtlBurCost":number,
      /**  Determined by setting on Part.AttExpDt if required or tracked.  */  
   "ExpirationDate":string,
      /**  Required Shipping  Documents Available.A flag manually set by the user to indicate that the required documents for the Part/Lot are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Part/Lot.  If the Part.ShipDocReq = yes  then PartLot.ShipDocsA vail must = yes before the system will allow shipment of the Part/LotRequires DocManagement license.  */  
   "ShipDocAvail":boolean,
      /**  Determined by setting on Part.AttBatch if required or tracked.  */  
   "Batch":string,
      /**  Determined by setting on Part.AttMfgBatch if required or tracked.  */  
   "MfgBatch":string,
      /**  Determined by setting on Part.AttMfgLot if required or tracked.  */  
   "MfgLot":string,
      /**  Determined by setting on Part.AttHeat if required or tracked.  */  
   "HeatNum":string,
      /**  Determined by setting on Part.AttFirmware if required or tracked.  */  
   "FirmWare":string,
      /**  Determined by setting on Part.AttBeforeDt if required or tracked.  */  
   "BestBeforeDt":string,
      /**  Determined by setting on Part.AttMfgDt if required or tracked.  */  
   "MfgDt":string,
      /**  Determined by setting on Part.AttCureDt if required or tracked.  */  
   "CureDt":string,
      /**  Expire Date  */  
   "ExpireDt":string,
      /**   Used only when costing method is by LOT FIFO. FIFO Average Unit Labor Cost of the Part per Lot.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating a FIFO lot average cost the following logic is used.
 NEW AVG COST = sum of all (FIFO OnHandQty * FIFO costs)
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   "FIFOLotLaborCost":number,
      /**  Used only for lot FIFO costing method. FIFO Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOLotLaborCost for the formula for calculating average unit costs.  */  
   "FIFOLotBurdenCost":number,
      /**  Used only for costing by lot FIFO.  FIFO Average Material Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   "FIFOLotMaterialCost":number,
      /**  Used only when costing by lot FIFO. FIFO Average Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   "FIFOLotSubContCost":number,
      /**  Use only when lot FIFO costing method is used. FIFO Lot Average Material Burden Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   "FIFOLotMtlBurCost":number,
      /**   Malaysia Localization
LMW Commissioner of Oath's Number  */  
   "CSFLMWComOath":string,
      /**   Malaysia Localization
CJ5 Form Number  */  
   "CSFCJ5FormNbr":string,
      /**   Malaysia Localization
CJ5 Vessel Number  */  
   "CSFCJ5Vessel":string,
      /**   Malaysia Localization
The start date of CJ5 approved period  */  
   "CSFCJ5ApvlStart":string,
      /**   Malaysia Localization
The end date of CJ5 approved period  */  
   "CSFCJ5ApvlEnd":string,
      /**  Stores the number of the import document.  */  
   "ImportNum":string,
      /**  Stores the Country from which the document is imported.  */  
   "ImportedFrom":number,
      /**  Location description from which the document is imported.  */  
   "ImportedFromDesc":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MXImportLocation  */  
   "MXImportLocation":string,
      /**  MXImportDate  */  
   "MXImportDate":string,
      /**  Total OnHand Quantity used specific for Average Costing calculations  */  
   "TotalQtyAvg":number,
      /**  Country number of the Origin Country (defaults from Part Country of Origin).  */  
   "ISOrigCountryNum":number,
      /**   Malaysia localization         
Indicates if LMW fields are available  */  
   "CSFLMWAvail":boolean,
      /**  Indicates if the Lot is created from LotEntry, used for Defer functionality.  */  
   "DeferManual":boolean,
      /**  On Hand quantity for the part in the specified lot  */  
   "OnHandQty":number,
      /**  Plant to which the lot belongs to  */  
   "Plant":string,
   "ScrLotBurdenCost":number,
   "ScrLotLaborCost":number,
   "ScrLotMaterialCost":number,
   "ScrLotMtlBurCost":number,
   "ScrLotSubContCost":number,
      /**  Source of transaction  */  
   "TransactionSource":string,
      /**   Malaysia localization         
Indicated if CSF fields are available  */  
   "CSFCJ5Avail":boolean,
      /**  Part UOM Code  */  
   "IUM":string,
   "BitFlag":number,
   "ISOrigCntyDescription":string,
   "PartNumPartDescription":string,
   "PartNumTrackDimension":boolean,
   "PartNumSalesUM":string,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumSellingFactor":number,
   "PartNumPricePerCode":string,
   "PartNumTrackSerialNum":boolean,
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
      @param vLotNum
      @param vPartNum
      @param vRowid
   */  
export interface CheckDupLotNum_input{
      /**  The Lot Number to be checked for duplicate  */  
   vLotNum:string,
      /**  Part Number associated with the current Lot Number  */  
   vPartNum:string,
      /**  RowIdent field of the PartLot  */  
   vRowid:string,
}

export interface CheckDupLotNum_output{
parameters : {
      /**  output parameters  */  
   vMessage:string,
}
}

   /** Required : 
      @param pcPartNum
      @param pcLotNum
      @param pcDeferOption
   */  
export interface ChkForNeedsLotAttrs_input{
   pcPartNum:string,
   pcLotNum:string,
   pcDeferOption:string,
}

export interface ChkForNeedsLotAttrs_output{
parameters : {
      /**  output parameters  */  
   needsLotAttrs:boolean,
}
}

   /** Required : 
      @param partNum
      @param lotNum
   */  
export interface DeleteByID_input{
   partNum:string,
   lotNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_LotSelectUpdateTableset{
   PartLot:Erp_Tablesets_PartLotRow[],
   PartLotAttch:Erp_Tablesets_PartLotAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartLotAttchRow{
   Company:string,
   PartNum:string,
   LotNum:string,
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

export interface Erp_Tablesets_PartLotListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part.  */  
   PartNum:string,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  Optional lot number description.  */  
   PartLotDescription:string,
      /**  Indicates that there is still some of the lot on hand.  */  
   OnHand:boolean,
      /**  Earliest date that the lot was referenced.  */  
   FirstRefDate:string,
      /**  Latest date that the lot was referenced.  */  
   LastRefDate:string,
      /**   Used only when costing method is by lot. Average Unit Labor Cost of the Part.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   LotLaborCost:number,
      /**  Used only for lot costing method. Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the LaborCost for the formula for calculating average unit costs.  */  
   LotBurdenCost:number,
      /**  Used only for costing by lot.  Average Material Unit cost.  maintained Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See LotLaborCost description for explanation of updating with the receipts cost.  */  
   LotMaterialCost:number,
      /**  Used only when costing by lot. Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   LotSubContCost:number,
      /**  Use only when lot t cosintg methid is used. Lot  Material Burden Unit cost. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   LotMtlBurCost:number,
      /**  Determined by setting on Part.AttExpDt if required or tracked.  */  
   ExpirationDate:string,
      /**  Required Shipping  Documents Available.A flag manually set by the user to indicate that the required documents for the Part/Lot are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Part/Lot.  If the Part.ShipDocReq = yes  then PartLot.ShipDocsA vail must = yes before the system will allow shipment of the Part/LotRequires DocManagement license.  */  
   ShipDocAvail:boolean,
      /**  Determined by setting on Part.AttBatch if required or tracked.  */  
   Batch:string,
      /**  Determined by setting on Part.AttMfgBatch if required or tracked.  */  
   MfgBatch:string,
      /**  Determined by setting on Part.AttMfgLot if required or tracked.  */  
   MfgLot:string,
      /**  Determined by setting on Part.AttHeat if required or tracked.  */  
   HeatNum:string,
      /**  Determined by setting on Part.AttFirmware if required or tracked.  */  
   FirmWare:string,
      /**  Determined by setting on Part.AttBeforeDt if required or tracked.  */  
   BestBeforeDt:string,
      /**  Determined by setting on Part.AttMfgDt if required or tracked.  */  
   MfgDt:string,
      /**  Determined by setting on Part.AttCureDt if required or tracked.  */  
   CureDt:string,
      /**  Expire Date  */  
   ExpireDt:string,
      /**   Used only when costing method is by LOT FIFO. FIFO Average Unit Labor Cost of the Part per Lot.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating a FIFO lot average cost the following logic is used.
 NEW AVG COST = sum of all (FIFO OnHandQty * FIFO costs)
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   FIFOLotLaborCost:number,
      /**  Used only for lot FIFO costing method. FIFO Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOLotLaborCost for the formula for calculating average unit costs.  */  
   FIFOLotBurdenCost:number,
      /**  Used only for costing by lot FIFO.  FIFO Average Material Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOLotMaterialCost:number,
      /**  Used only when costing by lot FIFO. FIFO Average Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOLotSubContCost:number,
      /**  Use only when lot FIFO costing method is used. FIFO Lot Average Material Burden Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOLotMtlBurCost:number,
      /**   Malaysia Localization
LMW Commissioner of Oath's Number  */  
   CSFLMWComOath:string,
      /**   Malaysia Localization
CJ5 Form Number  */  
   CSFCJ5FormNbr:string,
      /**   Malaysia Localization
CJ5 Vessel Number  */  
   CSFCJ5Vessel:string,
      /**   Malaysia Localization
The start date of CJ5 approved period  */  
   CSFCJ5ApvlStart:string,
      /**   Malaysia Localization
The end date of CJ5 approved period  */  
   CSFCJ5ApvlEnd:string,
      /**  Stores the number of the import document.  */  
   ImportNum:string,
      /**  Stores the Country from which the document is imported.  */  
   ImportedFrom:number,
      /**  Location description from which the document is imported.  */  
   ImportedFromDesc:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Source of transaction  */  
   TransactionSource:string,
   ScrLotBurdenCost:number,
   ScrLotLaborCost:number,
   ScrLotMaterialCost:number,
   ScrLotMtlBurCost:number,
   ScrLotSubContCost:number,
      /**  Plant to which the lot belongs to  */  
   Plant:string,
      /**  On Hand quantity for the part in the specified lot  */  
   OnHandQty:number,
      /**   Malaysia localization         
Indicated if CSF fields are available  */  
   CSFCJ5Avail:boolean,
      /**   Malaysia localization         
Indicates if LMW fields are available  */  
   CSFLMWAvail:boolean,
      /**  Indicates the pricing per quantity for this part. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Maintainable only via Part Maintenance. The initial default is "E". Used as default PricePerCode in order entry and invoice entry.  */  
   PartNumPricePerCode:string,
      /**   Onhand quantity is always tracked in the Parts primary inventory uom (Part.IUM). Checking this box indicates that you want to allow tracking of onhand quantity by additional uoms. 
The actual UOMs to be tracked for the part are indicated by PartUOM.TrackOnHand. In order to set the PartUOM.TrackOhHand = True the Part.TrackDimension must = true.
This replaces the old 8.3 Track Dimension feature  */  
   PartNumTrackDimension:boolean,
      /**  Primary Inventory Unit of Measure. The unit costs, are based on this uom. Used as a default for issue transactions for the part.  Part onhand and allocation quantities are tracked by this uom.  The quantities can also be tracked by other uoms (see PartUOM table) but tracking at this uom is mandatory.   Use UOMClass.DefUOMCode of the system default UOMClass  when creating new part records (see XASyst.DefUOMClassID).  */  
   PartNumIUM:string,
      /**  The Selling Unit of measure for the Part. The UOM which the unit prices are based on. Defaults as the Part.IUM.  */  
   PartNumSalesUM:string,
      /**  Indicates if Lot numbers are prompted for in transactions for this part.  Backflushing and AutoReceiving functions are ignored when TrackLots = Yes.  */  
   PartNumTrackLots:boolean,
      /**  Describes the Part.  */  
   PartNumPartDescription:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.  

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   PartNumSellingFactor:number,
      /**  Indicates if this part is serial number tracked  */  
   PartNumTrackSerialNum:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartLotListTableset{
   PartLotList:Erp_Tablesets_PartLotListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartLotRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The PartNum field identifies the Part.  */  
   PartNum:string,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  Optional lot number description.  */  
   PartLotDescription:string,
      /**  Indicates that there is still some of the lot on hand.  */  
   OnHand:boolean,
      /**  Earliest date that the lot was referenced.  */  
   FirstRefDate:string,
      /**  Latest date that the lot was referenced.  */  
   LastRefDate:string,
      /**   Used only when costing method is by lot. Average Unit Labor Cost of the Part.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating an average cost the following logic is used.
 NEW AVG COST = ((ONHAND QTY * AVG COST) + TOTAL RECPT COST) / (ONHAND QTY + RECPT QTY).  Exceptions to this formula are if the onhand qty begins as a negative, then its value is not included in the calculations.  If the receipt transaction is of negative value then the average cost will not be changed.
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the Part record are used as default cost in job material detail. The system is configurable to use either Average, Standard or Last unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   LotLaborCost:number,
      /**  Used only for lot costing method. Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the LaborCost for the formula for calculating average unit costs.  */  
   LotBurdenCost:number,
      /**  Used only for costing by lot.  Average Material Unit cost.  maintained Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See LotLaborCost description for explanation of updating with the receipts cost.  */  
   LotMaterialCost:number,
      /**  Used only when costing by lot. Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   LotSubContCost:number,
      /**  Use only when lot t cosintg methid is used. Lot  Material Burden Unit cost. Indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the AvgLaborCost description for explanation of updating with the receipts cost.  */  
   LotMtlBurCost:number,
      /**  Determined by setting on Part.AttExpDt if required or tracked.  */  
   ExpirationDate:string,
      /**  Required Shipping  Documents Available.A flag manually set by the user to indicate that the required documents for the Part/Lot are available. In order to set to Yes, at least one attachment having a DocType with Shipment = yes must exist for the Part/Lot.  If the Part.ShipDocReq = yes  then PartLot.ShipDocsA vail must = yes before the system will allow shipment of the Part/LotRequires DocManagement license.  */  
   ShipDocAvail:boolean,
      /**  Determined by setting on Part.AttBatch if required or tracked.  */  
   Batch:string,
      /**  Determined by setting on Part.AttMfgBatch if required or tracked.  */  
   MfgBatch:string,
      /**  Determined by setting on Part.AttMfgLot if required or tracked.  */  
   MfgLot:string,
      /**  Determined by setting on Part.AttHeat if required or tracked.  */  
   HeatNum:string,
      /**  Determined by setting on Part.AttFirmware if required or tracked.  */  
   FirmWare:string,
      /**  Determined by setting on Part.AttBeforeDt if required or tracked.  */  
   BestBeforeDt:string,
      /**  Determined by setting on Part.AttMfgDt if required or tracked.  */  
   MfgDt:string,
      /**  Determined by setting on Part.AttCureDt if required or tracked.  */  
   CureDt:string,
      /**  Expire Date  */  
   ExpireDt:string,
      /**   Used only when costing method is by LOT FIFO. FIFO Average Unit Labor Cost of the Part per Lot.  It is directly updated by by  Manufacture receipts, Bill of Material cost rollup, Purchase Part receipts or cost adjustment program.  Basically when updating a FIFO lot average cost the following logic is used.
 NEW AVG COST = sum of all (FIFO OnHandQty * FIFO costs)
GENERAL NOTES ABOUT UNIT COSTS:
The unit cost fields in the PartCost record are used as default cost in job material detail. The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during receipt entry regardless of the Costing method specified.  */  
   FIFOLotLaborCost:number,
      /**  Used only for lot FIFO costing method. FIFO Average burden unit cost. This is updated by Manufactured receipt process, Purchased Part Receipt and inventory adjustment programs.  See the description in the FIFOLotLaborCost for the formula for calculating average unit costs.  */  
   FIFOLotBurdenCost:number,
      /**  Used only for costing by lot FIFO.  FIFO Average Material Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOLotMaterialCost:number,
      /**  Used only when costing by lot FIFO. FIFO Average Subcontract Unit cost. Indirectly maintained by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOLotSubContCost:number,
      /**  Use only when lot FIFO costing method is used. FIFO Lot Average Material Burden Unit cost maintained indirectly by Manufactured cost receipts, Purchased Parts Receipts, Inventory cost adjustment. See the FIFOLotLaborCost description for explanation of updating with the receipts cost.  */  
   FIFOLotMtlBurCost:number,
      /**   Malaysia Localization
LMW Commissioner of Oath's Number  */  
   CSFLMWComOath:string,
      /**   Malaysia Localization
CJ5 Form Number  */  
   CSFCJ5FormNbr:string,
      /**   Malaysia Localization
CJ5 Vessel Number  */  
   CSFCJ5Vessel:string,
      /**   Malaysia Localization
The start date of CJ5 approved period  */  
   CSFCJ5ApvlStart:string,
      /**   Malaysia Localization
The end date of CJ5 approved period  */  
   CSFCJ5ApvlEnd:string,
      /**  Stores the number of the import document.  */  
   ImportNum:string,
      /**  Stores the Country from which the document is imported.  */  
   ImportedFrom:number,
      /**  Location description from which the document is imported.  */  
   ImportedFromDesc:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MXImportLocation  */  
   MXImportLocation:string,
      /**  MXImportDate  */  
   MXImportDate:string,
      /**  Total OnHand Quantity used specific for Average Costing calculations  */  
   TotalQtyAvg:number,
      /**  Country number of the Origin Country (defaults from Part Country of Origin).  */  
   ISOrigCountryNum:number,
      /**   Malaysia localization         
Indicates if LMW fields are available  */  
   CSFLMWAvail:boolean,
      /**  Indicates if the Lot is created from LotEntry, used for Defer functionality.  */  
   DeferManual:boolean,
      /**  On Hand quantity for the part in the specified lot  */  
   OnHandQty:number,
      /**  Plant to which the lot belongs to  */  
   Plant:string,
   ScrLotBurdenCost:number,
   ScrLotLaborCost:number,
   ScrLotMaterialCost:number,
   ScrLotMtlBurCost:number,
   ScrLotSubContCost:number,
      /**  Source of transaction  */  
   TransactionSource:string,
      /**   Malaysia localization         
Indicated if CSF fields are available  */  
   CSFCJ5Avail:boolean,
      /**  Part UOM Code  */  
   IUM:string,
   BitFlag:number,
   ISOrigCntyDescription:string,
   PartNumPartDescription:string,
   PartNumTrackDimension:boolean,
   PartNumSalesUM:string,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumSellingFactor:number,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtLotSelectUpdateTableset{
   PartLot:Erp_Tablesets_PartLotRow[],
   PartLotAttch:Erp_Tablesets_PartLotAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param vPartNum
   */  
export interface GenerateNewLotNum_input{
      /**  Part Number associated with the current Lot Number  */  
   vPartNum:string,
}

export interface GenerateNewLotNum_output{
parameters : {
      /**  output parameters  */  
   vNewLotNum:string,
}
}

   /** Required : 
      @param partNum
      @param lotNum
   */  
export interface GetByID_input{
   partNum:string,
   lotNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_LotSelectUpdateTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_LotSelectUpdateTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_LotSelectUpdateTableset[],
}

   /** Required : 
      @param ipWarehouseCode
      @param ipBinNum
      @param whereclause
      @param pageSize
      @param absolutePage
   */  
export interface GetListByBinNum_input{
      /**  Warehouse Code.  */  
   ipWarehouseCode:string,
      /**  Bin number.  */  
   ipBinNum:string,
      /**  WhereClause.  */  
   whereclause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListByBinNum_output{
   returnObj:Erp_Tablesets_PartLotListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipWarehouseCode
      @param ipPartNum
      @param ipUOMCode
   */  
export interface GetListByWarehouse_input{
      /**  Warehouse Code.  */  
   ipWarehouseCode:string,
      /**  PartNum.  */  
   ipPartNum:string,
      /**  UOMCode.  */  
   ipUOMCode:string,
}

export interface GetListByWarehouse_output{
   returnObj:Erp_Tablesets_PartLotListTableset[],
}

   /** Required : 
      @param ipWarehouseCode
      @param ipBinNum
      @param attributeSetID
      @param whereclause
      @param pageSize
      @param absolutePage
   */  
export interface GetListPartLot_input{
      /**  Warehouse Code.  */  
   ipWarehouseCode:string,
      /**  Bin number.  */  
   ipBinNum:string,
      /**  Attribute Set ID  */  
   attributeSetID:number,
      /**  WhereClause.  */  
   whereclause:string,
      /**  Page size.  */  
   pageSize:number,
      /**  Absolute page.  */  
   absolutePage:number,
}

export interface GetListPartLot_output{
   returnObj:Erp_Tablesets_PartLotListTableset[],
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
   returnObj:Erp_Tablesets_PartLotListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param lotNum
   */  
export interface GetNewPartLotAttch_input{
   ds:Erp_Tablesets_LotSelectUpdateTableset[],
   partNum:string,
   lotNum:string,
}

export interface GetNewPartLotAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LotSelectUpdateTableset,
}
}

   /** Required : 
      @param ds
      @param partNum
   */  
export interface GetNewPartLot_input{
   ds:Erp_Tablesets_LotSelectUpdateTableset[],
   partNum:string,
}

export interface GetNewPartLot_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LotSelectUpdateTableset,
}
}

   /** Required : 
      @param whereClausePartLot
      @param whereClausePartLotAttch
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartLot:string,
   whereClausePartLotAttch:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_LotSelectUpdateTableset[],
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
      @param attributeSetID
      @param ds
   */  
export interface OnChangeAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_LotSelectUpdateTableset[],
}

export interface OnChangeAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LotSelectUpdateTableset,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
}
}

   /** Required : 
      @param partNum
   */  
export interface OnChangePartNum_input{
   partNum:string,
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   revisionNum:string,
   AttributeSetID:number,
}
}

   /** Required : 
      @param revisionNum
      @param partNum
      @param AttributeSetID
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   partNum:string,
   AttributeSetID:number,
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   AttributeSetID:number,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtLotSelectUpdateTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtLotSelectUpdateTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_LotSelectUpdateTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LotSelectUpdateTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ValidateLotAttributes_input{
   ds:Erp_Tablesets_LotSelectUpdateTableset[],
}

export interface ValidateLotAttributes_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LotSelectUpdateTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ValidateShippingDocumentsAttached_input{
   ds:Erp_Tablesets_LotSelectUpdateTableset[],
}

export interface ValidateShippingDocumentsAttached_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LotSelectUpdateTableset,
}
}

