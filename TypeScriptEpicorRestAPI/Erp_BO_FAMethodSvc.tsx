import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.FAMethodSvc
// Description: FAMethod class
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get FAMethods items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FAMethods
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAMethodRow
   */  
export function get_FAMethods(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/FAMethods", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FAMethods
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FAMethodRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.FAMethodRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FAMethods(requestBody:Erp_Tablesets_FAMethodRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/FAMethods", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the FAMethod item
   Description: Calls GetByID to retrieve the FAMethod item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FAMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetMethod Desc: AssetMethod   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FAMethodRow
   */  
export function get_FAMethods_Company_AssetMethod(Company:string, AssetMethod:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FAMethodRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/FAMethods(" + Company + "," + AssetMethod + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_FAMethodRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FAMethod for the service
   Description: Calls UpdateExt to update FAMethod. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FAMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetMethod Desc: AssetMethod   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.FAMethodRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FAMethods_Company_AssetMethod(Company:string, AssetMethod:string, requestBody:Erp_Tablesets_FAMethodRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/FAMethods(" + Company + "," + AssetMethod + ")", {
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
   Summary: Call UpdateExt to delete FAMethod item
   Description: Call UpdateExt to delete FAMethod item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FAMethod
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param AssetMethod Desc: AssetMethod   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FAMethods_Company_AssetMethod(Company:string, AssetMethod:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/FAMethods(" + Company + "," + AssetMethod + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FAMethodListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAMethodListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAMethodListRow)
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseFAMethod:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseFAMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFAMethod=" + whereClauseFAMethod
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(assetMethod:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof assetMethod!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "assetMethod=" + assetMethod
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method AssignAnnualCharge
   Description: Updates temp table depreciation method formulas.
   OperationID: AssignAnnualCharge
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AssignAnnualCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignAnnualCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignAnnualCharge(requestBody:AssignAnnualCharge_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AssignAnnualCharge_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/AssignAnnualCharge", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AssignAnnualCharge_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignPeriodCharge
   Description: To be called after changing FAMethod.PeriodChargeType field
   OperationID: AssignPeriodCharge
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AssignPeriodCharge_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignPeriodCharge_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignPeriodCharge(requestBody:AssignPeriodCharge_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AssignPeriodCharge_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/AssignPeriodCharge", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AssignPeriodCharge_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignAnnualFormula
   Description: To be called after changing FAMethod.DisplayAnnualFormula
   OperationID: AssignAnnualFormula
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AssignAnnualFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignAnnualFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignAnnualFormula(requestBody:AssignAnnualFormula_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AssignAnnualFormula_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/AssignAnnualFormula", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AssignAnnualFormula_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AssignPeriodFormula
   Description: To be called after changing FAMethod.DisplayPeriodFormula
   OperationID: AssignPeriodFormula
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AssignPeriodFormula_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AssignPeriodFormula_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AssignPeriodFormula(requestBody:AssignPeriodFormula_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AssignPeriodFormula_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/AssignPeriodFormula", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AssignPeriodFormula_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeAltMethod
   Description: To be called on leave of FAMethod.AltAssetMethod field
   OperationID: ChangeAltMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeAltMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAltMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAltMethod(requestBody:ChangeAltMethod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeAltMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/ChangeAltMethod", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeAltMethod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDepChargeBasis
   Description: Annual
            To be called on leave of FAMethod.DepChargeBasis field
   OperationID: ChangeDepChargeBasis
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDepChargeBasis_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDepChargeBasis_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDepChargeBasis(requestBody:ChangeDepChargeBasis_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDepChargeBasis_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/ChangeDepChargeBasis", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeDepChargeBasis_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSwitchMethod
   Description: To be called on leave of FAMethod.SwitchMethod field
   OperationID: ChangeSwitchMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSwitchMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSwitchMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSwitchMethod(requestBody:ChangeSwitchMethod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSwitchMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/ChangeSwitchMethod", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeSwitchMethod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TestSyntax
   Description: Test the formula syntax.
   OperationID: TestSyntax
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/TestSyntax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestSyntax_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestSyntax(requestBody:TestSyntax_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<TestSyntax_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/TestSyntax", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as TestSyntax_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AnnualVariables
   Description: Returns variables to create depreciation method formulas. Used in annual formula context menu.
   OperationID: AnnualVariables
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AnnualVariables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AnnualVariables(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AnnualVariables_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/AnnualVariables", {
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
         resolve(data as AnnualVariables_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PeriodVariables
   Description: Returns variables to create depreciation method period formulas. Used in period formula context menu.
   OperationID: PeriodVariables
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/PeriodVariables_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PeriodVariables(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PeriodVariables_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/PeriodVariables", {
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
         resolve(data as PeriodVariables_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Functions
   Description: Returns functions to create depreciation method formulas.
   OperationID: Functions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Functions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Functions(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Functions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/Functions", {
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
         resolve(data as Functions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Operators
   Description: Returns operators to create depreciation method formulas.
   OperationID: Operators
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Operators_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Operators(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Operators_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/Operators", {
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
         resolve(data as Operators_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFAMethod
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFAMethod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFAMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFAMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFAMethod(requestBody:GetNewFAMethod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFAMethod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/GetNewFAMethod", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewFAMethod_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.FAMethodSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAMethodListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAMethodListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FAMethodRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FAMethodRow,
}

export interface Erp_Tablesets_FAMethodListRow{
      /**  Company of the depreciation methods table.  */  
   "Company":string,
      /**  Identifier of the depreciation method.  */  
   "AssetMethod":string,
      /**  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  */  
   "Description":string,
      /**  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  */  
   "DepreciationMethod":string,
      /**  Flag to indicate that calculated depreciation between the fiscal period of asset commission date and the first open fiscal period should be distributed over all open remaining periods of the first depreciation year or when false then the calculated depreciation will be applied to the first open fiscal period.  */  
   "AdditionSpread":boolean,
      /**  Flag to indicate that the total of depreciations in the last year of depreciation should be distributed over all fiscal periods of the last year.  */  
   "Finalspread":boolean,
      /**  Indicates if this depreciation method is used by an asset register.  */  
   "InUse":boolean,
      /**  Indicates if this depreciation method is allowed to switch to another method.  */  
   "AllowSwitch":boolean,
      /**  Alternate Depreciation Method  */  
   "AltAssetMethod":string,
      /**  Depreciation Charge Basis.  Valid values are: "ANNUAL" or "PERIOD".  */  
   "DepChargeBasis":string,
      /**  Indicates how Annual Charge amount needs to be calculated. Valid values are: "RATE", "LIFE", "SUMYEAR", "DECBAL", "FORMULA", "SPREAD" or "FIXED".  If Rate is selected then Annual Charge is calculated using the pre-defined formula for "Rate Straight Line" depreciation calculation. If Life is selected then Annual Charge is calculated using the pre-defined formula for "Life Straight Line" depreciation calculation. If SumYear is selected then Annual Charge is calculated using the pre-defined formula for "Sum of Year Digits" depreciation calculation. If DecBal is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance" depreciation calculation. If BalToLn is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance to Straight Line" depreciation calculation. If MACRS is selected then Annual Charge is calculated using the pre-defined formula for "MACRS (USA)" depreciation calculation. If Formula is selected then Annual Charge will be calculated using a user-maintainable formula.  If Spread is selected then Annual Charge is taken from the value stored from the Spread Code table. If Fixed is selected then the Annual Charge is manually entered by the user through Asset Maintenance.  */  
   "AnnualChargeType":string,
      /**  Formula used to calculate the asset annual depreciation charge.  Only valid if AnnualChargeType is NOT "SPREAD" nor "FIXED".  */  
   "AnnualFormula":string,
      /**  Indicates how Period Charge amount needs to be calculated.  Valid values are: "FORMULA", "SPREAD" or "FIXED".  If Formula is selected then Period Charge is derived using the period formula. If Spread is selected then Period Charge is taken from the value stored from the Spread Code table. If Fixed is seleted then the Period Charge is manually entered by the user through Asset Maintenance.  */  
   "PeriodChargeType":string,
      /**  Indicates how the Annual Charge Amount will be distributed over periods.  Valid values are: "EQUAL"; "SPREAD"; or "NUMDAYS".  If Equal then Annual Charge will be divided equally among fiscal periods.  If Spread then Annual Charge will be prorated using the Spread Code values. If NumDays then Annual Charge will be prorated using the Number of Days per period.  */  
   "ProrateType":string,
      /**  System maintained field.  Indicates that this depreciation method uses a pre-defined formula in calculating depreciation costs.  */  
   "SystemFlag":boolean,
      /**  Indicates when to apply the automatic switching of depreciation method from the original method to the alternate method.  Valid values of this field are: "NEVER" (Never), "EXPENSE" (On Greater Expense) and "BOOKVAL" (On Book Value Reaching % of Asset Cost).  */  
   "SwitchMethod":string,
      /**  The Percentage that will be used to check if an automatic switching of depreciation method is necessary.  If SwitchMethod is "BOOKVAL" then an automatic switch of depreciation method will occur if the Book Value becomes <= SwitchPercent (%) of Asset Cost.  */  
   "SwitchPercent":number,
      /**  Formula used to calculate the asset period depreciation charge.  Only valid if PeriodChargeType is "FORMULA".  */  
   "PeriodFormula":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  External In Use Flag.  */  
   "InUseFlag":boolean,
   "AltAssetMethodDescription":string,
   "DisplayAnnualFormula":string,
   "DisplayPeriodFormula":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FAMethodRow{
      /**  Company of the depreciation methods table.  */  
   "Company":string,
      /**  Identifier of the depreciation method.  */  
   "AssetMethod":string,
      /**  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  */  
   "Description":string,
      /**  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  */  
   "DepreciationMethod":string,
      /**  Flag to indicate that calculated depreciation between the fiscal period of asset commission date and the first open fiscal period should be distributed over all open remaining periods of the first depreciation year or when false then the calculated depreciation will be applied to the first open fiscal period.  */  
   "AdditionSpread":boolean,
      /**  Flag to indicate that the total of depreciations in the last year of depreciation should be distributed over all fiscal periods of the last year.  */  
   "Finalspread":boolean,
      /**  Indicates if this depreciation method is used by an asset register.  */  
   "InUse":boolean,
      /**  Indicates if this depreciation method is allowed to switch to another method.  */  
   "AllowSwitch":boolean,
      /**  Alternate Depreciation Method  */  
   "AltAssetMethod":string,
      /**  Depreciation Charge Basis.  Valid values are: "ANNUAL" or "PERIOD".  */  
   "DepChargeBasis":string,
      /**  Indicates how Annual Charge amount needs to be calculated. Valid values are: "RATE", "LIFE", "SUMYEAR", "DECBAL", "FORMULA", "SPREAD" or "FIXED".  If Rate is selected then Annual Charge is calculated using the pre-defined formula for "Rate Straight Line" depreciation calculation. If Life is selected then Annual Charge is calculated using the pre-defined formula for "Life Straight Line" depreciation calculation. If SumYear is selected then Annual Charge is calculated using the pre-defined formula for "Sum of Year Digits" depreciation calculation. If DecBal is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance" depreciation calculation. If BalToLn is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance to Straight Line" depreciation calculation. If MACRS is selected then Annual Charge is calculated using the pre-defined formula for "MACRS (USA)" depreciation calculation. If Formula is selected then Annual Charge will be calculated using a user-maintainable formula.  If Spread is selected then Annual Charge is taken from the value stored from the Spread Code table. If Fixed is selected then the Annual Charge is manually entered by the user through Asset Maintenance.  */  
   "AnnualChargeType":string,
      /**  Formula used to calculate the asset annual depreciation charge.  Only valid if AnnualChargeType is NOT "SPREAD" nor "FIXED".  */  
   "AnnualFormula":string,
      /**  Indicates how Period Charge amount needs to be calculated.  Valid values are: "FORMULA", "SPREAD" or "FIXED".  If Formula is selected then Period Charge is derived using the period formula. If Spread is selected then Period Charge is taken from the value stored from the Spread Code table. If Fixed is seleted then the Period Charge is manually entered by the user through Asset Maintenance.  */  
   "PeriodChargeType":string,
      /**  Indicates how the Annual Charge Amount will be distributed over periods.  Valid values are: "EQUAL"; "SPREAD"; or "NUMDAYS".  If Equal then Annual Charge will be divided equally among fiscal periods.  If Spread then Annual Charge will be prorated using the Spread Code values. If NumDays then Annual Charge will be prorated using the Number of Days per period.  */  
   "ProrateType":string,
      /**  System maintained field.  Indicates that this depreciation method uses a pre-defined formula in calculating depreciation costs.  */  
   "SystemFlag":boolean,
      /**  Indicates when to apply the automatic switching of depreciation method from the original method to the alternate method.  Valid values of this field are: "NEVER" (Never), "EXPENSE" (On Greater Expense) and "BOOKVAL" (On Book Value Reaching % of Asset Cost).  */  
   "SwitchMethod":string,
      /**  The Percentage that will be used to check if an automatic switching of depreciation method is necessary.  If SwitchMethod is "BOOKVAL" then an automatic switch of depreciation method will occur if the Book Value becomes <= SwitchPercent (%) of Asset Cost.  */  
   "SwitchPercent":number,
      /**  Formula used to calculate the asset period depreciation charge.  Only valid if PeriodChargeType is "FORMULA".  */  
   "PeriodFormula":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Remaining Years parameter calculation basis.  */  
   "RemYearsCalculation":string,
      /**  External In Use Flag.  */  
   "InUseFlag":boolean,
   "AltAssetMethodDescription":string,
      /**  Formula used to calculate the asset annual depreciation charge.  Only valid if AnnualChargeType is NOT "SPREAD" nor "FIXED".  */  
   "DisplayAnnualFormula":string,
      /**  Formula used to calculate the asset period depreciation charge.  Only valid if PeriodChargeType is "FORMULA".  */  
   "DisplayPeriodFormula":string,
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
export interface AnnualVariables_output{
      /**  Variable list  */  
   returnObj:string,
}

   /** Required : 
      @param ds
   */  
export interface AssignAnnualCharge_input{
   ds:Erp_Tablesets_FAMethodTableset[],
}

export interface AssignAnnualCharge_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAMethodTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface AssignAnnualFormula_input{
   ds:Erp_Tablesets_FAMethodTableset[],
}

export interface AssignAnnualFormula_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAMethodTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface AssignPeriodCharge_input{
   ds:Erp_Tablesets_FAMethodTableset[],
}

export interface AssignPeriodCharge_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAMethodTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface AssignPeriodFormula_input{
   ds:Erp_Tablesets_FAMethodTableset[],
}

export interface AssignPeriodFormula_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAMethodTableset,
}
}

   /** Required : 
      @param ipAltMethod
      @param ds
   */  
export interface ChangeAltMethod_input{
      /**  alternative asset method that was entered.  */  
   ipAltMethod:string,
   ds:Erp_Tablesets_FAMethodTableset[],
}

export interface ChangeAltMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAMethodTableset,
}
}

   /** Required : 
      @param ipDepCharge
      @param ds
   */  
export interface ChangeDepChargeBasis_input{
      /**  depreciation charge basis that was entered.  */  
   ipDepCharge:string,
   ds:Erp_Tablesets_FAMethodTableset[],
}

export interface ChangeDepChargeBasis_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAMethodTableset,
}
}

   /** Required : 
      @param ipSwitchMethod
      @param ds
   */  
export interface ChangeSwitchMethod_input{
      /**  switch method that was entered.  */  
   ipSwitchMethod:string,
   ds:Erp_Tablesets_FAMethodTableset[],
}

export interface ChangeSwitchMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAMethodTableset,
}
}

   /** Required : 
      @param assetMethod
   */  
export interface DeleteByID_input{
   assetMethod:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_FAMethodListRow{
      /**  Company of the depreciation methods table.  */  
   Company:string,
      /**  Identifier of the depreciation method.  */  
   AssetMethod:string,
      /**  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  */  
   Description:string,
      /**  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  */  
   DepreciationMethod:string,
      /**  Flag to indicate that calculated depreciation between the fiscal period of asset commission date and the first open fiscal period should be distributed over all open remaining periods of the first depreciation year or when false then the calculated depreciation will be applied to the first open fiscal period.  */  
   AdditionSpread:boolean,
      /**  Flag to indicate that the total of depreciations in the last year of depreciation should be distributed over all fiscal periods of the last year.  */  
   Finalspread:boolean,
      /**  Indicates if this depreciation method is used by an asset register.  */  
   InUse:boolean,
      /**  Indicates if this depreciation method is allowed to switch to another method.  */  
   AllowSwitch:boolean,
      /**  Alternate Depreciation Method  */  
   AltAssetMethod:string,
      /**  Depreciation Charge Basis.  Valid values are: "ANNUAL" or "PERIOD".  */  
   DepChargeBasis:string,
      /**  Indicates how Annual Charge amount needs to be calculated. Valid values are: "RATE", "LIFE", "SUMYEAR", "DECBAL", "FORMULA", "SPREAD" or "FIXED".  If Rate is selected then Annual Charge is calculated using the pre-defined formula for "Rate Straight Line" depreciation calculation. If Life is selected then Annual Charge is calculated using the pre-defined formula for "Life Straight Line" depreciation calculation. If SumYear is selected then Annual Charge is calculated using the pre-defined formula for "Sum of Year Digits" depreciation calculation. If DecBal is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance" depreciation calculation. If BalToLn is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance to Straight Line" depreciation calculation. If MACRS is selected then Annual Charge is calculated using the pre-defined formula for "MACRS (USA)" depreciation calculation. If Formula is selected then Annual Charge will be calculated using a user-maintainable formula.  If Spread is selected then Annual Charge is taken from the value stored from the Spread Code table. If Fixed is selected then the Annual Charge is manually entered by the user through Asset Maintenance.  */  
   AnnualChargeType:string,
      /**  Formula used to calculate the asset annual depreciation charge.  Only valid if AnnualChargeType is NOT "SPREAD" nor "FIXED".  */  
   AnnualFormula:string,
      /**  Indicates how Period Charge amount needs to be calculated.  Valid values are: "FORMULA", "SPREAD" or "FIXED".  If Formula is selected then Period Charge is derived using the period formula. If Spread is selected then Period Charge is taken from the value stored from the Spread Code table. If Fixed is seleted then the Period Charge is manually entered by the user through Asset Maintenance.  */  
   PeriodChargeType:string,
      /**  Indicates how the Annual Charge Amount will be distributed over periods.  Valid values are: "EQUAL"; "SPREAD"; or "NUMDAYS".  If Equal then Annual Charge will be divided equally among fiscal periods.  If Spread then Annual Charge will be prorated using the Spread Code values. If NumDays then Annual Charge will be prorated using the Number of Days per period.  */  
   ProrateType:string,
      /**  System maintained field.  Indicates that this depreciation method uses a pre-defined formula in calculating depreciation costs.  */  
   SystemFlag:boolean,
      /**  Indicates when to apply the automatic switching of depreciation method from the original method to the alternate method.  Valid values of this field are: "NEVER" (Never), "EXPENSE" (On Greater Expense) and "BOOKVAL" (On Book Value Reaching % of Asset Cost).  */  
   SwitchMethod:string,
      /**  The Percentage that will be used to check if an automatic switching of depreciation method is necessary.  If SwitchMethod is "BOOKVAL" then an automatic switch of depreciation method will occur if the Book Value becomes <= SwitchPercent (%) of Asset Cost.  */  
   SwitchPercent:number,
      /**  Formula used to calculate the asset period depreciation charge.  Only valid if PeriodChargeType is "FORMULA".  */  
   PeriodFormula:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  External In Use Flag.  */  
   InUseFlag:boolean,
   AltAssetMethodDescription:string,
   DisplayAnnualFormula:string,
   DisplayPeriodFormula:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FAMethodListTableset{
   FAMethodList:Erp_Tablesets_FAMethodListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_FAMethodRow{
      /**  Company of the depreciation methods table.  */  
   Company:string,
      /**  Identifier of the depreciation method.  */  
   AssetMethod:string,
      /**  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  */  
   Description:string,
      /**  The depreciation method description. These are the pre-defined depreciation methods provided for this release: Rate Straight-Line; Life Straight-Line; Declining Balance; Declining Balance to Straight-Line; Sum of the Years Digits; Fixed Amount Per Year; and Fixed Amount Per Month.  */  
   DepreciationMethod:string,
      /**  Flag to indicate that calculated depreciation between the fiscal period of asset commission date and the first open fiscal period should be distributed over all open remaining periods of the first depreciation year or when false then the calculated depreciation will be applied to the first open fiscal period.  */  
   AdditionSpread:boolean,
      /**  Flag to indicate that the total of depreciations in the last year of depreciation should be distributed over all fiscal periods of the last year.  */  
   Finalspread:boolean,
      /**  Indicates if this depreciation method is used by an asset register.  */  
   InUse:boolean,
      /**  Indicates if this depreciation method is allowed to switch to another method.  */  
   AllowSwitch:boolean,
      /**  Alternate Depreciation Method  */  
   AltAssetMethod:string,
      /**  Depreciation Charge Basis.  Valid values are: "ANNUAL" or "PERIOD".  */  
   DepChargeBasis:string,
      /**  Indicates how Annual Charge amount needs to be calculated. Valid values are: "RATE", "LIFE", "SUMYEAR", "DECBAL", "FORMULA", "SPREAD" or "FIXED".  If Rate is selected then Annual Charge is calculated using the pre-defined formula for "Rate Straight Line" depreciation calculation. If Life is selected then Annual Charge is calculated using the pre-defined formula for "Life Straight Line" depreciation calculation. If SumYear is selected then Annual Charge is calculated using the pre-defined formula for "Sum of Year Digits" depreciation calculation. If DecBal is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance" depreciation calculation. If BalToLn is selected then Annual Charge is calculated using the pre-defined formula for "Declining Balance to Straight Line" depreciation calculation. If MACRS is selected then Annual Charge is calculated using the pre-defined formula for "MACRS (USA)" depreciation calculation. If Formula is selected then Annual Charge will be calculated using a user-maintainable formula.  If Spread is selected then Annual Charge is taken from the value stored from the Spread Code table. If Fixed is selected then the Annual Charge is manually entered by the user through Asset Maintenance.  */  
   AnnualChargeType:string,
      /**  Formula used to calculate the asset annual depreciation charge.  Only valid if AnnualChargeType is NOT "SPREAD" nor "FIXED".  */  
   AnnualFormula:string,
      /**  Indicates how Period Charge amount needs to be calculated.  Valid values are: "FORMULA", "SPREAD" or "FIXED".  If Formula is selected then Period Charge is derived using the period formula. If Spread is selected then Period Charge is taken from the value stored from the Spread Code table. If Fixed is seleted then the Period Charge is manually entered by the user through Asset Maintenance.  */  
   PeriodChargeType:string,
      /**  Indicates how the Annual Charge Amount will be distributed over periods.  Valid values are: "EQUAL"; "SPREAD"; or "NUMDAYS".  If Equal then Annual Charge will be divided equally among fiscal periods.  If Spread then Annual Charge will be prorated using the Spread Code values. If NumDays then Annual Charge will be prorated using the Number of Days per period.  */  
   ProrateType:string,
      /**  System maintained field.  Indicates that this depreciation method uses a pre-defined formula in calculating depreciation costs.  */  
   SystemFlag:boolean,
      /**  Indicates when to apply the automatic switching of depreciation method from the original method to the alternate method.  Valid values of this field are: "NEVER" (Never), "EXPENSE" (On Greater Expense) and "BOOKVAL" (On Book Value Reaching % of Asset Cost).  */  
   SwitchMethod:string,
      /**  The Percentage that will be used to check if an automatic switching of depreciation method is necessary.  If SwitchMethod is "BOOKVAL" then an automatic switch of depreciation method will occur if the Book Value becomes <= SwitchPercent (%) of Asset Cost.  */  
   SwitchPercent:number,
      /**  Formula used to calculate the asset period depreciation charge.  Only valid if PeriodChargeType is "FORMULA".  */  
   PeriodFormula:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Remaining Years parameter calculation basis.  */  
   RemYearsCalculation:string,
      /**  External In Use Flag.  */  
   InUseFlag:boolean,
   AltAssetMethodDescription:string,
      /**  Formula used to calculate the asset annual depreciation charge.  Only valid if AnnualChargeType is NOT "SPREAD" nor "FIXED".  */  
   DisplayAnnualFormula:string,
      /**  Formula used to calculate the asset period depreciation charge.  Only valid if PeriodChargeType is "FORMULA".  */  
   DisplayPeriodFormula:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FAMethodTableset{
   FAMethod:Erp_Tablesets_FAMethodRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtFAMethodTableset{
   FAMethod:Erp_Tablesets_FAMethodRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Functions_output{
      /**  Function list  */  
   returnObj:string,
}

   /** Required : 
      @param assetMethod
   */  
export interface GetByID_input{
   assetMethod:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_FAMethodTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_FAMethodTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_FAMethodTableset[],
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
   returnObj:Erp_Tablesets_FAMethodListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewFAMethod_input{
   ds:Erp_Tablesets_FAMethodTableset[],
}

export interface GetNewFAMethod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAMethodTableset,
}
}

   /** Required : 
      @param whereClauseFAMethod
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseFAMethod:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_FAMethodTableset[],
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

export interface Operators_output{
      /**  Operator list  */  
   returnObj:string,
}

export interface PeriodVariables_output{
      /**  Variable list  */  
   returnObj:string,
}

   /** Required : 
      @param ipFormulaToCheck
      @param ipDepChargeBasis
   */  
export interface TestSyntax_input{
      /**  Formula to check  */  
   ipFormulaToCheck:string,
      /**  DepChargeBasis Annual or Period  */  
   ipDepChargeBasis:string,
}

export interface TestSyntax_output{
parameters : {
      /**  output parameters  */  
   opSyntaxIsCorrect:boolean,
   opSyntaxMessage:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtFAMethodTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtFAMethodTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_FAMethodTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_FAMethodTableset,
}
}

