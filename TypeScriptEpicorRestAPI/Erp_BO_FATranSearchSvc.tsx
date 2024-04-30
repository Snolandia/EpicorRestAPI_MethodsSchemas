import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.FATranSearchSvc
// Description: FATran records for Asset Tracker
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get FATranSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FATranSearches
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAScheduleRow
   */  
export function get_FATranSearches(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAScheduleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAScheduleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FATranSearches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAScheduleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.FAScheduleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FATranSearches(requestBody:Erp_Tablesets_FAScheduleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the FATranSearch item
   Description: Calls GetByID to retrieve the FATranSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FATranSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param DetailNum Desc: DetailNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FAScheduleRow
   */  
export function get_FATranSearches_Company_AssetNum_AssetRegID_DetailNum(Company:string, AssetNum:string, AssetRegID:string, DetailNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAScheduleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_FAScheduleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FATranSearch for the service
   Description: Calls UpdateExt to update FATranSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FATranSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param DetailNum Desc: DetailNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAScheduleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FATranSearches_Company_AssetNum_AssetRegID_DetailNum(Company:string, AssetNum:string, AssetRegID:string, DetailNum:string, requestBody:Erp_Tablesets_FAScheduleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + ")", {
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
   Summary: Call UpdateExt to delete FATranSearch item
   Description: Call UpdateExt to delete FATranSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FATranSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param DetailNum Desc: DetailNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FATranSearches_Company_AssetNum_AssetRegID_DetailNum(Company:string, AssetNum:string, AssetRegID:string, DetailNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + ")", {
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
   Description: Get FATrans items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FATrans1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param DetailNum Desc: DetailNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FATranRow
   */  
export function get_FATranSearches_Company_AssetNum_AssetRegID_DetailNum_FATrans(Company:string, AssetNum:string, AssetRegID:string, DetailNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FATranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + ")/FATrans", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FATranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FATran item
   Description: Calls GetByID to retrieve the FATran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FATran1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param DetailNum Desc: DetailNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FATranRow
   */  
export function get_FATranSearches_Company_AssetNum_AssetRegID_DetailNum_FATrans_Company_AssetNum_AssetRegID_DetailNum_SeqNum(Company:string, AssetNum:string, AssetRegID:string, DetailNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FATranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATranSearches(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + ")/FATrans(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_FATranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get FATrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FATrans
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FATranRow
   */  
export function get_FATrans(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FATranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATrans", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FATranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FATrans
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FATranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.FATranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FATrans(requestBody:Erp_Tablesets_FATranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATrans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the FATran item
   Description: Calls GetByID to retrieve the FATran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FATran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param DetailNum Desc: DetailNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FATranRow
   */  
export function get_FATrans_Company_AssetNum_AssetRegID_DetailNum_SeqNum(Company:string, AssetNum:string, AssetRegID:string, DetailNum:string, SeqNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FATranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATrans(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + "," + SeqNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_FATranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FATran for the service
   Description: Calls UpdateExt to update FATran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FATran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param DetailNum Desc: DetailNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.FATranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FATrans_Company_AssetNum_AssetRegID_DetailNum_SeqNum(Company:string, AssetNum:string, AssetRegID:string, DetailNum:string, SeqNum:string, requestBody:Erp_Tablesets_FATranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATrans(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + "," + SeqNum + ")", {
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
   Summary: Call UpdateExt to delete FATran item
   Description: Call UpdateExt to delete FATran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FATran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetNum Desc: AssetNum   Required: True   Allow empty value : True
      @param AssetRegID Desc: AssetRegID   Required: True   Allow empty value : True
      @param DetailNum Desc: DetailNum   Required: True
      @param SeqNum Desc: SeqNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FATrans_Company_AssetNum_AssetRegID_DetailNum_SeqNum(Company:string, AssetNum:string, AssetRegID:string, DetailNum:string, SeqNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/FATrans(" + Company + "," + AssetNum + "," + AssetRegID + "," + DetailNum + "," + SeqNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAScheduleListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAScheduleListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAScheduleListRow)
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
export function get_GetRows(whereClauseFASchedule:string, whereClauseFATran:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFASchedule!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFASchedule=" + whereClauseFASchedule
   }
   if(typeof whereClauseFATran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFATran=" + whereClauseFATran
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(assetNum:string, assetRegID:string, detailNum:string, epicorHeaders?:Headers){
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
   if(typeof assetRegID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "assetRegID=" + assetRegID
   }
   if(typeof detailNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "detailNum=" + detailNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method GetSortedFASchedules
   Description: Gets and sorts the FASchedule/FATran records by FiscalYear/FiscalPeriod.
   OperationID: GetSortedFASchedules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSortedFASchedules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSortedFASchedules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSortedFASchedules(requestBody:GetSortedFASchedules_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSortedFASchedules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/GetSortedFASchedules", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetSortedFASchedules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFASchedule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFASchedule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFASchedule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFASchedule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFASchedule(requestBody:GetNewFASchedule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFASchedule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/GetNewFASchedule", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewFASchedule_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFATran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFATran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFATran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFATran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFATran(requestBody:GetNewFATran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFATran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/GetNewFATran", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewFATran_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FATranSearchSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAScheduleListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAScheduleListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAScheduleRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAScheduleRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FATranRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FATranRow,
}

export interface Erp_Tablesets_FAScheduleListRow{
      /**  company of asset transactions  */  
   "Company":string,
      /**  Identifier of the asset  */  
   "AssetNum":string,
      /**  Identifier of the Asset Register.  */  
   "AssetRegID":string,
      /**  Unique sequence number of the asset trransactions  */  
   "DetailNum":number,
      /**  The G/L Book that will be used when posting asset depreciations against this register.  */  
   "BookID":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The fiscal year of last posted gl entry of this transaction.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period of last posted gl entry of this transaction.  */  
   "FiscalPeriod":number,
      /**  The depreciation amount of the asset for this transaction.  */  
   "Depreciation":number,
      /**  The bookvalue of the asset after posting this treansaction.  */  
   "BookValue":number,
      /**  The date of the last posting to the gl of this transaction. Transaction can be posted multiple times.  */  
   "PostDate":string,
      /**  flag to indicate the transaction is posted at least once.  */  
   "Posted":boolean,
      /**  The class of the asset.  */  
   "ClassCode":string,
      /**  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "PostedDepreciation":number,
      /**  The transaction is closed  when the fiscal period is closed for assets.  */  
   "Closed":boolean,
      /**  for future use.  */  
   "Modified":boolean,
      /**  The depreciation amount of the asset for this transaction in the document currency.  */  
   "DocDepreciation":number,
      /**  The bookvalue of the asset after posting this transaction in the document currency.  */  
   "DocBookValue":number,
      /**  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "DocPostedDepreciation":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt1Depreciation":number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   "Rpt1BookValue":number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt1PostedDepreciation":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt2Depreciation":number,
      /**  The bookvalue of the asset after posting this transaction in reporting currency.  */  
   "Rpt2BookValue":number,
      /**  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt2PostedDepreciation":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt3Depreciation":number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   "Rpt3BookValue":number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt3PostedDepreciation":number,
      /**  Year number not related to the fiscal year.  */  
   "YearNum":number,
      /**  The depreciation amount of the asset for this transaction.  */  
   "GrantDepreciation":number,
      /**  The bookvalue of the asset after posting this treansaction.  */  
   "GrantBookValue":number,
      /**  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "PostedGrantDepn":number,
      /**  The depreciation amount of the asset for this transaction in the document currency.  */  
   "DocGrantDepreciation":number,
      /**  The bookvalue of the asset after posting this transaction in the document currency.  */  
   "DocGrantBookValue":number,
      /**  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "DocPostedGrantDepn":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt1GrantDepreciation":number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   "Rpt1GrantBookValue":number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt1PostedGrantDepn":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt2GrantDepreciation":number,
      /**  The bookvalue of the asset after posting this transaction in reporting currency.  */  
   "Rpt2GrantBookValue":number,
      /**  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt2PostedGrantDepn":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt3GrantDepreciation":number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   "Rpt3GrantBookValue":number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt3PostedGrantDepn":number,
      /**  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  */  
   "DepRecalcDate":string,
      /**  The alternate Detail Number that will be used when Dynamic Depreciation Year option is set.  */  
   "DepDetailNum":number,
      /**  The depreciation year of last posted gl entry of this transaction.  */  
   "DepYear":number,
      /**  Depreciation year suffix.  */  
   "DepYearSuffix":string,
      /**  The depreciation period of last posted gl entry of this transaction.  */  
   "DepPeriod":number,
      /**  flag to indicate if the depreciation for this period is for holiday period and should not be included.  */  
   "PeriodHoliday":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "CurrencyCode":string,
      /**  Currency Symbol  */  
   "CurrSymbol":string,
      /**  New sort order according to FiscalYear/FiscalPeriod  */  
   "DispDetailNum":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FAScheduleRow{
      /**  company of asset transactions  */  
   "Company":string,
      /**  Identifier of the asset  */  
   "AssetNum":string,
      /**  Identifier of the Asset Register.  */  
   "AssetRegID":string,
      /**  Unique sequence number of the asset trransactions  */  
   "DetailNum":number,
      /**  The G/L Book that will be used when posting asset depreciations against this register.  */  
   "BookID":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The fiscal year of last posted gl entry of this transaction.  */  
   "FiscalYear":number,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal period of last posted gl entry of this transaction.  */  
   "FiscalPeriod":number,
      /**  The depreciation amount of the asset for this transaction.  */  
   "Depreciation":number,
      /**  The bookvalue of the asset after posting this treansaction.  */  
   "BookValue":number,
      /**  The date of the last posting to the gl of this transaction. Transaction can be posted multiple times.  */  
   "PostDate":string,
      /**  flag to indicate the transaction is posted at least once.  */  
   "Posted":boolean,
      /**  The class of the asset.  */  
   "ClassCode":string,
      /**  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "PostedDepreciation":number,
      /**  The transaction is closed  when the fiscal period is closed for assets.  */  
   "Closed":boolean,
      /**  for future use.  */  
   "Modified":boolean,
      /**  The depreciation amount of the asset for this transaction in the document currency.  */  
   "DocDepreciation":number,
      /**  The bookvalue of the asset after posting this transaction in the document currency.  */  
   "DocBookValue":number,
      /**  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "DocPostedDepreciation":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt1Depreciation":number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   "Rpt1BookValue":number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt1PostedDepreciation":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt2Depreciation":number,
      /**  The bookvalue of the asset after posting this transaction in reporting currency.  */  
   "Rpt2BookValue":number,
      /**  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt2PostedDepreciation":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt3Depreciation":number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   "Rpt3BookValue":number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt3PostedDepreciation":number,
      /**  Year number not related to the fiscal year.  */  
   "YearNum":number,
      /**  The depreciation amount of the asset for this transaction.  */  
   "GrantDepreciation":number,
      /**  The bookvalue of the asset after posting this treansaction.  */  
   "GrantBookValue":number,
      /**  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "PostedGrantDepn":number,
      /**  The depreciation amount of the asset for this transaction in the document currency.  */  
   "DocGrantDepreciation":number,
      /**  The bookvalue of the asset after posting this transaction in the document currency.  */  
   "DocGrantBookValue":number,
      /**  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "DocPostedGrantDepn":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt1GrantDepreciation":number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   "Rpt1GrantBookValue":number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt1PostedGrantDepn":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt2GrantDepreciation":number,
      /**  The bookvalue of the asset after posting this transaction in reporting currency.  */  
   "Rpt2GrantBookValue":number,
      /**  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt2PostedGrantDepn":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt3GrantDepreciation":number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   "Rpt3GrantBookValue":number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt3PostedGrantDepn":number,
      /**  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  */  
   "DepRecalcDate":string,
      /**  The alternate Detail Number that will be used when Dynamic Depreciation Year option is set.  */  
   "DepDetailNum":number,
      /**  The depreciation year of last posted gl entry of this transaction.  */  
   "DepYear":number,
      /**  Depreciation year suffix.  */  
   "DepYearSuffix":string,
      /**  The depreciation period of last posted gl entry of this transaction.  */  
   "DepPeriod":number,
      /**  flag to indicate if the depreciation for this period is for holiday period and should not be included.  */  
   "PeriodHoliday":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
   "CurrencyCode":string,
      /**  Currency Symbol  */  
   "CurrSymbol":string,
      /**  New sort order according to FiscalYear/FiscalPeriod  */  
   "DispDetailNum":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FATranRow{
      /**  company of asset transactions  */  
   "Company":string,
      /**  Identifier of the asset  */  
   "AssetNum":string,
      /**  Identifier of the Asset Register.  */  
   "AssetRegID":string,
      /**  Unique detail number of the asset depreciation transaction  */  
   "DetailNum":number,
      /**  Unique sequence number of the asset depreciation transaction  */  
   "SeqNum":number,
      /**  Sequence of the Asset. Currently only 0 is supported.  */  
   "AssetSeq":number,
      /**  The fiscal year of last posted gl entry of this transaction.  */  
   "FiscalYear":number,
      /**  The fiscal period of last posted gl entry of this transaction.  */  
   "FiscalPeriod":number,
      /**  The depreciation amount of the asset for this transaction.  */  
   "Depreciation":number,
      /**  The bookvalue of the asset after posting this treansaction.  */  
   "BookValue":number,
      /**  The date of the last posting to the gl of this transaction. Transaction can be posted multiple times.  */  
   "PostDate":string,
      /**  The gl journal of the last posting to the gl.  */  
   "JournalCode":string,
      /**  The journal number of the last posting to the gl.  */  
   "JournalNum":number,
      /**  flag to indicate the transaction is posted at least once.  */  
   "Posted":boolean,
      /**  The class of the asset.  */  
   "ClassCode":string,
      /**  The user who posted the transaction the last time.  */  
   "PostedBy":string,
      /**  The depreciation value posted to the GL. If the depreciation value varies from the post value than the difference will be posted during the next posting process.  */  
   "PostValue":number,
      /**  The transaction is closed  when the fiscal period is closed for assets.  */  
   "Closed":boolean,
      /**  for future use.  */  
   "Modified":boolean,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  The G/L Book that will be used when posting asset depreciations against this register.  */  
   "BookID":string,
      /**  The depreciation amount of the asset for this transaction in the document currency.  */  
   "DocDepreciation":number,
      /**  The bookvalue of the asset after posting this transaction in the document currency.  */  
   "DocBookValue":number,
      /**  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "DocPostValue":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt1Depreciation":number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   "Rpt1BookValue":number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt1PostValue":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt2Depreciation":number,
      /**  The bookvalue of the asset after posting this transaction in reporting currency.  */  
   "Rpt2BookValue":number,
      /**  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt2PostValue":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt3Depreciation":number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   "Rpt3BookValue":number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt3PostValue":number,
      /**  Year number not related to the fiscal year.  */  
   "YearNum":number,
      /**  The depreciation amount of the asset for this transaction.  */  
   "GrantDepreciation":number,
      /**  The bookvalue of the asset after posting this treansaction.  */  
   "GrantBookValue":number,
      /**  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "PostGrantValue":number,
      /**  The depreciation amount of the asset for this transaction in the document currency.  */  
   "DocGrantDepreciation":number,
      /**  The bookvalue of the asset after posting this transaction in the document currency.  */  
   "DocGrantBookValue":number,
      /**  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "DocPostGrantValue":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt1GrantDepreciation":number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   "Rpt1GrantBookValue":number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt1PostGrantValue":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt2GrantDepreciation":number,
      /**  The bookvalue of the asset after posting this transaction in reporting currency.  */  
   "Rpt2GrantBookValue":number,
      /**  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt2PostGrantValue":number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   "Rpt3GrantDepreciation":number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   "Rpt3GrantBookValue":number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   "Rpt3PostGrantValue":number,
      /**  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  */  
   "DepRecalcDate":string,
      /**  GUID - reference on PE ABT.  */  
   "ABTUID":string,
      /**  The alternate Detail Number that will be used when Dynamic Depreciation Year option is set.  */  
   "DepDetailNum":number,
      /**  The depreciation year of last posted gl entry of this transaction.  */  
   "DepYear":number,
      /**  Depreciation year suffix.  */  
   "DepYearSuffix":string,
      /**  The depreciation period of last posted gl entry of this transaction.  */  
   "DepPeriod":number,
      /**  flag to indicate if the depreciation for this period is for holiday period and should not be included.  */  
   "PeriodHoliday":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Source of depreciation transaction.  */  
   "TranType":number,
      /**  Indicates that the transaction is reflected in FAsset costs.  */  
   "HdrCostRecorded":boolean,
      /**  List of Asset Registers in which the transaction is reflected.  */  
   "RecordedRegList":string,
      /**  SrcTranNum  */  
   "SrcTranNum":number,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangeDate  */  
   "ChangeDate":string,
   "CurrencyCode":string,
   "CurrSymbol":string,
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
      @param assetNum
      @param assetRegID
      @param detailNum
   */  
export interface DeleteByID_input{
   assetNum:string,
   assetRegID:string,
   detailNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_FAScheduleListRow{
      /**  company of asset transactions  */  
   Company:string,
      /**  Identifier of the asset  */  
   AssetNum:string,
      /**  Identifier of the Asset Register.  */  
   AssetRegID:string,
      /**  Unique sequence number of the asset trransactions  */  
   DetailNum:number,
      /**  The G/L Book that will be used when posting asset depreciations against this register.  */  
   BookID:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The fiscal year of last posted gl entry of this transaction.  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period of last posted gl entry of this transaction.  */  
   FiscalPeriod:number,
      /**  The depreciation amount of the asset for this transaction.  */  
   Depreciation:number,
      /**  The bookvalue of the asset after posting this treansaction.  */  
   BookValue:number,
      /**  The date of the last posting to the gl of this transaction. Transaction can be posted multiple times.  */  
   PostDate:string,
      /**  flag to indicate the transaction is posted at least once.  */  
   Posted:boolean,
      /**  The class of the asset.  */  
   ClassCode:string,
      /**  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   PostedDepreciation:number,
      /**  The transaction is closed  when the fiscal period is closed for assets.  */  
   Closed:boolean,
      /**  for future use.  */  
   Modified:boolean,
      /**  The depreciation amount of the asset for this transaction in the document currency.  */  
   DocDepreciation:number,
      /**  The bookvalue of the asset after posting this transaction in the document currency.  */  
   DocBookValue:number,
      /**  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   DocPostedDepreciation:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt1Depreciation:number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   Rpt1BookValue:number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt1PostedDepreciation:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt2Depreciation:number,
      /**  The bookvalue of the asset after posting this transaction in reporting currency.  */  
   Rpt2BookValue:number,
      /**  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt2PostedDepreciation:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt3Depreciation:number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   Rpt3BookValue:number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt3PostedDepreciation:number,
      /**  Year number not related to the fiscal year.  */  
   YearNum:number,
      /**  The depreciation amount of the asset for this transaction.  */  
   GrantDepreciation:number,
      /**  The bookvalue of the asset after posting this treansaction.  */  
   GrantBookValue:number,
      /**  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   PostedGrantDepn:number,
      /**  The depreciation amount of the asset for this transaction in the document currency.  */  
   DocGrantDepreciation:number,
      /**  The bookvalue of the asset after posting this transaction in the document currency.  */  
   DocGrantBookValue:number,
      /**  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   DocPostedGrantDepn:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt1GrantDepreciation:number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   Rpt1GrantBookValue:number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt1PostedGrantDepn:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt2GrantDepreciation:number,
      /**  The bookvalue of the asset after posting this transaction in reporting currency.  */  
   Rpt2GrantBookValue:number,
      /**  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt2PostedGrantDepn:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt3GrantDepreciation:number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   Rpt3GrantBookValue:number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt3PostedGrantDepn:number,
      /**  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  */  
   DepRecalcDate:string,
      /**  The alternate Detail Number that will be used when Dynamic Depreciation Year option is set.  */  
   DepDetailNum:number,
      /**  The depreciation year of last posted gl entry of this transaction.  */  
   DepYear:number,
      /**  Depreciation year suffix.  */  
   DepYearSuffix:string,
      /**  The depreciation period of last posted gl entry of this transaction.  */  
   DepPeriod:number,
      /**  flag to indicate if the depreciation for this period is for holiday period and should not be included.  */  
   PeriodHoliday:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   CurrencyCode:string,
      /**  Currency Symbol  */  
   CurrSymbol:string,
      /**  New sort order according to FiscalYear/FiscalPeriod  */  
   DispDetailNum:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FAScheduleListTableset{
   FAScheduleList:Erp_Tablesets_FAScheduleListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FAScheduleRow{
      /**  company of asset transactions  */  
   Company:string,
      /**  Identifier of the asset  */  
   AssetNum:string,
      /**  Identifier of the Asset Register.  */  
   AssetRegID:string,
      /**  Unique sequence number of the asset trransactions  */  
   DetailNum:number,
      /**  The G/L Book that will be used when posting asset depreciations against this register.  */  
   BookID:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The fiscal year of last posted gl entry of this transaction.  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal period of last posted gl entry of this transaction.  */  
   FiscalPeriod:number,
      /**  The depreciation amount of the asset for this transaction.  */  
   Depreciation:number,
      /**  The bookvalue of the asset after posting this treansaction.  */  
   BookValue:number,
      /**  The date of the last posting to the gl of this transaction. Transaction can be posted multiple times.  */  
   PostDate:string,
      /**  flag to indicate the transaction is posted at least once.  */  
   Posted:boolean,
      /**  The class of the asset.  */  
   ClassCode:string,
      /**  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   PostedDepreciation:number,
      /**  The transaction is closed  when the fiscal period is closed for assets.  */  
   Closed:boolean,
      /**  for future use.  */  
   Modified:boolean,
      /**  The depreciation amount of the asset for this transaction in the document currency.  */  
   DocDepreciation:number,
      /**  The bookvalue of the asset after posting this transaction in the document currency.  */  
   DocBookValue:number,
      /**  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   DocPostedDepreciation:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt1Depreciation:number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   Rpt1BookValue:number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt1PostedDepreciation:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt2Depreciation:number,
      /**  The bookvalue of the asset after posting this transaction in reporting currency.  */  
   Rpt2BookValue:number,
      /**  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt2PostedDepreciation:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt3Depreciation:number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   Rpt3BookValue:number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt3PostedDepreciation:number,
      /**  Year number not related to the fiscal year.  */  
   YearNum:number,
      /**  The depreciation amount of the asset for this transaction.  */  
   GrantDepreciation:number,
      /**  The bookvalue of the asset after posting this treansaction.  */  
   GrantBookValue:number,
      /**  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   PostedGrantDepn:number,
      /**  The depreciation amount of the asset for this transaction in the document currency.  */  
   DocGrantDepreciation:number,
      /**  The bookvalue of the asset after posting this transaction in the document currency.  */  
   DocGrantBookValue:number,
      /**  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   DocPostedGrantDepn:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt1GrantDepreciation:number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   Rpt1GrantBookValue:number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt1PostedGrantDepn:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt2GrantDepreciation:number,
      /**  The bookvalue of the asset after posting this transaction in reporting currency.  */  
   Rpt2GrantBookValue:number,
      /**  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt2PostedGrantDepn:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt3GrantDepreciation:number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   Rpt3GrantBookValue:number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt3PostedGrantDepn:number,
      /**  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  */  
   DepRecalcDate:string,
      /**  The alternate Detail Number that will be used when Dynamic Depreciation Year option is set.  */  
   DepDetailNum:number,
      /**  The depreciation year of last posted gl entry of this transaction.  */  
   DepYear:number,
      /**  Depreciation year suffix.  */  
   DepYearSuffix:string,
      /**  The depreciation period of last posted gl entry of this transaction.  */  
   DepPeriod:number,
      /**  flag to indicate if the depreciation for this period is for holiday period and should not be included.  */  
   PeriodHoliday:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
   CurrencyCode:string,
      /**  Currency Symbol  */  
   CurrSymbol:string,
      /**  New sort order according to FiscalYear/FiscalPeriod  */  
   DispDetailNum:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FATranRow{
      /**  company of asset transactions  */  
   Company:string,
      /**  Identifier of the asset  */  
   AssetNum:string,
      /**  Identifier of the Asset Register.  */  
   AssetRegID:string,
      /**  Unique detail number of the asset depreciation transaction  */  
   DetailNum:number,
      /**  Unique sequence number of the asset depreciation transaction  */  
   SeqNum:number,
      /**  Sequence of the Asset. Currently only 0 is supported.  */  
   AssetSeq:number,
      /**  The fiscal year of last posted gl entry of this transaction.  */  
   FiscalYear:number,
      /**  The fiscal period of last posted gl entry of this transaction.  */  
   FiscalPeriod:number,
      /**  The depreciation amount of the asset for this transaction.  */  
   Depreciation:number,
      /**  The bookvalue of the asset after posting this treansaction.  */  
   BookValue:number,
      /**  The date of the last posting to the gl of this transaction. Transaction can be posted multiple times.  */  
   PostDate:string,
      /**  The gl journal of the last posting to the gl.  */  
   JournalCode:string,
      /**  The journal number of the last posting to the gl.  */  
   JournalNum:number,
      /**  flag to indicate the transaction is posted at least once.  */  
   Posted:boolean,
      /**  The class of the asset.  */  
   ClassCode:string,
      /**  The user who posted the transaction the last time.  */  
   PostedBy:string,
      /**  The depreciation value posted to the GL. If the depreciation value varies from the post value than the difference will be posted during the next posting process.  */  
   PostValue:number,
      /**  The transaction is closed  when the fiscal period is closed for assets.  */  
   Closed:boolean,
      /**  for future use.  */  
   Modified:boolean,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The G/L Book that will be used when posting asset depreciations against this register.  */  
   BookID:string,
      /**  The depreciation amount of the asset for this transaction in the document currency.  */  
   DocDepreciation:number,
      /**  The bookvalue of the asset after posting this transaction in the document currency.  */  
   DocBookValue:number,
      /**  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   DocPostValue:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt1Depreciation:number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   Rpt1BookValue:number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt1PostValue:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt2Depreciation:number,
      /**  The bookvalue of the asset after posting this transaction in reporting currency.  */  
   Rpt2BookValue:number,
      /**  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt2PostValue:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt3Depreciation:number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   Rpt3BookValue:number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt3PostValue:number,
      /**  Year number not related to the fiscal year.  */  
   YearNum:number,
      /**  The depreciation amount of the asset for this transaction.  */  
   GrantDepreciation:number,
      /**  The bookvalue of the asset after posting this treansaction.  */  
   GrantBookValue:number,
      /**  The depreciation value posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   PostGrantValue:number,
      /**  The depreciation amount of the asset for this transaction in the document currency.  */  
   DocGrantDepreciation:number,
      /**  The bookvalue of the asset after posting this transaction in the document currency.  */  
   DocGrantBookValue:number,
      /**  The depreciation value in the document currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   DocPostGrantValue:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt1GrantDepreciation:number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   Rpt1GrantBookValue:number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt1PostGrantValue:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt2GrantDepreciation:number,
      /**  The bookvalue of the asset after posting this transaction in reporting currency.  */  
   Rpt2GrantBookValue:number,
      /**  The depreciation value in the reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt2PostGrantValue:number,
      /**  The depreciation amount of the asset for this transaction in reporting currency.  */  
   Rpt3GrantDepreciation:number,
      /**  The bookvalue of the asset after posting this treansaction in reporting currency.  */  
   Rpt3GrantBookValue:number,
      /**  The depreciation value in reporting currency posted to the GL. If the depreciation value varies from the posted depreciation then the difference will be posted during the next posting process.  */  
   Rpt3PostGrantValue:number,
      /**  The last depreciation recalculation apply date.  This is the date used to get the exchange rate for the depreciation calculation process.  */  
   DepRecalcDate:string,
      /**  GUID - reference on PE ABT.  */  
   ABTUID:string,
      /**  The alternate Detail Number that will be used when Dynamic Depreciation Year option is set.  */  
   DepDetailNum:number,
      /**  The depreciation year of last posted gl entry of this transaction.  */  
   DepYear:number,
      /**  Depreciation year suffix.  */  
   DepYearSuffix:string,
      /**  The depreciation period of last posted gl entry of this transaction.  */  
   DepPeriod:number,
      /**  flag to indicate if the depreciation for this period is for holiday period and should not be included.  */  
   PeriodHoliday:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Source of depreciation transaction.  */  
   TranType:number,
      /**  Indicates that the transaction is reflected in FAsset costs.  */  
   HdrCostRecorded:boolean,
      /**  List of Asset Registers in which the transaction is reflected.  */  
   RecordedRegList:string,
      /**  SrcTranNum  */  
   SrcTranNum:number,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
   CurrencyCode:string,
   CurrSymbol:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FATranSearchTableset{
   FASchedule:Erp_Tablesets_FAScheduleRow[],
   FATran:Erp_Tablesets_FATranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtFATranSearchTableset{
   FASchedule:Erp_Tablesets_FAScheduleRow[],
   FATran:Erp_Tablesets_FATranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param assetNum
      @param assetRegID
      @param detailNum
   */  
export interface GetByID_input{
   assetNum:string,
   assetRegID:string,
   detailNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_FATranSearchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_FATranSearchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_FATranSearchTableset[],
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
   returnObj:Erp_Tablesets_FAScheduleListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param assetNum
      @param assetRegID
   */  
export interface GetNewFASchedule_input{
   ds:Erp_Tablesets_FATranSearchTableset[],
   assetNum:string,
   assetRegID:string,
}

export interface GetNewFASchedule_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FATranSearchTableset,
}
}

   /** Required : 
      @param ds
      @param assetNum
      @param assetRegID
      @param detailNum
   */  
export interface GetNewFATran_input{
   ds:Erp_Tablesets_FATranSearchTableset[],
   assetNum:string,
   assetRegID:string,
   detailNum:number,
}

export interface GetNewFATran_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FATranSearchTableset,
}
}

   /** Required : 
      @param whereClauseFASchedule
      @param whereClauseFATran
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFASchedule:string,
   whereClauseFATran:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_FATranSearchTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipAssetNum
      @param ipAssetRegID
      @param ds
   */  
export interface GetSortedFASchedules_input{
      /**  Input AssetNum  */  
   ipAssetNum:string,
      /**  Input Asset Register ID  */  
   ipAssetRegID:string,
   ds:Erp_Tablesets_FATranSearchTableset[],
}

export interface GetSortedFASchedules_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FATranSearchTableset,
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
   ds:Erp_Tablesets_UpdExtFATranSearchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtFATranSearchTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_FATranSearchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FATranSearchTableset,
}
}

