import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PlantConfCtrlSvc
// Description: PlantConfCtrlSvc BO.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/$metadata", {
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
   Description: Get PlantConfCtrls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantConfCtrls
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfCtrlRow
   */  
export function get_PlantConfCtrls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantConfCtrls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PlantConfCtrlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantConfCtrls(requestBody:Erp_Tablesets_PlantConfCtrlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PlantConfCtrl item
   Description: Calls GetByID to retrieve the PlantConfCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfCtrl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantConfCtrlRow
   */  
export function get_PlantConfCtrls_Company_Plant(Company:string, Plant:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantConfCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")", {
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
         resolve(data as Erp_Tablesets_PlantConfCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlantConfCtrl for the service
   Description: Calls UpdateExt to update PlantConfCtrl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantConfCtrl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlantConfCtrls_Company_Plant(Company:string, Plant:string, requestBody:Erp_Tablesets_PlantConfCtrlRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")", {
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
   Summary: Call UpdateExt to delete PlantConfCtrl item
   Description: Call UpdateExt to delete PlantConfCtrl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantConfCtrl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlantConfCtrls_Company_Plant(Company:string, Plant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")", {
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
   Description: Get PlantConfCtrlEGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantConfCtrlEGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfCtrlEGLCRow
   */  
export function get_PlantConfCtrls_Company_Plant_PlantConfCtrlEGLCs(Company:string, Plant:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlEGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantConfCtrlEGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlEGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlantConfCtrlEGLC item
   Description: Calls GetByID to retrieve the PlantConfCtrlEGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfCtrlEGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantConfCtrlEGLCRow
   */  
export function get_PlantConfCtrls_Company_Plant_PlantConfCtrlEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, Plant:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantConfCtrlEGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantConfCtrlEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
         resolve(data as Erp_Tablesets_PlantConfCtrlEGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PlantConfABCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantConfABCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfABCRow
   */  
export function get_PlantConfCtrls_Company_Plant_PlantConfABCs(Company:string, Plant:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfABCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantConfABCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfABCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlantConfABC item
   Description: Calls GetByID to retrieve the PlantConfABC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfABC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ABCCode Desc: ABCCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantConfABCRow
   */  
export function get_PlantConfCtrls_Company_Plant_PlantConfABCs_Company_Plant_ABCCode(Company:string, Plant:string, ABCCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantConfABCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantConfABCs(" + Company + "," + Plant + "," + ABCCode + ")", {
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
         resolve(data as Erp_Tablesets_PlantConfABCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PlantMFBills items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantMFBills1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantMFBillRow
   */  
export function get_PlantConfCtrls_Company_Plant_PlantMFBills(Company:string, Plant:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantMFBillRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantMFBills", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantMFBillRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlantMFBill item
   Description: Calls GetByID to retrieve the PlantMFBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantMFBill1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PayBTFlag Desc: PayBTFlag   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantMFBillRow
   */  
export function get_PlantConfCtrls_Company_Plant_PlantMFBills_Company_Plant_PayBTFlag(Company:string, Plant:string, PayBTFlag:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantMFBillRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantMFBills(" + Company + "," + Plant + "," + PayBTFlag + ")", {
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
         resolve(data as Erp_Tablesets_PlantMFBillRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PlantShareds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantShareds1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantSharedRow
   */  
export function get_PlantConfCtrls_Company_Plant_PlantShareds(Company:string, Plant:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantSharedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantShareds", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantSharedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlantShared item
   Description: Calls GetByID to retrieve the PlantShared item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantShared1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantSharedRow
   */  
export function get_PlantConfCtrls_Company_Plant_PlantShareds_Company_WarehouseCode_Plant(Company:string, Plant:string, WarehouseCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantSharedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantShareds(" + Company + "," + WarehouseCode + "," + Plant + ")", {
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
         resolve(data as Erp_Tablesets_PlantSharedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PlntTranDefs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlntTranDefs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlntTranDefRow
   */  
export function get_PlantConfCtrls_Company_Plant_PlntTranDefs(Company:string, Plant:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlntTranDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlntTranDefs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlntTranDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlntTranDef item
   Description: Calls GetByID to retrieve the PlntTranDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlntTranDef1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param FromPlant Desc: FromPlant   Required: True   Allow empty value : True
      @param ToPlant Desc: ToPlant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlntTranDefRow
   */  
export function get_PlantConfCtrls_Company_Plant_PlntTranDefs_Company_FromPlant_ToPlant(Company:string, Plant:string, FromPlant:string, ToPlant:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlntTranDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlntTranDefs(" + Company + "," + FromPlant + "," + ToPlant + ")", {
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
         resolve(data as Erp_Tablesets_PlntTranDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PltUPSEmails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PltUPSEmails1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PltUPSEmailRow
   */  
export function get_PlantConfCtrls_Company_Plant_PltUPSEmails(Company:string, Plant:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PltUPSEmailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PltUPSEmails", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PltUPSEmailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PltUPSEmail item
   Description: Calls GetByID to retrieve the PltUPSEmail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PltUPSEmail1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PltUPSEmailRow
   */  
export function get_PlantConfCtrls_Company_Plant_PltUPSEmails_Company_Plant_UPSQVSeq(Company:string, Plant:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PltUPSEmailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PltUPSEmails(" + Company + "," + Plant + "," + UPSQVSeq + ")", {
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
         resolve(data as Erp_Tablesets_PltUPSEmailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PlantConfCtrlAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PlantConfCtrlAttches1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfCtrlAttchRow
   */  
export function get_PlantConfCtrls_Company_Plant_PlantConfCtrlAttches(Company:string, Plant:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantConfCtrlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PlantConfCtrlAttch item
   Description: Calls GetByID to retrieve the PlantConfCtrlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfCtrlAttch1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantConfCtrlAttchRow
   */  
export function get_PlantConfCtrls_Company_Plant_PlantConfCtrlAttches_Company_Plant_DrawingSeq(Company:string, Plant:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantConfCtrlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrls(" + Company + "," + Plant + ")/PlantConfCtrlAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_PlantConfCtrlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get PlantConfCtrlEGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantConfCtrlEGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfCtrlEGLCRow
   */  
export function get_PlantConfCtrlEGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlEGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlEGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlEGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantConfCtrlEGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlEGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PlantConfCtrlEGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantConfCtrlEGLCs(requestBody:Erp_Tablesets_PlantConfCtrlEGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlEGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PlantConfCtrlEGLC item
   Description: Calls GetByID to retrieve the PlantConfCtrlEGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfCtrlEGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantConfCtrlEGLCRow
   */  
export function get_PlantConfCtrlEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantConfCtrlEGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
         resolve(data as Erp_Tablesets_PlantConfCtrlEGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlantConfCtrlEGLC for the service
   Description: Calls UpdateExt to update PlantConfCtrlEGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantConfCtrlEGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlEGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlantConfCtrlEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, requestBody:Erp_Tablesets_PlantConfCtrlEGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Summary: Call UpdateExt to delete PlantConfCtrlEGLC item
   Description: Call UpdateExt to delete PlantConfCtrlEGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantConfCtrlEGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlantConfCtrlEGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlEGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get PlantConfABCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantConfABCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfABCRow
   */  
export function get_PlantConfABCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfABCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfABCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfABCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantConfABCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantConfABCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PlantConfABCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantConfABCs(requestBody:Erp_Tablesets_PlantConfABCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfABCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PlantConfABC item
   Description: Calls GetByID to retrieve the PlantConfABC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfABC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ABCCode Desc: ABCCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantConfABCRow
   */  
export function get_PlantConfABCs_Company_Plant_ABCCode(Company:string, Plant:string, ABCCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantConfABCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfABCs(" + Company + "," + Plant + "," + ABCCode + ")", {
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
         resolve(data as Erp_Tablesets_PlantConfABCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlantConfABC for the service
   Description: Calls UpdateExt to update PlantConfABC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantConfABC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ABCCode Desc: ABCCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantConfABCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlantConfABCs_Company_Plant_ABCCode(Company:string, Plant:string, ABCCode:string, requestBody:Erp_Tablesets_PlantConfABCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfABCs(" + Company + "," + Plant + "," + ABCCode + ")", {
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
   Summary: Call UpdateExt to delete PlantConfABC item
   Description: Call UpdateExt to delete PlantConfABC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantConfABC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ABCCode Desc: ABCCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlantConfABCs_Company_Plant_ABCCode(Company:string, Plant:string, ABCCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfABCs(" + Company + "," + Plant + "," + ABCCode + ")", {
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
   Description: Get PlantMFBills items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantMFBills
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantMFBillRow
   */  
export function get_PlantMFBills(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantMFBillRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantMFBills", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantMFBillRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantMFBills
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantMFBillRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PlantMFBillRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantMFBills(requestBody:Erp_Tablesets_PlantMFBillRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantMFBills", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PlantMFBill item
   Description: Calls GetByID to retrieve the PlantMFBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantMFBill
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PayBTFlag Desc: PayBTFlag   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantMFBillRow
   */  
export function get_PlantMFBills_Company_Plant_PayBTFlag(Company:string, Plant:string, PayBTFlag:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantMFBillRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantMFBills(" + Company + "," + Plant + "," + PayBTFlag + ")", {
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
         resolve(data as Erp_Tablesets_PlantMFBillRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlantMFBill for the service
   Description: Calls UpdateExt to update PlantMFBill. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantMFBill
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PayBTFlag Desc: PayBTFlag   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantMFBillRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlantMFBills_Company_Plant_PayBTFlag(Company:string, Plant:string, PayBTFlag:string, requestBody:Erp_Tablesets_PlantMFBillRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantMFBills(" + Company + "," + Plant + "," + PayBTFlag + ")", {
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
   Summary: Call UpdateExt to delete PlantMFBill item
   Description: Call UpdateExt to delete PlantMFBill item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantMFBill
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PayBTFlag Desc: PayBTFlag   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlantMFBills_Company_Plant_PayBTFlag(Company:string, Plant:string, PayBTFlag:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantMFBills(" + Company + "," + Plant + "," + PayBTFlag + ")", {
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
   Description: Get PlantShareds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantShareds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantSharedRow
   */  
export function get_PlantShareds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantSharedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantShareds", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantSharedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantShareds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantSharedRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PlantSharedRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantShareds(requestBody:Erp_Tablesets_PlantSharedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantShareds", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PlantShared item
   Description: Calls GetByID to retrieve the PlantShared item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantShared
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantSharedRow
   */  
export function get_PlantShareds_Company_WarehouseCode_Plant(Company:string, WarehouseCode:string, Plant:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantSharedRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantShareds(" + Company + "," + WarehouseCode + "," + Plant + ")", {
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
         resolve(data as Erp_Tablesets_PlantSharedRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlantShared for the service
   Description: Calls UpdateExt to update PlantShared. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantShared
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantSharedRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlantShareds_Company_WarehouseCode_Plant(Company:string, WarehouseCode:string, Plant:string, requestBody:Erp_Tablesets_PlantSharedRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantShareds(" + Company + "," + WarehouseCode + "," + Plant + ")", {
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
   Summary: Call UpdateExt to delete PlantShared item
   Description: Call UpdateExt to delete PlantShared item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantShared
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param WarehouseCode Desc: WarehouseCode   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlantShareds_Company_WarehouseCode_Plant(Company:string, WarehouseCode:string, Plant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantShareds(" + Company + "," + WarehouseCode + "," + Plant + ")", {
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
   Description: Get PlntTranDefs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlntTranDefs
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlntTranDefRow
   */  
export function get_PlntTranDefs(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlntTranDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlntTranDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlntTranDefs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlntTranDefRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PlntTranDefRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlntTranDefs(requestBody:Erp_Tablesets_PlntTranDefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PlntTranDef item
   Description: Calls GetByID to retrieve the PlntTranDef item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlntTranDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FromPlant Desc: FromPlant   Required: True   Allow empty value : True
      @param ToPlant Desc: ToPlant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlntTranDefRow
   */  
export function get_PlntTranDefs_Company_FromPlant_ToPlant(Company:string, FromPlant:string, ToPlant:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlntTranDefRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs(" + Company + "," + FromPlant + "," + ToPlant + ")", {
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
         resolve(data as Erp_Tablesets_PlntTranDefRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlntTranDef for the service
   Description: Calls UpdateExt to update PlntTranDef. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlntTranDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FromPlant Desc: FromPlant   Required: True   Allow empty value : True
      @param ToPlant Desc: ToPlant   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlntTranDefRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlntTranDefs_Company_FromPlant_ToPlant(Company:string, FromPlant:string, ToPlant:string, requestBody:Erp_Tablesets_PlntTranDefRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs(" + Company + "," + FromPlant + "," + ToPlant + ")", {
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
   Summary: Call UpdateExt to delete PlntTranDef item
   Description: Call UpdateExt to delete PlntTranDef item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlntTranDef
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FromPlant Desc: FromPlant   Required: True   Allow empty value : True
      @param ToPlant Desc: ToPlant   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlntTranDefs_Company_FromPlant_ToPlant(Company:string, FromPlant:string, ToPlant:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs(" + Company + "," + FromPlant + "," + ToPlant + ")", {
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
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FromPlant Desc: FromPlant   Required: True   Allow empty value : True
      @param ToPlant Desc: ToPlant   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_PlntTranDefs_Company_FromPlant_ToPlant_EntityGLCs(Company:string, FromPlant:string, ToPlant:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs(" + Company + "," + FromPlant + "," + ToPlant + ")/EntityGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param FromPlant Desc: FromPlant   Required: True   Allow empty value : True
      @param ToPlant Desc: ToPlant   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_PlntTranDefs_Company_FromPlant_ToPlant_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, FromPlant:string, ToPlant:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlntTranDefs(" + Company + "," + FromPlant + "," + ToPlant + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/EntityGLCs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EntityGLCs(requestBody:Erp_Tablesets_EntityGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/EntityGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EntityGLCRow
   */  
export function get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
         resolve(data as Erp_Tablesets_EntityGLCRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, requestBody:Erp_Tablesets_EntityGLCRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RelatedToFile Desc: RelatedToFile   Required: True   Allow empty value : True
      @param Key1 Desc: Key1   Required: True   Allow empty value : True
      @param Key2 Desc: Key2   Required: True   Allow empty value : True
      @param Key3 Desc: Key3   Required: True   Allow empty value : True
      @param Key4 Desc: Key4   Required: True   Allow empty value : True
      @param Key5 Desc: Key5   Required: True   Allow empty value : True
      @param Key6 Desc: Key6   Required: True   Allow empty value : True
      @param GLControlType Desc: GLControlType   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get PltUPSEmails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PltUPSEmails
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PltUPSEmailRow
   */  
export function get_PltUPSEmails(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PltUPSEmailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PltUPSEmails", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PltUPSEmailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PltUPSEmails
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PltUPSEmailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PltUPSEmailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PltUPSEmails(requestBody:Erp_Tablesets_PltUPSEmailRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PltUPSEmails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PltUPSEmail item
   Description: Calls GetByID to retrieve the PltUPSEmail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PltUPSEmail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PltUPSEmailRow
   */  
export function get_PltUPSEmails_Company_Plant_UPSQVSeq(Company:string, Plant:string, UPSQVSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PltUPSEmailRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PltUPSEmails(" + Company + "," + Plant + "," + UPSQVSeq + ")", {
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
         resolve(data as Erp_Tablesets_PltUPSEmailRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PltUPSEmail for the service
   Description: Calls UpdateExt to update PltUPSEmail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PltUPSEmail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PltUPSEmailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PltUPSEmails_Company_Plant_UPSQVSeq(Company:string, Plant:string, UPSQVSeq:string, requestBody:Erp_Tablesets_PltUPSEmailRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PltUPSEmails(" + Company + "," + Plant + "," + UPSQVSeq + ")", {
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
   Summary: Call UpdateExt to delete PltUPSEmail item
   Description: Call UpdateExt to delete PltUPSEmail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PltUPSEmail
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param UPSQVSeq Desc: UPSQVSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PltUPSEmails_Company_Plant_UPSQVSeq(Company:string, Plant:string, UPSQVSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PltUPSEmails(" + Company + "," + Plant + "," + UPSQVSeq + ")", {
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
   Description: Get PlantConfCtrlAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PlantConfCtrlAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfCtrlAttchRow
   */  
export function get_PlantConfCtrlAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PlantConfCtrlAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PlantConfCtrlAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PlantConfCtrlAttches(requestBody:Erp_Tablesets_PlantConfCtrlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PlantConfCtrlAttch item
   Description: Calls GetByID to retrieve the PlantConfCtrlAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PlantConfCtrlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PlantConfCtrlAttchRow
   */  
export function get_PlantConfCtrlAttches_Company_Plant_DrawingSeq(Company:string, Plant:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PlantConfCtrlAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_PlantConfCtrlAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PlantConfCtrlAttch for the service
   Description: Calls UpdateExt to update PlantConfCtrlAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PlantConfCtrlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PlantConfCtrlAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PlantConfCtrlAttches_Company_Plant_DrawingSeq(Company:string, Plant:string, DrawingSeq:string, requestBody:Erp_Tablesets_PlantConfCtrlAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete PlantConfCtrlAttch item
   Description: Call UpdateExt to delete PlantConfCtrlAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PlantConfCtrlAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PlantConfCtrlAttches_Company_Plant_DrawingSeq(Company:string, Plant:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/PlantConfCtrlAttches(" + Company + "," + Plant + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PlantConfCtrlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePlantConfCtrl:string, whereClausePlantConfCtrlAttch:string, whereClausePlantConfABC:string, whereClausePlantMFBill:string, whereClausePlantShared:string, whereClausePlntTranDef:string, whereClauseEntityGLC:string, whereClausePltUPSEmail:string, whereClausePlantConfCtrlEGLC:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePlantConfCtrl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlantConfCtrl=" + whereClausePlantConfCtrl
   }
   if(typeof whereClausePlantConfCtrlAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlantConfCtrlAttch=" + whereClausePlantConfCtrlAttch
   }
   if(typeof whereClausePlantConfABC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlantConfABC=" + whereClausePlantConfABC
   }
   if(typeof whereClausePlantMFBill!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlantMFBill=" + whereClausePlantMFBill
   }
   if(typeof whereClausePlantShared!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlantShared=" + whereClausePlantShared
   }
   if(typeof whereClausePlntTranDef!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlntTranDef=" + whereClausePlntTranDef
   }
   if(typeof whereClauseEntityGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEntityGLC=" + whereClauseEntityGLC
   }
   if(typeof whereClausePltUPSEmail!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePltUPSEmail=" + whereClausePltUPSEmail
   }
   if(typeof whereClausePlantConfCtrlEGLC!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePlantConfCtrlEGLC=" + whereClausePlantConfCtrlEGLC
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetRows" + params, {
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
export function get_GetByID(plant:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof plant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plant=" + plant
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetList" + params, {
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
   Summary: Invoke method CustomGetNewPlantShared
   Description: Logic for new PlantShared
   OperationID: CustomGetNewPlantShared
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CustomGetNewPlantShared_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomGetNewPlantShared_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomGetNewPlantShared(requestBody:CustomGetNewPlantShared_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CustomGetNewPlantShared_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/CustomGetNewPlantShared", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CustomGetNewPlantShared_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckApprovalDefaults
   Description: Checks if a workflow group already exists for any of the selected options.
If yes, returns a message asking if the defaults should be rebuilt
   OperationID: CheckApprovalDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckApprovalDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckApprovalDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckApprovalDefaults(requestBody:CheckApprovalDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckApprovalDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/CheckApprovalDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckApprovalDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateApprovalDefaults
   Description: Creates default records needed for time and expense approvals.
   OperationID: CreateApprovalDefaults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateApprovalDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateApprovalDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateApprovalDefaults(requestBody:CreateApprovalDefaults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateApprovalDefaults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/CreateApprovalDefaults", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CreateApprovalDefaults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCompleteList
   Description: This method is the same as GetList(), except that it causes a bypass of the call to
removeUnauthorizedRows.  It is to be used only in the situations where the
user is allowed to see Plants for which they are not authorized, such as in
this example from Vantage Help for Multi-Plant Management:
The selection list for Plants will include all Plants for the To option
when creating Plant to Plant transfers. However, when receiving a Plant
to Plant transfer the user must be authorized to the receiving Plant.
   OperationID: GetCompleteList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCompleteList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCompleteList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCompleteList(requestBody:GetCompleteList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCompleteList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetCompleteList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetCompleteList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDfltApprTasksParam
   Description: Creates a record in the DfltApprTasksParams DataSet so the user can choose
what default tasks are created
   OperationID: GetDfltApprTasksParam
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDfltApprTasksParam_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDfltApprTasksParam(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDfltApprTasksParam_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetDfltApprTasksParam", {
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
         resolve(data as GetDfltApprTasksParam_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDisabledFields
   Description: This method will send a list of fields to be disabled on the UI
side if either the Multi-Plant or Advanced Planning and Scheduling
license is not available or MRP, data collection and field service.
   OperationID: GetDisabledFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDisabledFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDisabledFields(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDisabledFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetDisabledFields", {
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
         resolve(data as GetDisabledFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsAuthorizedForPlant
   Description: IsAuthorizedForPlant
   OperationID: IsAuthorizedForPlant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsAuthorizedForPlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsAuthorizedForPlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsAuthorizedForPlant(requestBody:IsAuthorizedForPlant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsAuthorizedForPlant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/IsAuthorizedForPlant", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as IsAuthorizedForPlant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfAbcCode
   Description: Purpose:
Parameters:  none
Notes:
<param name="ds">PlantConf data set </param><param name="ipABCCode">Plant ABC code</param>
   OperationID: OnChangeOfAbcCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfAbcCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfAbcCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfAbcCode(requestBody:OnChangeOfAbcCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfAbcCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeOfAbcCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfAbcCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfCCProdCal
   Description: This method validates CCProdCal
   OperationID: OnChangeOfCCProdCal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfCCProdCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfCCProdCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfCCProdCal(requestBody:OnChangeOfCCProdCal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfCCProdCal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeOfCCProdCal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfCCProdCal_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfExpenseApprovalReqd
   Description: This method resets default values when ExpenseApprovalReqd changes
   OperationID: OnChangeOfExpenseApprovalReqd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfExpenseApprovalReqd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfExpenseApprovalReqd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfExpenseApprovalReqd(requestBody:OnChangeOfExpenseApprovalReqd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfExpenseApprovalReqd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeOfExpenseApprovalReqd", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfExpenseApprovalReqd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfExpenseRestrictEntry
   Description: This method resets default values when ExpenseRestrictEntry changes
   OperationID: OnChangeOfExpenseRestrictEntry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfExpenseRestrictEntry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfExpenseRestrictEntry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfExpenseRestrictEntry(requestBody:OnChangeOfExpenseRestrictEntry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfExpenseRestrictEntry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeOfExpenseRestrictEntry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfExpenseRestrictEntry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfLowLvlSerialTrk
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipLLSerTrk">PlantConfCtrl.LowLvlSerialTrk</param><param name="ds">The Plant data set </param>
   OperationID: OnChangeOfLowLvlSerialTrk
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfLowLvlSerialTrk_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLowLvlSerialTrk_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfLowLvlSerialTrk(requestBody:OnChangeOfLowLvlSerialTrk_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfLowLvlSerialTrk_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeOfLowLvlSerialTrk", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfLowLvlSerialTrk_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfMaintTmpJobNum
   Description: This method should be called when Equip.TemplateJobNum changes.
   OperationID: OnChangeOfMaintTmpJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfMaintTmpJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfMaintTmpJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfMaintTmpJobNum(requestBody:OnChangeOfMaintTmpJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfMaintTmpJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeOfMaintTmpJobNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfMaintTmpJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfPcntTolerance
   OperationID: OnChangeOfPcntTolerance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfPcntTolerance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfPcntTolerance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfPcntTolerance(requestBody:OnChangeOfPcntTolerance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfPcntTolerance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeOfPcntTolerance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfPcntTolerance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfQtyTolerance
   OperationID: OnChangeOfQtyTolerance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfQtyTolerance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfQtyTolerance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfQtyTolerance(requestBody:OnChangeOfQtyTolerance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfQtyTolerance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeOfQtyTolerance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfQtyTolerance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeEnablePartAllocQueue
   Description: Invoked when any of the EnablePartAllocQueue flags are changed.
   OperationID: OnChangeEnablePartAllocQueue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeEnablePartAllocQueue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEnablePartAllocQueue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeEnablePartAllocQueue(requestBody:OnChangeEnablePartAllocQueue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeEnablePartAllocQueue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeEnablePartAllocQueue", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeEnablePartAllocQueue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfSerialTracking
   Description: This method validates SerialTracking
   OperationID: OnChangeOfSerialTracking
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfSerialTracking_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfSerialTracking_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfSerialTracking(requestBody:OnChangeOfSerialTracking_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfSerialTracking_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeOfSerialTracking", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfSerialTracking_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfStockValPcnt
   Description: Purpose:
Parameters:  none
Notes:
/// <param name="ipStockValPcnt">Stock Value Percent</param>
   OperationID: OnChangeOfStockValPcnt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfStockValPcnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfStockValPcnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfStockValPcnt(requestBody:OnChangeOfStockValPcnt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfStockValPcnt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeOfStockValPcnt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfStockValPcnt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfTimeApprovalReqd
   Description: This method resets default values when TimeApprovalReqd changes
   OperationID: OnChangeOfTimeApprovalReqd
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfTimeApprovalReqd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfTimeApprovalReqd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfTimeApprovalReqd(requestBody:OnChangeOfTimeApprovalReqd_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfTimeApprovalReqd_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeOfTimeApprovalReqd", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfTimeApprovalReqd_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfTimeRestrictEntry
   Description: This method resets default values when TimeRestrictEntry changes
   OperationID: OnChangeOfTimeRestrictEntry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfTimeRestrictEntry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfTimeRestrictEntry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfTimeRestrictEntry(requestBody:OnChangeOfTimeRestrictEntry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfTimeRestrictEntry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeOfTimeRestrictEntry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfTimeRestrictEntry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfValueTolerance
   Description: Purpose:
Parameters:  none
Notes:
/// <param name="ipValTolerance">Value of tolerance</param>
   OperationID: OnChangeOfValueTolerance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfValueTolerance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfValueTolerance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfValueTolerance(requestBody:OnChangeOfValueTolerance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfValueTolerance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangeOfValueTolerance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfValueTolerance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ResourceTransfer
   Description: Plant Resource Transfers allow you to create new plants from the resources available in current plants.
Once resources are moved to a new plant, they are no longer available in their previous plant.
   OperationID: ResourceTransfer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ResourceTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResourceTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ResourceTransfer(requestBody:ResourceTransfer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ResourceTransfer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/ResourceTransfer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ResourceTransfer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetUPSQVEnable
   Description: SetUPSQVEnable
   OperationID: SetUPSQVEnable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetUPSQVEnable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVEnable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetUPSQVEnable(requestBody:SetUPSQVEnable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetUPSQVEnable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/SetUPSQVEnable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetUPSQVEnable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePayBTFlag
   Description: ValidatePayBTFlag
   OperationID: ValidatePayBTFlag
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePayBTFlag_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePayBTFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePayBTFlag(requestBody:ValidatePayBTFlag_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePayBTFlag_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/ValidatePayBTFlag", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidatePayBTFlag_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetBinContractTypeWarehousesList
   Description: Return a generic dataset: datatable(string WarehouseCode, string WarehouseDescription)
List of warehouses with at least a bin of BinType = 'Cont'
   OperationID: GetBinContractTypeWarehousesList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetBinContractTypeWarehousesList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBinContractTypeWarehousesList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBinContractTypeWarehousesList(requestBody:GetBinContractTypeWarehousesList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBinContractTypeWarehousesList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetBinContractTypeWarehousesList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetBinContractTypeWarehousesList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCWarehouseCode
   Description: Validates PlantConfCtrl.DefPlanContractWhse column changing:
The WarehouseCode field should only allow warehouses with at least one bin location flagged as contract bin.
   OperationID: OnChangePCWarehouseCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCWarehouseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCWarehouseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCWarehouseCode(requestBody:OnChangePCWarehouseCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCWarehouseCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/OnChangePCWarehouseCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangePCWarehouseCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TestMachineMESODataConnection
   Description: Tests the connection to Mattec OData
   OperationID: TestMachineMESODataConnection
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/TestMachineMESODataConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestMachineMESODataConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestMachineMESODataConnection(requestBody:TestMachineMESODataConnection_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<TestMachineMESODataConnection_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/TestMachineMESODataConnection", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as TestMachineMESODataConnection_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPlantConfCtrl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantConfCtrl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPlantConfCtrl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantConfCtrl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlantConfCtrl(requestBody:GetNewPlantConfCtrl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPlantConfCtrl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetNewPlantConfCtrl", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPlantConfCtrl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPlantConfCtrlAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantConfCtrlAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPlantConfCtrlAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantConfCtrlAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlantConfCtrlAttch(requestBody:GetNewPlantConfCtrlAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPlantConfCtrlAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetNewPlantConfCtrlAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPlantConfCtrlAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPlantConfABC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantConfABC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPlantConfABC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantConfABC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlantConfABC(requestBody:GetNewPlantConfABC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPlantConfABC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetNewPlantConfABC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPlantConfABC_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPlantMFBill
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantMFBill
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPlantMFBill_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantMFBill_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlantMFBill(requestBody:GetNewPlantMFBill_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPlantMFBill_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetNewPlantMFBill", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPlantMFBill_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPlantShared
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantShared
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPlantShared_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantShared_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlantShared(requestBody:GetNewPlantShared_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPlantShared_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetNewPlantShared", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPlantShared_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPlntTranDef
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlntTranDef
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPlntTranDef_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlntTranDef_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlntTranDef(requestBody:GetNewPlntTranDef_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPlntTranDef_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetNewPlntTranDef", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPlntTranDef_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEntityGLC(requestBody:GetNewEntityGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewEntityGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetNewEntityGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewEntityGLC_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPltUPSEmail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPltUPSEmail
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPltUPSEmail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPltUPSEmail_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPltUPSEmail(requestBody:GetNewPltUPSEmail_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPltUPSEmail_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetNewPltUPSEmail", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPltUPSEmail_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPlantConfCtrlEGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPlantConfCtrlEGLC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPlantConfCtrlEGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPlantConfCtrlEGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPlantConfCtrlEGLC(requestBody:GetNewPlantConfCtrlEGLC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPlantConfCtrlEGLC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetNewPlantConfCtrlEGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPlantConfCtrlEGLC_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PlantConfCtrlSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EntityGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfABCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantConfABCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantConfCtrlAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlEGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantConfCtrlEGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantConfCtrlListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantConfCtrlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantConfCtrlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantMFBillRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantMFBillRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlantSharedRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlantSharedRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PlntTranDefRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PlntTranDefRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PltUPSEmailRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PltUPSEmailRow,
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Identifier of the GL Control Type.  */  
   "GLControlType":string,
      /**  GL Control Identifier.  */  
   "GLControlCode":string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   "BusinessEntity":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   "GlobalEntityGLC":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  BankAcctID of the related BankAcct record.  */  
   "BankAcctID":string,
   "BankFeeID":string,
      /**  CallCode of the related FSCallCd record.  */  
   "CallCode":string,
   "ChargeCode":string,
      /**  ClassCode of the related FAClass record.  */  
   "ClassCode":string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   "ClassID":string,
      /**  ContractCode of the related FSContCd record.  */  
   "ContractCode":string,
      /**  CurrencyCode of the related Currency record.  */  
   "CurrencyCode":string,
      /**  CustNum of the related Customer record  */  
   "CustNum":number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   "DeductionID":string,
      /**  EmpID of the related PREmpMas record.  */  
   "EmpID":string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   "ExpenseCode":string,
      /**  ExtSystemID of ExtCompany table  */  
   "ExtSystemID":string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   "FromPlant":string,
      /**  GroupCode of the related FAGroup record.  */  
   "GroupCode":string,
   "GroupID":string,
   "HeadNum":number,
   "InvoiceNum":string,
      /**  JCDept of the related JCDept record.  */  
   "JCDept":string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   "MiscCode":string,
      /**  PartNum of the related Part record.  */  
   "PartNum":string,
      /**  PayTypeID of PayType  */  
   "PayTypeID":string,
   "PerConName":string,
      /**  PI Status  */  
   "PIStatus":string,
      /**  Plant of the related PlantConfCtrl record.  */  
   "Plant":string,
      /**  ProdCode of the related ProdGrup record.  */  
   "ProdCode":string,
      /**  ProjectID of the related Project record.  */  
   "ProjectID":string,
      /**  PurchCode of the related GLPurch record.  */  
   "PurchCode":string,
      /**  RateCode of the related GLRate record.  */  
   "RateCode":string,
      /**  ReasonCode of the related Reason record.  */  
   "ReasonCode":string,
      /**  ReasonType of the related Reason record.  */  
   "ReasonType":string,
      /**  SalesCatID of the related SalesCat record.  */  
   "SalesCatID":string,
      /**  Shift value of the related JCShift record.  */  
   "Shift":number,
      /**  TaxCode of the related SalesTax record.  */  
   "TaxCode":string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   "TaxTblID":string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   "ToPlant":string,
      /**  TransferMethod of ExtCompany table  */  
   "TransferMethod":string,
      /**  Type ID  */  
   "TypeID":string,
      /**  VendorNum of the related Vendor record.  */  
   "VendorNum":number,
      /**  WarehouseCode of the related Warehse record.  */  
   "WarehouseCode":string,
   "ExpenseTypeCode":string,
   "IsFiltered":boolean,
   "OprTypeCode":string,
   "CashDeskID":string,
   "TIN":string,
   "ReclassCodeID":string,
   "BitFlag":number,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlantConfABCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  ABC Code.  Valid values are "A" through "Z".  */  
   "ABCCode":string,
      /**  This flag indicates whether the CountFreq defined in this record should over ride the count frequency in the AbcCode table.  */  
   "OvrrideCountFreq":boolean,
      /**  This setting can be overrides AbcCode.CountFreq and can be overridden in WarehseABC.  */  
   "CountFreq":number,
      /**  This flag is set to true prevent items that should only be counted during physical inventory from being selected for cycle counting. This setting can be overridden in WarehseABC.  */  
   "ExcludeFromCC":boolean,
      /**  Stock Valuation Percent. Used by Calculate ABC Codes to determine what ABC code to assign to a part/warehouse record. This setting can be overridden in WarehseABC.  */  
   "StockValPcnt":number,
      /**  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse, PartSite, or WarehseABC. Zero indicates that any quantity variance is considered out of tolerance  */  
   "PcntTolerance":number,
      /**  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this ABC code and the value in PcntTolerance will be used to determine if the count variance is within tolerance.  */  
   "CalcPcnt":boolean,
      /**  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this ABC code and the value in QtyTolerance will be used to determine if the count variance is within tolerance.  */  
   "CalcQty":boolean,
      /**  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this ABC code and the value in ValueTolerance will be used to determine if the count variance is within tolerance.  */  
   "CalcValue":boolean,
      /**  This flag indicates whether the StockValPcnt defined in this record should over ride the count frequency in the AbcCode table.  */  
   "OvrrideStockValPcnt":boolean,
      /**  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse, PartSite, or WarehseABC. Zero indicates that any quantity variance is considered out of  */  
   "QtyTolerance":number,
      /**  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, or WarehseABC.  An entry of zero will indicate that any value variance will be considered out  */  
   "ValueTolerance":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlantConfCtrlAttchRow{
   "Company":string,
   "Plant":string,
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

export interface Erp_Tablesets_PlantConfCtrlEGLCRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   "RelatedToFile":string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   "Key1":string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   "Key2":string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key3":string,
      /**   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key4":string,
      /**   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key5":string,
      /**   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
   "Key6":string,
      /**  Identifier of the GL Control Type.  */  
   "GLControlType":string,
      /**  GL Control Identifier.  */  
   "GLControlCode":string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   "BusinessEntity":string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   "ExtCompanyID":string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   "IsExternalCompany":boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   "GlobalEntityGLC":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Plant for PlantConfCtrl  */  
   "Plant":string,
   "BitFlag":number,
   "GLCntrlDescription":string,
   "GLCntrlTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlantConfCtrlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  The Site name.  */  
   "Name":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlantConfCtrlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  The Site name.  */  
   "Name":string,
      /**  Warehse.WarehouseCode of the warehouse selected as the default warehouse for this Site.  */  
   "DefaultWhse":string,
      /**  System date on which the last MRP processing was run.  */  
   "MRPLastRunDate":string,
      /**  System Time (hr-min-sec) when the last MRP process was run.  */  
   "MRPLastRunTime":number,
      /**  Warehse.WarehouseCode of the warehouse selected as the default inspection warehouse for this Site.  */  
   "DefInspWhse":string,
      /**  Indicates if Labor Collection should calculate Idle time.  Idle time is the time that the employee is getting paid for but is not doing any direct or Indirect labor activity.  The Labor Collection will automatically generate an Indirect detail record to capture these hours if this flag is set to "Yes".  If this is "yes" then the IdleIndirectCode and IdleWCCode must be entered and valid.  */  
   "CalcIdleTime":boolean,
      /**  The ResourceGrpID used by labor collection to create the LaborDtl entry for idle time when CalcIdleTime = Yes. For production labor (LaborType = "S" or "P") the default is from the JobOpDtl.ResourceGrpId from the primary JobOpDtl.  For indirect labor (LaborType = I) there is no default.  */  
   "IdleResourceGrpID":string,
      /**  The indirect labor code (Indirect.IndirectCode) that Labor Collection will use when it creates the Idle Time detail record in LaborDtl.  This must be valid if the CalcIdleTime = Yes.  */  
   "IndirectCode":string,
      /**  The number of hours (+-) difference from the server time zone to the Site time zone.  Data collection transactions will be offset by this amount.  */  
   "TimeZoneOffset":number,
      /**  Related to TimeZoneOffset. Calculated from users entry in TimeZoneOffset, the number of seconds (+-) difference from the server time zone to the Site time zone.   Used for clock in clock out in data collection.  */  
   "TimeOffsetSec":number,
      /**  This is the job number prefix that MRP uses when generating an unfirm job. Two Sites of the same company cannot have the same prefix.  */  
   "UnfirmJobPrefix":string,
      /**  This is the job number prefix that for firm jobs.  */  
   "FirmJobPrefix":string,
      /**  Default receiving warehouse. Used as default in receipt entry.  */  
   "DefRcvWhse":string,
      /**  Default receiving bin Used as default in receipt entry.  */  
   "DefRcvBin":string,
      /**  Default shipping warehouse. Used as default in shipment entry.  */  
   "DefShipWhse":string,
      /**  Default shipping bin. Used as default in shipping entry.  */  
   "DefShipBin":string,
      /**  KanBan Prefix  */  
   "KanBanPrefix":string,
      /**  This is the job number prefix that MRP uses when generating an unfirm transfer order. Two Sites of the same company cannot have the same prefix.  */  
   "MRPTOPrefix":string,
      /**  This is the job number prefix that Epicor ERP uses when generating a firm transfer order. Two Sites of the same company cannot have the same prefix.  */  
   "ManualTOPrefix":string,
      /**  Scheduled Date used in last MRP run  */  
   "MRPLastScheduledDate":string,
      /**  Cut Off Date used in last MRP run  */  
   "MRPLastCutOffDate":string,
      /**  Is this a residential delivery  */  
   "ResDelivery":boolean,
      /**  Is a Saturday delivery acceptable  */  
   "SatDelivery":boolean,
      /**  Is a Saturday pickup available  */  
   "SatPickup":boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   "Hazmat":boolean,
      /**  Documents Only delivery  */  
   "DocOnly":boolean,
      /**  Reference Notes for the delivery  */  
   "RefNotes":string,
      /**  Apply Handling Charge to shipment  */  
   "ApplyChrg":boolean,
      /**  Handling Charge Amount  */  
   "ChrgAmount":number,
      /**  Prefer COD delivery  */  
   "COD":boolean,
      /**  Add Freight COD Amount owed  */  
   "CODFreight":boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   "CODCheck":boolean,
      /**  Amount due on Cashier's check or money order  */  
   "CODAmount":number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   "GroundType":string,
      /**  Indicates whether to send an email notification of delivery  */  
   "NotifyFlag":boolean,
      /**  The list of email address to notify about a delivery  */  
   "NotifyEMail":string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   "DeclaredIns":boolean,
      /**  Declared Insurance Amount  */  
   "DeclaredAmt":number,
      /**  Default for JobHead.ProductionYield for this Site.  */  
   "ProductionYieldDefault":boolean,
      /**  Indicates whether the calculated production yield adjustment should be automatically applied.  */  
   "PrdYldAdjust":boolean,
      /**  Indicates whether an alert should be sent if the production yield calculation determines that an adjustment should be made. The alert will indicate if the adjustment has been made automatically or not (based on the setting of Site.PrdYieldAdjust). If the  */  
   "PrdYldAlert":boolean,
      /**  Service delivery requires signature  */  
   "ServSignature":boolean,
      /**  Service Priority Alert flag  */  
   "ServAlert":boolean,
      /**  Service Home Delivery allowed  */  
   "ServHomeDel":boolean,
      /**  Service Home Delivery Type Code  */  
   "DeliveryType":string,
      /**  Service Home Delivery date  */  
   "ServDeliveryDate":string,
      /**  Home delivery phone number  */  
   "ServPhone":string,
      /**  Service Delivery Instructions  */  
   "ServInstruct":string,
      /**  Service Signature release is on file  */  
   "ServRelease":boolean,
      /**  Service Signature Release authorization number  */  
   "ServAuthNum":string,
      /**  Service Reference 1  */  
   "ServRef1":string,
      /**  Service Reference 2  */  
   "ServRef2":string,
      /**  Service Reference 3  */  
   "ServRef3":string,
      /**  Service Reference 4  */  
   "ServRef4":string,
      /**  Service Reference 5  */  
   "ServRef5":string,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   "IndividualPackIDs":boolean,
      /**  Indicates if the shipment is international.  */  
   "IntrntlShip":boolean,
      /**  Certificates of Origin required flag. Used in manifesting.  */  
   "CertOfOrigin":boolean,
      /**  Commercial Invoice required flag. Used in manifesting.  */  
   "CommercialInvoice":boolean,
      /**  Ship Export Declaration required flag. Used in manifesting.  */  
   "ShipExprtDeclartn":boolean,
      /**  Letter of Instruction required. Used in manifesting.  */  
   "LetterOfInstr":boolean,
      /**  Freight Forwarder ID.  */  
   "FFID":string,
      /**  Freight Forwarder Company Name  */  
   "FFCompName":string,
      /**  Freight Forwarder first address line.  */  
   "FFContact":string,
      /**  Freight Forwarder second address line.  */  
   "FFAddress1":string,
      /**  Freight Forwarder third address line.  */  
   "FFAddress2":string,
      /**  Freight Forwarder city portion of address.  */  
   "FFAddress3":string,
      /**  Freight Forwarder state portion of address.  */  
   "FFCity":string,
      /**  Freight Forwarder postal code or zip code portion of address.  */  
   "FFState":string,
      /**  Freight Forwarder country portion of address.  */  
   "FFZip":string,
      /**  Non Standard Package flag. Used in manifesting.  */  
   "FFCountry":string,
      /**  Additional Handling flag. Used in manifesting.  */  
   "NonStdPkg":boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   "DeliveryConf":number,
      /**  Freight Forwarder country number portion of address.  */  
   "FFCountryNum":number,
      /**  Freight Forwarder phone Number.  */  
   "FFPhoneNum":string,
      /**  UPS Quantum View  */  
   "UPSQuantumView":boolean,
      /**  UPS Quantum View From Name  */  
   "UPSQVShipFromName":string,
      /**  UPS Quantum View Memo  */  
   "UPSQVMemo":string,
      /**  Default inspection bin. Used as default in inspection processing.  */  
   "DefInspBin":string,
      /**  Default DMR warehouse. Used as default in DMR processing.  */  
   "DefDMRWhse":string,
      /**  Default DMR bin. Used as default in DMR processing.  */  
   "DefDMRBin":string,
      /**   Indicates whether serial number entry will be required when inventory movement is bin-to-bin within the same warehouse. All other inventory movement will still require serial number entry. This flag is only used if Serial Tracking Option is set to Full Serial Trace.
Defaults to True.  */  
   "BinToBinReqSN":boolean,
      /**   Indicates the level of serial tracking for component items for the Site.
Defaults to 1.
Requires code/desc entry in object designer:
1 = No Lower Level Serial Tracking
2 = Full Lower Level Serial Tracking
3 = Outbound Serial Tracking Only.  */  
   "LowLvlSerialTrk":number,
      /**   Indicates the level of serial tracking for the Site.
Default value for new SiteConfigCtrl = 1.
Requires code/desc entry in object designer:
1 = No Serial Tracking
2 = Full Serial Tracking
3 = Outbound Serial Tracking Only.  */  
   "SerialTracking":number,
      /**   Controls the level of warnings that the user is given during job receipt processes for matching component serial numbers to the top level serial numbers.
Defaults to 1
Requires code/desc entry in object designer:
1 = No Warnings
2 = Warn but Allow Processing
3 = Warn and Do Not Allow Processing  */  
   "SerialMatchWarn":number,
      /**  The maximum number of transactions to be auto-selected by the Handheld Auto-Select Transactions function.  */  
   "HHAutoSelectTranMax":number,
      /**   Defines what method will be used to automatically select parts for cycle counting. This can be overridden in the Warehse table.
Default = 1.
Code/Desc:
1 = Repetitive, 2 = Random.  */  
   "CCSelectMethod":number,
      /**  Default Search Sort for Sales Order Fulfillment Workbench.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  */  
   "SearchSortOrder":string,
      /**  Default Search Sort for Job Fulfillment Workbench.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  */  
   "SearchSortJob":string,
      /**  Default Search Sort for Transfer Fulfillment Workbench.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  */  
   "SearchSortTransfer":string,
      /**  Default Priority for a Pick Transaction.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   "PriorityPick":number,
      /**  Default Priority for a Putaway Transaction.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   "PriorityPutaway":number,
      /**  Default Priority for a Bin To Bin Replenishment Transaction.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   "PriorityBinToBinReplenish":number,
      /**  Replenish By Quantity or Volume.  Valid values:  Q and V  */  
   "ReplenishBy":string,
      /**  Lock Orders on Pick?  */  
   "LockOrdersOnPick":boolean,
      /**  Sort Queue by Priority?  */  
   "SortQueueByPriority":boolean,
      /**  Warehse.WarehouseCode of the warehouse selected as the default warehouse for Job Allocation Picks in this Site.  */  
   "DefJobPickWhse":string,
      /**  Default Job Pick bin. Used as default in Job Allocation Picks.  */  
   "DefJobPickBin":string,
      /**  Warehse.WarehouseCode of the warehouse selected as the default warehouse for Transfer Order Allocation Picks in this Site.  */  
   "DefTFOrdPickWhse":string,
      /**  Default Transfer Order Pick bin. Used as default in Transfer Order Allocation Picks.  */  
   "DefTFOrdPickBin":string,
      /**  The Production Calendar to be used in the calculation of the schedules for Cycle Counting. If this field is left blank then the current Production Calendar defined on the Site.  */  
   "CCProdCal":string,
      /**   Default value for Fulfillment Workbench.  Qualifies the unit of measure of the NetWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new part records.
Having a NetWeightUOM will provides the ability to calculate total  weight.  */  
   "DefNetWeightUOM":string,
      /**   Default value for Fulfillment Workbench.  Qualifies the unit of measure of the NewVolume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  when creating new part records.
Having a Net Volume UOM will provides the ability to calculate total volume  */  
   "DefNetVolumeUOM":string,
      /**  The Job should automatically attempt to reserve inventory upon Release.  */  
   "JobReleaseAutoReserve":boolean,
      /**  System date on which the last Recycle Job processing was run.  */  
   "RecycleLastDate":string,
      /**  System Time (hr-min-sec) when the last Recycle Job process was run.  */  
   "RecycleLastTime":number,
      /**  By default this field will be false. Setting this to true will allow the loan logic to be enabled in Job Material Transfer Etnry.  */  
   "AllowJobMtlLoans":boolean,
      /**   This field will be disabled if the above field is false.
The combo box will have two options:
1.  Repay Material when All Materials Received (AllRecvd)
2.  Repay Material when sufficient has been Received (SuffRecvd)  */  
   "JobMtlRepayMethod":string,
      /**  Default Drop Shipping warehouse. Used as default in Drop Shipment processing.  */  
   "DefDSWhse":string,
      /**  Determines if time needs to be approved.  */  
   "TimeApprovalReqd":boolean,
      /**  Defines if time approver can add a time transaction.  */  
   "TimeApproverCanAdd":boolean,
      /**  Defines if time approver can delete a time transaction.  */  
   "TimeApproverCanDel":boolean,
      /**  Defines if time approver can update a time transaction.  */  
   "TimeApproverCanUpd":boolean,
      /**  Defines if the method for approving indirect time transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  */  
   "TimeIndirectLogic":string,
      /**  Defines if the method for approving production time transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  */  
   "TimeProductionLogic":string,
      /**  The default workflow group for Time transactions entered in this Site.  */  
   "TimeWFGroupID":string,
      /**  The default task set for Time transactions entered in this Site.  */  
   "TimeTaskSetID":string,
      /**  Determines if expenses need to be approved.  */  
   "ExpenseApprovalReqd":boolean,
      /**  Defines if expense approver can add an expense transaction.  */  
   "ExpenseApproverCanAdd":boolean,
      /**  Defines if expense approver can delete an expense transaction.  */  
   "ExpenseApproverCanDel":boolean,
      /**  Defines if expense approver can update an expense transaction.  */  
   "ExpenseApproverCanUpd":boolean,
      /**  Defines if the method for approving indirect expense transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  */  
   "ExpenseIndirectLogic":string,
      /**  Defines if the method for approving production expense transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  */  
   "ExpenseProductionLogic":string,
      /**  The default workflow group for Expense transactions entered in this Site.  */  
   "ExpenseWFGroupID":string,
      /**  The default task set for Expense transactions entered in this Site.  */  
   "ExpenseTaskSetID":string,
      /**  Determines if labor time needs to be approved.  */  
   "TimeMESApprovalReqd":boolean,
      /**  Indicates if the current user is restricted to entering time against employees where their username is set in the Employee record.  */  
   "TimeRestrictEntry":boolean,
      /**  Indicates if the current user is restricted to entering expenses against employees where their username is set in the Employee record.  */  
   "ExpenseRestrictEntry":boolean,
      /**  Used in Project Analysis to check if it should only include posted labor during the processing.  */  
   "OnlyPostedLabor":boolean,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   "MaintTmpJobNum":string,
      /**  Prefix that will be used when generating  Maintenance Job numbers for this Site.  Note: If blank, then system will use value defined at company level (see MMSyst.JobPrefix).  */  
   "MaintJobPrefix":string,
      /**  Indicates if the supervisor of an employee can maintain time transactions on behalf of the employee.  */  
   "TimeSuperCanMaintain":boolean,
      /**  Indicates if the supervisor of an employee can maintain expense transactions on behalf of the employee.  */  
   "ExpenseSuperCanMaintain":boolean,
      /**  This field determines how inventory allocations are enforced at the Site level.  */  
   "EnforceAllocations":string,
      /**  Defines if the method for approving advance request expense transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  */  
   "ExpenseAdvReqLogic":string,
      /**  Indicates if the new Expense Detail will be automatically submitted when saved.  */  
   "ExpenseAutoSubmit":boolean,
      /**  Indicates if the new Time Detail will be automatically submitted when saved.  */  
   "TimeAutoSubmit":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates the record is used with Machine MES  */  
   "ExternalMES":boolean,
      /**  The Machine MES Integration type  */  
   "ExternalMESType":string,
      /**  The Machine MES output file location  */  
   "ExternalMESRoute":string,
      /**  Allow Credit Hold Orders to be released for Picking  */  
   "AllowReleaseOfCreditHoldOrder":boolean,
      /**  This flag determies if partially reserved or allocated sales order releases can be Released for Picking.   If checked, then the "Ship Order Complete" and "Ship Line Complete" flags on the sales order are ignored when determining if a sales order releases can be Released for Picking.  */  
   "AllowReleaseOfPartialSalesOrder":boolean,
      /**  The Machine MES input file location  */  
   "ExternalMESInput":string,
      /**  Select this check box to disable the Pack Out sheet of Customer Shipment Entry  */  
   "DisablePackOut":boolean,
      /**  Suppress Sales Order make direct Job warning  */  
   "SuppressSOMakeDirWrn":boolean,
      /**  Unpack to Picked Status  */  
   "AssumePickedOrders":boolean,
      /**  Use Order or Shipping Warehouse/Bin  */  
   "DefOrdShipWhseBin":boolean,
      /**  Apply Burden to all operation Resources  */  
   "ApplyBurdenCost":boolean,
      /**  If the Purchase Contracts module is being used, specify how the related demand requirements should be handled for this site.  */  
   "PurchaseScheduleMode":string,
      /**  Include Completed Qtys/Hours in Send Ahead Calculations  */  
   "IncludeCompleteQtys":boolean,
      /**  Assign Material Dates (engineered, unengineered, scheduling)  */  
   "AssignMtlDates":string,
      /**  If you select this check box, the Setup is marked as Complete and load for Setup Hours is relieved when production for an operation is marked as Complete.  */  
   "AutoCompleteSetup":boolean,
      /**  Controls the action to be taken when part number of a Job Mtl is being changed and there is already an issued qty to the original part number.  */  
   "MtlIssuedAction":string,
      /**  Default Planning Contract Wharehouse. It is only allowed warehouses with at least one bin location flagged as contract bin.  */  
   "DefPlanContractWhse":string,
      /**  PartLeadTime's flag allows the user to trigger the CTP calculations to include the parts lead time and net out existing supply and demand for the part.  */  
   "PartLeadTime":boolean,
      /**  This flag controls which sales order releases can be processed by the Fulfillment Workbench.  If checked, then only those order releases where the associated OrderHed.ReadyToFulfill = true can be loaded into the workbench.  If not checked, then OrderHed.ReadyToFulfill is not considered when loading the workbench.  */  
   "ReadyToFulfillRequired":boolean,
      /**  Indicates if there is to be package control enforcement during Job Receipt to Inventory.  */  
   "EnforceJobRcptToInv":boolean,
      /**  The default package control employee for Time and Expense.  */  
   "TimeExpenseDefaultEmpID":string,
      /**  The package control supervisor override password.  */  
   "SupervisorOverridePassword":string,
      /**  Indicates if Package Control is enabled for this site.  */  
   "EnablePackageControl":boolean,
      /**  Identifies the default Reason Code for a repack.  */  
   "DefaultRepackReasonCode":string,
      /**  Default General bin. Used as default in receipt entry.  */  
   "DefGenBin":string,
      /**  This flag affects the job creation in CTP for a Make to Order release upon clicking the Confirm button. F = Create Firm Job, a Firm Job to Order  will be created. U = Create Unfirm Job, the CTP job (which by its nature of an unfirm status) will remain. N = No Job, the CTP job will be deleted and there will not be any job created but the calculated date will affect the order release date. Default value = “F”  */  
   "CTPJobCreateMTO":string,
      /**  This flag affects the job creation in CTP for a Make To Stock release upon clicking the Confirm button. F = Create Firm Job, a Firm Job to Stock will be created. U = Create Unfirm Job, the CTP job (which by its nature of an unfirm status) will remain. N = No Job, the CTP job will be deleted and there will not be any job created but the calculated date will affect the order release date. Default value = “F”  */  
   "CTPJobCreateMTS":string,
      /**  Maximum Number of PCIDs allowed to be created during the Generate PCID function in various UI’s  */  
   "MaxPCIDAllowedToCreate":number,
      /**  ConsumeReturnables  */  
   "ConsumeReturnables":string,
      /**  ConsumeExpendables  */  
   "ConsumeExpendables":string,
      /**  True if the Docking Station on the ShipDtl is a distinct value.  */  
   "IsDockingStationDistinct":boolean,
      /**  Use3rdPartySched  */  
   "Use3rdPartySched":boolean,
      /**  MtlQueueMaxRowsToReturn  */  
   "MtlQueueMaxRowsToReturn":number,
      /**  MtlQueueEndDaysOffset  */  
   "MtlQueueEndDaysOffset":number,
      /**  GenNewPCIDDelaySeconds  */  
   "GenNewPCIDDelaySeconds":number,
      /**  GenNewPCIDLimitDays  */  
   "GenNewPCIDLimitDays":number,
      /**  Logical field to indicate if the site configuration will allow to the Employee override HCM Payroll default  */  
   "CanEmployeeOverrideHCM":boolean,
      /**  List field the default payroll configuration for HCM Integration  */  
   "PayrollValuesForHCM":string,
      /**  Indicates whether Rate Shopping functionality is enabled for the site.  */  
   "ManifestRateShopping":boolean,
      /**  The URL of the Rate Shopping website for this site.  */  
   "ManifestRateShoppingURL":string,
      /**  Minimum Job Output Generate Interval. This value is in seconds. A value of 0 means no limit.  */  
   "MinJOGenerateInterval":number,
      /**  Maximum Job Output Reprint Window. This value is in minutes. A value of 0 means no limit.  */  
   "MaxJOReprintWindow":number,
      /**  Maximum Ad Hoc Job Output Job Window. This value is in days. A value of 0 means no limit.  */  
   "MaxAHJOJobWindow":number,
      /**  Maximum Partial PCID Job Window. This value is in days. A value of 0 means no limit.  */  
   "MaxPartialJobWindow":number,
      /**  Code used when generating Identificatin Numbers.  */  
   "SiteIDCode":string,
      /**  The flag in Site Configuration that allows to automatically void a PCID when it becomes empty  */  
   "VoidPCIDWhenEmpty":boolean,
      /**  When true, the allocation of inventory within a PCID will be allowed.  */  
   "AllowAllocationOfPCIDInventory":boolean,
      /**  False = Transfer Order shipping whs/bin will default to the From Site primary warehouse and bin for the part if defined, else use the From Site Default General Whse. True = shipping whs/bin will default to: PartAlloc whs/bin if an entry exists for TFOrdDtl, else use the TFOrdDtl Staging warehouse and bin.  */  
   "DefTOShipWhseBin":boolean,
      /**  The Machine MES OData URL  */  
   "ExternalMESODataURL":string,
      /**  The Machine MES OData username  */  
   "ExternalMESODataUsername":string,
      /**  The Machine MES OData password  */  
   "ExternalMESODataPassword":string,
      /**  Indicates if the fulfillment queue is available for sales orders.  */  
   "EnablePartAllocQueueOrder":boolean,
      /**  Indicates the PartAllocTemplate to use when allocating sales orders using automated fulfillment.  */  
   "AllocTemplateIDOrder":string,
      /**  If Log WIP Changes is set to true, changes to PartWip will be logged in PartWipTran.  Default is false.  Must have AMM to set this to true.  Once WIP Changes have been logged, they will remain indefinitely.  Use the Database Purge and Summarice to purge history that is no longer desired.  */  
   "LogWIPChanges":boolean,
      /**  Indicates if/when sales order releases should automatically be sent to the fulfillment queue.  */  
   "SendToPartAllocQueueOrder":string,
      /**  Indicates the PartAllocTemplate to use when allocating jobs using automated fulfillment.  */  
   "AllocTemplateIDJob":string,
      /**  Indicates the PartAllocTemplate to use when allocating transfer orders using automated fulfillment.  */  
   "AllocTemplateIDTransfer":string,
      /**  Indicates if the fulfillment queue is available for jobs.  */  
   "EnablePartAllocQueueJob":boolean,
      /**  Indicates if the fulfillment queue is available for transfer orders.  */  
   "EnablePartAllocQueueTransfer":boolean,
      /**  OpCompleteConsumeWIP  */  
   "OpCompleteConsumeWIP":boolean,
      /**  Indicates if/when job materials should automatically be sent to the fulfillment queue.  */  
   "SendToPartAllocQueueJob":string,
      /**  Indicates if/when transfer order lines should automatically be sent to the fulfillment queue.  */  
   "SendToPartAllocQueueTransfer":string,
      /**  If this field is true, it marks the selected site as Connected Process Control (CPC) as enabled. If disabled, connection and/or sync will not be done.  */  
   "ECPCEnabled":boolean,
      /**  Controls the action that is to be taken when job ship quantity is not in shipping location  */  
   "WIPShippingAction":string,
      /**  ShippingProdCal  */  
   "ShippingProdCal":string,
      /**  InvalidRequestDateAction  */  
   "InvalidRequestDateAction":string,
      /**  InvalidNeedByDateAction  */  
   "InvalidNeedByDateAction":string,
      /**  Place to populate a warning message to be displayed after update.  */  
   "AfterUpdateMessage":string,
   "EnableSerTrkOpts":boolean,
      /**  Defines if expense approver can add and delete an expense transaction.  */  
   "ExpenseApproverCanAddDel":boolean,
      /**  External field used on the Site Configuration Entry in order to enable or disable HCM fields  */  
   "IsHCMCompanyEnabled":boolean,
   "LowLvlSrlTrkDesc":string,
   "SerialMatchWrnDesc":string,
   "SerialTrkDesc":string,
      /**  Defines if time approver can add and delete a time transaction.  */  
   "TimeApproverCanAddDel":boolean,
   "AssignMtlDatesDesc":string,
      /**  External MES OData Password masked.  */  
   "ExternalMESODataPasswordMasked":string,
   "BitFlag":number,
   "DefaultRepackReasonCodeDescription":string,
   "DefaultWhseDescription":string,
   "DefDMRBinDescription":string,
   "DefDMRWhseDescription":string,
   "DefInspBinDescription":string,
   "DefInspWhseDescription":string,
   "DefJobPickBinDescription":string,
   "DefJobPickWhseDescription":string,
   "DefPCWhseDescription":string,
   "DefRcvBinDescription":string,
   "DefRcvWhseDescription":string,
   "DefShipBinDescription":string,
   "DefShipWhseDescription":string,
   "DefTFOrdPickBinDescription":string,
   "DefTFOrdPickWhseDescription":string,
   "DeliveryTypeDescription":string,
   "IdleResourceIDDescription":string,
   "IndirectCodeDescription":string,
   "JobHeadPartDescription":string,
   "PlantSendToFSA":boolean,
   "PlantName":string,
   "ProdCalDescription":string,
   "ShippingProdCalDescription":string,
   "TimeExpenseDefaultEmpIDName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlantMFBillRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   "PayBTFlag":string,
      /**   Describes the billing type.  Valid values and their description are:
1 - Shipper
2 - FedEx  Collect
3 - Third Party
4 - UPS Prepaid
5 - FedEx Recipient
6 - UPS Consignee
7 - UPS Freight Collect
8 - UPS Free On Board
9 - UPS Cost and Freight
10 - UPS Delivery Duty Paid
11 - UPS Shpping Duty and Tax Consignee  */  
   "PayTypeDesc":string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   "PayAccount":string,
      /**  Shipping Billing Address  */  
   "PayBTAddress1":string,
      /**  Shipping biling address line 2  */  
   "PayBTAddress2":string,
      /**  Shipping biling address line 3.  */  
   "PayBTAddress3":string,
      /**  Shipping billing city  */  
   "PayBTCity":string,
      /**  Shipping Billing state or province  */  
   "PayBTState":string,
      /**  Pay billing postal code  */  
   "PayBTZip":string,
      /**  Shipping biling country  */  
   "PayBTCountry":string,
      /**  Internal field used to store the country number.  */  
   "PayBTCountryNum":number,
      /**  Shipping billing phone number  */  
   "PayBTPhone":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlantSharedRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site Identifier for the Site that shares the warehouse.  This field cannot be blank.  */  
   "Plant":string,
      /**  A warehouse that is owned by the RemoteSite and shared with the Site. This field cannot be blank.  */  
   "WarehouseCode":string,
      /**  Remote Site Identifier for the Site that owns the warehouse.  This field cannot be blank.  */  
   "RemotePlant":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PlantName":string,
   "RemotePlantName":string,
   "WarehouseCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PlntTranDefRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Site that the transfer is from.  */  
   "FromPlant":string,
      /**  Site that the transfer is to.  */  
   "ToPlant":string,
      /**  Journal Code of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Estimated number of days to transfer material between Sites.  */  
   "TranDays":number,
      /**  ID of the division that is used to create eliminating entries.  */  
   "ConsolidationDivision":string,
      /**  Unique identifier for this category assigned by the user.  */  
   "InterDivSalesCatID":string,
      /**  Default ShipVia Code used for Unfirm Transfer Orders in MRP.  Cannot be blank  */  
   "DefaultShipViaCode":string,
      /**   Previous version used the following structure:
if (FromSite.GLDivision <> ToSite.GLDivision) then ?
now wil be more flexible
if (   PlntTranDef.InterDivisional   =  Yes   ) then  */  
   "InterDivisional":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Plant A/R GL Account  */  
   "PlantARAcct":string,
      /**  Plant A/R GL Account Desc  */  
   "PlantARAcctDesc":string,
      /**  Plant AP GL Account Number  */  
   "PlantAPAcct":string,
      /**  Plant AP GL Account Description  */  
   "PlantAPAcctDesc":string,
      /**  Contra AR GL Account Number  */  
   "ContraARAcct":string,
      /**  Contra AR GL Account Description  */  
   "ContraARAcctDesc":string,
      /**  Contra AP GL Account  */  
   "ContraAPAcct":string,
      /**  Contra AP GL Account Description  */  
   "ContraAPAcctDesc":string,
      /**  Contra COGS GL Account  */  
   "ContraCOGSAcct":string,
      /**  Contra COGS GL Account Description  */  
   "ContraCOGSAcctDesc":string,
      /**  Contra Revenue GL Account  */  
   "ContraRevenueAcct":string,
      /**  Contra Revenue GL Account Description  */  
   "ContraRevenueAcctDesc":string,
      /**  Contra Asset GL Account  */  
   "ContraAssetAcct":string,
      /**  Contra Asset GL Account Description  */  
   "ContraAssetAcctDesc":string,
      /**  Journal Code Description  */  
   "JournalCodeDesc":string,
      /**  Consolidation Division Description  */  
   "ConsolidationDivisionDesc":string,
      /**  Transit GL Account  */  
   "TransitAcct":string,
      /**  Transit GL Account Description  */  
   "TransitAcctDesc":string,
      /**  Inter Division Sales Category Description  */  
   "InterDivSalesCatDesc":string,
   "BitFlag":number,
   "DefautShipViaDescription":string,
   "DefautShipViaWebDesc":string,
   "FromPlantName":string,
   "InverDivSalesCatDescription":string,
   "JournalCodeJrnlDescription":string,
   "ToPlantName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PltUPSEmailRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  UPS Quantum View Sequence  */  
   "UPSQVSeq":number,
      /**  Email address to notify for a UPS shipment  */  
   "EmailAddress":string,
      /**  Logical indicating if the EmailAddress is to be updated at shipping.  */  
   "ShipmentNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   "FailureNotify":boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   "DeliveryNotify":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Logical indicating to the UI if the QV Detail and list is to be enabled.  */  
   "EnableQuantumView":boolean,
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
   */  
export interface CheckApprovalDefaults_input{
   ds:Erp_Tablesets_DfltApprTasksParamsTableset[],
}

export interface CheckApprovalDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DfltApprTasksParamsTableset,
   cQuestionText:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CreateApprovalDefaults_input{
   ds:Erp_Tablesets_DfltApprTasksParamsTableset[],
}

export interface CreateApprovalDefaults_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_DfltApprTasksParamsTableset,
   cReturnText:string,
}
}

   /** Required : 
      @param ds
      @param plant
      @param remotePlant
      @param warehouseCode
   */  
export interface CustomGetNewPlantShared_input{
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
      /**  Plant  */  
   plant:string,
      /**  Remote Plant  */  
   remotePlant:string,
      /**  Warehouse Code  */  
   warehouseCode:string,
}

export interface CustomGetNewPlantShared_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param plant
   */  
export interface DeleteByID_input{
   plant:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_DfltApprTasksParamsRow{
   Company:string,
      /**  Create defaults for multi-level approval  */  
   CreateForMultiLvlApp:boolean,
      /**  Create defaults for supervisor approval  */  
   CreateForSuperApp:boolean,
      /**  Create defaults for project manager approval  */  
   CreateForPMApp:boolean,
      /**  Create defaults for project manager/supervisor approval  */  
   CreateForPMAndSupApp:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_DfltApprTasksParamsTableset{
   DfltApprTasksParams:Erp_Tablesets_DfltApprTasksParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_EntityGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
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
      /**  Identifier of the GL Control Type.  */  
   GLControlType:string,
      /**  GL Control Identifier.  */  
   GLControlCode:string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   BusinessEntity:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   GlobalEntityGLC:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankAcctID of the related BankAcct record.  */  
   BankAcctID:string,
   BankFeeID:string,
      /**  CallCode of the related FSCallCd record.  */  
   CallCode:string,
   ChargeCode:string,
      /**  ClassCode of the related FAClass record.  */  
   ClassCode:string,
      /**  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  */  
   ClassID:string,
      /**  ContractCode of the related FSContCd record.  */  
   ContractCode:string,
      /**  CurrencyCode of the related Currency record.  */  
   CurrencyCode:string,
      /**  CustNum of the related Customer record  */  
   CustNum:number,
      /**  DeductionID of PRClsDed or PRDeduct.  */  
   DeductionID:string,
      /**  EmpID of the related PREmpMas record.  */  
   EmpID:string,
      /**  ExpenseCode of PayTLbr, LabExpCd  */  
   ExpenseCode:string,
      /**  ExtSystemID of ExtCompany table  */  
   ExtSystemID:string,
      /**  FromPlant value of the related PlntTranDef record.  */  
   FromPlant:string,
      /**  GroupCode of the related FAGroup record.  */  
   GroupCode:string,
   GroupID:string,
   HeadNum:number,
   InvoiceNum:string,
      /**  JCDept of the related JCDept record.  */  
   JCDept:string,
      /**  MiscCode of the related MiscChrg or PurMisc record.  */  
   MiscCode:string,
      /**  PartNum of the related Part record.  */  
   PartNum:string,
      /**  PayTypeID of PayType  */  
   PayTypeID:string,
   PerConName:string,
      /**  PI Status  */  
   PIStatus:string,
      /**  Plant of the related PlantConfCtrl record.  */  
   Plant:string,
      /**  ProdCode of the related ProdGrup record.  */  
   ProdCode:string,
      /**  ProjectID of the related Project record.  */  
   ProjectID:string,
      /**  PurchCode of the related GLPurch record.  */  
   PurchCode:string,
      /**  RateCode of the related GLRate record.  */  
   RateCode:string,
      /**  ReasonCode of the related Reason record.  */  
   ReasonCode:string,
      /**  ReasonType of the related Reason record.  */  
   ReasonType:string,
      /**  SalesCatID of the related SalesCat record.  */  
   SalesCatID:string,
      /**  Shift value of the related JCShift record.  */  
   Shift:number,
      /**  TaxCode of the related SalesTax record.  */  
   TaxCode:string,
      /**  TaxTblID of PRTaxMas or PRClsTax.  */  
   TaxTblID:string,
      /**  ToPlant value of the related PlntTranDef record.  */  
   ToPlant:string,
      /**  TransferMethod of ExtCompany table  */  
   TransferMethod:string,
      /**  Type ID  */  
   TypeID:string,
      /**  VendorNum of the related Vendor record.  */  
   VendorNum:number,
      /**  WarehouseCode of the related Warehse record.  */  
   WarehouseCode:string,
   ExpenseTypeCode:string,
   IsFiltered:boolean,
   OprTypeCode:string,
   CashDeskID:string,
   TIN:string,
   ReclassCodeID:string,
   BitFlag:number,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantConfABCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  ABC Code.  Valid values are "A" through "Z".  */  
   ABCCode:string,
      /**  This flag indicates whether the CountFreq defined in this record should over ride the count frequency in the AbcCode table.  */  
   OvrrideCountFreq:boolean,
      /**  This setting can be overrides AbcCode.CountFreq and can be overridden in WarehseABC.  */  
   CountFreq:number,
      /**  This flag is set to true prevent items that should only be counted during physical inventory from being selected for cycle counting. This setting can be overridden in WarehseABC.  */  
   ExcludeFromCC:boolean,
      /**  Stock Valuation Percent. Used by Calculate ABC Codes to determine what ABC code to assign to a part/warehouse record. This setting can be overridden in WarehseABC.  */  
   StockValPcnt:number,
      /**  Percent Tolerance. Entered as a positive number, Used to define the default percent tolerance for parts for which no percent tolerance is set up in PartWhse, PartSite, or WarehseABC. Zero indicates that any quantity variance is considered out of tolerance  */  
   PcntTolerance:number,
      /**  False = there is no percent tolerance consideration and any percent variance is considered within tolerance. True = percent tolerance is active for this ABC code and the value in PcntTolerance will be used to determine if the count variance is within tolerance.  */  
   CalcPcnt:boolean,
      /**  False = there is no quantity tolerance consideration and any quantity variance is considered within tolerance. True = quantity tolerance is active for this ABC code and the value in QtyTolerance will be used to determine if the count variance is within tolerance.  */  
   CalcQty:boolean,
      /**  False = there is no value tolerance consideration and any value variance is considered within tolerance. True = value tolerance is active for this ABC code and the value in ValueTolerance will be used to determine if the count variance is within tolerance.  */  
   CalcValue:boolean,
      /**  This flag indicates whether the StockValPcnt defined in this record should over ride the count frequency in the AbcCode table.  */  
   OvrrideStockValPcnt:boolean,
      /**  Quantity tolerance. Entered as a positive whole number, Used to define the default quantity tolerance for parts for which no quantity tolerance is set up in PartWhse, PartSite, or WarehseABC. Zero indicates that any quantity variance is considered out of  */  
   QtyTolerance:number,
      /**  Value tolerance. Entered as a positive number. Used to define the default value tolerance for parts for which no value tolerance is set up in PartWhse, PartSite, or WarehseABC.  An entry of zero will indicate that any value variance will be considered out  */  
   ValueTolerance:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantConfCtrlAttchRow{
   Company:string,
   Plant:string,
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

export interface Erp_Tablesets_PlantConfCtrlEGLCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  */  
   RelatedToFile:string,
      /**  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  */  
   Key1:string,
      /**   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  */  
   Key2:string,
      /**   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  */  
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
      /**  Identifier of the GL Control Type.  */  
   GLControlType:string,
      /**  GL Control Identifier.  */  
   GLControlCode:string,
      /**  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  */  
   BusinessEntity:string,
      /**  Global Company identifier.  Used in Multi-Company Journal.  */  
   ExtCompanyID:string,
      /**  Flag to indicate the account in this record is for an external company.  */  
   IsExternalCompany:boolean,
      /**  Marks this EntityGLC as global, available to be sent out to other companies.  */  
   GlobalEntityGLC:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Plant for PlantConfCtrl  */  
   Plant:string,
   BitFlag:number,
   GLCntrlDescription:string,
   GLCntrlTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantConfCtrlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  The Site name.  */  
   Name:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantConfCtrlListTableset{
   PlantConfCtrlList:Erp_Tablesets_PlantConfCtrlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PlantConfCtrlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  The Site name.  */  
   Name:string,
      /**  Warehse.WarehouseCode of the warehouse selected as the default warehouse for this Site.  */  
   DefaultWhse:string,
      /**  System date on which the last MRP processing was run.  */  
   MRPLastRunDate:string,
      /**  System Time (hr-min-sec) when the last MRP process was run.  */  
   MRPLastRunTime:number,
      /**  Warehse.WarehouseCode of the warehouse selected as the default inspection warehouse for this Site.  */  
   DefInspWhse:string,
      /**  Indicates if Labor Collection should calculate Idle time.  Idle time is the time that the employee is getting paid for but is not doing any direct or Indirect labor activity.  The Labor Collection will automatically generate an Indirect detail record to capture these hours if this flag is set to "Yes".  If this is "yes" then the IdleIndirectCode and IdleWCCode must be entered and valid.  */  
   CalcIdleTime:boolean,
      /**  The ResourceGrpID used by labor collection to create the LaborDtl entry for idle time when CalcIdleTime = Yes. For production labor (LaborType = "S" or "P") the default is from the JobOpDtl.ResourceGrpId from the primary JobOpDtl.  For indirect labor (LaborType = I) there is no default.  */  
   IdleResourceGrpID:string,
      /**  The indirect labor code (Indirect.IndirectCode) that Labor Collection will use when it creates the Idle Time detail record in LaborDtl.  This must be valid if the CalcIdleTime = Yes.  */  
   IndirectCode:string,
      /**  The number of hours (+-) difference from the server time zone to the Site time zone.  Data collection transactions will be offset by this amount.  */  
   TimeZoneOffset:number,
      /**  Related to TimeZoneOffset. Calculated from users entry in TimeZoneOffset, the number of seconds (+-) difference from the server time zone to the Site time zone.   Used for clock in clock out in data collection.  */  
   TimeOffsetSec:number,
      /**  This is the job number prefix that MRP uses when generating an unfirm job. Two Sites of the same company cannot have the same prefix.  */  
   UnfirmJobPrefix:string,
      /**  This is the job number prefix that for firm jobs.  */  
   FirmJobPrefix:string,
      /**  Default receiving warehouse. Used as default in receipt entry.  */  
   DefRcvWhse:string,
      /**  Default receiving bin Used as default in receipt entry.  */  
   DefRcvBin:string,
      /**  Default shipping warehouse. Used as default in shipment entry.  */  
   DefShipWhse:string,
      /**  Default shipping bin. Used as default in shipping entry.  */  
   DefShipBin:string,
      /**  KanBan Prefix  */  
   KanBanPrefix:string,
      /**  This is the job number prefix that MRP uses when generating an unfirm transfer order. Two Sites of the same company cannot have the same prefix.  */  
   MRPTOPrefix:string,
      /**  This is the job number prefix that Epicor ERP uses when generating a firm transfer order. Two Sites of the same company cannot have the same prefix.  */  
   ManualTOPrefix:string,
      /**  Scheduled Date used in last MRP run  */  
   MRPLastScheduledDate:string,
      /**  Cut Off Date used in last MRP run  */  
   MRPLastCutOffDate:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Default for JobHead.ProductionYield for this Site.  */  
   ProductionYieldDefault:boolean,
      /**  Indicates whether the calculated production yield adjustment should be automatically applied.  */  
   PrdYldAdjust:boolean,
      /**  Indicates whether an alert should be sent if the production yield calculation determines that an adjustment should be made. The alert will indicate if the adjustment has been made automatically or not (based on the setting of Site.PrdYieldAdjust). If the  */  
   PrdYldAlert:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Indicates if the shipment is international.  */  
   IntrntlShip:boolean,
      /**  Certificates of Origin required flag. Used in manifesting.  */  
   CertOfOrigin:boolean,
      /**  Commercial Invoice required flag. Used in manifesting.  */  
   CommercialInvoice:boolean,
      /**  Ship Export Declaration required flag. Used in manifesting.  */  
   ShipExprtDeclartn:boolean,
      /**  Letter of Instruction required. Used in manifesting.  */  
   LetterOfInstr:boolean,
      /**  Freight Forwarder ID.  */  
   FFID:string,
      /**  Freight Forwarder Company Name  */  
   FFCompName:string,
      /**  Freight Forwarder first address line.  */  
   FFContact:string,
      /**  Freight Forwarder second address line.  */  
   FFAddress1:string,
      /**  Freight Forwarder third address line.  */  
   FFAddress2:string,
      /**  Freight Forwarder city portion of address.  */  
   FFAddress3:string,
      /**  Freight Forwarder state portion of address.  */  
   FFCity:string,
      /**  Freight Forwarder postal code or zip code portion of address.  */  
   FFState:string,
      /**  Freight Forwarder country portion of address.  */  
   FFZip:string,
      /**  Non Standard Package flag. Used in manifesting.  */  
   FFCountry:string,
      /**  Additional Handling flag. Used in manifesting.  */  
   NonStdPkg:boolean,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Freight Forwarder country number portion of address.  */  
   FFCountryNum:number,
      /**  Freight Forwarder phone Number.  */  
   FFPhoneNum:string,
      /**  UPS Quantum View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View From Name  */  
   UPSQVShipFromName:string,
      /**  UPS Quantum View Memo  */  
   UPSQVMemo:string,
      /**  Default inspection bin. Used as default in inspection processing.  */  
   DefInspBin:string,
      /**  Default DMR warehouse. Used as default in DMR processing.  */  
   DefDMRWhse:string,
      /**  Default DMR bin. Used as default in DMR processing.  */  
   DefDMRBin:string,
      /**   Indicates whether serial number entry will be required when inventory movement is bin-to-bin within the same warehouse. All other inventory movement will still require serial number entry. This flag is only used if Serial Tracking Option is set to Full Serial Trace.
Defaults to True.  */  
   BinToBinReqSN:boolean,
      /**   Indicates the level of serial tracking for component items for the Site.
Defaults to 1.
Requires code/desc entry in object designer:
1 = No Lower Level Serial Tracking
2 = Full Lower Level Serial Tracking
3 = Outbound Serial Tracking Only.  */  
   LowLvlSerialTrk:number,
      /**   Indicates the level of serial tracking for the Site.
Default value for new SiteConfigCtrl = 1.
Requires code/desc entry in object designer:
1 = No Serial Tracking
2 = Full Serial Tracking
3 = Outbound Serial Tracking Only.  */  
   SerialTracking:number,
      /**   Controls the level of warnings that the user is given during job receipt processes for matching component serial numbers to the top level serial numbers.
Defaults to 1
Requires code/desc entry in object designer:
1 = No Warnings
2 = Warn but Allow Processing
3 = Warn and Do Not Allow Processing  */  
   SerialMatchWarn:number,
      /**  The maximum number of transactions to be auto-selected by the Handheld Auto-Select Transactions function.  */  
   HHAutoSelectTranMax:number,
      /**   Defines what method will be used to automatically select parts for cycle counting. This can be overridden in the Warehse table.
Default = 1.
Code/Desc:
1 = Repetitive, 2 = Random.  */  
   CCSelectMethod:number,
      /**  Default Search Sort for Sales Order Fulfillment Workbench.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  */  
   SearchSortOrder:string,
      /**  Default Search Sort for Job Fulfillment Workbench.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  */  
   SearchSortJob:string,
      /**  Default Search Sort for Transfer Fulfillment Workbench.  Valid values:  FIFO, LIFO, BINASC, BINDESC, QTYASC, or QTYDESC.  */  
   SearchSortTransfer:string,
      /**  Default Priority for a Pick Transaction.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   PriorityPick:number,
      /**  Default Priority for a Putaway Transaction.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   PriorityPutaway:number,
      /**  Default Priority for a Bin To Bin Replenishment Transaction.  Valid values:  1,2,3,4,5,6,7,8,9.  One is the highest priority.  */  
   PriorityBinToBinReplenish:number,
      /**  Replenish By Quantity or Volume.  Valid values:  Q and V  */  
   ReplenishBy:string,
      /**  Lock Orders on Pick?  */  
   LockOrdersOnPick:boolean,
      /**  Sort Queue by Priority?  */  
   SortQueueByPriority:boolean,
      /**  Warehse.WarehouseCode of the warehouse selected as the default warehouse for Job Allocation Picks in this Site.  */  
   DefJobPickWhse:string,
      /**  Default Job Pick bin. Used as default in Job Allocation Picks.  */  
   DefJobPickBin:string,
      /**  Warehse.WarehouseCode of the warehouse selected as the default warehouse for Transfer Order Allocation Picks in this Site.  */  
   DefTFOrdPickWhse:string,
      /**  Default Transfer Order Pick bin. Used as default in Transfer Order Allocation Picks.  */  
   DefTFOrdPickBin:string,
      /**  The Production Calendar to be used in the calculation of the schedules for Cycle Counting. If this field is left blank then the current Production Calendar defined on the Site.  */  
   CCProdCal:string,
      /**   Default value for Fulfillment Workbench.  Qualifies the unit of measure of the NetWeight field.
Must be a UOMConv of the UOMClass with ClassType of "weight".   Use UOMClass.DefUOMCode of the "weight" UOMClass as a default  when creating new part records.
Having a NetWeightUOM will provides the ability to calculate total  weight.  */  
   DefNetWeightUOM:string,
      /**   Default value for Fulfillment Workbench.  Qualifies the unit of measure of the NewVolume field.
Must be a UOMConv of the UOMClass with ClassType of "volume".   Use UOMClass.DefUOMCode of the "volume" UOMClass as a default  when creating new part records.
Having a Net Volume UOM will provides the ability to calculate total volume  */  
   DefNetVolumeUOM:string,
      /**  The Job should automatically attempt to reserve inventory upon Release.  */  
   JobReleaseAutoReserve:boolean,
      /**  System date on which the last Recycle Job processing was run.  */  
   RecycleLastDate:string,
      /**  System Time (hr-min-sec) when the last Recycle Job process was run.  */  
   RecycleLastTime:number,
      /**  By default this field will be false. Setting this to true will allow the loan logic to be enabled in Job Material Transfer Etnry.  */  
   AllowJobMtlLoans:boolean,
      /**   This field will be disabled if the above field is false.
The combo box will have two options:
1.  Repay Material when All Materials Received (AllRecvd)
2.  Repay Material when sufficient has been Received (SuffRecvd)  */  
   JobMtlRepayMethod:string,
      /**  Default Drop Shipping warehouse. Used as default in Drop Shipment processing.  */  
   DefDSWhse:string,
      /**  Determines if time needs to be approved.  */  
   TimeApprovalReqd:boolean,
      /**  Defines if time approver can add a time transaction.  */  
   TimeApproverCanAdd:boolean,
      /**  Defines if time approver can delete a time transaction.  */  
   TimeApproverCanDel:boolean,
      /**  Defines if time approver can update a time transaction.  */  
   TimeApproverCanUpd:boolean,
      /**  Defines if the method for approving indirect time transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  */  
   TimeIndirectLogic:string,
      /**  Defines if the method for approving production time transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  */  
   TimeProductionLogic:string,
      /**  The default workflow group for Time transactions entered in this Site.  */  
   TimeWFGroupID:string,
      /**  The default task set for Time transactions entered in this Site.  */  
   TimeTaskSetID:string,
      /**  Determines if expenses need to be approved.  */  
   ExpenseApprovalReqd:boolean,
      /**  Defines if expense approver can add an expense transaction.  */  
   ExpenseApproverCanAdd:boolean,
      /**  Defines if expense approver can delete an expense transaction.  */  
   ExpenseApproverCanDel:boolean,
      /**  Defines if expense approver can update an expense transaction.  */  
   ExpenseApproverCanUpd:boolean,
      /**  Defines if the method for approving indirect expense transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  */  
   ExpenseIndirectLogic:string,
      /**  Defines if the method for approving production expense transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  */  
   ExpenseProductionLogic:string,
      /**  The default workflow group for Expense transactions entered in this Site.  */  
   ExpenseWFGroupID:string,
      /**  The default task set for Expense transactions entered in this Site.  */  
   ExpenseTaskSetID:string,
      /**  Determines if labor time needs to be approved.  */  
   TimeMESApprovalReqd:boolean,
      /**  Indicates if the current user is restricted to entering time against employees where their username is set in the Employee record.  */  
   TimeRestrictEntry:boolean,
      /**  Indicates if the current user is restricted to entering expenses against employees where their username is set in the Employee record.  */  
   ExpenseRestrictEntry:boolean,
      /**  Used in Project Analysis to check if it should only include posted labor during the processing.  */  
   OnlyPostedLabor:boolean,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   MaintTmpJobNum:string,
      /**  Prefix that will be used when generating  Maintenance Job numbers for this Site.  Note: If blank, then system will use value defined at company level (see MMSyst.JobPrefix).  */  
   MaintJobPrefix:string,
      /**  Indicates if the supervisor of an employee can maintain time transactions on behalf of the employee.  */  
   TimeSuperCanMaintain:boolean,
      /**  Indicates if the supervisor of an employee can maintain expense transactions on behalf of the employee.  */  
   ExpenseSuperCanMaintain:boolean,
      /**  This field determines how inventory allocations are enforced at the Site level.  */  
   EnforceAllocations:string,
      /**  Defines if the method for approving advance request expense transactions is Automatic for all transactions within the Site or if it is specified at the Employee level.  Valid values are "A" for Automatic and "E" for Employee.  */  
   ExpenseAdvReqLogic:string,
      /**  Indicates if the new Expense Detail will be automatically submitted when saved.  */  
   ExpenseAutoSubmit:boolean,
      /**  Indicates if the new Time Detail will be automatically submitted when saved.  */  
   TimeAutoSubmit:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates the record is used with Machine MES  */  
   ExternalMES:boolean,
      /**  The Machine MES Integration type  */  
   ExternalMESType:string,
      /**  The Machine MES output file location  */  
   ExternalMESRoute:string,
      /**  Allow Credit Hold Orders to be released for Picking  */  
   AllowReleaseOfCreditHoldOrder:boolean,
      /**  This flag determies if partially reserved or allocated sales order releases can be Released for Picking.   If checked, then the "Ship Order Complete" and "Ship Line Complete" flags on the sales order are ignored when determining if a sales order releases can be Released for Picking.  */  
   AllowReleaseOfPartialSalesOrder:boolean,
      /**  The Machine MES input file location  */  
   ExternalMESInput:string,
      /**  Select this check box to disable the Pack Out sheet of Customer Shipment Entry  */  
   DisablePackOut:boolean,
      /**  Suppress Sales Order make direct Job warning  */  
   SuppressSOMakeDirWrn:boolean,
      /**  Unpack to Picked Status  */  
   AssumePickedOrders:boolean,
      /**  Use Order or Shipping Warehouse/Bin  */  
   DefOrdShipWhseBin:boolean,
      /**  Apply Burden to all operation Resources  */  
   ApplyBurdenCost:boolean,
      /**  If the Purchase Contracts module is being used, specify how the related demand requirements should be handled for this site.  */  
   PurchaseScheduleMode:string,
      /**  Include Completed Qtys/Hours in Send Ahead Calculations  */  
   IncludeCompleteQtys:boolean,
      /**  Assign Material Dates (engineered, unengineered, scheduling)  */  
   AssignMtlDates:string,
      /**  If you select this check box, the Setup is marked as Complete and load for Setup Hours is relieved when production for an operation is marked as Complete.  */  
   AutoCompleteSetup:boolean,
      /**  Controls the action to be taken when part number of a Job Mtl is being changed and there is already an issued qty to the original part number.  */  
   MtlIssuedAction:string,
      /**  Default Planning Contract Wharehouse. It is only allowed warehouses with at least one bin location flagged as contract bin.  */  
   DefPlanContractWhse:string,
      /**  PartLeadTime's flag allows the user to trigger the CTP calculations to include the parts lead time and net out existing supply and demand for the part.  */  
   PartLeadTime:boolean,
      /**  This flag controls which sales order releases can be processed by the Fulfillment Workbench.  If checked, then only those order releases where the associated OrderHed.ReadyToFulfill = true can be loaded into the workbench.  If not checked, then OrderHed.ReadyToFulfill is not considered when loading the workbench.  */  
   ReadyToFulfillRequired:boolean,
      /**  Indicates if there is to be package control enforcement during Job Receipt to Inventory.  */  
   EnforceJobRcptToInv:boolean,
      /**  The default package control employee for Time and Expense.  */  
   TimeExpenseDefaultEmpID:string,
      /**  The package control supervisor override password.  */  
   SupervisorOverridePassword:string,
      /**  Indicates if Package Control is enabled for this site.  */  
   EnablePackageControl:boolean,
      /**  Identifies the default Reason Code for a repack.  */  
   DefaultRepackReasonCode:string,
      /**  Default General bin. Used as default in receipt entry.  */  
   DefGenBin:string,
      /**  This flag affects the job creation in CTP for a Make to Order release upon clicking the Confirm button. F = Create Firm Job, a Firm Job to Order  will be created. U = Create Unfirm Job, the CTP job (which by its nature of an unfirm status) will remain. N = No Job, the CTP job will be deleted and there will not be any job created but the calculated date will affect the order release date. Default value = “F”  */  
   CTPJobCreateMTO:string,
      /**  This flag affects the job creation in CTP for a Make To Stock release upon clicking the Confirm button. F = Create Firm Job, a Firm Job to Stock will be created. U = Create Unfirm Job, the CTP job (which by its nature of an unfirm status) will remain. N = No Job, the CTP job will be deleted and there will not be any job created but the calculated date will affect the order release date. Default value = “F”  */  
   CTPJobCreateMTS:string,
      /**  Maximum Number of PCIDs allowed to be created during the Generate PCID function in various UI’s  */  
   MaxPCIDAllowedToCreate:number,
      /**  ConsumeReturnables  */  
   ConsumeReturnables:string,
      /**  ConsumeExpendables  */  
   ConsumeExpendables:string,
      /**  True if the Docking Station on the ShipDtl is a distinct value.  */  
   IsDockingStationDistinct:boolean,
      /**  Use3rdPartySched  */  
   Use3rdPartySched:boolean,
      /**  MtlQueueMaxRowsToReturn  */  
   MtlQueueMaxRowsToReturn:number,
      /**  MtlQueueEndDaysOffset  */  
   MtlQueueEndDaysOffset:number,
      /**  GenNewPCIDDelaySeconds  */  
   GenNewPCIDDelaySeconds:number,
      /**  GenNewPCIDLimitDays  */  
   GenNewPCIDLimitDays:number,
      /**  Logical field to indicate if the site configuration will allow to the Employee override HCM Payroll default  */  
   CanEmployeeOverrideHCM:boolean,
      /**  List field the default payroll configuration for HCM Integration  */  
   PayrollValuesForHCM:string,
      /**  Indicates whether Rate Shopping functionality is enabled for the site.  */  
   ManifestRateShopping:boolean,
      /**  The URL of the Rate Shopping website for this site.  */  
   ManifestRateShoppingURL:string,
      /**  Minimum Job Output Generate Interval. This value is in seconds. A value of 0 means no limit.  */  
   MinJOGenerateInterval:number,
      /**  Maximum Job Output Reprint Window. This value is in minutes. A value of 0 means no limit.  */  
   MaxJOReprintWindow:number,
      /**  Maximum Ad Hoc Job Output Job Window. This value is in days. A value of 0 means no limit.  */  
   MaxAHJOJobWindow:number,
      /**  Maximum Partial PCID Job Window. This value is in days. A value of 0 means no limit.  */  
   MaxPartialJobWindow:number,
      /**  Code used when generating Identificatin Numbers.  */  
   SiteIDCode:string,
      /**  The flag in Site Configuration that allows to automatically void a PCID when it becomes empty  */  
   VoidPCIDWhenEmpty:boolean,
      /**  When true, the allocation of inventory within a PCID will be allowed.  */  
   AllowAllocationOfPCIDInventory:boolean,
      /**  False = Transfer Order shipping whs/bin will default to the From Site primary warehouse and bin for the part if defined, else use the From Site Default General Whse. True = shipping whs/bin will default to: PartAlloc whs/bin if an entry exists for TFOrdDtl, else use the TFOrdDtl Staging warehouse and bin.  */  
   DefTOShipWhseBin:boolean,
      /**  The Machine MES OData URL  */  
   ExternalMESODataURL:string,
      /**  The Machine MES OData username  */  
   ExternalMESODataUsername:string,
      /**  The Machine MES OData password  */  
   ExternalMESODataPassword:string,
      /**  Indicates if the fulfillment queue is available for sales orders.  */  
   EnablePartAllocQueueOrder:boolean,
      /**  Indicates the PartAllocTemplate to use when allocating sales orders using automated fulfillment.  */  
   AllocTemplateIDOrder:string,
      /**  If Log WIP Changes is set to true, changes to PartWip will be logged in PartWipTran.  Default is false.  Must have AMM to set this to true.  Once WIP Changes have been logged, they will remain indefinitely.  Use the Database Purge and Summarice to purge history that is no longer desired.  */  
   LogWIPChanges:boolean,
      /**  Indicates if/when sales order releases should automatically be sent to the fulfillment queue.  */  
   SendToPartAllocQueueOrder:string,
      /**  Indicates the PartAllocTemplate to use when allocating jobs using automated fulfillment.  */  
   AllocTemplateIDJob:string,
      /**  Indicates the PartAllocTemplate to use when allocating transfer orders using automated fulfillment.  */  
   AllocTemplateIDTransfer:string,
      /**  Indicates if the fulfillment queue is available for jobs.  */  
   EnablePartAllocQueueJob:boolean,
      /**  Indicates if the fulfillment queue is available for transfer orders.  */  
   EnablePartAllocQueueTransfer:boolean,
      /**  OpCompleteConsumeWIP  */  
   OpCompleteConsumeWIP:boolean,
      /**  Indicates if/when job materials should automatically be sent to the fulfillment queue.  */  
   SendToPartAllocQueueJob:string,
      /**  Indicates if/when transfer order lines should automatically be sent to the fulfillment queue.  */  
   SendToPartAllocQueueTransfer:string,
      /**  If this field is true, it marks the selected site as Connected Process Control (CPC) as enabled. If disabled, connection and/or sync will not be done.  */  
   ECPCEnabled:boolean,
      /**  Controls the action that is to be taken when job ship quantity is not in shipping location  */  
   WIPShippingAction:string,
      /**  ShippingProdCal  */  
   ShippingProdCal:string,
      /**  InvalidRequestDateAction  */  
   InvalidRequestDateAction:string,
      /**  InvalidNeedByDateAction  */  
   InvalidNeedByDateAction:string,
      /**  Place to populate a warning message to be displayed after update.  */  
   AfterUpdateMessage:string,
   EnableSerTrkOpts:boolean,
      /**  Defines if expense approver can add and delete an expense transaction.  */  
   ExpenseApproverCanAddDel:boolean,
      /**  External field used on the Site Configuration Entry in order to enable or disable HCM fields  */  
   IsHCMCompanyEnabled:boolean,
   LowLvlSrlTrkDesc:string,
   SerialMatchWrnDesc:string,
   SerialTrkDesc:string,
      /**  Defines if time approver can add and delete a time transaction.  */  
   TimeApproverCanAddDel:boolean,
   AssignMtlDatesDesc:string,
      /**  External MES OData Password masked.  */  
   ExternalMESODataPasswordMasked:string,
   BitFlag:number,
   DefaultRepackReasonCodeDescription:string,
   DefaultWhseDescription:string,
   DefDMRBinDescription:string,
   DefDMRWhseDescription:string,
   DefInspBinDescription:string,
   DefInspWhseDescription:string,
   DefJobPickBinDescription:string,
   DefJobPickWhseDescription:string,
   DefPCWhseDescription:string,
   DefRcvBinDescription:string,
   DefRcvWhseDescription:string,
   DefShipBinDescription:string,
   DefShipWhseDescription:string,
   DefTFOrdPickBinDescription:string,
   DefTFOrdPickWhseDescription:string,
   DeliveryTypeDescription:string,
   IdleResourceIDDescription:string,
   IndirectCodeDescription:string,
   JobHeadPartDescription:string,
   PlantSendToFSA:boolean,
   PlantName:string,
   ProdCalDescription:string,
   ShippingProdCalDescription:string,
   TimeExpenseDefaultEmpIDName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantConfCtrlTableset{
   PlantConfCtrl:Erp_Tablesets_PlantConfCtrlRow[],
   PlantConfCtrlAttch:Erp_Tablesets_PlantConfCtrlAttchRow[],
   PlantConfABC:Erp_Tablesets_PlantConfABCRow[],
   PlantMFBill:Erp_Tablesets_PlantMFBillRow[],
   PlantShared:Erp_Tablesets_PlantSharedRow[],
   PlntTranDef:Erp_Tablesets_PlntTranDefRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   PltUPSEmail:Erp_Tablesets_PltUPSEmailRow[],
   PlantConfCtrlEGLC:Erp_Tablesets_PlantConfCtrlEGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PlantMFBillRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   PayBTFlag:string,
      /**   Describes the billing type.  Valid values and their description are:
1 - Shipper
2 - FedEx  Collect
3 - Third Party
4 - UPS Prepaid
5 - FedEx Recipient
6 - UPS Consignee
7 - UPS Freight Collect
8 - UPS Free On Board
9 - UPS Cost and Freight
10 - UPS Delivery Duty Paid
11 - UPS Shpping Duty and Tax Consignee  */  
   PayTypeDesc:string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   PayAccount:string,
      /**  Shipping Billing Address  */  
   PayBTAddress1:string,
      /**  Shipping biling address line 2  */  
   PayBTAddress2:string,
      /**  Shipping biling address line 3.  */  
   PayBTAddress3:string,
      /**  Shipping billing city  */  
   PayBTCity:string,
      /**  Shipping Billing state or province  */  
   PayBTState:string,
      /**  Pay billing postal code  */  
   PayBTZip:string,
      /**  Shipping biling country  */  
   PayBTCountry:string,
      /**  Internal field used to store the country number.  */  
   PayBTCountryNum:number,
      /**  Shipping billing phone number  */  
   PayBTPhone:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlantSharedRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier for the Site that shares the warehouse.  This field cannot be blank.  */  
   Plant:string,
      /**  A warehouse that is owned by the RemoteSite and shared with the Site. This field cannot be blank.  */  
   WarehouseCode:string,
      /**  Remote Site Identifier for the Site that owns the warehouse.  This field cannot be blank.  */  
   RemotePlant:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PlantName:string,
   RemotePlantName:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PlntTranDefRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site that the transfer is from.  */  
   FromPlant:string,
      /**  Site that the transfer is to.  */  
   ToPlant:string,
      /**  Journal Code of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Estimated number of days to transfer material between Sites.  */  
   TranDays:number,
      /**  ID of the division that is used to create eliminating entries.  */  
   ConsolidationDivision:string,
      /**  Unique identifier for this category assigned by the user.  */  
   InterDivSalesCatID:string,
      /**  Default ShipVia Code used for Unfirm Transfer Orders in MRP.  Cannot be blank  */  
   DefaultShipViaCode:string,
      /**   Previous version used the following structure:
if (FromSite.GLDivision <> ToSite.GLDivision) then ?
now wil be more flexible
if (   PlntTranDef.InterDivisional   =  Yes   ) then  */  
   InterDivisional:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Plant A/R GL Account  */  
   PlantARAcct:string,
      /**  Plant A/R GL Account Desc  */  
   PlantARAcctDesc:string,
      /**  Plant AP GL Account Number  */  
   PlantAPAcct:string,
      /**  Plant AP GL Account Description  */  
   PlantAPAcctDesc:string,
      /**  Contra AR GL Account Number  */  
   ContraARAcct:string,
      /**  Contra AR GL Account Description  */  
   ContraARAcctDesc:string,
      /**  Contra AP GL Account  */  
   ContraAPAcct:string,
      /**  Contra AP GL Account Description  */  
   ContraAPAcctDesc:string,
      /**  Contra COGS GL Account  */  
   ContraCOGSAcct:string,
      /**  Contra COGS GL Account Description  */  
   ContraCOGSAcctDesc:string,
      /**  Contra Revenue GL Account  */  
   ContraRevenueAcct:string,
      /**  Contra Revenue GL Account Description  */  
   ContraRevenueAcctDesc:string,
      /**  Contra Asset GL Account  */  
   ContraAssetAcct:string,
      /**  Contra Asset GL Account Description  */  
   ContraAssetAcctDesc:string,
      /**  Journal Code Description  */  
   JournalCodeDesc:string,
      /**  Consolidation Division Description  */  
   ConsolidationDivisionDesc:string,
      /**  Transit GL Account  */  
   TransitAcct:string,
      /**  Transit GL Account Description  */  
   TransitAcctDesc:string,
      /**  Inter Division Sales Category Description  */  
   InterDivSalesCatDesc:string,
   BitFlag:number,
   DefautShipViaDescription:string,
   DefautShipViaWebDesc:string,
   FromPlantName:string,
   InverDivSalesCatDescription:string,
   JournalCodeJrnlDescription:string,
   ToPlantName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PltUPSEmailRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  UPS Quantum View Sequence  */  
   UPSQVSeq:number,
      /**  Email address to notify for a UPS shipment  */  
   EmailAddress:string,
      /**  Logical indicating if the EmailAddress is to be updated at shipping.  */  
   ShipmentNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of a failed shipment.  */  
   FailureNotify:boolean,
      /**  Logical indicating if the Email Address is to be notified of delivery.  */  
   DeliveryNotify:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Logical indicating to the UI if the QV Detail and list is to be enabled.  */  
   EnableQuantumView:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtPlantConfCtrlTableset{
   PlantConfCtrl:Erp_Tablesets_PlantConfCtrlRow[],
   PlantConfCtrlAttch:Erp_Tablesets_PlantConfCtrlAttchRow[],
   PlantConfABC:Erp_Tablesets_PlantConfABCRow[],
   PlantMFBill:Erp_Tablesets_PlantMFBillRow[],
   PlantShared:Erp_Tablesets_PlantSharedRow[],
   PlntTranDef:Erp_Tablesets_PlntTranDefRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   PltUPSEmail:Erp_Tablesets_PltUPSEmailRow[],
   PlantConfCtrlEGLC:Erp_Tablesets_PlantConfCtrlEGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param sPlantID
   */  
export interface GetBinContractTypeWarehousesList_input{
   sPlantID:string,
}

export interface GetBinContractTypeWarehousesList_output{
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param plant
   */  
export interface GetByID_input{
   plant:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PlantConfCtrlTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PlantConfCtrlTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PlantConfCtrlTableset[],
}

   /** Required : 
      @param systemCode
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   systemCode:string,
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetCompleteList_input{
      /**  (optional)Additional Where conditions.  */  
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetCompleteList_output{
   returnObj:Erp_Tablesets_PlantConfCtrlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetDfltApprTasksParam_output{
   returnObj:Erp_Tablesets_DfltApprTasksParamsTableset[],
}

export interface GetDisabledFields_output{
parameters : {
      /**  output parameters  */  
   DisabledList:string,
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
   returnObj:Erp_Tablesets_PlantConfCtrlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
   */  
export interface GetNewEntityGLC_input{
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}

export interface GetNewEntityGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ds
      @param plant
   */  
export interface GetNewPlantConfABC_input{
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
   plant:string,
}

export interface GetNewPlantConfABC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ds
      @param plant
   */  
export interface GetNewPlantConfCtrlAttch_input{
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
   plant:string,
}

export interface GetNewPlantConfCtrlAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ds
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
   */  
export interface GetNewPlantConfCtrlEGLC_input{
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
   relatedToFile:string,
   key1:string,
   key2:string,
   key3:string,
   key4:string,
   key5:string,
   key6:string,
}

export interface GetNewPlantConfCtrlEGLC_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPlantConfCtrl_input{
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
}

export interface GetNewPlantConfCtrl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ds
      @param plant
   */  
export interface GetNewPlantMFBill_input{
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
   plant:string,
}

export interface GetNewPlantMFBill_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ds
      @param warehouseCode
   */  
export interface GetNewPlantShared_input{
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
   warehouseCode:string,
}

export interface GetNewPlantShared_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ds
      @param fromPlant
   */  
export interface GetNewPlntTranDef_input{
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
   fromPlant:string,
}

export interface GetNewPlntTranDef_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ds
      @param plant
   */  
export interface GetNewPltUPSEmail_input{
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
   plant:string,
}

export interface GetNewPltUPSEmail_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param whereClausePlantConfCtrl
      @param whereClausePlantConfCtrlAttch
      @param whereClausePlantConfABC
      @param whereClausePlantMFBill
      @param whereClausePlantShared
      @param whereClausePlntTranDef
      @param whereClauseEntityGLC
      @param whereClausePltUPSEmail
      @param whereClausePlantConfCtrlEGLC
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePlantConfCtrl:string,
   whereClausePlantConfCtrlAttch:string,
   whereClausePlantConfABC:string,
   whereClausePlantMFBill:string,
   whereClausePlantShared:string,
   whereClausePlntTranDef:string,
   whereClauseEntityGLC:string,
   whereClausePltUPSEmail:string,
   whereClausePlantConfCtrlEGLC:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PlantConfCtrlTableset[],
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
      @param plantID
   */  
export interface IsAuthorizedForPlant_input{
      /**  Plant ID  */  
   plantID:string,
}

export interface IsAuthorizedForPlant_output{
parameters : {
      /**  output parameters  */  
   isValid:boolean,
}
}

   /** Required : 
      @param enable
      @param demandType
      @param ds
   */  
export interface OnChangeEnablePartAllocQueue_input{
      /**  The new value of the enable flag.  */  
   enable:boolean,
      /**  The demandType related to the enable flag that is being changed (Job, Order, Transfer).  */  
   demandType:string,
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
}

export interface OnChangeEnablePartAllocQueue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
   message:string,
}
}

   /** Required : 
      @param ds
      @param ipABCCode
   */  
export interface OnChangeOfAbcCode_input{
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
   ipABCCode:string,
}

export interface OnChangeOfAbcCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param calendarID
      @param ds
   */  
export interface OnChangeOfCCProdCal_input{
      /**  Proposed Cycle Count Calendar ID field  */  
   calendarID:string,
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
}

export interface OnChangeOfCCProdCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ipApprovalRequired
      @param ds
   */  
export interface OnChangeOfExpenseApprovalReqd_input{
      /**  Proposed ExpenseApprovalReqd field  */  
   ipApprovalRequired:boolean,
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
}

export interface OnChangeOfExpenseApprovalReqd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ipRestrictEntry
      @param ds
   */  
export interface OnChangeOfExpenseRestrictEntry_input{
      /**  Proposed ExpenseRestrictEntry field  */  
   ipRestrictEntry:boolean,
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
}

export interface OnChangeOfExpenseRestrictEntry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ipLLSerTrk
      @param ds
   */  
export interface OnChangeOfLowLvlSerialTrk_input{
   ipLLSerTrk:number,
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
}

export interface OnChangeOfLowLvlSerialTrk_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ipJobNum
      @param ds
   */  
export interface OnChangeOfMaintTmpJobNum_input{
      /**  Job Num  */  
   ipJobNum:string,
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
}

export interface OnChangeOfMaintTmpJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ipPcntTolerance
   */  
export interface OnChangeOfPcntTolerance_input{
      /**  Percentage Tolerance  */  
   ipPcntTolerance:number,
}

export interface OnChangeOfPcntTolerance_output{
}

   /** Required : 
      @param ipQtyTolerance
   */  
export interface OnChangeOfQtyTolerance_input{
      /**  Quantity Tolerance Value  */  
   ipQtyTolerance:number,
}

export interface OnChangeOfQtyTolerance_output{
}

   /** Required : 
      @param ipSerialTracking
      @param ds
   */  
export interface OnChangeOfSerialTracking_input{
      /**  Proposed Serial Tracking field  */  
   ipSerialTracking:number,
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
}

export interface OnChangeOfSerialTracking_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ipStockValPcnt
   */  
export interface OnChangeOfStockValPcnt_input{
   ipStockValPcnt:number,
}

export interface OnChangeOfStockValPcnt_output{
}

   /** Required : 
      @param ipApprovalRequired
      @param ds
   */  
export interface OnChangeOfTimeApprovalReqd_input{
      /**  Proposed TimeApprovalReqd field  */  
   ipApprovalRequired:boolean,
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
}

export interface OnChangeOfTimeApprovalReqd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ipRestrictEntry
      @param ds
   */  
export interface OnChangeOfTimeRestrictEntry_input{
      /**  Proposed TimeRestrictEntry field  */  
   ipRestrictEntry:boolean,
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
}

export interface OnChangeOfTimeRestrictEntry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ipValTolerance
   */  
export interface OnChangeOfValueTolerance_input{
   ipValTolerance:number,
}

export interface OnChangeOfValueTolerance_output{
}

   /** Required : 
      @param ds
      @param WarehouseCode
   */  
export interface OnChangePCWarehouseCode_input{
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
   WarehouseCode:string,
}

export interface OnChangePCWarehouseCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param pcPlant
      @param pcRemotePlant
      @param pcWrkCenterList
      @param pcWareHseList
      @param plExecuteTransfer
   */  
export interface ResourceTransfer_input{
      /**  The plant from where you want to move the resources  */  
   pcPlant:string,
      /**  The plant where you want to move the resources  */  
   pcRemotePlant:string,
      /**  The delimited list of Work centers that you want to transfer to the remote plant  */  
   pcWrkCenterList:string,
      /**  The delimited list of warehouses that you want to transfer to the remote plant  */  
   pcWareHseList:string,
      /**  Yes will update the records.  No will run a simulation  */  
   plExecuteTransfer:boolean,
}

export interface ResourceTransfer_output{
parameters : {
      /**  output parameters  */  
   pcMessage:string,
   cTransferLog:string,
}
}

   /** Required : 
      @param ipQVEnable
      @param ds
   */  
export interface SetUPSQVEnable_input{
      /**  logical indicating if the quantum view is to enabled/disabled  */  
   ipQVEnable:boolean,
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
}

export interface SetUPSQVEnable_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param plant
   */  
export interface TestMachineMESODataConnection_input{
   plant:string,
}

export interface TestMachineMESODataConnection_output{
parameters : {
      /**  output parameters  */  
   msgConnection:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPlantConfCtrlTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPlantConfCtrlTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PlantConfCtrlTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PlantConfCtrlTableset,
}
}

   /** Required : 
      @param ipPayBTFlag
   */  
export interface ValidatePayBTFlag_input{
      /**  requested pay bt flag to edit  */  
   ipPayBTFlag:string,
}

export interface ValidatePayBTFlag_output{
}

