import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CompanySvc
// Description: Company Configuration Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/$metadata", {
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
   Description: Get Companies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Companies
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CompanyRow
   */  
export function get_Companies(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Companies
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CompanyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CompanyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Companies(requestBody:Erp_Tablesets_CompanyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the Company item
   Description: Calls GetByID to retrieve the Company item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Company
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CompanyRow
   */  
export function get_Companies_Company1(Company1:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")", {
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
         resolve(data as Erp_Tablesets_CompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Company for the service
   Description: Calls UpdateExt to update Company. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Company
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CompanyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Companies_Company1(Company1:string, requestBody:Erp_Tablesets_CompanyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")", {
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
   Summary: Call UpdateExt to delete Company item
   Description: Call UpdateExt to delete Company item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Company
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Companies_Company1(Company1:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")", {
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
   Description: Get AGCompanies items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_AGCompanies1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AGCompanyRow
   */  
export function get_Companies_Company1_AGCompanies(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AGCompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/AGCompanies", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AGCompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the AGCompany item
   Description: Calls GetByID to retrieve the AGCompany item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AGCompany1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.AGCompanyRow
   */  
export function get_Companies_Company1_AGCompanies_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AGCompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/AGCompanies(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_AGCompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get APSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_APSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APSystRow
   */  
export function get_Companies_Company1_APSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/APSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the APSyst item
   Description: Calls GetByID to retrieve the APSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APSystRow
   */  
export function get_Companies_Company1_APSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/APSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_APSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ARSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ARSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARSystRow
   */  
export function get_Companies_Company1_ARSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/ARSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ARSyst item
   Description: Calls GetByID to retrieve the ARSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ARSystRow
   */  
export function get_Companies_Company1_ARSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/ARSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_ARSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get BMSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BMSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BMSystRow
   */  
export function get_Companies_Company1_BMSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BMSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/BMSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BMSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BMSyst item
   Description: Calls GetByID to retrieve the BMSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BMSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BMSystRow
   */  
export function get_Companies_Company1_BMSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BMSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/BMSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_BMSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get BorderPcts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_BorderPcts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BorderPctRow
   */  
export function get_Companies_Company1_BorderPcts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BorderPctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/BorderPcts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BorderPctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the BorderPct item
   Description: Calls GetByID to retrieve the BorderPct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BorderPct1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DestCountryNum Desc: DestCountryNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BorderPctRow
   */  
export function get_Companies_Company1_BorderPcts_Company_DestCountryNum(Company1:string, Company:string, DestCountryNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BorderPctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/BorderPcts(" + Company + "," + DestCountryNum + ")", {
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
         resolve(data as Erp_Tablesets_BorderPctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CRSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CRSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRSystRow
   */  
export function get_Companies_Company1_CRSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CRSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CRSyst item
   Description: Calls GetByID to retrieve the CRSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CRSystRow
   */  
export function get_Companies_Company1_CRSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CRSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CRSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_CRSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CSFSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CSFSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CSFSystRow
   */  
export function get_Companies_Company1_CSFSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CSFSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CSFSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CSFSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CSFSyst item
   Description: Calls GetByID to retrieve the CSFSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CSFSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CSFSystRow
   */  
export function get_Companies_Company1_CSFSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CSFSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CSFSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_CSFSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get Currencies items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_Currencies1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrencyRow
   */  
export function get_Companies_Company1_Currencies(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/Currencies", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the Currency item
   Description: Calls GetByID to retrieve the Currency item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Currency1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CurrencyRow
   */  
export function get_Companies_Company1_Currencies_Company_CurrencyCode(Company1:string, Company:string, CurrencyCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrencyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/Currencies(" + Company + "," + CurrencyCode + ")", {
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
         resolve(data as Erp_Tablesets_CurrencyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get CurrRateGrps items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CurrRateGrps1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateGrpRow
   */  
export function get_Companies_Company1_CurrRateGrps(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CurrRateGrps", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CurrRateGrp item
   Description: Calls GetByID to retrieve the CurrRateGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateGrp1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CurrRateGrpRow
   */  
export function get_Companies_Company1_CurrRateGrps_Company_RateGrpCode(Company1:string, Company:string, RateGrpCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrRateGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CurrRateGrps(" + Company + "," + RateGrpCode + ")", {
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
         resolve(data as Erp_Tablesets_CurrRateGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get EQSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EQSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EQSystRow
   */  
export function get_Companies_Company1_EQSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EQSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/EQSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EQSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the EQSyst item
   Description: Calls GetByID to retrieve the EQSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EQSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EQSystRow
   */  
export function get_Companies_Company1_EQSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EQSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/EQSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_EQSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ExtPRSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ExtPRSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRSystRow
   */  
export function get_Companies_Company1_ExtPRSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/ExtPRSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ExtPRSyst item
   Description: Calls GetByID to retrieve the ExtPRSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ExtPRSystRow
   */  
export function get_Companies_Company1_ExtPRSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtPRSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/ExtPRSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_ExtPRSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get FsSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_FsSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FsSystRow
   */  
export function get_Companies_Company1_FsSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FsSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/FsSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FsSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the FsSyst item
   Description: Calls GetByID to retrieve the FsSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FsSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FsSystRow
   */  
export function get_Companies_Company1_FsSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FsSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/FsSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_FsSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get GLSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GLSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLSystRow
   */  
export function get_Companies_Company1_GLSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/GLSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GLSyst item
   Description: Calls GetByID to retrieve the GLSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLSystRow
   */  
export function get_Companies_Company1_GLSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/GLSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_GLSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ISSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ISSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ISSystRow
   */  
export function get_Companies_Company1_ISSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ISSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/ISSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ISSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ISSyst item
   Description: Calls GetByID to retrieve the ISSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ISSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ISSystRow
   */  
export function get_Companies_Company1_ISSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ISSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/ISSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_ISSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get JCSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_JCSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JCSystRow
   */  
export function get_Companies_Company1_JCSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JCSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/JCSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JCSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the JCSyst item
   Description: Calls GetByID to retrieve the JCSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JCSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.JCSystRow
   */  
export function get_Companies_Company1_JCSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JCSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/JCSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_JCSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get MMSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_MMSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MMSystRow
   */  
export function get_Companies_Company1_MMSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MMSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/MMSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MMSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the MMSyst item
   Description: Calls GetByID to retrieve the MMSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MMSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MMSystRow
   */  
export function get_Companies_Company1_MMSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MMSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/MMSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_MMSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PDMSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PDMSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PDMSystRow
   */  
export function get_Companies_Company1_PDMSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PDMSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/PDMSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PDMSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PDMSyst item
   Description: Calls GetByID to retrieve the PDMSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PDMSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PDMSystRow
   */  
export function get_Companies_Company1_PDMSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PDMSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/PDMSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_PDMSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PECompWhldHists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PECompWhldHists1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PECompWhldHistRow
   */  
export function get_Companies_Company1_PECompWhldHists(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PECompWhldHistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/PECompWhldHists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PECompWhldHistRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PECompWhldHist item
   Description: Calls GetByID to retrieve the PECompWhldHist item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PECompWhldHist1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecordSeq Desc: RecordSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PECompWhldHistRow
   */  
export function get_Companies_Company1_PECompWhldHists_Company_RecordSeq(Company1:string, Company:string, RecordSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PECompWhldHistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/PECompWhldHists(" + Company + "," + RecordSeq + ")", {
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
         resolve(data as Erp_Tablesets_PECompWhldHistRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get PRSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PRSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRSystRow
   */  
export function get_Companies_Company1_PRSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/PRSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the PRSyst item
   Description: Calls GetByID to retrieve the PRSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PRSystRow
   */  
export function get_Companies_Company1_PRSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/PRSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_PRSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get TaxSvcConfigs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxSvcConfigs1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcConfigRow
   */  
export function get_Companies_Company1_TaxSvcConfigs(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcConfigRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/TaxSvcConfigs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcConfigRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the TaxSvcConfig item
   Description: Calls GetByID to retrieve the TaxSvcConfig item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcConfig1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   */  
export function get_Companies_Company1_TaxSvcConfigs_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxSvcConfigRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/TaxSvcConfigs(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_TaxSvcConfigRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get XaSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_XaSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.XaSystRow
   */  
export function get_Companies_Company1_XaSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_XaSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/XaSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_XaSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the XaSyst item
   Description: Calls GetByID to retrieve the XaSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_XaSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.XaSystRow
   */  
export function get_Companies_Company1_XaSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_XaSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/XaSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_XaSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get XbSysts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_XbSysts1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.XbSystRow
   */  
export function get_Companies_Company1_XbSysts(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_XbSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/XbSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_XbSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the XbSyst item
   Description: Calls GetByID to retrieve the XbSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_XbSyst1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.XbSystRow
   */  
export function get_Companies_Company1_XbSysts_Company(Company1:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_XbSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/XbSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_XbSystRow)
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
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
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
export function get_Companies_Company1_EntityGLCs(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/EntityGLCs", {
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
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
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
export function get_Companies_Company1_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company1:string, Company:string, RelatedToFile:string, Key1:string, Key2:string, Key3:string, Key4:string, Key5:string, Key6:string, GLControlType:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EntityGLCRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get CompanyAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CompanyAttches1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CompanyAttchRow
   */  
export function get_Companies_Company1_CompanyAttches(Company1:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CompanyAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CompanyAttch item
   Description: Calls GetByID to retrieve the CompanyAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CompanyAttch1
      @param Company1 Desc: Company1   Required: True   Allow empty value : True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CompanyAttchRow
   */  
export function get_Companies_Company1_CompanyAttches_Company_DrawingSeq(Company1:string, Company:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CompanyAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Companies(" + Company1 + ")/CompanyAttches(" + Company + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_CompanyAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get AGCompanies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AGCompanies
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AGCompanyRow
   */  
export function get_AGCompanies(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AGCompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/AGCompanies", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AGCompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AGCompanies
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AGCompanyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.AGCompanyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AGCompanies(requestBody:Erp_Tablesets_AGCompanyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/AGCompanies", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the AGCompany item
   Description: Calls GetByID to retrieve the AGCompany item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AGCompany
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.AGCompanyRow
   */  
export function get_AGCompanies_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_AGCompanyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/AGCompanies(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_AGCompanyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update AGCompany for the service
   Description: Calls UpdateExt to update AGCompany. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AGCompany
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.AGCompanyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_AGCompanies_Company(Company:string, requestBody:Erp_Tablesets_AGCompanyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/AGCompanies(" + Company + ")", {
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
   Summary: Call UpdateExt to delete AGCompany item
   Description: Call UpdateExt to delete AGCompany item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AGCompany
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_AGCompanies_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/AGCompanies(" + Company + ")", {
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
   Description: Get APSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APSystRow
   */  
export function get_APSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/APSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.APSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_APSysts(requestBody:Erp_Tablesets_APSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/APSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the APSyst item
   Description: Calls GetByID to retrieve the APSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.APSystRow
   */  
export function get_APSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_APSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/APSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_APSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update APSyst for the service
   Description: Calls UpdateExt to update APSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.APSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_APSysts_Company(Company:string, requestBody:Erp_Tablesets_APSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/APSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete APSyst item
   Description: Call UpdateExt to delete APSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_APSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/APSysts(" + Company + ")", {
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
   Description: Get ARSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ARSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ARSystRow
   */  
export function get_ARSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ARSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ARSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ARSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ARSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ARSysts(requestBody:Erp_Tablesets_ARSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ARSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ARSyst item
   Description: Calls GetByID to retrieve the ARSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ARSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ARSystRow
   */  
export function get_ARSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ARSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ARSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_ARSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ARSyst for the service
   Description: Calls UpdateExt to update ARSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ARSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ARSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ARSysts_Company(Company:string, requestBody:Erp_Tablesets_ARSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ARSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete ARSyst item
   Description: Call UpdateExt to delete ARSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ARSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ARSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ARSysts(" + Company + ")", {
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
   Description: Get BMSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BMSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BMSystRow
   */  
export function get_BMSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BMSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BMSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BMSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BMSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BMSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BMSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BMSysts(requestBody:Erp_Tablesets_BMSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BMSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the BMSyst item
   Description: Calls GetByID to retrieve the BMSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BMSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BMSystRow
   */  
export function get_BMSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BMSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BMSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_BMSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BMSyst for the service
   Description: Calls UpdateExt to update BMSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BMSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BMSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BMSysts_Company(Company:string, requestBody:Erp_Tablesets_BMSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BMSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete BMSyst item
   Description: Call UpdateExt to delete BMSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BMSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BMSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BMSysts(" + Company + ")", {
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
   Description: Get BorderPcts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_BorderPcts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.BorderPctRow
   */  
export function get_BorderPcts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BorderPctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BorderPcts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BorderPctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_BorderPcts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.BorderPctRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.BorderPctRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_BorderPcts(requestBody:Erp_Tablesets_BorderPctRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BorderPcts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the BorderPct item
   Description: Calls GetByID to retrieve the BorderPct item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_BorderPct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DestCountryNum Desc: DestCountryNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.BorderPctRow
   */  
export function get_BorderPcts_Company_DestCountryNum(Company:string, DestCountryNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_BorderPctRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BorderPcts(" + Company + "," + DestCountryNum + ")", {
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
         resolve(data as Erp_Tablesets_BorderPctRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update BorderPct for the service
   Description: Calls UpdateExt to update BorderPct. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_BorderPct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DestCountryNum Desc: DestCountryNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.BorderPctRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_BorderPcts_Company_DestCountryNum(Company:string, DestCountryNum:string, requestBody:Erp_Tablesets_BorderPctRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BorderPcts(" + Company + "," + DestCountryNum + ")", {
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
   Summary: Call UpdateExt to delete BorderPct item
   Description: Call UpdateExt to delete BorderPct item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_BorderPct
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DestCountryNum Desc: DestCountryNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_BorderPcts_Company_DestCountryNum(Company:string, DestCountryNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/BorderPcts(" + Company + "," + DestCountryNum + ")", {
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
   Description: Get CRSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CRSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CRSystRow
   */  
export function get_CRSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CRSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CRSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CRSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CRSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CRSysts(requestBody:Erp_Tablesets_CRSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CRSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CRSyst item
   Description: Calls GetByID to retrieve the CRSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CRSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CRSystRow
   */  
export function get_CRSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CRSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CRSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_CRSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CRSyst for the service
   Description: Calls UpdateExt to update CRSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CRSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CRSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CRSysts_Company(Company:string, requestBody:Erp_Tablesets_CRSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CRSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete CRSyst item
   Description: Call UpdateExt to delete CRSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CRSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CRSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CRSysts(" + Company + ")", {
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
   Description: Get CSFSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CSFSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CSFSystRow
   */  
export function get_CSFSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CSFSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CSFSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CSFSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CSFSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CSFSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CSFSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CSFSysts(requestBody:Erp_Tablesets_CSFSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CSFSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CSFSyst item
   Description: Calls GetByID to retrieve the CSFSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CSFSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CSFSystRow
   */  
export function get_CSFSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CSFSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CSFSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_CSFSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CSFSyst for the service
   Description: Calls UpdateExt to update CSFSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CSFSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CSFSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CSFSysts_Company(Company:string, requestBody:Erp_Tablesets_CSFSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CSFSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete CSFSyst item
   Description: Call UpdateExt to delete CSFSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CSFSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CSFSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CSFSysts(" + Company + ")", {
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
   Description: Get Currencies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Currencies
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrencyRow
   */  
export function get_Currencies(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Currencies", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Currencies
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrencyRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CurrencyRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Currencies(requestBody:Erp_Tablesets_CurrencyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Currencies", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the Currency item
   Description: Calls GetByID to retrieve the Currency item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Currency
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CurrencyRow
   */  
export function get_Currencies_Company_CurrencyCode(Company:string, CurrencyCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrencyRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Currencies(" + Company + "," + CurrencyCode + ")", {
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
         resolve(data as Erp_Tablesets_CurrencyRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Currency for the service
   Description: Calls UpdateExt to update Currency. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Currency
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrencyRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Currencies_Company_CurrencyCode(Company:string, CurrencyCode:string, requestBody:Erp_Tablesets_CurrencyRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Currencies(" + Company + "," + CurrencyCode + ")", {
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
   Summary: Call UpdateExt to delete Currency item
   Description: Call UpdateExt to delete Currency item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Currency
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CurrencyCode Desc: CurrencyCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Currencies_Company_CurrencyCode(Company:string, CurrencyCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Currencies(" + Company + "," + CurrencyCode + ")", {
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
   Description: Get CurrRateGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrRateGrps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrRateGrpRow
   */  
export function get_CurrRateGrps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CurrRateGrps", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrRateGrps
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CurrRateGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CurrRateGrps(requestBody:Erp_Tablesets_CurrRateGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CurrRateGrps", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CurrRateGrp item
   Description: Calls GetByID to retrieve the CurrRateGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrRateGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CurrRateGrpRow
   */  
export function get_CurrRateGrps_Company_RateGrpCode(Company:string, RateGrpCode:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrRateGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")", {
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
         resolve(data as Erp_Tablesets_CurrRateGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CurrRateGrp for the service
   Description: Calls UpdateExt to update CurrRateGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrRateGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrRateGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CurrRateGrps_Company_RateGrpCode(Company:string, RateGrpCode:string, requestBody:Erp_Tablesets_CurrRateGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")", {
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
   Summary: Call UpdateExt to delete CurrRateGrp item
   Description: Call UpdateExt to delete CurrRateGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrRateGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CurrRateGrps_Company_RateGrpCode(Company:string, RateGrpCode:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CurrRateGrps(" + Company + "," + RateGrpCode + ")", {
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
   Description: Get EQSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EQSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EQSystRow
   */  
export function get_EQSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EQSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EQSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EQSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EQSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EQSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.EQSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_EQSysts(requestBody:Erp_Tablesets_EQSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EQSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the EQSyst item
   Description: Calls GetByID to retrieve the EQSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EQSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.EQSystRow
   */  
export function get_EQSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_EQSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EQSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_EQSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update EQSyst for the service
   Description: Calls UpdateExt to update EQSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EQSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.EQSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_EQSysts_Company(Company:string, requestBody:Erp_Tablesets_EQSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EQSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete EQSyst item
   Description: Call UpdateExt to delete EQSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EQSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_EQSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EQSysts(" + Company + ")", {
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
   Description: Get ExtPRSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ExtPRSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ExtPRSystRow
   */  
export function get_ExtPRSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ExtPRSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ExtPRSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ExtPRSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ExtPRSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtPRSysts(requestBody:Erp_Tablesets_ExtPRSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ExtPRSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ExtPRSyst item
   Description: Calls GetByID to retrieve the ExtPRSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ExtPRSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ExtPRSystRow
   */  
export function get_ExtPRSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ExtPRSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ExtPRSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_ExtPRSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ExtPRSyst for the service
   Description: Calls UpdateExt to update ExtPRSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ExtPRSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ExtPRSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ExtPRSysts_Company(Company:string, requestBody:Erp_Tablesets_ExtPRSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ExtPRSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete ExtPRSyst item
   Description: Call UpdateExt to delete ExtPRSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ExtPRSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ExtPRSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ExtPRSysts(" + Company + ")", {
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
   Description: Get FsSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_FsSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.FsSystRow
   */  
export function get_FsSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FsSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/FsSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FsSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_FsSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.FsSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.FsSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FsSysts(requestBody:Erp_Tablesets_FsSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/FsSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the FsSyst item
   Description: Calls GetByID to retrieve the FsSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_FsSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.FsSystRow
   */  
export function get_FsSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_FsSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/FsSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_FsSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update FsSyst for the service
   Description: Calls UpdateExt to update FsSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_FsSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.FsSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_FsSysts_Company(Company:string, requestBody:Erp_Tablesets_FsSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/FsSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete FsSyst item
   Description: Call UpdateExt to delete FsSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_FsSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_FsSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/FsSysts(" + Company + ")", {
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
   Description: Get GLSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLSystRow
   */  
export function get_GLSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GLSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLSysts(requestBody:Erp_Tablesets_GLSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GLSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the GLSyst item
   Description: Calls GetByID to retrieve the GLSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLSystRow
   */  
export function get_GLSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GLSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_GLSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLSyst for the service
   Description: Calls UpdateExt to update GLSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLSysts_Company(Company:string, requestBody:Erp_Tablesets_GLSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GLSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete GLSyst item
   Description: Call UpdateExt to delete GLSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GLSysts(" + Company + ")", {
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
   Description: Get ISSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ISSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ISSystRow
   */  
export function get_ISSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ISSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ISSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ISSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ISSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ISSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.ISSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ISSysts(requestBody:Erp_Tablesets_ISSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ISSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the ISSyst item
   Description: Calls GetByID to retrieve the ISSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ISSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.ISSystRow
   */  
export function get_ISSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_ISSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ISSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_ISSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ISSyst for the service
   Description: Calls UpdateExt to update ISSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ISSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.ISSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ISSysts_Company(Company:string, requestBody:Erp_Tablesets_ISSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ISSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete ISSyst item
   Description: Call UpdateExt to delete ISSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ISSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ISSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ISSysts(" + Company + ")", {
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
   Description: Get JCSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_JCSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.JCSystRow
   */  
export function get_JCSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JCSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/JCSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JCSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_JCSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.JCSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.JCSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_JCSysts(requestBody:Erp_Tablesets_JCSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/JCSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the JCSyst item
   Description: Calls GetByID to retrieve the JCSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_JCSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.JCSystRow
   */  
export function get_JCSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_JCSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/JCSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_JCSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update JCSyst for the service
   Description: Calls UpdateExt to update JCSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_JCSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.JCSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_JCSysts_Company(Company:string, requestBody:Erp_Tablesets_JCSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/JCSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete JCSyst item
   Description: Call UpdateExt to delete JCSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_JCSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_JCSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/JCSysts(" + Company + ")", {
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
   Description: Get MMSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MMSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MMSystRow
   */  
export function get_MMSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MMSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/MMSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MMSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MMSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MMSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MMSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MMSysts(requestBody:Erp_Tablesets_MMSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/MMSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the MMSyst item
   Description: Calls GetByID to retrieve the MMSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MMSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MMSystRow
   */  
export function get_MMSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MMSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/MMSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_MMSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MMSyst for the service
   Description: Calls UpdateExt to update MMSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MMSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MMSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MMSysts_Company(Company:string, requestBody:Erp_Tablesets_MMSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/MMSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete MMSyst item
   Description: Call UpdateExt to delete MMSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MMSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MMSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/MMSysts(" + Company + ")", {
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
   Description: Get PDMSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PDMSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PDMSystRow
   */  
export function get_PDMSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PDMSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PDMSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PDMSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PDMSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PDMSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PDMSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PDMSysts(requestBody:Erp_Tablesets_PDMSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PDMSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PDMSyst item
   Description: Calls GetByID to retrieve the PDMSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PDMSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PDMSystRow
   */  
export function get_PDMSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PDMSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PDMSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_PDMSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PDMSyst for the service
   Description: Calls UpdateExt to update PDMSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PDMSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PDMSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PDMSysts_Company(Company:string, requestBody:Erp_Tablesets_PDMSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PDMSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete PDMSyst item
   Description: Call UpdateExt to delete PDMSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PDMSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PDMSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PDMSysts(" + Company + ")", {
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
   Description: Get PECompWhldHists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PECompWhldHists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PECompWhldHistRow
   */  
export function get_PECompWhldHists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PECompWhldHistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PECompWhldHists", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PECompWhldHistRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PECompWhldHists
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PECompWhldHistRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PECompWhldHistRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PECompWhldHists(requestBody:Erp_Tablesets_PECompWhldHistRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PECompWhldHists", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PECompWhldHist item
   Description: Calls GetByID to retrieve the PECompWhldHist item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PECompWhldHist
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecordSeq Desc: RecordSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PECompWhldHistRow
   */  
export function get_PECompWhldHists_Company_RecordSeq(Company:string, RecordSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PECompWhldHistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PECompWhldHists(" + Company + "," + RecordSeq + ")", {
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
         resolve(data as Erp_Tablesets_PECompWhldHistRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PECompWhldHist for the service
   Description: Calls UpdateExt to update PECompWhldHist. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PECompWhldHist
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecordSeq Desc: RecordSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PECompWhldHistRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PECompWhldHists_Company_RecordSeq(Company:string, RecordSeq:string, requestBody:Erp_Tablesets_PECompWhldHistRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PECompWhldHists(" + Company + "," + RecordSeq + ")", {
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
   Summary: Call UpdateExt to delete PECompWhldHist item
   Description: Call UpdateExt to delete PECompWhldHist item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PECompWhldHist
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RecordSeq Desc: RecordSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PECompWhldHists_Company_RecordSeq(Company:string, RecordSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PECompWhldHists(" + Company + "," + RecordSeq + ")", {
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
   Description: Get PRSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PRSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PRSystRow
   */  
export function get_PRSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PRSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PRSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PRSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PRSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PRSysts(requestBody:Erp_Tablesets_PRSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PRSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the PRSyst item
   Description: Calls GetByID to retrieve the PRSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PRSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PRSystRow
   */  
export function get_PRSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PRSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PRSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_PRSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PRSyst for the service
   Description: Calls UpdateExt to update PRSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PRSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PRSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PRSysts_Company(Company:string, requestBody:Erp_Tablesets_PRSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PRSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete PRSyst item
   Description: Call UpdateExt to delete PRSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PRSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PRSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/PRSysts(" + Company + ")", {
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
   Description: Get TaxSvcConfigs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxSvcConfigs
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcConfigRow
   */  
export function get_TaxSvcConfigs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcConfigRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/TaxSvcConfigs", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcConfigRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxSvcConfigs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.TaxSvcConfigRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxSvcConfigs(requestBody:Erp_Tablesets_TaxSvcConfigRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/TaxSvcConfigs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the TaxSvcConfig item
   Description: Calls GetByID to retrieve the TaxSvcConfig item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxSvcConfig
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   */  
export function get_TaxSvcConfigs_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxSvcConfigRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/TaxSvcConfigs(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_TaxSvcConfigRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update TaxSvcConfig for the service
   Description: Calls UpdateExt to update TaxSvcConfig. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxSvcConfig
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxSvcConfigs_Company(Company:string, requestBody:Erp_Tablesets_TaxSvcConfigRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/TaxSvcConfigs(" + Company + ")", {
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
   Summary: Call UpdateExt to delete TaxSvcConfig item
   Description: Call UpdateExt to delete TaxSvcConfig item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxSvcConfig
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_TaxSvcConfigs_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/TaxSvcConfigs(" + Company + ")", {
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
   Description: Get XaSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_XaSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.XaSystRow
   */  
export function get_XaSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_XaSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XaSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_XaSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_XaSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.XaSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.XaSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_XaSysts(requestBody:Erp_Tablesets_XaSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XaSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the XaSyst item
   Description: Calls GetByID to retrieve the XaSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_XaSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.XaSystRow
   */  
export function get_XaSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_XaSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XaSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_XaSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update XaSyst for the service
   Description: Calls UpdateExt to update XaSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_XaSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.XaSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_XaSysts_Company(Company:string, requestBody:Erp_Tablesets_XaSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XaSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete XaSyst item
   Description: Call UpdateExt to delete XaSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_XaSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_XaSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XaSysts(" + Company + ")", {
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
   Description: Get XbSysts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_XbSysts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.XbSystRow
   */  
export function get_XbSysts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_XbSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XbSysts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_XbSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_XbSysts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.XbSystRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.XbSystRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_XbSysts(requestBody:Erp_Tablesets_XbSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XbSysts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the XbSyst item
   Description: Calls GetByID to retrieve the XbSyst item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_XbSyst
      @param Company Desc: Company   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.XbSystRow
   */  
export function get_XbSysts_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_XbSystRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XbSysts(" + Company + ")", {
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
         resolve(data as Erp_Tablesets_XbSystRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update XbSyst for the service
   Description: Calls UpdateExt to update XbSyst. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_XbSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.XbSystRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_XbSysts_Company(Company:string, requestBody:Erp_Tablesets_XbSystRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XbSysts(" + Company + ")", {
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
   Summary: Call UpdateExt to delete XbSyst item
   Description: Call UpdateExt to delete XbSyst item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_XbSyst
      @param Company Desc: Company   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_XbSysts_Company(Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/XbSysts(" + Company + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EntityGLCs", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EntityGLCs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", {
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
   Description: Get CompanyAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CompanyAttches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CompanyAttchRow
   */  
export function get_CompanyAttches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CompanyAttches", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CompanyAttches
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CompanyAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CompanyAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CompanyAttches(requestBody:Erp_Tablesets_CompanyAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CompanyAttches", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CompanyAttch item
   Description: Calls GetByID to retrieve the CompanyAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CompanyAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CompanyAttchRow
   */  
export function get_CompanyAttches_Company_DrawingSeq(Company:string, DrawingSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CompanyAttchRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CompanyAttches(" + Company + "," + DrawingSeq + ")", {
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
         resolve(data as Erp_Tablesets_CompanyAttchRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CompanyAttch for the service
   Description: Calls UpdateExt to update CompanyAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CompanyAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CompanyAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CompanyAttches_Company_DrawingSeq(Company:string, DrawingSeq:string, requestBody:Erp_Tablesets_CompanyAttchRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CompanyAttches(" + Company + "," + DrawingSeq + ")", {
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
   Summary: Call UpdateExt to delete CompanyAttch item
   Description: Call UpdateExt to delete CompanyAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CompanyAttch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param DrawingSeq Desc: DrawingSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CompanyAttches_Company_DrawingSeq(Company:string, DrawingSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CompanyAttches(" + Company + "," + DrawingSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CompanyListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyListRow)
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
export function get_GetRows(whereClauseCompany:string, whereClauseCompanyAttch:string, whereClauseAGCompany:string, whereClauseAPSyst:string, whereClauseARSyst:string, whereClauseBMSyst:string, whereClauseBorderPct:string, whereClauseCRSyst:string, whereClauseCSFSyst:string, whereClauseCurrency:string, whereClauseCurrRateGrp:string, whereClauseEQSyst:string, whereClauseExtPRSyst:string, whereClauseFsSyst:string, whereClauseGLSyst:string, whereClauseISSyst:string, whereClauseJCSyst:string, whereClauseMMSyst:string, whereClausePDMSyst:string, whereClausePECompWhldHist:string, whereClausePRSyst:string, whereClauseTaxSvcConfig:string, whereClauseXaSyst:string, whereClauseXbSyst:string, whereClauseEntityGLC:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCompany!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCompany=" + whereClauseCompany
   }
   if(typeof whereClauseCompanyAttch!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCompanyAttch=" + whereClauseCompanyAttch
   }
   if(typeof whereClauseAGCompany!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAGCompany=" + whereClauseAGCompany
   }
   if(typeof whereClauseAPSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseAPSyst=" + whereClauseAPSyst
   }
   if(typeof whereClauseARSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseARSyst=" + whereClauseARSyst
   }
   if(typeof whereClauseBMSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBMSyst=" + whereClauseBMSyst
   }
   if(typeof whereClauseBorderPct!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseBorderPct=" + whereClauseBorderPct
   }
   if(typeof whereClauseCRSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCRSyst=" + whereClauseCRSyst
   }
   if(typeof whereClauseCSFSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCSFSyst=" + whereClauseCSFSyst
   }
   if(typeof whereClauseCurrency!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCurrency=" + whereClauseCurrency
   }
   if(typeof whereClauseCurrRateGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCurrRateGrp=" + whereClauseCurrRateGrp
   }
   if(typeof whereClauseEQSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseEQSyst=" + whereClauseEQSyst
   }
   if(typeof whereClauseExtPRSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseExtPRSyst=" + whereClauseExtPRSyst
   }
   if(typeof whereClauseFsSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseFsSyst=" + whereClauseFsSyst
   }
   if(typeof whereClauseGLSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLSyst=" + whereClauseGLSyst
   }
   if(typeof whereClauseISSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseISSyst=" + whereClauseISSyst
   }
   if(typeof whereClauseJCSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseJCSyst=" + whereClauseJCSyst
   }
   if(typeof whereClauseMMSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMMSyst=" + whereClauseMMSyst
   }
   if(typeof whereClausePDMSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePDMSyst=" + whereClausePDMSyst
   }
   if(typeof whereClausePECompWhldHist!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePECompWhldHist=" + whereClausePECompWhldHist
   }
   if(typeof whereClausePRSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePRSyst=" + whereClausePRSyst
   }
   if(typeof whereClauseTaxSvcConfig!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxSvcConfig=" + whereClauseTaxSvcConfig
   }
   if(typeof whereClauseXaSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseXaSyst=" + whereClauseXaSyst
   }
   if(typeof whereClauseXbSyst!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseXbSyst=" + whereClauseXbSyst
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetRows" + params, {
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
export function get_GetByID(company:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof company!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "company=" + company
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetByID" + params, {
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
   Summary: Invoke method ChangeJPFiscalCalendarID
   Description: Performs required logic when XbSyst.JPFiscalCalendarID is modified.
   OperationID: ChangeJPFiscalCalendarID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeJPFiscalCalendarID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJPFiscalCalendarID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJPFiscalCalendarID(requestBody:ChangeJPFiscalCalendarID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeJPFiscalCalendarID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ChangeJPFiscalCalendarID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeJPFiscalCalendarID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSendToFSA
   Description: Performs required logic when Company.SendToFSA is modified.
   OperationID: ChangeSendToFSA
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSendToFSA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSendToFSA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSendToFSA(requestBody:ChangeSendToFSA_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSendToFSA_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ChangeSendToFSA", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeSendToFSA_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckAPTaxLnLevel
   Description: This method will determine if the APTaxLnLevel is changing and output a message to the user
   OperationID: CheckAPTaxLnLevel
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckAPTaxLnLevel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAPTaxLnLevel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAPTaxLnLevel(requestBody:CheckAPTaxLnLevel_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckAPTaxLnLevel_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CheckAPTaxLnLevel", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckAPTaxLnLevel_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckARinvcDates
   Description: This method test the link of the dates in AR Invoice
   OperationID: CheckARinvcDates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckARinvcDates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckARinvcDates(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckARinvcDates_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CheckARinvcDates", {
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
         resolve(data as CheckARinvcDates_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDefTaxLiability
   Description: This method checks whether Tax Liability exists and not flagged as used in Tax Connect
   OperationID: CheckDefTaxLiability
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDefTaxLiability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDefTaxLiability_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDefTaxLiability(requestBody:CheckDefTaxLiability_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDefTaxLiability_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CheckDefTaxLiability", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckDefTaxLiability_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDefTaxType
   Description: This method checks whether Tax Type exists
   OperationID: CheckDefTaxType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDefTaxType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDefTaxType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDefTaxType(requestBody:CheckDefTaxType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDefTaxType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CheckDefTaxType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckDefTaxType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPayrollDate
   Description: This method is to be run before the update method (or on leave of the field).
If there is a problem with the date, a message will be returned for the user to approve
or cancel.  If the user approved the error, then the update method can be run.
   OperationID: CheckPayrollDate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPayrollDate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPayrollDate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPayrollDate(requestBody:CheckPayrollDate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPayrollDate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CheckPayrollDate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckPayrollDate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckRedStornoOpt
   Description: Prevent setting this option if tran type docs have red storno set
   OperationID: CheckRedStornoOpt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckRedStornoOpt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRedStornoOpt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckRedStornoOpt(requestBody:CheckRedStornoOpt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckRedStornoOpt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CheckRedStornoOpt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckRedStornoOpt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckUDCodeEx
   Description: Checks whether user-defined code exists and active.
   OperationID: CheckUDCodeEx
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckUDCodeEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckUDCodeEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckUDCodeEx(requestBody:CheckUDCodeEx_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckUDCodeEx_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CheckUDCodeEx", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckUDCodeEx_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckUDCodesExistence
   Description: Checks whether user-defined code exists and active.
   OperationID: CheckUDCodesExistence
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckUDCodesExistence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckUDCodesExistence_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckUDCodesExistence(requestBody:CheckUDCodesExistence_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckUDCodesExistence_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CheckUDCodesExistence", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckUDCodesExistence_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckVATFormat
   Description: This method test the validity of the VAT format
   OperationID: CheckVATFormat
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckVATFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckVATFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckVATFormat(requestBody:CheckVATFormat_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckVATFormat_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CheckVATFormat", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckVATFormat_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChgCompanyFisCal
   Description: none
   OperationID: ChgCompanyFisCal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChgCompanyFisCal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChgCompanyFisCal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChgCompanyFisCal(requestBody:ChgCompanyFisCal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChgCompanyFisCal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ChgCompanyFisCal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChgCompanyFisCal_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChgCountry
   Description: This method defaults the tax region information when the Company.CountryNum
field changes
   OperationID: ChgCountry
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChgCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChgCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChgCountry(requestBody:ChgCountry_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChgCountry_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ChgCountry", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChgCountry_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChgingMJTemplate
   Description: This method defaults the Maintenance Job Description when the MMSyst.TemplateJobNum
field changes
   OperationID: ChgingMJTemplate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChgingMJTemplate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChgingMJTemplate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChgingMJTemplate(requestBody:ChgingMJTemplate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChgingMJTemplate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ChgingMJTemplate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChgingMJTemplate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChgJCSystForecastPeriods
   Description: none
   OperationID: ChgJCSystForecastPeriods
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChgJCSystForecastPeriods_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChgJCSystForecastPeriods_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChgJCSystForecastPeriods(requestBody:ChgJCSystForecastPeriods_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChgJCSystForecastPeriods_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ChgJCSystForecastPeriods", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChgJCSystForecastPeriods_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CleanHCMLink
   Description: This method remove all HCM Link on related Payroll tables.
   OperationID: CleanHCMLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CleanHCMLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CleanHCMLink(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CleanHCMLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CleanHCMLink", {
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
         resolve(data as CleanHCMLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DisabledGLFields
   Description: This method sens back a list of fields to be disabled
   OperationID: DisabledGLFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DisabledGLFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DisabledGLFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DisabledGLFields(requestBody:DisabledGLFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DisabledGLFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/DisabledGLFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DisabledGLFields_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ETCAfterAddrVal
   Description: After the tax integration has been called, update the Company address if it
was changed.
   OperationID: ETCAfterAddrVal
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ETCAfterAddrVal_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ETCAfterAddrVal_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ETCAfterAddrVal(requestBody:ETCAfterAddrVal_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ETCAfterAddrVal_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ETCAfterAddrVal", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ETCAfterAddrVal_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ETCValidateAddress
   Description: Call tax integration and loads temp tables from the results.
   OperationID: ETCValidateAddress
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ETCValidateAddress_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ETCValidateAddress_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ETCValidateAddress(requestBody:ETCValidateAddress_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ETCValidateAddress_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ETCValidateAddress", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ETCValidateAddress_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FormatList
   Description: This method returns the list of available G/L account format styles
   OperationID: FormatList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FormatList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FormatList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FormatList(requestBody:FormatList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FormatList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/FormatList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as FormatList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetBookMethodList
   Description: Get list of revision statuses.
   OperationID: GetBookMethodList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBookMethodList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetBookMethodList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetBookMethodList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetBookMethodList", {
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
         resolve(data as GetBookMethodList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCheckOffLabels
   Description: This method returns a delimited list of the CheckOff labels for either Job, Quote or DMR
   OperationID: GetCheckOffLabels
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCheckOffLabels_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCheckOffLabels_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCheckOffLabels(requestBody:GetCheckOffLabels_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCheckOffLabels_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetCheckOffLabels", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetCheckOffLabels_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCPayCompanyList
   Description: This method returns a list of valid Central Payment 'Parent Company' IDs
UI note - user should  select only ONE of the valid codes.
   OperationID: GetCPayCompanyList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCPayCompanyList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCPayCompanyList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCPayCompanyList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetCPayCompanyList", {
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
         resolve(data as GetCPayCompanyList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetModLicensing
   Description: This method returns the licensing flags for the company beging updates.
If updating a company different from the one logged in on, then you need
to use these variables in your licensing checks
   OperationID: GetModLicensing
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetModLicensing_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetModLicensing_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetModLicensing(requestBody:GetModLicensing_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetModLicensing_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetModLicensing", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetModLicensing_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBorderPercent
   Description: This method replaces the standard GetNewBorderPct() method so the Company can be
passed as a parameter
   OperationID: GetNewBorderPercent
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBorderPercent_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBorderPercent_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBorderPercent(requestBody:GetNewBorderPercent_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBorderPercent_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewBorderPercent", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewBorderPercent_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSerialNumbers
   Description: This method provides a list of license serial number available for use
   OperationID: GetSerialNumbers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSerialNumbers(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSerialNumbers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetSerialNumbers", {
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
         resolve(data as GetSerialNumbers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeBankAcctID
   Description: OnChangeBankAcctID
   OperationID: OnChangeBankAcctID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBankAcctID(requestBody:OnChangeBankAcctID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBankAcctID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangeBankAcctID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeBankAcctID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeARBankAcctID
   Description: OnChangeARankAcctID
   OperationID: OnChangeARBankAcctID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeARBankAcctID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeARBankAcctID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeARBankAcctID(requestBody:OnChangeARBankAcctID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeARBankAcctID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangeARBankAcctID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeARBankAcctID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeCentralCollectionParentCompany
   Description: This method allow to validate if there are still customers or un-posted invoices with central collection.
   OperationID: OnChangeCentralCollectionParentCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeCentralCollectionParentCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCentralCollectionParentCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeCentralCollectionParentCompany(requestBody:OnChangeCentralCollectionParentCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeCentralCollectionParentCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangeCentralCollectionParentCompany", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeCentralCollectionParentCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeUseAltBillToAddr
   Description: OnChangeUseAltBillToAddr
   OperationID: OnChangeUseAltBillToAddr
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeUseAltBillToAddr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUseAltBillToAddr_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeUseAltBillToAddr(requestBody:OnChangeUseAltBillToAddr_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeUseAltBillToAddr_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangeUseAltBillToAddr", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeUseAltBillToAddr_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAddrValEnabled
   Description: OnChangeAddrValEnabled
   OperationID: OnChangeAddrValEnabled
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAddrValEnabled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAddrValEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAddrValEnabled(requestBody:OnChangeAddrValEnabled_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAddrValEnabled_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangeAddrValEnabled", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeAddrValEnabled_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeDefTaxLiability
   Description: This method should be called when Default Tax Liability is changed
   OperationID: OnChangeDefTaxLiability
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeDefTaxLiability_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeDefTaxLiability_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeDefTaxLiability(requestBody:OnChangeDefTaxLiability_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeDefTaxLiability_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangeDefTaxLiability", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeDefTaxLiability_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFlow
   Description: This method should be called when Flow value is changed
   OperationID: OnChangeFlow
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFlow_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFlow_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFlow(requestBody:OnChangeFlow_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFlow_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangeFlow", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeFlow_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMasterChart
   Description: This method is called when the MasterCOA is changed.
   OperationID: OnChangeMasterChart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMasterChart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMasterChart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMasterChart(requestBody:OnChangeMasterChart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMasterChart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangeMasterChart", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeMasterChart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeGJJournalCode
   Description: This method is called when the GJJournalCode is changed.
   OperationID: OnChangeGJJournalCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeGJJournalCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeGJJournalCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeGJJournalCode(requestBody:OnChangeGJJournalCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeGJJournalCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangeGJJournalCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeGJJournalCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingDestCountryNum
   Description: This method should be called when Destination Country is Changed
   OperationID: OnChangingDestCountryNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingDestCountryNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingDestCountryNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingDestCountryNum(requestBody:OnChangingDestCountryNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingDestCountryNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangingDestCountryNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingDestCountryNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSiteIsLegalEntity
   Description: This method should be called when SiteIsLegalEntity is changed
   OperationID: OnChangeSiteIsLegalEntity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSiteIsLegalEntity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSiteIsLegalEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSiteIsLegalEntity(requestBody:OnChangeSiteIsLegalEntity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSiteIsLegalEntity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangeSiteIsLegalEntity", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeSiteIsLegalEntity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingSubRateGrp
   Description: This method should be called when SubRateGrp is Changed
   OperationID: OnChangingSubRateGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingSubRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSubRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingSubRateGrp(requestBody:OnChangingSubRateGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingSubRateGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangingSubRateGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangingSubRateGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TestTaxConnection
   Description: This method will test the tax integration connection to Avalara
   OperationID: TestTaxConnection
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/TestTaxConnection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestTaxConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestTaxConnection(requestBody:TestTaxConnection_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<TestTaxConnection_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/TestTaxConnection", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as TestTaxConnection_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method TestExtCRMConnection
   Description: Tests the connection for Salesforce
   OperationID: TestExtCRMConnection
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestExtCRMConnection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TestExtCRMConnection(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<TestExtCRMConnection_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/TestExtCRMConnection", {
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
         resolve(data as TestExtCRMConnection_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeTranDocType
   Description: OnChangeTranDocType
   OperationID: OnChangeTranDocType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeTranDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeTranDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeTranDocType(requestBody:OnChangeTranDocType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeTranDocType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangeTranDocType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeTranDocType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeELIDefReportID
   Description: OnChangeELIDefReportID
   OperationID: OnChangeELIDefReportID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeELIDefReportID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeELIDefReportID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeELIDefReportID(requestBody:OnChangeELIDefReportID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeELIDefReportID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangeELIDefReportID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeELIDefReportID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeELIDefEinvoicePath
   Description: Invoked when ELIDefEinvoicePath is changed
   OperationID: OnChangeELIDefEinvoicePath
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeELIDefEinvoicePath_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeELIDefEinvoicePath_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeELIDefEinvoicePath(requestBody:OnChangeELIDefEinvoicePath_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeELIDefEinvoicePath_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/OnChangeELIDefEinvoicePath", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeELIDefEinvoicePath_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOCRAlgorithmList
   Description: This method returns a list of valid OCR Algorithms
   OperationID: GetOCRAlgorithmList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOCRAlgorithmList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOCRAlgorithmList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetOCRAlgorithmList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetOCRAlgorithmList", {
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
         resolve(data as GetOCRAlgorithmList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetMaxWorkQueueRecords
   Description: This method returns the value MaxWorkQueueRecords parameter in XaSyst
   OperationID: GetMaxWorkQueueRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMaxWorkQueueRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetMaxWorkQueueRecords(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetMaxWorkQueueRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetMaxWorkQueueRecords", {
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
         resolve(data as GetMaxWorkQueueRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   Description: none
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method InitializeCompany
   Description: none
   OperationID: InitializeCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InitializeCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InitializeCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InitializeCompany(requestBody:InitializeCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InitializeCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/InitializeCompany", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as InitializeCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSystemTimeZoneList
   Description: This method returns a list of Microsoft Time Zone Index Values and their corresponding display name
   OperationID: GetSystemTimeZoneList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSystemTimeZoneList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSystemTimeZoneList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSystemTimeZoneList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetSystemTimeZoneList", {
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
         resolve(data as GetSystemTimeZoneList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method NLCopyDigipoortSettingToAllCompanies
   Description: Copy Digipoort setting to all Netherlands companies
   OperationID: NLCopyDigipoortSettingToAllCompanies
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/NLCopyDigipoortSettingToAllCompanies_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NLCopyDigipoortSettingToAllCompanies(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<NLCopyDigipoortSettingToAllCompanies_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/NLCopyDigipoortSettingToAllCompanies", {
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
         resolve(data as NLCopyDigipoortSettingToAllCompanies_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInitialPath
   Description: Get the initial default path where the  Configuration file is going to be created
   OperationID: GetInitialPath
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInitialPath_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInitialPath(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInitialPath_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetInitialPath", {
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
         resolve(data as GetInitialPath_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSendToFSA
   Description: Method that validates if the SendToFSA flag was changed to false.
   OperationID: ValidateSendToFSA
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSendToFSA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSendToFSA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSendToFSA(requestBody:ValidateSendToFSA_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSendToFSA_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ValidateSendToFSA", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateSendToFSA_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateIntrastatCodeForCompany
   Description: Method that validates if Intrastat code is configured for Company Country
   OperationID: ValidateIntrastatCodeForCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateIntrastatCodeForCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateIntrastatCodeForCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateIntrastatCodeForCompany(requestBody:ValidateIntrastatCodeForCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateIntrastatCodeForCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ValidateIntrastatCodeForCompany", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateIntrastatCodeForCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLegalNumbers
   Description: return the tran doc types linked to legal numbers to fill the combo
   OperationID: GetLegalNumbers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetLegalNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLegalNumbers(requestBody:GetLegalNumbers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLegalNumbers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetLegalNumbers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetLegalNumbers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQuickShipURL
   Description: Retrieve the Quick Ship URL
   OperationID: GetQuickShipURL
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQuickShipURL_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQuickShipURL(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetQuickShipURL_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetQuickShipURL", {
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
         resolve(data as GetQuickShipURL_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CompanyTaxConnectEnabled
   Description: Returns if tax connect is enabled
   OperationID: CompanyTaxConnectEnabled
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CompanyTaxConnectEnabled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CompanyTaxConnectEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CompanyTaxConnectEnabled(requestBody:CompanyTaxConnectEnabled_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CompanyTaxConnectEnabled_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CompanyTaxConnectEnabled", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CompanyTaxConnectEnabled_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CompanyTaxConnectCertCaptureEnabled
   Description: Returns if avalara certcapture is enabled
   OperationID: CompanyTaxConnectCertCaptureEnabled
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CompanyTaxConnectCertCaptureEnabled_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CompanyTaxConnectCertCaptureEnabled_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CompanyTaxConnectCertCaptureEnabled(requestBody:CompanyTaxConnectCertCaptureEnabled_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CompanyTaxConnectCertCaptureEnabled_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/CompanyTaxConnectCertCaptureEnabled", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CompanyTaxConnectCertCaptureEnabled_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SiteIsLegalEntity
   Description: Indicates site can be used as a legal entity.
   OperationID: SiteIsLegalEntity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/SiteIsLegalEntity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SiteIsLegalEntity(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SiteIsLegalEntity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/SiteIsLegalEntity", {
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
         resolve(data as SiteIsLegalEntity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateMYIndustryCodeOnChanging
   Description: Validate and correct proposed Industry Code value
   OperationID: ValidateMYIndustryCodeOnChanging
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateMYIndustryCodeOnChanging_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateMYIndustryCodeOnChanging_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateMYIndustryCodeOnChanging(requestBody:ValidateMYIndustryCodeOnChanging_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateMYIndustryCodeOnChanging_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/ValidateMYIndustryCodeOnChanging", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateMYIndustryCodeOnChanging_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCompany
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCompany(requestBody:GetNewCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewCompany", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCompanyAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCompanyAttch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCompanyAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCompanyAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCompanyAttch(requestBody:GetNewCompanyAttch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCompanyAttch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewCompanyAttch", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCompanyAttch_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAGCompany
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAGCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAGCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAGCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAGCompany(requestBody:GetNewAGCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAGCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewAGCompany", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewAGCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewAPSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewAPSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewAPSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewAPSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewAPSyst(requestBody:GetNewAPSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewAPSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewAPSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewAPSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewARSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewARSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewARSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewARSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewARSyst(requestBody:GetNewARSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewARSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewARSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewARSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBMSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBMSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBMSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBMSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBMSyst(requestBody:GetNewBMSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBMSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewBMSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewBMSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewBorderPct
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewBorderPct
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewBorderPct_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewBorderPct_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewBorderPct(requestBody:GetNewBorderPct_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewBorderPct_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewBorderPct", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewBorderPct_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCRSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCRSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCRSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCRSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCRSyst(requestBody:GetNewCRSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCRSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewCRSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCRSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCSFSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCSFSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCSFSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCSFSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCSFSyst(requestBody:GetNewCSFSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCSFSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewCSFSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCSFSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCurrency
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrency
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCurrency_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrency_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCurrency(requestBody:GetNewCurrency_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCurrency_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewCurrency", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCurrency_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCurrRateGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrRateGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCurrRateGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrRateGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCurrRateGrp(requestBody:GetNewCurrRateGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCurrRateGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewCurrRateGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCurrRateGrp_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewEQSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEQSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewEQSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEQSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewEQSyst(requestBody:GetNewEQSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewEQSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewEQSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewEQSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewExtPRSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewExtPRSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewExtPRSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewExtPRSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewExtPRSyst(requestBody:GetNewExtPRSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewExtPRSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewExtPRSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewExtPRSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewFsSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewFsSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewFsSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewFsSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewFsSyst(requestBody:GetNewFsSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewFsSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewFsSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewFsSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLSyst(requestBody:GetNewGLSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewGLSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewGLSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewISSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewISSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewISSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewISSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewISSyst(requestBody:GetNewISSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewISSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewISSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewISSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewJCSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewJCSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewJCSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewJCSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewJCSyst(requestBody:GetNewJCSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewJCSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewJCSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewJCSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMMSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMMSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMMSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMMSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMMSyst(requestBody:GetNewMMSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMMSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewMMSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewMMSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPDMSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPDMSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPDMSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPDMSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPDMSyst(requestBody:GetNewPDMSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPDMSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewPDMSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPDMSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPECompWhldHist
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPECompWhldHist
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPECompWhldHist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPECompWhldHist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPECompWhldHist(requestBody:GetNewPECompWhldHist_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPECompWhldHist_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewPECompWhldHist", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPECompWhldHist_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPRSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPRSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPRSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPRSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPRSyst(requestBody:GetNewPRSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPRSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewPRSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewPRSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewTaxSvcConfig
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxSvcConfig
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewTaxSvcConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxSvcConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxSvcConfig(requestBody:GetNewTaxSvcConfig_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewTaxSvcConfig_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewTaxSvcConfig", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewTaxSvcConfig_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewXaSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewXaSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewXaSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewXaSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewXaSyst(requestBody:GetNewXaSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewXaSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewXaSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewXaSyst_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewXbSyst
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewXbSyst
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewXbSyst_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewXbSyst_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewXbSyst(requestBody:GetNewXbSyst_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewXbSyst_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewXbSyst", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewXbSyst_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetNewEntityGLC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CompanySvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AGCompanyRow{
   "odatametadata":string,
   "value":Erp_Tablesets_AGCompanyRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_APSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ARSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ARSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BMSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BMSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_BorderPctRow{
   "odatametadata":string,
   "value":Erp_Tablesets_BorderPctRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CRSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CRSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CSFSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CSFSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyAttchRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CompanyAttchRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CompanyListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CompanyRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CompanyRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrRateGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CurrRateGrpRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrencyRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CurrencyRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EQSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EQSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow{
   "odatametadata":string,
   "value":Erp_Tablesets_EntityGLCRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ExtPRSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ExtPRSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_FsSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_FsSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ISSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_ISSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_JCSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_JCSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MMSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MMSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PDMSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PDMSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PECompWhldHistRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PECompWhldHistRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PRSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PRSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcConfigRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxSvcConfigRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_XaSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_XaSystRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_XbSystRow{
   "odatametadata":string,
   "value":Erp_Tablesets_XbSystRow,
}

export interface Erp_Tablesets_AGCompanyRow{
      /**  Company  */  
   "Company":string,
      /**  Generated Files Folder  */  
   "GenFilesFolder":string,
      /**  Inventory Movement Mandatory CUIT  */  
   "InvMoveMandCUIT":boolean,
      /**  Sales Order Mandatory CUIT  */  
   "SOMandCUIT":boolean,
      /**  Default Import Destination  */  
   "DefaultDestination":string,
      /**  Transport Key  */  
   "TransportKey":string,
      /**  Withholding Certificate Signer  */  
   "WHCertificateSigner":string,
      /**  Signer Position  */  
   "SignerPosition":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Web Service Code  */  
   "WebServiceConfigCode":string,
      /**  ElectronicCreditInvMinAmt  */  
   "ElectronicCreditInvMinAmt":number,
      /**  FinOption  */  
   "FinOption":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_APSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Indicates if Receipt transactions are to be used to create invoices. This flag is used by the Receipt entry program to set the value of the RcvHead.SaveForInvoicing.  Invoice entry pulls in receipt details  Receipt.SaveForInvoicing = Yes and Receipt.Invoiced =  No.  */  
   "SaveReceipts":boolean,
      /**  Configures the A/P automatic invoice payment selection process to unconditionally take any available discount amount.  */  
   "AlwaysDiscount":boolean,
      /**  Identifies default aging format, the details of which is stored in the AgingRptFmt table.  */  
   "FmtCode":string,
      /**  Stores the FmtCode of the AgingRptFmt record that is to be considered the A/P default.  */  
   "DefaultFmtCode":string,
      /**  Used by AP Check printing.  It is the line # at which the check perforation is.  */  
   "CheckPerforationLineNum":number,
      /**  For internal use only.  Used with CPayCompany to enforce security of the Centralized Payment Parent company.  */  
   "CPayParent":string,
      /**  Company that is the Parent of Centralized Payment process.  More than one company can be attached to a serial number that has the Centralized Payment module entered.  This field designates which of those companies is the Central Payment Parent Company and can therefore create invoices flagged for centralized payment.  */  
   "CPayCompany":string,
      /**  Indicates if user is allowed to override the Reverse Charge Method in the AP invoice line.  */  
   "AllowReverseCharges":boolean,
      /**  It used to catch rounding differences that might occur when vendor invoices are settled in a currency different from the invoice currency  */  
   "RoundTolerance":number,
      /**  If the value is true and in case the total balance of an invoice transaction is within the total rounding setup for the currency of the invoice the balance is automatically accepted and booked as a rounding difference.  If the value is false the user has to balance the transaction manually.  */  
   "RoundInvoice":boolean,
      /**   Determines how a logged invoice is processed through the accounting system.
TR = Authorization Tracking.  Logged invoices are not processed by the Posting Engine.  Logging invoices is done for tracking purposes.  Full accounting is done when the AP Invoice is created.
TA - Account for Taxes.  When logged invoices are posted, accounts payable and tax amounts are booked directly to the respective accounts, the invoice net amount is posted to a Logged Invoice Suspense Account.  The entry is removed from the suspense account when the logged invoice is converted to an AP Invoice.
S - Book All to a Suspense Account.  When the logged invoice is posted the tax invoice and net amount are posted to a Logged Invoice Suspense Account.  The entry is removed from the suspense account when the logged invoice is voided or converted to a regular AP Invoice.  */  
   "LogInvAccting":string,
      /**  List of authorized administrators who are able to mark a logged action as complete.  */  
   "AuthAdmins":string,
      /**  Indicates if Logged Invoices are created in an Aprpoved state or if they must be manually approved.  If the Accounting Option is 'Authorization Tracking' logged invoices can not be auto approved.  */  
   "LogInvAutoAprv":boolean,
      /**  First G/L Update Stage  */  
   "GLStage":string,
      /**  Next available number in PI numbering sequence  */  
   "NextPINum":number,
      /**  Number of digits allowed for PI Numbering  */  
   "NumDigit":number,
      /**  Next available number sequence for ap invoices created from employee expenses.  */  
   "NextExpInvSeq":number,
      /**  This flag will be used to default the InvcHead.ReadyToCalc field when an Account Payable invoice is created. Defaults to No.  */  
   "InvcReadyToCalcDflt":boolean,
      /**  Indicates which date to use (Apply/Invoice Date) to calculate exchange rates.  */  
   "ExchangeDateToUse":number,
      /**  Invoice Legal Numbers based on “Apply/Invoice” Date for AP invoices and Debit Memos  */  
   "LNBasedOnDate":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates that it need to copy exchange Rates during generation of AP Debit Memo.  */  
   "CopyExcRateDM":boolean,
      /**  Indicates that it need to copy exchange Rates for creating AP Correction Invoice.  */  
   "CopyExcRateCorrInv":boolean,
      /**  The Taxable option from Purchase Order Entry is brought into AP Invoice Entry.  */  
   "UsePODtlTaxable":boolean,
      /**  Invoice Legal Number required for AP Invoices and Debit Memos.  */  
   "LNReqForInvc":boolean,
      /**  Apply pre-payments on accounts payable (AP) invoices automatically.  */  
   "ApplyAPPrePayAuto":boolean,
      /**  Field to enable functionality of Dates Set Up  */  
   "DatesSetUp":boolean,
      /**  Field to Allow Amend the Apply Date on AP Invoices  */  
   "APAmdApplyDate":boolean,
      /**  Field to Allow Amend the Tax Point Date on AP Invoices  */  
   "APAmdTaxPDate":boolean,
      /**  Field to Allow Amend the Tax Rate Date on AP Invoices  */  
   "APAmdTaxRateD":boolean,
      /**  Field to default the Apply Date on AP Invoices  */  
   "APDefApplyDate":string,
      /**  Field to default the Tax Point Date on AP Invoices  */  
   "APDefTaxPDate":string,
      /**  Field to default the Tax Rate Date on AP Invoices  */  
   "APDefTaxRateD":string,
      /**  Field to link the Apply Date on AP Invoices  */  
   "APLinkApplyDate":string,
      /**  Field to link the Tax Point Date on AP Invoices  */  
   "APLinkTaxPDate":string,
      /**  Field to link the Tax Rate Date on AP Invoices  */  
   "APLinkTaxRateD":string,
      /**  TWAPLegNumSource  */  
   "TWAPLegNumSource":string,
      /**  TWAPThresholdTax  */  
   "TWAPThresholdTax":number,
      /**  Current Tax Year  */  
   "TaxYear":number,
      /**  Taxpayer Identification Number for Payer  */  
   "PayersTIN":string,
      /**  Name Control for 1099 Payer  */  
   "NameControl":string,
      /**  Office Code for 1099 Payer  */  
   "OfficeCode":string,
      /**  First line of the Payer name  */  
   "Name1":string,
      /**  Second line of Payer name  */  
   "Name2":string,
      /**  First address line of the Payer address  */  
   "Address1":string,
      /**  Second address line of the Payer address  */  
   "Address2":string,
      /**  Third address line of the Payer address  */  
   "Address3":string,
      /**  City portion of the address of the Payer address  */  
   "City":string,
      /**  State portion of the Payer address  */  
   "State":string,
      /**  Postal code or zip code portion of the Payer address  */  
   "ZIP":string,
      /**  The phone number of the Payer  */  
   "PhoneNum":string,
      /**  Transmitter Control Code  */  
   "TransControlCode":string,
      /**  COExtWordAmt  */  
   "COExtWordAmt":string,
      /**  DeferredExpCurr  */  
   "DeferredExpCurr":number,
      /**  Flag that allows to create multiple invoicing of receipts  */  
   "AllowMultInvcReceipts":boolean,
      /**  Days outstanding allowed. It is used to validate if the days between the invoice date and receipt date are greater or equal than this value  */  
   "DaysOutstanding":number,
      /**  Percentage of tolerance that is allowed in each receipt and its invoiced and not invoiced lines  */  
   "PcntTolerance":number,
      /**  Amount of tolerance that is allowed in each receipt and its not invoiced lines  */  
   "AmountTolerance":number,
      /**  Type of the Payer  */  
   "TaxEntityType":string,
      /**  Subcategory of the Payer  */  
   "TaxEntitySubCat":string,
      /**  Contact person name  */  
   "ContactPerson":string,
      /**  Role/Designation of the contact person  */  
   "RoleCode":string,
      /**  Name of the office branch  */  
   "BranchName":string,
      /**  Permanent Account Number for Payer  */  
   "PayersPAN":string,
      /**  Contact person email address  */  
   "EMailAddress":string,
      /**  Area code for the phone number of the Payer  */  
   "AreaCode":string,
      /**  The fax number of the Payer  */  
   "FaxNum":string,
      /**  The action to take when an AP Invoice Invoice Date or Apply Date is greater than today plus the days horizon.  Options are (W)arning, (S)top, (N)one  */  
   "FutureDateAction":string,
      /**  The number of days beyond today's date that an AP Invoice Invoice Date or Appy Date can be.  */  
   "FutureDateDaysHorizon":number,
      /**  Form 1099-K Filer  */  
   "US1099KFiler":string,
      /**  Form 1099-K PSE Name  */  
   "US1099KPSEName":string,
      /**  Form 1099-K PSE Phone  */  
   "US1099KPSEPhone":string,
      /**  Indicates that the exchange rate will be copied when creating an AP Cancellation Invoice.  */  
   "CopyExcRateCancelInv":boolean,
      /**  APTaxRoundOption  */  
   "APTaxRoundOption":number,
      /**  EInvoice  */  
   "EInvoice":boolean,
      /**  TaxRegionCode  */  
   "TaxRegionCode":string,
      /**  Centralized Payment  */  
   "CentralizedPayment":boolean,
      /**  US1099ReportBySite  */  
   "US1099ReportBySite":boolean,
      /**  Indicates which date is used for TaxTran Transaction Date - AP Invoices related records  */  
   "APTaxRptDate":number,
   "AuthAdminsName":string,
      /**  Indicates which date to use to calculate exchange rates  */  
   "ExchangeDate":number,
   "TaxRegionCodeDesc":string,
   "BitFlag":number,
   "AgingRptFmtDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ARSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Used to establish the beginning Invoice #. When the system generates a new InvcHead it will assign the greater of (StartInvoiceNum) or (the last Invoice # on file + 1) as the invoice number.  */  
   "StartInvoiceNum":number,
      /**  Indicates if Shipment transactions are to be used to create invoices. This flag is used by the Shipping entry program to set the value of the  "Invoiced" flag field. (see ShipHead.Invoiced).  Invoice entry generates invoices for Shipments which contain  "Invoiced" flag =  No.  */  
   "SaveShipments":boolean,
      /**  Order Entry action to a Credit Held customer.  Valid values are "WARN" or "STOP".  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the order and customer placed on credit hold.  STOP means that the order line addition/change to the order is not accepted and the order and customer are not placed on credit hold.  */  
   "CreditOrderAction":string,
      /**  Shipping Entry action to a Credit Held order.  Valid values are "WARN" or "STOP".  WARN means that the user is warned that the order is on credit hold, but allowed to proceed (or cancel) with the shipment.  STOP means that the shipment for that order is not accepted.  */  
   "CreditShipAction":string,
      /**  The Journal Code of the Journal that will be used for A/R invoices. Normally this would be called Sales Journal.  */  
   "SJJournalCode":string,
      /**   The Journal Code of the Journal that will be used for A/R adjustments and application of credit memos.
Normally this would be called the Adjustments Journal.  */  
   "AJJournalCode":string,
      /**  Use Shipment date for Invoice Date  */  
   "UseShipDateForInvDate":boolean,
      /**  Stores the FmtCode of the AgingRptFmt record that is to be considered the A/R default.  */  
   "DefaultFmtCode":string,
      /**  Identifies default aging format, the details of which is stored in the AgingRptFmt table.  */  
   "FmtCode":string,
      /**  This flag will be used to default the InvcHead.ReadyToCalc field when an invoice is created. Defaults to No  */  
   "InvcReadyToCalcDflt":boolean,
      /**  Indicates if user is allowed to override the Reverse Charge Method in the AR invoice line.  */  
   "AllowReverseCharges":boolean,
      /**  It is used to catch rounding differences that might occur when customer invoices are settled in a currency different from the invoice currency.  */  
   "RoundTolerance":number,
      /**  if Yes it means that tax rounding and calculation level (line or total) are performed according to rules set on each customer, if NO - according to company setup  */  
   "TaxARCustomRules":boolean,
      /**  Credit checking relationship  */  
   "RlsClassCredit":string,
      /**  Reporting relationship class  */  
   "RlsClassReport":string,
      /**  Payer-sold to relationship, lets payer customer pays for the sold to customer, who is billed in the invoice  */  
   "RlsClassPayerSold":string,
      /**  Accepts payments from any customer within the same national account, regardless of parent-child status  */  
   "AcrossNatAcc":boolean,
      /**  This field is used to enable ability in Cash Receipts to prorate the discount amount back to the original sales accounts instead of the Discount Account of the module or group part.  */  
   "ProrateDiscToLine":boolean,
      /**  Indicates if legal numbers are required for invoices.  */  
   "LNReqForInvc":boolean,
      /**  Indicates how finance/late charges are calculated and charged with these two options: Percentage on Invoice Amount (Default) or Percentage on Amount Overdue.  */  
   "ChargeMethod":boolean,
      /**  Indicates if finance charge shall only be applied once per invoice. In case it?s not checked, finance charges shall be calculated each time the process is executed.  */  
   "OncePerInvoice":boolean,
      /**  Indicates that the system will generate a combined reminder letter and finance charge invoice.  */  
   "CombWReminder":boolean,
      /**  A/R Clearing Accounting  */  
   "ARClearing":boolean,
      /**  Indicates if user is allowed to set Invoice Settlement in Different Currency for Cash Receipts and Credit Memo.  */  
   "AllowSettlementInDiffCurr":boolean,
      /**  Field to default the Apply Date on AR Invoices.  */  
   "ARDefApplyDate":string,
      /**  Field to default the Shipment Date on AR Invoices.  */  
   "ARDefShipDate":string,
      /**  Field to default the Tax Point Date on AR Invoices.  */  
   "ARDefTaxPDate":string,
      /**  Field to default the Currency Date on AR Invoices.  */  
   "ARDefCurrDate":string,
      /**  Field to default the Tax Rate Date on AR Invoices.  */  
   "ARDefTaxRateD":string,
      /**  Field to link the Apply Date on AR Invoices.  */  
   "ARLinkApplyDate":string,
      /**  Field to link the Shipment Date on AR Invoices.  */  
   "ARLinkShipDate":string,
      /**  Field to link the Tax Point Date on AR Invoices.  */  
   "ARLinkTaxPDate":string,
      /**  Field to link the Currency Date Date on AR Invoices.  */  
   "ARLinkCurrDate":string,
      /**  Field to link the Tax Rate Date on AR Invoices.  */  
   "ARLinkTaxRateD":string,
      /**  Field to Allow Amend the Apply Date on AR Invoices.  */  
   "ARAmdApplyDate":boolean,
      /**  Field to Allow Amend the Shipment Date on AR Invoices.  */  
   "ARAmdShipDate":boolean,
      /**  Field to Allow Amend the Tax Point Date on AR Invoices.  */  
   "ARAmdTaxPDate":boolean,
      /**  Field to Allow Amend the Currency Date on AR Invoices.  */  
   "ARAmdCurreDate":boolean,
      /**  Field to Allow Amend the Tax Rate Date on AR Invoices.  */  
   "ARAmdTaxRateD":boolean,
      /**  Field to enable funcionality of Dates Set Up  */  
   "DatesSetUp":boolean,
      /**  Field to default the Tax Rate Date for cancellation or adjusment credit on AR Invoices.  */  
   "ARDefTaxRCrD":string,
      /**  Field to Allow Amend the Tax Rate Date for cancellation or adjusment credit on AR Invoices.  */  
   "ARAmdTaxRCrD":boolean,
      /**  This field will hold the default value for InvcHead.UseAltBillTo which indicates if the Alternate Bill To address should be used for taxing instead of the ship to address.  */  
   "UseAltBillToAddr":boolean,
      /**  Flag to indicate if the Exchange Rate should be copied from the original Invoice for a Correction Invoice.  */  
   "CopyExchangeRate":boolean,
      /**  Indicates first PI stage that updates the G/L  */  
   "GLStage":string,
      /**  Endorse AP  */  
   "EndorseAP":boolean,
      /**  GL Status  */  
   "GLStatus":boolean,
      /**  Unapproved Status  */  
   "UnapprovedStatus":string,
      /**  Portfolio Status  */  
   "PortfolioStatus":string,
      /**  Bank Status  */  
   "BankStatus":string,
      /**  Settled Status  */  
   "SettledStatus":string,
      /**  Next available number in PI numbering sequence  */  
   "NextPINum":number,
      /**  Number of digits allowed for PI Numbering  */  
   "NumDigit":number,
      /**  Cash Receipts from sale preferred bank.  */  
   "PreferredBank":string,
      /**  IsDiscountforCreditM  */  
   "IsDiscountforCreditM":boolean,
      /**  MandateCounter  */  
   "MandateCounter":number,
      /**  SEPADDMsgCounter  */  
   "SEPADDMsgCounter":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates that for AR Invoices the confirmation taxes can be used.  */  
   "AllowConfirmationTax":boolean,
      /**  UseAltBillToID  */  
   "UseAltBillToID":boolean,
      /**  CopyExcRateCancelInv  */  
   "CopyExcRateCancelInv":boolean,
      /**  CopyExcRateCM  */  
   "CopyExcRateCM":boolean,
      /**  ExchangeDate  */  
   "ExchangeDate":number,
      /**  AllowOverpaidInv  */  
   "AllowOverpaidInv":boolean,
      /**  AutoARBal  */  
   "AutoARBal":boolean,
      /**  CancelledStatus  */  
   "CancelledStatus":string,
      /**  AdjDocLevTax  */  
   "AdjDocLevTax":boolean,
      /**  RetainCreditOverride  */  
   "RetainCreditOverride":boolean,
      /**  LNCashRecForUnappliedRec  */  
   "LNCashRecForUnappliedRec":boolean,
      /**  AllowNegativeDiscount  */  
   "AllowNegativeDiscount":boolean,
      /**  AllowNegativeQuantity  */  
   "AllowNegativeQuantity":boolean,
      /**  UseControlledCM  */  
   "UseControlledCM":boolean,
      /**  Use Copy Numbers in AR Invoice  */  
   "UseCopyNumInARInv":boolean,
      /**  Miscellaneous AR Invoice action to a Credit Held customer.  Valid values are "WARN" or "STOPENTRY", “STOPPOST”, “IGNORE”.  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the invoice.  STOPENTRY means that the user is given a message that invoice cannot be created.  STOPPOST means the user is giving a message the invoice cannot be created, but it cannot be posted until the customer is removed from credit hold.  IGNORE means no message is received but the invoice will be marked as on credit hold.  */  
   "CreditLimitInvoiceAction":string,
      /**  Maximum Write Off Amount  */  
   "MaxWriteOffAmt":number,
      /**  Allow Negative Write Off  */  
   "AllowNegativeWriteOff":boolean,
      /**  Invoice Deposit Tax Treatment  */  
   "DepTaxTreatment":string,
      /**  Can be set = yes, if Deposit Invoice Tax treatment is Tax Shipment Net movement. Allow shipment invoice with negative net tax elements  */  
   "DepAllowNegativeTax":boolean,
      /**  Product Tax Category  */  
   "DepTaxCatID":string,
      /**  Require Deposit Invoice  */  
   "DepInvcRequired":boolean,
      /**  Invoice Days Delay  */  
   "DepDaysDelay":number,
      /**  Deposit transaction Document Type of type AR Invoice  */  
   "DepTranDocTypeID":string,
      /**  Deposit Invoices show prior linked Deposit Invoices  */  
   "DepShowLinkedInvc":boolean,
      /**  MandatoryARRemittanceSlip  */  
   "MandatoryARRemittanceSlip":boolean,
      /**  Endorsed to Supplier PI Status  */  
   "EndorsedToSupplierStatus":string,
      /**  AllowNegBal  */  
   "AllowNegBal":boolean,
      /**  Company that is the Parent of Centralized Collection process.  This field designates which company is the Central Collection Parent Company and can therefore receive and pay the invoices flagged for centralized collection.  */  
   "CColCompany":string,
      /**  Flag to indicate if Invoices created automatically will be marked for Central Collection.  */  
   "CentralCollectionForAutoInv":boolean,
      /**  Use Bill To Tax ID in Sales List  */  
   "UseBillToTaxIDInSL":boolean,
      /**  Split Revenue based on combination of Product Group and Tax Effective Rate GLC  */  
   "SplitRevenueByTaxEffRate":boolean,
      /**  EnableSettlementFeature  */  
   "EnableSettlementFeature":boolean,
   "ARClearingAcctDesc":string,
      /**  XASyst.ARClearingDept  */  
   "ARClearingDept":string,
   "ARClearingDisplayAccount":string,
      /**  XASyst.ARClearingDiv  */  
   "ARClearingDiv":string,
      /**  Indicates which date is used for TaxTran Transaction Date - AR Invoices related records  */  
   "ARTaxRptDate":number,
      /**  If yes, enable IntPay acount (from GLSyst)  */  
   "ARVoucherInvoices":boolean,
   "DEPTaxCatIDDescription":string,
   "DepTranDocTypeLinkDescription":string,
   "isRlsCreditEmpty":boolean,
   "isRlsPayEmpty":boolean,
   "isRlsReportEmpty":boolean,
      /**  XASyst.ARClearingChart  */  
   "ARClearingChart":string,
   "BitFlag":number,
   "AgingRptFmtDescription":string,
   "AJJournalCodeJrnlDescription":string,
   "PIStatusBStatusDesc":string,
   "PIStatusCStatusDesc":string,
   "PIStatusEToSStatusDesc":string,
   "PIStatusPStatusDesc":string,
   "PIStatusSStatusDesc":string,
   "PIStatusUStatusDesc":string,
   "PreferredBankDescription":string,
   "PreferredBankBankName":string,
   "SJJournalCodeJrnlDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BMSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unapprove part revisions when checked out to ECO.  */  
   "UnapproveRevOnCheckout":boolean,
      /**  Indicates if the user's password will be verified during operations such as Rev approve/unapprove, checkout, checkin.  */  
   "VerifyPassword":boolean,
      /**  If TRUE then a workflow group and task set is required on ECO Group records.  */  
   "WorkflowRequired":boolean,
      /**  If TRUE then the Engineering Workbench is limited to one user per ECO Group.  If FALSE then individual revisions within a group can be locked.  */  
   "SingleUser":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_BorderPctRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   "DestCountryNum":number,
      /**  This is used to calculate the percentage of the miscellaneous charge to be applied in the Intrastat.  */  
   "PctAtBorder":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "DestCountryNumDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CRSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Company default Task set.  Used to assign to new lead/opportunity/quote when there isn't a task set for the Sales Territory for the Quote.  */  
   "DefTaskSetID":string,
      /**  Company default Marketing Campaign.  Used to assign to a new lead/opportunity/quote.  */  
   "DefMktgCampaignID":string,
      /**  Company default Web Marketing Campaign.  Used to assign to a new lead/opportunity/quote.  */  
   "DefWebMktgCampaignID":string,
      /**  Default "win" reason Code.  From Reason table with Code type of "w"  */  
   "WinReasonCode":string,
      /**  Default "Loss" reason Code.  From Reason table with Code type of "L"  */  
   "LossReasonCode":string,
      /**  Default "Task Completion" reason Code.  From Reason table with Code type of "T"  */  
   "TaskReasonCode":string,
      /**  Indicates that the win Function will close all open tasks on the LOQ  */  
   "CloseTasksWin":boolean,
      /**  Indicates that the Lose Function will close all open tasks on the LOQ  */  
   "CloseTasksLose":boolean,
      /**  Company default Sales territory  */  
   "TerritoryID":string,
      /**  Company default Inter-Company Marketing Campaign.  Used to assign to a new lead/opportunity/quote.  */  
   "DefICMktgCampaignID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  This flag indicates if the territory security is applied to sales order. By applying territory security at SO the user only can load sales orders and customers for the territory that his workforce has access.  */  
   "UseTerritorySecurity":boolean,
      /**  Number  of calls assigned to the owner that are loaded automatically when opening CRM Call log.  */  
   "CRMCallsShown":number,
      /**  This fields defines if the Epicor ERP CRM is integrated to an External CRM.  Only enabled if there is an active license for External CRM Integration.  */  
   "ExternalCRMIntegration":boolean,
      /**  This fields define the external software used as the Extenral CRM. The valid option are  S: Salesfore.com .  */  
   "ExternalCRMSystem":string,
      /**  This is the URL used to integrate to the External CRM system  */  
   "ExternalCRMURL":string,
      /**  This field determines what system is used as the primary master file holder. The valid values are E : Epicor ERP  C: External CRM  */  
   "ExternalCRMMasterFile":string,
      /**  This field defines the token used to integrate to the External CRM  */  
   "ExternalToken":string,
      /**  This field defines the user id used to integrate to the External CRM  */  
   "ExternalCRMLoginID":string,
      /**  This field defines the token password to integrate to the External CRM  */  
   "ExternalCRMPassword":string,
      /**  This field defines the time zone used by the External CRM. This is used in cases where the External CRM is located in a different time zone than Epicor ERP.  */  
   "ExternalCRMTimeZoneID":string,
      /**  This field defines the default Industry Class Type used by the External CRM. The valid values are all the active Industry Class Type Id defined in Epicor ERP.  */  
   "ExternalCRMDefaultICTypeID":string,
      /**  This field defines the last time that the External CRM has been Synchronized to Epicor ERP. This field is maintained by the External CRM Synchronization  process.  */  
   "ExternalCRMLastSync":string,
      /**  This field defines the last time that Customer Contacts  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   "ExternalCRMLastSyncContact":string,
      /**  This field defines the last time that the Customers  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   "ExternalCRMLastSyncCustomer":string,
      /**  This field defines the last time that  Part  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   "ExternalCRMLastSyncPart":string,
      /**  This field defines the last time that  Quotes  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   "ExternalCRMLastSyncQuote":string,
      /**  This field is used by the External CRM integration only.  */  
   "ExternalCRMCreateSO":number,
      /**  External CRM masked password.  */  
   "ExternalCRMPasswordMasked":string,
   "BitFlag":number,
   "DefICMktgCampDescription":string,
   "DefMktgCampaignIDCampDescription":string,
   "DefTaskSetIDWorkflowType":string,
   "DefTaskSetIDTaskSetDescription":string,
   "DefWebMtkgCampDescription":string,
   "ExternalCRMDefaultICTypeDescription":string,
   "LossReasonDescription":string,
   "TaskReasonDescription":string,
   "TerritoryIDTerritoryDesc":string,
   "WinReasonDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CSFSystRow{
      /**  Company Identifier.  */  
   "Company":string,
   "TaxInfo1":string,
   "TaxInfo2":string,
   "TaxInfo3":string,
   "TaxInfo4":string,
   "TaxInfo5":string,
   "TaxInfo6":string,
   "TaxInfo7":string,
   "TaxInfo8":string,
   "TaxInfo9":string,
   "TaxInfo10":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RedStornoOpt  */  
   "RedStornoOpt":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CompanyAttchRow{
   "Company":string,
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

export interface Erp_Tablesets_CompanyListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Company Name  */  
   "Name":string,
      /**  First company address line.  */  
   "Address1":string,
      /**  City portion of company address.  */  
   "City":string,
      /**  State portion of company address.  */  
   "State":string,
      /**  Postal code or zip code portion of company address.  */  
   "Zip":string,
      /**  Company phone number  */  
   "PhoneNum":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CompanyRow{
   "Company1":string,
      /**  Company Name  */  
   "Name":string,
      /**  First company address line.  */  
   "Address1":string,
      /**  Second company address line.  */  
   "Address2":string,
      /**  Third company address line.  */  
   "Address3":string,
      /**  City portion of company address.  */  
   "City":string,
      /**  State portion of company address.  */  
   "State":string,
      /**  Postal code or zip code portion of company address.  */  
   "Zip":string,
      /**  Country portion of company address.  */  
   "Country":string,
      /**  Company phone number  */  
   "PhoneNum":string,
      /**  Company fax number  */  
   "FaxNum":string,
      /**  Federal Income Tax Number  */  
   "FEIN":string,
      /**  State Tax ID  */  
   "StateTaxID":string,
      /**  Current fiscal year  */  
   "CurrentFiscalYear":number,
      /**  This is the Trading Partner ID that is used for incoming and outgoing EDI.  */  
   "EDICode":string,
      /**  The Tax Region Code for this company. This tax region is used to define the 'interior'. It is used as a default tax region in Vendor Maintenance.  */  
   "TaxRegionCode":string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   "CountryNum":number,
      /**  Added for FRx Integration which requires that the company is identified by a unique positive integer, as opposed to a character string.  FRx calls this the entity number.  It is maintained on the General Ledger configuration screen.  */  
   "Number":number,
      /**  Data Source Name for the FRx database for this company.  Must be linked to a SQL Server 7.0 database to allow exporting of data for financial reporting using FRx.  This field is maintained on the General Ledger configuration screen for each company.  */  
   "FRxDSN":string,
      /**  The file set where the eScheduling XML messages will be sent.  It must be a valid DOS file name.  If eScheduling is being used with the Manufacturing System this field is required.  */  
   "EschedFileSet":string,
      /**  Unique identifier from and external G/L interface  */  
   "ExternalID":string,
      /**  Name of file that contains the company's logo image.  This can be blank (no logo available).  This is used for Customer/Sales/Supplier Connect.  */  
   "LogoFile":string,
      /**  Path the Employee Photos are stored in.  */  
   "EmpPhotoPath":string,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   "CalendarID":string,
      /**  The User ID for FRx.  */  
   "FrxUserid":string,
      /**  FRxUserID password  */  
   "FRxPassWord":string,
      /**  The fiscal calendar id for the company.  */  
   "FiscalCalendarID":string,
      /**  Company legal name  */  
   "LegalName":string,
      /**  Tax Payer Registration Reason Code  */  
   "TaxRegReason":string,
      /**  Economic Activity Type  */  
   "ActTypeCode":string,
      /**  Organization Registration Code  */  
   "OrgRegCode":string,
      /**  Chief Executive Officerr name  */  
   "ManagerName":string,
      /**  Chief Financial Officer Name  */  
   "ChiefAcctName":string,
      /**  Type of report  */  
   "ReportTypePref":string,
      /**  WIApplication  */  
   "WIApplication":string,
      /**  WIAutoCreateJob  */  
   "WIAutoCreateJob":boolean,
      /**  WIGetDetails  */  
   "WIGetDetails":boolean,
      /**  WISchedule  */  
   "WISchedule":boolean,
      /**  WIRelease  */  
   "WIRelease":boolean,
      /**  WIShippingCosts  */  
   "WIShippingCosts":boolean,
      /**  DeepCopy  */  
   "DeepCopy":boolean,
      /**  DeepCopyDupOrRevEst  */  
   "DeepCopyDupOrRevEst":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  MapURL  */  
   "MapURL":string,
      /**  MXMunicipio  */  
   "MXMunicipio":string,
      /**  APBOE Check  */  
   "APBOECheck":number,
      /**  COSequenceCert  */  
   "COSequenceCert":number,
      /**  Determines if the Company has to be synchronized with Epicor FSA application.  */  
   "SendToFSA":boolean,
      /**  Epicor client number for CRE  */  
   "EpicorAccountNum":number,
      /**  StartDate  */  
   "StartDate":string,
      /**  Kind of Employer F - Federal Government, S - State and Local Governmental Employer, T - Tax Exempt Employer, Y - State and Local Tax Exempt Employer, N - None Apply  */  
   "KindOfEmp":string,
      /**  Use the Employment Code field to select either the 941 (Option R) tax form or the 944 (Option F) tax form, depending upon the tax form the employer files. This selection is used in the W2 Processing program during W2 form export.  */  
   "EmploymentCode":string,
      /**  Purchase Schedule Mode specifies how the related demand requirements should be handled for this company.  */  
   "PurchaseScheduleMode":string,
      /**  Currency.BaseCurrCode field  */  
   "BaseCurrCode":string,
   "ExtPRConfig":boolean,
      /**  Has Currency Transactions  */  
   "HasCurrTrans":boolean,
   "Intrastat":boolean,
      /**  Name of product (MFGSYS Name)  */  
   "ProductName":string,
   "AllowSchedulingBeforeToday":boolean,
   "BitFlag":number,
   "CalendarDescription":string,
   "FiscalCalDescription":string,
   "TaxRegionDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CurrRateGrpRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Description  */  
   "Description":string,
      /**  Determines if the record is inactive  */  
   "Inactive":boolean,
      /**  Determins if there is a base rate group to use if no rules or rates are defined for a currency  */  
   "BaseRateGrpCode":string,
      /**  Currency to use during single or double currency conversions  */  
   "CrossCurrCode":string,
      /**  Determine if rounding should be done after conversion  */  
   "CrossRound":boolean,
      /**  Number of decimals to use during rounding  */  
   "CrossRoundDec":number,
      /**  Currency used for double currency conversions  */  
   "AltCrossCurrCode":string,
      /**  Determine if rounding should be done after conversion  */  
   "AltCrossRound":boolean,
      /**  Number of decimals to use during rounding  */  
   "AltCrossRoundDec":number,
      /**  Determines whether or not this rate group is shared between more than one company.  */  
   "GlobalGrp":boolean,
      /**  Determines whether or not this record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  Number of decimals for the exchange rates  */  
   "RateNumDec":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  control when the GlobalGrp field should be enabled.  */  
   "EnableGlobalGrp":boolean,
      /**  Control when the GlobalLock field should be enabled.  */  
   "EnableGlobalLock":boolean,
      /**  Indicates if the Currency is Global (master or linked)  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany and GlbRateGrpCode that is linking to this Rate Group.  */  
   "GlbLink":string,
      /**  Company Name from linked global rate group.  */  
   "GlbCompanyName":string,
      /**  Rate group Code from linked global rate group.  */  
   "GlbRateGrpCode":string,
      /**  Description from linked global rate group.  */  
   "GlbRateGrpDesc":string,
      /**  Company ID from linked global rate group.  */  
   "GlbCompanyID":string,
   "BitFlag":number,
   "AltCrossCurrCurrName":string,
   "AltCrossCurrCurrDesc":string,
   "AltCrossCurrCurrencyID":string,
   "AltCrossCurrDocumentDesc":string,
   "AltCrossCurrCurrSymbol":string,
   "BaseRateGrpDescDescription":string,
   "CrossCurrCurrDesc":string,
   "CrossCurrCurrName":string,
   "CrossCurrCurrencyID":string,
   "CrossCurrDocumentDesc":string,
   "CrossCurrCurrSymbol":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CurrencyRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Description of the currency  */  
   "CurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "CurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "DocumentDesc":string,
      /**  Notes the about the Currency.  */  
   "Note":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "CurrName":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "CurrencyID":string,
      /**  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  */  
   "DecimalsGeneral":number,
      /**  Indicates if the currency is active  */  
   "Inactive":boolean,
      /**  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  */  
   "DecimalsPrice":number,
      /**  Can only maintain exchange rates for currencies with this flag checked  */  
   "MaintRate":boolean,
      /**  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  */  
   "DecimalsCost":number,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   "BaseCurr":boolean,
      /**  Define multiple that Unit Prices for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpUnitPrice":number,
      /**  Indicates if this is a reporting currency  */  
   "ReportCurr":boolean,
      /**  Define multiple that Unit Tax for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpUnitTax":number,
      /**  Define multiple that Extended Prices (total line amount) for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpExtPrice":number,
      /**  Define multiple that Extended Tax (total line tax) for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpExtTax":number,
      /**  Define multiple that Total amount for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpTotalAmt":number,
      /**  Determines whether or not this currency is shared between more than one company.  */  
   "GlobalCurr":boolean,
      /**  Define multiple that Total Tax amount for sales related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpTotalTax":number,
      /**  Determines whether or not this currency record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  Define the rule how Unit Price for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleUnitPrice":number,
      /**  Display factor for exchange rates  */  
   "ScaleFactor":number,
      /**  Define the rule how Unit Tax for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleUnitTax":number,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   "CountryNum":number,
      /**  Define the rule how Extended Prices (total line amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleExtPrice":number,
      /**  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  */  
   "ReportCurrPos":number,
      /**  Define the rule how Extended Tax (total tax amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleExtTax":number,
      /**  Define the rule how total amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleTotalAmt":number,
      /**  Define the rule how total tax amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleTotalTax":number,
      /**  It used in AP Invoice, if the rounding amount remaining is less or equal to the tolerance, the remaining amount is automatically booked.  */  
   "RoundTolerance":number,
      /**  ISO unique identifier  */  
   "ISONumber":number,
      /**  Store ID for Credit Card Processing  */  
   "StoreID":string,
      /**  Define multiple that Annual Depreciation Charge for asset related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpAnnualCharge":number,
      /**  Define multiple that Period Depreciation Charge for asset  related documents shall be rounded to, 0- no rounding.  */  
   "RoundMltpPeriodCharge":number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRuleAnnualCharge":number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   "RoundRulePeriodCharge":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AGAFIPCode  */  
   "AGAFIPCode":string,
      /**  This Currency Code is used for CRE Processors.  */  
   "ISOCurrCode":string,
      /**  ProcessorNum  */  
   "ProcessorNum":number,
   "BookCurr":boolean,
   "CompanyBase":boolean,
      /**  Name of Country.  */  
   "CountryName":string,
      /**  Control when the Base Currency should be enable.  */  
   "EnableBaseCurr":boolean,
      /**  If currency exist in any transaction the decimals fields should be disables.  */  
   "EnableDecimals":boolean,
      /**  control when the Global Currency field should be enable.  */  
   "EnableGlobalCurr":boolean,
      /**  Control when the GlobalLock field should be enable.  */  
   "EnableGlobalLock":boolean,
      /**  Control when the Inactive field should be enable.  */  
   "EnableInactive":boolean,
      /**  GlbCompany that is linked to this currency  */  
   "GlbCompany":string,
      /**  GlbCompany Name that is linked to this currency  */  
   "GlbCompanyName":string,
      /**  GlbCurrency Description that is linked to this currency  */  
   "GlbCurrDesc":string,
      /**  GlbCurrency Code that is linked to this currency  */  
   "GlbCurrencyCode":string,
      /**  GlbCurrency ID that is linked to this currency  */  
   "GlbCurrencyID":string,
      /**  GlbCurrency Symbol that is linked to this currency  */  
   "GlbCurrSymbol":string,
      /**  Indicates if the Currency is Global (master or linked)  */  
   "GlbFlag":boolean,
      /**  Delimited list of GlbCompany and GlbCurrencyCode that is linking to this currency  */  
   "GlbLink":string,
   "HasCCInterface":boolean,
      /**  This field store the RowID of the record that is marked as Base Currency.  */  
   "BaseRowRowID":string,
   "BitFlag":number,
   "CountryDescription":string,
   "CreditCardProcessorDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_EQSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Used to establish the beginning Sales Order #. When the system generates a new order it will assign the greater of (StartOrderNum) or (the last orders # on file + 1) as the order number.  */  
   "StartQuoteNum":number,
      /**  A integer that express the # of days from the date quoted that someone should follow up with the customer concerning the quote. This is used by quote entry to calculate a default follow up date (QuoteHed.FollowUpDate). Default follow up date is QuoteHed.DateQuoted + EQSyst.FollowUpDays  */  
   "FollowUpDays":number,
      /**  An integer that express the # of days from the quoted date when quotes will expire. This is used by quote entry to calculate the QuoteHed.ExpirationDate  */  
   "ExpirationDays":number,
      /**  An integer that defines the # of days in which the quoting process needs to be completed in. Quote entry uses this in calculating the QuoteHed.DueDate.  */  
   "QuoteDueDays":number,
      /**  Label used for the QuoteHed.CheckOff1 field.  There are 5 CheckOffLabel fields. They are all optional. If entered then the corresponding QuoteHed.CheckOff fields become active.  */  
   "CheckOff1Label":string,
      /**  Label used for the QuoteHed.CheckOff2 field.  */  
   "CheckOff2Label":string,
      /**  Label used for the QuoteHed.CheckOff3 field.  */  
   "CheckOff3Label":string,
      /**  Label used for theQuoteHed.CheckOff4 field.  */  
   "CheckOff4Label":string,
      /**  Label used for the QuoteHed.CheckOff5 field.  */  
   "CheckOff5Label":string,
      /**  The ID that establishes link to the default QMarkUp record which was indicated as the System Wide default. Provides default markup percents used by quote entry when none are associated to the specific customer. This ID is not directly entered. Instead it is updated by the user checking a toggle box during QMarkUp maintenance indicating "System Default". This may be left blank, which indicates there are no defaults.  */  
   "MarkUpID":string,
      /**  Footer message for bottom of quote form  */  
   "Message1":string,
      /**  Footer message for bottom of quote form  */  
   "Message2":string,
      /**  If set to Yes, the user must change the Quote "Quoted"  flag to No before they are allowed to make any changes.  */  
   "PreventQQChange":boolean,
      /**  If this is Yes, then when Quotes are set to "Quoted"  or any header flag is changed on a "Planned" job the user will be prompted to enter a description of the changes.  This option is only available when "PreventQQChange" = Yes.  */  
   "LogChanges":boolean,
      /**  System Option to generate all the quantities from the price breaks in quote detail entry.  */  
   "GenQuoteQtys":boolean,
      /**  This flag will be used to default the QuoteHed.ReadyToCalc field when an invoice is created. Defaults to No  */  
   "QuoReadyToCalcDflt":boolean,
      /**  Option to keep the Quote Detail quantity constant.  */  
   "ReduceRelQty":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Refresh Worksheet on Demand . If this flag is check the Quote Worksheet will automatically refresh and it will only refresh if the user manually select the action in Quote Entry.  */  
   "RefreshWorksheetOD":boolean,
      /**  GetCostsFromInventory  */  
   "GetCostsFromInventory":boolean,
      /**  DfltExpectedQtyTo  */  
   "DfltExpectedQtyTo":string,
      /**  DfltOrderQtyToExpQty  */  
   "DfltOrderQtyToExpQty":boolean,
      /**  SellingExpectedQty  */  
   "SellingExpectedQty":number,
      /**  Quotes can be used as souce BOM if true  */  
   "UseQuoteBOM":boolean,
      /**   If true, the system will defer update of Required Qty when the QuoteAsm QtyPer field is updated 
*** FUTURE USE  */  
   "DeferQtyUpd":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
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

export interface Erp_Tablesets_ExtPRSystRow{
      /**  Company ID  */  
   "Company":string,
      /**  Default File  */  
   "FilePath":string,
      /**  3rd Party Payroll provider assigned company identifier  */  
   "ExtIntCompID":string,
      /**  Consolidates single entry per employee  */  
   "ConsHrs":boolean,
      /**  Indicates if an identifier is required in the export file  */  
   "TempD":boolean,
      /**  Export Zero Hours as Blank  */  
   "ZeroNul":boolean,
      /**  Indicates that only child records will be sent to the export file  */  
   "SupHead":boolean,
      /**  2nd Period Start Day  */  
   "SemiMonthDay":number,
      /**  Indicates which normal character will separate each field  */  
   "Delimiter":string,
      /**  Total hours for Base, OT and premium per line  */  
   "TotalAllHrs":boolean,
      /**  Group hours by pay type  */  
   "GrpPayTypeID":boolean,
      /**  Default Export Layout  */  
   "PayExportLayoutID":string,
      /**  Detailed Labor Hours  */  
   "DetailHours":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  When checked, separate lines are created for Base, Overtime and Other (Premium) hours in Export File  */  
   "SplitExportLines":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_FsSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Used to establish the beginning Service Contract Number. When the system generates a new Contract it will assign the greater of (StartContractNum) or (the last Contract Num. on file + 1) as the Contract number.  */  
   "StartContractNum":number,
      /**  Used to establish the beginning Service Call Number. When the system generates a new Service Call it will assign the greater of (StartServiceCallNum) or (the last Service Call Number on file + 1) as the Service Call number.  */  
   "StartServiceCallNum":number,
      /**  This is the window of days that is used to determine if a service contract is going to expire soon.  If the current date plus the expire horizon is greater than or equal to the entered expire date on a contract, the contract is considered to be expiring soon.  */  
   "ExpireHorizon":number,
      /**  This flag is used when printing service call tickets.  If "YES" then labor and material pricing will print on the ticket.  */  
   "PrintPrice":boolean,
      /**  Product Group Code. This will be used as a default for service calls.  This can be blank or must be valid in the ProdGrup table.  */  
   "CallProdCode":string,
      /**  This prefix will be used for service call job.  The service call job will be the prefix + service call number + service call Line number.  */  
   "CallJobPrefix":string,
      /**  This flag is to be set to 'YES' during intial startup. When this flag is set to 'YES' all Service Contracts will be created as active invoiced and shipped.  The idea is that a cusomter that purchases FS may already have active service contracts that have been invoiced.  */  
   "ContractStartup":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  This field stores the allowed Contract Renewal Period which is used to determine how long a contract/renewal can be renewed past its expiration date.  If the RenewalPeriod = 0 then it means that ALL expired contracts can still be renewed anytime.  */  
   "RenewalPeriod":number,
   "BitFlag":number,
   "CallProdDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Maintained through Category Maintenance.  The sales category may be used in the Financial Statements to compare Income Statement accounts against.  */  
   "SalesCategory":string,
      /**  Indicates if the A/R module is interfaced with General Ledger.  When interfaced A/R posting routines will automatically create "posted" journal  entries in G/L.  */  
   "ARInterfaced":boolean,
      /**  Indicates if the Accounts Payable module is interfaced with General Ledger.  When interfaced A/P posting routines will automatically create "posted" journal  entries in G/L.  */  
   "APInterfaced":boolean,
      /**  Indicates if the Payroll module is interfaced with General Ledger.  When interfaced, P/R posting routines will automatically create "posted" journal  entries in G/L.  */  
   "PRInterfaced":boolean,
      /**  Configuration option which controls if the user has the option in the periodic Inventory/Wip/Cost of sales calculation process to post the results to general ledger.  If this is set to No then the user will not have the option to post to G/L.  */  
   "PostInvtyWipCos":boolean,
      /**  The Journal Code of the Journal that will be used for Journal entry transactions. Manual Journal entries.  */  
   "GJJournalCode":string,
      /**   Indicates if the user wants to use Vouchering for A/R Invoices.  Only available if the G/L module is installed.
If yes then the system will do the following
- Print a Voucher # on the invoice.
- When invoices are printed they will be automatically posted. .  The "Voucher number" is actually the Journal Number to which the invoice posted.  */  
   "ARVoucherInvoices":boolean,
      /**   Indicates if the user wants to use Vouchering for A/P Invoices.  Only available if the G/L module is installed.
If yes then the system will print a Voucher assignment log when A/P invoices are posted.  The "Voucher number" is actually the Journal Number to which the invoice posted.  */  
   "APVoucherInvoices":boolean,
      /**  Allow unbalanced entries to be entered in General Journal Entry with a warning.  */  
   "AllowUnBalancedEntries":boolean,
      /**  Allow manual General Journal entries to be made for System Accounts.  */  
   "AllowManualGJEntries":boolean,
      /**  Flag to indicate that an External GL interface is being used  */  
   "ExtGL":boolean,
      /**  Identifies the Master COA for the company  */  
   "MasterCOA":string,
      /**   Indicates if GL balances are maintained real time or in batch. If Yes, the GLJrnDtl write trigger does NOT update the GLPeriodBal table.
If No, the GLJrnDtl write trigger updates the GLPeriod table.  The default value is no.  */  
   "BatchGLBalances":boolean,
      /**   If BatchGLBalances = yes the users have the ability to have the daily balances updated in batch mode.  This option is only available if BatchGLBalances equals Yes.
A Yes in this field indicates the GLJrnDtl write trigger does not update the GLDailyBal table.
If No, the GLJrnDtl write trigger updates the GLDailyBalTable.
The default value is No.  */  
   "BatchGLDailyBal":boolean,
      /**   This option determines which date gets stored in the GLJrnDtl.MatchDate field when GL transactions are matched.

If true, then the date that the transactions are matched is used.  If false, then the latest apply date of the matched transactions is used.  */  
   "MatchUsingCurrentDate":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  It is used to store default Book Mode in GL Journal Entry.  */  
   "DefaultBookMode":string,
      /**  The Journal Code of the Journal that will be used for Opening Journal entry transactions. Manual Journal entries.  */  
   "GJJournalCodeOpen":string,
      /**  The Journal Code of the Journal that will be used for Clousing Journal entry transactions. Manual Journal entries.  */  
   "GJJournalCodeClose":string,
      /**  It is used to store tax entry mode for GL Journal header. Possible values: 0`No Taxes~1`Taxable Journal Lines~2`Taxable Journal Lines or Tax adjustment Journal.  */  
   "TaxEntryMode":string,
      /**  It is used to store default value of tax liability for tax line in GL Journal entry routine.  */  
   "DefaultTaxLiability":string,
      /**  It is used to store default value of tax type for tax line in GL Journal entry routine.  */  
   "DefaultTaxType":string,
      /**  If the flag is on then posting rules conversion program creates a copy of current active revision before merging with the revision provided in the update/upgrade.  */  
   "KeepRevisionHistory":boolean,
   "FormatSelection":string,
   "DisplayGLFormat":string,
   "JournalCodeJrnlDescription":string,
   "DefaultTaxLiabilityDescription":string,
   "DefaultTaxTypeDescription":string,
      /**  The list of tax codes for Default Tax Liability  */  
   "TaxLiabilityTaxCodes":string,
   "BitFlag":number,
   "COADescription":string,
   "GJJournalJrnlDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_ISSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Enable Harbor Flag  */  
   "EnableHarbour":boolean,
      /**  Countries may differ in the way periods are reported.  */  
   "PeriodFormat":string,
      /**  Description Type  */  
   "DescType":string,
      /**  Intrastat Region  */  
   "DefISRegion":string,
      /**  Country of Origin required  */  
   "ISOrigCountryReq":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  APRGFlow2  */  
   "APRGFlow2":string,
      /**  APRGFlowSpec2  */  
   "APRGFlowSpec2":string,
      /**  APRGTranType2  */  
   "APRGTranType2":string,
      /**  ARRGFlow2  */  
   "ARRGFlow2":string,
      /**  ARRGFlowSpec2  */  
   "ARRGFlowSpec2":string,
      /**  ARRGTranType2  */  
   "ARRGTranType2":string,
      /**  Generate2APRGLine  */  
   "Generate2APRGLine":boolean,
      /**  Generate2ARRGLine  */  
   "Generate2ARRGLine":boolean,
      /**  Flow1Desc  */  
   "Flow1Desc":string,
      /**  Flow2Desc  */  
   "Flow2Desc":string,
      /**  StartIstatNum  */  
   "StartIstatNum":number,
      /**  APFlow  */  
   "APFlow":string,
      /**  APFlowSpec  */  
   "APFlowSpec":string,
      /**  APTranType  */  
   "APTranType":string,
      /**  APRGFlow  */  
   "APRGFlow":string,
      /**  APRGFlowSpec  */  
   "APRGFlowSpec":string,
      /**  APRGTranType  */  
   "APRGTranType":string,
      /**  ARFlow  */  
   "ARFlow":string,
      /**  ARFlowSpec  */  
   "ARFlowSpec":string,
      /**  ARTranType  */  
   "ARTranType":string,
      /**  ARRGFlow  */  
   "ARRGFlow":string,
      /**  ARRGFlowSpec  */  
   "ARRGFlowSpec":string,
      /**  ARRGTranType  */  
   "ARRGTranType":string,
      /**  ISCurrency  */  
   "ISCurrency":string,
      /**  APExtraTradeCommodityFlow  */  
   "APExtraTradeCommodityFlow":string,
      /**  APExtraTradeTranType  */  
   "APExtraTradeTranType":string,
      /**  APExtraTradeCustomsProcedure  */  
   "APExtraTradeCustomsProcedure":string,
      /**  APExtraTradeISCustomsDeclCountry  */  
   "APExtraTradeISCustomsDeclCountry":string,
      /**  APExtraTradeISEUBorderCrossingCountry  */  
   "APExtraTradeISEUBorderCrossingCountry":string,
      /**  APRGExtraTradeCommodityFlow  */  
   "APRGExtraTradeCommodityFlow":string,
      /**  APRGExtraTradeTranType  */  
   "APRGExtraTradeTranType":string,
      /**  APRGExtraTradeCustomsProcedure  */  
   "APRGExtraTradeCustomsProcedure":string,
      /**  APRGExtraTradeISCustomsDeclCountry  */  
   "APRGExtraTradeISCustomsDeclCountry":string,
      /**  APRGExtraTradeISEUBorderCrossingCountry  */  
   "APRGExtraTradeISEUBorderCrossingCountry":string,
      /**  Shipping Returned 2  */  
   "ARRGFlowSpec2Descr":string,
      /**  Shipping Returned  */  
   "ARRGFlowSpecDescr":string,
      /**  Generate2APRGExtraTradeLine  */  
   "Generate2APRGExtraTradeLine":boolean,
      /**  Shipping Returned 2  */  
   "ARRGTranType2Descr":string,
      /**  APRGExtraTradeCommodityFlow2  */  
   "APRGExtraTradeCommodityFlow2":string,
      /**  APRGExtraTradeTranType2  */  
   "APRGExtraTradeTranType2":string,
      /**  Shipping Returned  */  
   "ARRGTranTypeDescr":string,
      /**  Shipping Normal  */  
   "ARTranTypeDescr":string,
      /**  APRGExtraTradeCustomsProcedure2  */  
   "APRGExtraTradeCustomsProcedure2":string,
      /**  APRGExtraTradeISCustomsDeclCountry2  */  
   "APRGExtraTradeISCustomsDeclCountry2":string,
      /**  Intrastat Region Description  */  
   "RegionDesc":string,
      /**  APRGExtraTradeISEUBorderCrossingCountry2  */  
   "APRGExtraTradeISEUBorderCrossingCountry2":string,
      /**  Receipt Normal  */  
   "APFlowSpecDescr":string,
      /**  Receipt Returned 2  */  
   "APRGFlowSpec2Descr":string,
      /**  ARExtraTradeCommodityFlow  */  
   "ARExtraTradeCommodityFlow":string,
      /**  ARExtraTradeTranType  */  
   "ARExtraTradeTranType":string,
      /**  Receipt Returned  */  
   "APRGFlowSpecDescr":string,
      /**  Receipt Returned 2  */  
   "APRGTranType2Descr":string,
      /**  ARExtraTradeCustomsProcedure  */  
   "ARExtraTradeCustomsProcedure":string,
      /**  ARExtraTradeISCustomsDeclCountry  */  
   "ARExtraTradeISCustomsDeclCountry":string,
      /**  Receipt Returned  */  
   "APRGTranTypeDescr":string,
      /**  ARExtraTradeISEUBorderCrossingCountry  */  
   "ARExtraTradeISEUBorderCrossingCountry":string,
      /**  Receipt Normal  */  
   "APTranTypeDescr":string,
      /**  Shipping Normal  */  
   "ARFlowSpecDescr":string,
      /**  ARRGExtraTradeCommodityFlow  */  
   "ARRGExtraTradeCommodityFlow":string,
      /**  ARRGExtraTradeTranType  */  
   "ARRGExtraTradeTranType":string,
      /**  Used to populate the Intrastat Flow combos  */  
   "FlowList":string,
      /**  ARRGExtraTradeCustomsProcedure  */  
   "ARRGExtraTradeCustomsProcedure":string,
      /**  ARRGExtraTradeISCustomsDeclCountry  */  
   "ARRGExtraTradeISCustomsDeclCountry":string,
      /**  ARRGExtraTradeISEUBorderCrossingCountry  */  
   "ARRGExtraTradeISEUBorderCrossingCountry":string,
      /**  Generate2ARRGExtraTradeLine  */  
   "Generate2ARRGExtraTradeLine":boolean,
      /**  ARRGExtraTradeCommodityFlow2  */  
   "ARRGExtraTradeCommodityFlow2":string,
      /**  ARRGExtraTradeTranType2  */  
   "ARRGExtraTradeTranType2":string,
      /**  ARRGExtraTradeCustomsProcedure2  */  
   "ARRGExtraTradeCustomsProcedure2":string,
      /**  ARRGExtraTradeISCustomsDeclCountry2  */  
   "ARRGExtraTradeISCustomsDeclCountry2":string,
      /**  ARRGExtraTradeISEUBorderCrossingCountry2  */  
   "ARRGExtraTradeISEUBorderCrossingCountry2":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_JCSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Label used for the JobHead.CheckOff1 field.  There are 5 CheckOffLabel fields.  They are all optional.  If entered then the corresponding JobHead.CheckOff fields become active.  */  
   "CheckOff1Label":string,
      /**  Label used for the JobHead.CheckOff2 field.  */  
   "CheckOff2Label":string,
      /**  Label used for the JobHead.CheckOff3 field.  */  
   "CheckOff3Label":string,
      /**  Label used for the JobHead.CheckOff4 field.  */  
   "CheckOff4Label":string,
      /**  Label used for the JobHead.CheckOff5 field.  */  
   "CheckOff5Label":string,
      /**  Indicates the format of how labor time is entered.  It can be entered as (M) - hours/minutes or (H) - Hours/Hundredths.  */  
   "ClockFormat":string,
      /**  Indicates if the labor entry details will be transferred to the Payroll system.  This is used to set the value of LaborDtl.Payroll flag.  */  
   "FeedPayroll":boolean,
      /**  Controls how shop load is removed.  It can either be by Actual Hours  "H" or based on quantity completed "Q".  */  
   "RemoveLoad":string,
      /**  Controls whether or not entry of a Machine ID will be prompted for in Labor Entry and Labor Collection.  */  
   "MachinePrompt":boolean,
      /**  Indicates if system should prompt for entry of a Rework Reason code for rework transactions during Labor Collection or Labor Entry.  */  
   "ReworkReasons":boolean,
      /**  Indicates if system should prompt user to enter a Scrap Reason code for labor transactions where the scrap quantity is not zero during Labor Entry or Labor Collection.  */  
   "ScrapReasons":boolean,
      /**  Indicates the maximum number of digits to be entered into the JCSyst.NextJobNum field.  This also controls the number of digits that the system will generate when the user requests a "Next Job Number" while creating a new job number.  */  
   "JobSeqLength":number,
      /**  The value in this field represents the next default job sequence number.  The number of digits that can be entered is controlled by JCSyst.JobSeqLength.  Example of how the system uses these fields to generate a number that is inserted as part of the Job number when the user requests "Next Job Number" while creating a new job number would be: JobSeqLength = 6 and NextJobNumber = 100.  Then the system would try to insert  "000100" into the job number at the current insertion point.  */  
   "NextJobNumber":number,
      /**  Grace Period, stored as Hours/Hundredths  */  
   "Grace":number,
      /**   Default qualifier for the Production Standard field.  This is used as a default to the qualifier field in operation details when there is no related  OpStd record.  The valid qualifiers are:
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour, "PM" - Pieces/Minute, "OH" - Operations/Hour, "OM"  - Operations/minute, HR - Fixed Hours.  */  
   "StdFormat":string,
      /**   Default standard basis is to be used to with standards that are time per piece (HP & MP).  The basis is a Divisor.  Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours.  The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   "StdBasis":string,
      /**  Default for the JobOper and QuoteOpr.EstScrapType fields  */  
   "EstScrapType":string,
      /**  Indicates if system should prompt user to enter an Inventory Adjustment Reason code for quantity and cost adjustments.  */  
   "InvAdjReasons":boolean,
      /**  SchedPri.SchedCode value that is marked as the default scheduling code in the Scheduling Priority Code master file.  */  
   "SchedCode":string,
      /**  Default for scheduling operations that have been started.  A started operation is one with labor reported to it.  Global Scheduling uses this value.  */  
   "SchedStartedOps":boolean,
      /**  The number of weeks labor warning detail is stored until they are purged.  */  
   "WksLaborHistWarn":number,
      /**  This option controls whether or not the labor warnings messages are generated/reported.  When this option is turned on labor warning records are created and the labor edit list and/or entry/tracker programs report these warnings.  When it is turned off the labor edit list performs its own warning checking and no warnings are reported in the entry/tracker programs.  This option should only be turned on between labor periods (i.e. after all of the labor has been reported, but before the next periods information has been entered).  Only maintainable if the Data Collection module has been installed.  */  
   "GenLaborWarnMsg":boolean,
      /**  If set to Yes, the user must change the Job Engineered flag to No before they are allowed to make any changes to a Job.  */  
   "PreventPJChange":boolean,
      /**  If this is Yes, then when Jobs are set to "Planned"  or any header flag is changed on a "Planned" job the user will be prompted to enter a description of the changes.  This option is only available when "PreventPJChange" = Yes.  */  
   "LogChanges":boolean,
      /**  Number of minutes used by data collection to determine the time frame in which early clock in times are to be adjusted forward to the shift start time.  If clock in time falls within the  time range of (Shift Start - Allowance) to Shift Start then the clock in time will set to Shift Start time.  */  
   "EarlyClockInAllowance":number,
      /**  Number of minutes used by data collection to determine the time frame in which late clock in times are to be adjusted backwards to the shift start time.  If clock in time falls within the  time range of Shift Start to (Shift Start + Allowance)  then the clock in time will set to Shift Start time.  */  
   "LateClockInAllowance":number,
      /**  Number of minutes used by data collection to determine the time frame in which early clock out times are to be adjusted forward to the shift end time.  If clock out time falls within the  time range of (Shift End - Allowance) to Shift End  then the clock out time will set to Shift end.  */  
   "EarlyClockOutAllowance":number,
      /**  Minutes used to determine the time frame in which late clock out times are to be adjusted backwards to the shift end time.  If clock out time falls within the  time range of Shift end to (Shift Start + Allowance) then the clock out time will set to Shift End time.  */  
   "LateClockOutAllowance":number,
      /**  Default for "Floating " the part revision.  To "Float" the revision of unfirm jobs to the revision in effect at the time of the requirement.  */  
   "FloatPartRev":boolean,
      /**   Number of days before the forecast date in which any sales orders that exist should reduce the forecast quantity.
Ex: Forecast date of 3/31/98, Days before of 10, then any orders that have a date of 3/21/98 to 3/31/98 would reduce the forecast.  */  
   "ForecastDaysBefore":number,
      /**   Number of days after the forecast date in which any sales orders that exist should reduce the forecast quantity.
Ex: Forecast date of 3/31/98, Days after  of 10, then any orders that have a date of 4/01/98 to 4/10/98 would reduce the forecast.  */  
   "ForecastDaysAfter":number,
      /**   Indicates if the LateClockIn or EarlyClockOut grace period should be applied to the labor detail transactions.
Ex: 10 minute LateClockIn, Shift Start = 8:00am, Employee clocks in and starts an activity  at 8:05.  If DetailGrace = Yes then StartTime on the detail will be adjusted to 8:00.  If DetailGrace = No then StartTime remains as 8:05 and an the 5 minutes will be included in the  idle time.  This setting does NOT affect how Start/End times are adjusted for the timecard record.  In both cases for this example the start time for the timecard will be 8:00.  */  
   "DetailGrace":boolean,
      /**  If set to Yes, the user is unable to start production work for an operation which is waiting for First Article approval.  */  
   "PreventFABypass":boolean,
      /**  Used to get a value for jobs not referencing a sales order.  If a part in not in the price list then use Part.UnitPrice.  */  
   "ChgImpactPriceListCode":string,
      /**   Used in conjunction with the Late Grace Period to determine if a job is early, on-time or late.  Example: Early Grace Period is 4, Late Grace Period is 1, Job Required Date is 05/20/02: If the job is
scheduled to be completed before 05/16/02 it is Early.  If the job is
scheduled to be completed anywhere from 05/16/02 through 05/21/02 it is on-time.  If the job is scheduled to be completed after 05/21/02 it is late.  */  
   "EarlyGracePeriod":number,
      /**   Used in conjunction with the Early Grace Period to determine if a job is early, on-time or late.  Example: Early Grace Period is 4, Late Grace Period is 1, Job Required Date is 05/20/02: If the job is
scheduled to be completed before 05/16/02 it is Early.  If the job is
scheduled to be completed anywhere from 05/16/02 through 05/21/02 it is on-time.  If the job is scheduled to be completed after 05/21/02 it is late.  */  
   "LateGracePeriod":number,
      /**   NJ - Next Job
OR - Order Release  */  
   "QuickJobID":string,
      /**  KanBanPrefix  */  
   "KanBanPrefix":string,
      /**  The value in this field represents the next default transfer Order sequence number.  The number of digits that can be entered is controlled by JCSyst.OrderSeqLength.  Example of how the system uses these fields to generate a number that is inserted as part of the Transfer Order number when the user requests "Next Order Number" while creating a new Transfer Order number would be: OrderSeqLength = 6 and NextOrderNumber = 100.  Then the system would try to insert  "000100" into the Order number at the current insertion point.  */  
   "NextOrderNumber":number,
      /**  Indicates the maximum number of digits to be entered into the JCSyst.NextOrderNum field.  This also controls the number of digits that the system will generate when the user requests a "Next Order Number" while creating a new order number.  */  
   "OrderSeqLength":number,
      /**  The value in this field represents the next default transfer Order Line sequence number.  The number of digits that can be entered is controlled by JCSyst.OrderSeqLength.  Example of how the system uses these fields to generate a number that is inserted as part of the Transfer Detail Line number when the user requests "Next Line Number" when converting an MRP Transfer Line number would be: OrderSeqLength = 6 and NextTranLineNumber = 100.  Then the system would try to insert  "000100" into the Line Number at the current insertion point.  */  
   "NextTranLineNumber":number,
      /**  Determines if a scheduler is allowed to schedule/reschedule jobs/operations (from the Scheduling Boards) to do work before today.  */  
   "AllowSchedulingBeforeToday":boolean,
      /**  Indicates where to post all variances on a job that shipped direct for a standard cost part.  M = to the Product Group, C = to the Cost of Sales.  */  
   "DirectShipVar":string,
      /**  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  */  
   "SplitMfgCostElements":boolean,
      /**  This flag is used by ATP to determine if Unfirm Jobs should be considered in ATP calculations.  */  
   "UnfirmATP":boolean,
      /**   The ForecastPeriods field defines the forecast periods that are used with the import and export process.

Examples: Year, Semester, Quarter, Month, Week, Day

This field is used with the ForecastPeriodsPerYear field.  */  
   "ForecastPeriods":string,
      /**   The ForecastPeriodsPerYear field defines the number of forecast periods per year.

This field is used with the ForecastPeriods field.  */  
   "ForecastPeriodsPerYear":number,
      /**   The ReplaceMissingValues field is used to determine how periods with zero demand should be exported when exporting forecast data.

If yes, then zero demand will be replaced with the string "MISSING" as long as there is no demand in previous periods.  If previous periods have some demand, then zero demand will be left as zero.

If the value of this field is no, then zero demand will be left as zero when exporting demand.  */  
   "ReplaceMissingValues":boolean,
      /**   The ForecastImportDay field is used by the forecast import process to determine the forecast date for each forecast period.

The valid values for this field are dependent on the value in the ForecastPeriods field.  */  
   "ForecastImportDay":number,
      /**  If false then when an employee is booking hours to a job they can enter any Project Role code that has been set up on the employee. When the field is set to true then the Project Role entered MUST be one of the Project Role codes that have been assigned to the operation.  */  
   "ChkEmpPrjRole":boolean,
      /**   Defines where the default role code will be obtained.
The options are ?
Operation: Project Role code from the operation will be used.
Employee. Project Role Code from the Employee will be used.  */  
   "DfltPrjRoleLoc":string,
      /**  Defines the default revenue recognition method to be used in project entry.The options are Default =  (blank).Code/Desc: INV = On Invoice, LBR = Labor Booking, MAN = Manual, BDN = Actual Burden, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery  */  
   "DfltRevRecMthd":string,
      /**  Indicates whether the revenue recognition method can be changed on the project.  */  
   "AllowRevRecChg":boolean,
      /**  When set to Reserve following month the journal created will be flagged as a reversing journal.PCL = Reverse on Project Close, MON = Reverse Following Month  */  
   "RevRecJrnlReverse":string,
      /**  Defines where the invoice process will obtain the Project Role Rates from. Hierarchical works as defined for Invoice Preparation. All of the others will ONLY obtain the rates from the area defined. HIER = Hierarchical, PROJ = Project Only, EMPL = Employee Only, ROLE = Project Role Only  */  
   "DfltPrjRtSrc":string,
      /**  True indicates the user can change the Derive Project Rates from at the project level.  */  
   "AllowPrjRtSrcChg":boolean,
      /**  The default format to use when importing forecast data from external forecast solutions.  */  
   "ExtFcstImpFormat":string,
      /**  The default format to use when exporting sales history data to external forecast solutions.  */  
   "ExtFcstExpFormat":string,
      /**   Default of Invoicing Method of new Project. If advanced billing is not licensed the only options are CS and MB. Code/Desc:
CS = Customer Shipment, 
MB = Milestone Billing, 
FF = Fixed Fee;
CP = Cost Plus;
TM = Time and Material;
PP = Progress payment;

The default is Customer Shipment.  */  
   "ConInvMeth":string,
      /**  Tax Category to default into Project. MtlTaxCatID.  */  
   "MtlTaxCatID":string,
      /**  Tax Category to default into Project LbrTaxCatID.  */  
   "LbrTaxCatID":string,
      /**  Tax Category to default into Project. FeeTaxCatID.  */  
   "FeeTaxCatID":string,
      /**  Tax Category to default into Project. ODCaxCatID.  */  
   "ODCTaxCatID":string,
      /**  Tax Category to default into Project. SubTaxCatID.  */  
   "SubTaxCatID":string,
      /**  Tax Category to default into Project. BdnTaxCatID.  */  
   "BdnTaxCatID":string,
      /**  Tax Category to default into Project. TaxOnNetOfRet.  */  
   "TaxOnNetOfRet":boolean,
      /**  indicates if the company setting for ChkEmpPrjRole can be overridden at the project level.  */  
   "AllowChkEmpPrjRoleChg":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  AdvancedLaborRate  */  
   "AdvancedLaborRate":boolean,
      /**  CapRevID  */  
   "CapRevID":number,
      /**  AutoReceipt  */  
   "AutoReceipt":boolean,
      /**  MRPJobID  */  
   "MRPJobID":string,
      /**  Tax Category to default into Project. PbsTaxCatID. (Billing Schedule)  */  
   "PbsTaxCatID":string,
      /**  True indicates the user can link a sales order per wbs phase on project.  */  
   "SOAllowWBSPhase":boolean,
      /**  SOAutoRelWBSPhase  */  
   "SOAutoRelWBSPhase":boolean,
      /**  SchedAnUnEngineered  */  
   "SchedAnUnEngineered":boolean,
      /**  GetCostsFromTemplate  */  
   "GetCostsFromTemplate":boolean,
      /**  Allows moving Jobs across sites within the company and not only for the site where user is logged on.  */  
   "AllowMoveJobsAcrossPlants":boolean,
      /**  MPSOnly  */  
   "MPSOnly":boolean,
      /**  EnableSchedDebugLog  */  
   "EnableSchedDebugLog":boolean,
      /**  IncludeExtraDetailsLog  */  
   "IncludeExtraDetailsLog":boolean,
      /**  MtlQtyParentDefault  */  
   "MtlQtyParentDefault":number,
      /**  AssignPrimarySupplier  */  
   "AssignPrimarySupplier":boolean,
      /**  AvoidIncludeQuotePrjRevenue  */  
   "AvoidIncludeQuotePrjRevenue":boolean,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   "QtyPerCycle":number,
      /**  MaxLogDay  */  
   "MaxLogDay":number,
      /**  Default Option to activate Revenue Recognition at WBS Phase level  */  
   "DefaultRecognizeRevenueAtPhaseLevel":boolean,
      /**  EnableShipTo  */  
   "EnableShipTo":boolean,
   "StdFormatDesc":string,
   "TaxCatPbsDescription":string,
      /**  Include quotes without link to SO to Projected Revenue  */  
   "IncludeQuotePrjRevenue":boolean,
   "BitFlag":number,
   "ChgImpactPriceLstListDescription":string,
   "TaxCatBdnDescription":string,
   "TaxCatFeeDescription":string,
   "TaxCatLbrDescription":string,
   "TaxCatMtlDescription":string,
   "TaxCatODCDescription":string,
   "TaxCatSubDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MMSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Identifies the EquipStatusID that is to be used as the default for Equip.StatusID. This may be blank. Not directly maintainable. It gets set by Equipment Status maintenance when the user checks the "Default" box.  */  
   "DefaultStatusID":string,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   "TemplateJobNum":string,
      /**  Prefix that will be used when generating  Maintenance Job numbers for this company. Note this may be overridden at the Site level (see SiteConfCntrl.MaintJobPrefix)  */  
   "JobPrefix":string,
      /**  MMSyst.MaintBuffer, default for EquipPlan.MaintBuffer  */  
   "MaintBuffer":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "JobHeadPartDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PDMSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  PDM Export directory  */  
   "PDMExportDir":string,
      /**  PDM Import Directory  */  
   "PDMImportDir":string,
      /**  Document Export Directory  */  
   "DocExportDir":string,
      /**  Document Import Directory  */  
   "DocImportDir":string,
      /**  The default Group id for the ECO Group  */  
   "ECOGroupID":string,
      /**  Default pdm revision number  */  
   "RevisionNum":string,
      /**  The default pdm searchword for new parts.  */  
   "SearchWord":string,
      /**  File number used for identification of integration files.  */  
   "FileNum":number,
      /**  File name prefix for parts.  */  
   "PartPrefix":string,
      /**  File name prefix for Boms.  */  
   "BomPrefix":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PLM process will consider two types of revision. Current Revision: last approved revision with effective date less or equal than today. Last approved revision: (no matter the effective date) so if the customer has multiple revisions and one is approved, even if it’s for a future date, we will send this one.  */  
   "PLMRevision":string,
   "BitFlag":number,
   "ECOGroupIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PECompWhldHistRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Record Sequence  */  
   "RecordSeq":number,
      /**  Create Date  */  
   "CreateDate":string,
      /**  User Identifier.  */  
   "UserID":string,
      /**  Good Contributor  */  
   "GoodContributor":boolean,
      /**  Indicates the status of Withholding Agent.  */  
   "WithholdingAgent":boolean,
      /**  Collection Agent withholding status.  */  
   "CollectionAgent":boolean,
      /**  Not Found withholding status.  */  
   "NotFound":boolean,
      /**  No Address Provided withholding status.  */  
   "NoAddress":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PRSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  During Payroll Class maintenance the user is prompted for a password.  The entered password is encoded and then compared to this string.  An encoded string that is checked before allowing access to the payroll class maintenance program.  If blank then user is prompted to enter a password before allowing access to PRClass maintenance.  It does not matter what security level the user is, they just need to know this password in order to gain access.  */  
   "Password":string,
      /**   Controls the order in which checks are printed. Valid options are;
"SuperID", "Name", "EmpID","Dept".  */  
   "CheckSort":string,
      /**  Identifies the day of the month which the 2nd period starts for semimonthly payroll runs.  */  
   "SemiDay":number,
      /**  Date that the Manufacturing System payroll will become effective.  When initially starting up payroll the user enters the employee year to date information as of (PRStartDate - 1day).  If the user wants the initial quarter to date figures to be correct they should start payroll at the beginning of a quarter and enter that start date here.  */  
   "PRStartDate":string,
      /**   Encoded field which indicates if Payroll Managers have been set up.
(Blank = Not a PR manager).  Only users that are Payroll managers are allowed access to payroll class maintenance where they can establish the list of authorized users for the class.
There must always be at least one user where DspPayrollMgr = Yes.  */  
   "NoPRMgr":string,
      /**  Enable/Disable the HCM Integration. May be License specific (TBD)  */  
   "HCMEnabled":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PrintRates  */  
   "PrintRates":boolean,
      /**  If enabled the user is able to enter a max pay rate of 999999.9999 in Payroll Employee, currently the system only allows a max of 9999.9999.  */  
   "AllowHighPayRate":boolean,
      /**  Payroll checks exist for this company  */  
   "PRChecksExist":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_TaxSvcConfigRow{
      /**  Company Identifier  */  
   "Company":string,
      /**  The location of the AvaTax service when the address will not change between the client and web service.  */  
   "URL":string,
      /**  The intermediary server, for example a firewall, for the AvaTax service.  */  
   "ViaURL":string,
      /**  Stores the text case used for address validation. Possible values are Default, Upper, and Mixed  */  
   "TextCase":string,
      /**  The unique account number provided by Avalara for verification against the service. May also contain a username.  */  
   "Account":string,
      /**  The unique alpha-numeric key for the account provided by Avalara for verification against the service. May also contain a password if Account contains a username.  */  
   "Key":string,
      /**  Indicates whether the Epicor Tax Connect interface is active for this company. If false, no Tax Connect address validation or tax calculations will take place regardless of how the company flags are set for those functions.  */  
   "TaxConnectEnabled":boolean,
      /**   Indicates whether the system can perform address validation via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if address validations are authorized/available via the
Epicor Tax Connect. If false no address validation logic will be executed.  */  
   "AddrValEnabled":boolean,
      /**  Indicates whether the system should perform tax calculations via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if tax calculations are authorized/available via Epicor Tax Connect. If false the base Epicor tax calculations will take place.  */  
   "TaxCalcEnabled":boolean,
      /**  The Prefix to be used in conjunction with the SalesTaxSeq database sequence for automatically created SalesTax records  */  
   "TaxIdPrefix":string,
      /**  Request timeout value for tax connect requests, in seconds.  */  
   "RequestTimeOut":number,
      /**  The default tax category to assign to a Sales Order/Quote/Invoice  record if tax connect is enabled and no tax category is defaulted via the standard tax category default logic.  */  
   "DefaultTaxCatID":string,
      /**  This records the last document id retrieved from a ReconcileTaxHistory call to Avalara. It will be used to default the starting document ID in the Get Tax History action in Tax Reconciliation process.  */  
   "LastDocId":number,
      /**  Specifies if Tax Connect will run in Debug Mode. When TRUE the input-output XML files sent and received to Avalara will NOT be deleted so they can be reviewed.  */  
   "DebugMode":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  ValidateISOCode  */  
   "ValidateISOCode":boolean,
      /**  Indicates whether the system can perform CertCapture transactions. If CertCaptureEnabled is true, CertCapture features will be available. Otherwise, they won't.  */  
   "CertCaptureEnabled":boolean,
   "APTaxDisplayAccount":string,
   "APTaxAcctDesc":string,
   "ARTaxDisplayAccount":string,
   "ARTaxAcctDesc":string,
      /**  External field to be used to indicate that the Tax Connect service is off line. This filed can be set by the BL when a communication failure with tax connect occurs, or can be set manually in the UI when the user indicates that tax connect is offline. If set to true then the BL will not attempt any communication with the tax service. This is used to save unnecessary processing delays trying to communicate with the tax service when it is known that the service is unavailable.  */  
   "ETCOffline":boolean,
   "BitFlag":number,
   "TaxCatDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_XaSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  The default Unit of Measure that will be used when creating a part.  */  
   "DefaultUM":string,
      /**  Used as the default costing method when creating new parts in Part Master Maintenance. Remember that each Part defines its own costing method. The possible values are "A" - Average, "L" - Last or  "S" - standard.  */  
   "CostMethod":string,
      /**  Establishes the default Site ID to be used as the default for a Part's Primary Site field during Part maintenance.  The Default Warehouse must be in the DefaultSite.  */  
   "DefaultPlant":string,
      /**  Indicates if Company Name & Address should print on forms.  */  
   "PrintCompanyName":boolean,
      /**  Used to establish the beginning Sales Order #. When the system generates a new order it will assign the greater of (StartOrderNum) or (the last orders # on file + 1) as the order number.  */  
   "StartOrderNum":number,
      /**  Used to establish the beginning Purchase Order #. When the system generates a new PO, it will assign the greater of (StartPONum) or (the last orders # on file + 1) as the PO number.  */  
   "StartPONum":number,
      /**  Used to establish the beginning Packing Slip #. When the system generates a new packing slip it will assign the greater of (StartPSNum) or (the last Packing Slips  # on file + 1) as the PS number.  */  
   "StartPSNum":number,
      /**  Identifies the Terms master that is to be used as the default when creating customer masters. This can be left blank if there is no one best terms default. Otherwise it gets set via terms maintenance when the user checks the "Default" box.  */  
   "TermsCode":string,
      /**  Controls the entry of ship from job quantity in shipping entry program. If set to "yes" then job quantity field is enabled regardless of the order being linked to a job. This is intended only to be set to "yes" during the initial system implementation period. So that users can create and ship orders for manufactured items without forcing them to have established jobs  */  
   "ShipNoJob":boolean,
      /**  This field indicates if the system should generate sales order booking records. Booking tables are used to store changes in sales volume. See BookOrd & BookDtl for more info.  */  
   "BookOrders":boolean,
      /**  Option that controls the sensitivity of Bar Code Printing options.  */  
   "PrintBarCodes":boolean,
      /**  Used to establish the beginning RMA#. When the system generates a new RMA it will assign the greater of (StartRMANum) or (the last RMA # on file + 1) as the RMA number.  */  
   "StartRMANum":number,
      /**  Identifies the ShipVia master that is to be used as the default when creating Purchase Orders. This may be blank if there is no one normal ship via. Not directly maintainable. It gets set by Ship Via maintenance when the user checks the "Default" box.  */  
   "DefaultShipViaCode":string,
      /**  Used to establish the beginning PurchaseRFQ #. When the system generates a new RFQ it will assign the greater of (StartRFQNum) or (the last RFQ # on file + 1) as the RFQ number.  */  
   "StartRFQNum":number,
      /**  Label used for the DMRHead.CheckOff1 field.  There are 5 CheckOffLabel fields. They are all optional. If entered then the corresponding CheckOff fields become active.  */  
   "CheckOff1Label":string,
      /**  Label used for the DMRHead.CheckOff2 field.  */  
   "CheckOff2Label":string,
      /**  Label used for the DMRHead.CheckOff3 field.  */  
   "CheckOff3Label":string,
      /**  Label used for the DMR.CheckOff4 field.  */  
   "CheckOff4Label":string,
      /**  Label used for the DMRHead.CheckOff5 field.  */  
   "CheckOff5Label":string,
      /**  Global SN  */  
   "GlobalSN":boolean,
      /**  The Journal Code of the Journal that will be used for Inventory/WIP transactions. The Job management Calculate WIP/COS process creates entries in this journal.  */  
   "IJJournalCode":string,
      /**  Starting ID number for non-conformance records.  */  
   "StartNonConfID":number,
      /**  Starting ID number for non-conformance records.  */  
   "StartCorrActID":number,
      /**  Option to keep the Sales Order Detail quantity constant.  */  
   "ReduceRelQty":boolean,
      /**  System default buyer id.  This identifies the buyer that will be used during the auto po generation process when no buyer is defined by the PartClass or OpCode records.  */  
   "SysBuyerID":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available number is assigned by the system. The system generates a number by finding the order number of the last record on file and then a 1 to it.  */  
   "StartTFOrderNum":number,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   "AutoOrderBasedDisc":boolean,
      /**  The default shipvia code for the Counter Sales order.  */  
   "ShipViaCode":string,
      /**  The invoice group prefix for counter sales orders. The invoice group id is based on this prefix plus two digits of today's month  plus two digits of the today's daynumber.  */  
   "InvcGrpPfx":string,
      /**  If a Site does not have a specified SiteCostID, use this one instead  */  
   "PlantCostID":string,
      /**  The default task set for use in the Help Desk.  */  
   "HDDefaultTaskSetID":string,
      /**  If true, users can auto-complete Help Desk tasks by changing the current workflow stage.  */  
   "HDAutoCompleteTasks":boolean,
      /**  Indicates whether to use the shipping staging logic  */  
   "StagingReq":boolean,
      /**  True value indicates that the Epicor Advanced Quality module is active.  Related to IQS integration.  */  
   "EAQActive":boolean,
      /**  This field will hold the default URL for the Service Connect input channel.  This is only used as the default as the user can specify the individual URLs for data element to be passed to amd from the IQS application.  */  
   "DftInputChannel":string,
      /**  This field will hold the default URL for the Service Connect output channel.  This is only used as the default as the user can specify the individual URLs for data element to be passed to amd from the IQS application.  */  
   "DftOutputChannel":string,
      /**  Default Miscellaneous Freight Charge Customer Connect  */  
   "DefaultMiscFreightCC":string,
      /**  This flag will be used to default the OrderHed.ReadyToCalc field when an invoice is created. Defaults to No.  */  
   "SOReadyToCalcDflt":boolean,
      /**  Specifies if line discounts shall be applied to the unit price or the line value.  */  
   "SODiscountUnitPrice":boolean,
      /**   Default Unit of Measure Class. Used as the default value when creating new Part masters.
Must be  valid in the UOMClass table.
The UOMClass has a default UOMCode which replaces the 8.3 XASyst.DefaultUM.  */  
   "DefUOMClassID":string,
      /**  The character that will represent the place holder for any alphanumeric character ((e.g. 5 / A / a). Default is "&"  */  
   "AlphaNumeric":string,
      /**  Indicates the string to use when constructing an Example for a serial mask in Serial Mask Maintenance and the AlphaNumeric character is part of the mask. The default is "A".  */  
   "AlphaNumExample":string,
      /**  This is the character used to represent alpha characters (e.g. [a to z] or [A to Z]). Default is "@"  */  
   "AlphaOnly":string,
      /**  Indicates the string to use when constructing an Example for a serial mask in Serial Mask Maintenance and the AlphaOnly character is part of the mask. The default will be "B".  */  
   "AlphaOnlyExample":string,
      /**  This is the character used to represent a numeric character (e.g. [0 to 9]). Default is "#".  */  
   "NumericOnly":string,
      /**  This is the character used to represent a mandatory variable that can be any alphanumeric character. Therefore if the user enters 2 followed by this character in the mask then when a serial number is created these charaters must be replaced with any single character. Default is "?"  */  
   "AnyMandatory":string,
      /**  This character is used to represent an optional variable that can be any alphanumeric character. NOTE this character can ONLY be added as the last characters in the mask. Default is "!"  */  
   "OptionalAlphaNumeric":string,
      /**  This character is used to represent the characters that are to be stripped off when the internal serial number is created. This character can ONLY be at the front or back of the mask. The default is "~"  */  
   "StripChar":string,
      /**  When this character is entered in the mask surrounded by <> characters then a day number as a 2 numeric value will be automatically inserted into the serial number at that position. This will consume 2 characters of the serial number string. (Only allowed for auto generation masks). The default is "D"  */  
   "DayChar":string,
      /**  When this character  is entered in the mask surrounded by <> characters this will then automatically enter into the serial number the month number as a 2 numeric value. This will consume 2 characters of the serial number string. (Only allowed for auto generation masks). The default is "M"  */  
   "MonthChar":string,
      /**  When this is 2 character string is entered in the mask surrounded by <> characters this will then automatically enter into the serial number the last 2 numeric values of the current calendar year. This must be entered as 2 identical  characters and will consume 2 characters of the serial number string. (Only allowed for auto generation masks). The default is "YY"  */  
   "Year2Char":string,
      /**  When this 4 character string is entered in the mask surrounded by < > characters this will then automatically enter into the serial number the full value of the year. This must be entered as 4 identical  characters and will consume 4 characters of the serial number string. (Only allowed for auto generation masks) The default is "YYYY"  */  
   "Year4Char":string,
      /**  If this is entered in the mask it must be followed by a hard coded numeric value indicating the number of characters of the part number that will be included in the serial number. The PartChar and the hard coded number should be encased in <> characters when building the mask. E.g. if the part representation  character is entered as "P" and the part number is DS4000-1 and <P6> is entered in the mask then DS4000 will be included in the serial number. The default is "P". (Only allowed for auto generation masks)  */  
   "PartChar":string,
      /**  Indicates the string to use when constructing an Example for a serial mask in Serial Mask Maintenance and the PartChar character is part of the mask. The default will be  ?EPICORSERIALNUMBERMASKFORMATEXAMPLE?.  */  
   "PartCharExample":string,
      /**  Discount rounding option: NE - Round net price by extended amount, NP - Round net price by unit price,  EP - Round discount by extended amount; UP - Round discount by unit price.  */  
   "SODiscountRound":string,
      /**  Pack Slip counter used for generating new automatic SMI PO Receipts.  */  
   "SMIPackSlip":number,
      /**  This field holds the current year that is used as part of the key when generating an auto generated receipt for supplier managed inventories.  This is used in the program im/GenSMIReceipt.p  */  
   "SMIYear":number,
      /**  Default is blank.  Values include active shifts.  Selected value is used as the default value for Shift in Employee Maintenance.  */  
   "DefaultShift":number,
      /**  Select this checkbox to enable the AQM Integration. This checkbox enables movement of data in both directions, from the Epicor application to AQM and vice versa.  */  
   "IQSActive":boolean,
      /**  Specifies a selected folder path where the data will be exported. For example, C:\Epicor3Data\ServiceConnect\AQM\DataExportOut. Only enable if AQM integration is active.  */  
   "IQSOutputDir":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  StartBOLNum  */  
   "StartBOLNum":number,
      /**  Allow Project/WBS phase to be defined  */  
   "PrjAllowWBSPhase":boolean,
      /**  Default Job Type of Sales Order line.  */  
   "PrjJobType":string,
      /**  Use reference invoice costs for RMA  */  
   "RMAUseRefCosts":boolean,
      /**  Used for Sales Order to give the ability to find price lists using the base currency if the customer currency if foreign.  */  
   "UseOMBaseCurr":boolean,
      /**  PassedReqMove  */  
   "PassedReqMove":boolean,
      /**  FailedReqMove  */  
   "FailedReqMove":boolean,
      /**  PassedRMAReqMove  */  
   "PassedRMAReqMove":boolean,
      /**  FailedRMAReqMove  */  
   "FailedRMAReqMove":boolean,
      /**  QuoteToSOReadyToCalcDflt  */  
   "QuoteToSOReadyToCalcDflt":boolean,
      /**  This flag will be used to default the OrderHed.ReadyToFulfill field when a sales order is created.  */  
   "SOReadyToFulfillDflt":boolean,
      /**  Indicates the maximum number of levels of parent/child nesting allowed.  */  
   "MaxPCIDParentChildLevels":number,
      /**  Default Amount of Rows by Page to display in the MES Work Queue UI at Startup. Set it to ZERO to retrieve all the Work Queue records at once, into one single page.  */  
   "MaxWorkQueueRecords":number,
      /**  RMAAllowMultipleCredInv  */  
   "RMAAllowMultipleCredInv":boolean,
      /**  Specifies a legal number that will default when AR invoices import from Epicor FSA.  */  
   "FSATranDocTypeID":string,
      /**  FSAPromptForInstallation  */  
   "FSAPromptForInstallation":boolean,
      /**  Specifies a legal number that will default when Credit Memos import from Epicor FSA.  */  
   "FSATranDocTypeIDCreditMemo":string,
      /**  TransactionRetrievalDays  */  
   "TransactionRetrievalDays":number,
      /**  This field defines the format that will be used to export the data in the AQM Synchronization Process. The valid options are Extended: Extended version and Compact: Compact version. Only enabled if AQM integration is active.  */  
   "IQSOutputFormat":string,
      /**  This flag will be used to default the ReadyToFulfill field for jobs.  */  
   "JobReadyToFulfillDflt":boolean,
      /**  This flag will be used to default the ReadyToFulfill field for transfer orders.  */  
   "TransferReadyToFulfillDflt":boolean,
   "EnableSNMaskFields":boolean,
   "FSACMemoTranDocDesc":string,
   "FSAInvoiceTranDocDesc":string,
   "InvcTranType":string,
      /**  A temporary field for the UI for starting order number until the db StartOrderNum field format can be changed to contain 9 digits.  */  
   "TmpStartOrderNum":number,
   "CMTranType":string,
      /**  FSMDocTypeID (Attachment Document Type).  */  
   "FSMDocTypeID":string,
      /**  Company flag to enable FSM sync of Analysis Code  */  
   "FSMSyncAnalysisCd":boolean,
      /**  Company flag to enable FSM sync of Employee (Service Tech)  */  
   "FSMSyncEmpBasic":boolean,
      /**  Company flag to enable FSM sync of Asset Class (Equipment Type)  */  
   "FSMSyncFSAssetClass":boolean,
      /**  Company flag to enable FSM sync of Asset Class (Work Code)  */  
   "FSMSyncIndirect":boolean,
      /**  Company flag to enable FSM sync of Operation (Condition)  */  
   "FSMSyncOpMaster":boolean,
      /**  Company flag to enable FSM sync of Part Class  */  
   "FSMSyncPartClass":boolean,
      /**  Company flag to enable FSM sync of Site (Dispatch Location)  */  
   "FSMSyncPlant":boolean,
      /**  Company flag to enable FSM sync of Serial Number (Equipment)  */  
   "FSMSyncSerialNo":boolean,
      /**  Company flag to enable FSM sync of UOM  */  
   "FSMSyncUOM":boolean,
      /**  Company flag to enable FSM sync of Warehouse  */  
   "FSMSyncWarehse":boolean,
   "BitFlag":number,
   "DefaultPlantName":string,
   "HDTaskTaskSetDescription":string,
   "HDTaskWorkflowType":string,
   "IJJournalJrnlDescription":string,
   "PlantCostDescription":string,
   "ShiftDescription":string,
   "ShipViaDescription":string,
   "ShipViaWebDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_XbSystRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Contains the Label used for the user defined field in the Purchase Order Master.  */  
   "POUserChar1Label":string,
      /**  Contains the Label used for the 2nd user defined character  field in the Purchase Order Master.  */  
   "POUserChar2Label":string,
      /**  Contains the Label used for the 3rd user defined character field in the Purchase Order Master.  */  
   "POUserChar3Label":string,
      /**  Contains the Label used for the 4th user defined character field in the Purchase Order Master.  */  
   "POUserChar4Label":string,
      /**  Contains the Label used for the 1st user defined date field in the Purchase Order Master..  */  
   "POUserDate1Label":string,
      /**  Contains the Label used for the 2nd user defined date field in the Purchase Order Master.  */  
   "POUserDate2Label":string,
      /**  Contains the Label used for the 3rd user defined date field in the Purchase Order Master.  */  
   "POUserDate3Label":string,
      /**  Contains the Label used for the 4th user defined date  field in the Purchase Order Master.  */  
   "POUserDate4Label":string,
      /**  Contains the Label used for the 1st user defined decimal field in the Purchase Order Master..  */  
   "POUserDec1Label":string,
      /**  Contains the Label used for the 2nd user defined decimal field in the Purchase Order Master.  */  
   "POUserDec2Label":string,
      /**  Contains the Label used for the 1st user defined field in the Purchase Order Master.  */  
   "POUserInt1Label":string,
      /**  Contains the Label used for the 2nd user defined field in the Purchase Order Master.  */  
   "POUserInt2Label":string,
      /**  Company that is the Parent of Consolidated Purchasing.  More than one company can be attached to a serial number that has the Consolidated Purchasing module entered.  This field designates which of those companies is the parent of Consolidated Purchasing and can therefore create Consolidated Purchase Orders.  */  
   "ConsolidatedPurchasingCompany":string,
      /**  Holds the Currency.CurrencyCode value in which Consolidated Purchasing data will be exchanged.  */  
   "GlobalCurrencyCode":string,
      /**  Allow Express Part Checkout.  */  
   "ExpPartCKOut":boolean,
      /**  For internal use only.  Used with ConsolidatedPurchasingCompany to enforce security of the Consolidated Purchasing Parent company.  */  
   "ConsPurchasingParent":string,
      /**  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  */  
   "NewPoRelAtReceipt":boolean,
      /**  Use when creating payment records from credit card payments automatically from Sales Order or from Customer Shipment  */  
   "CashGrpPfx":string,
      /**  Invoice Group Prefix used for credit card groups  */  
   "CCInvPfx":string,
      /**  Bank Account code to be used when creating credit card payments  */  
   "DefBankAcctID":string,
      /**  Indicates whether or not Container Tracking is to calculate landed cost.  If yes, landed costs are calculated at the time the container is received.  The cubic sq feet of a container cannot be zero.  If no, landed costs are NOT calculated.  */  
   "SkipLandedCostCalc":boolean,
      /**  Does a sale that originated via Customer Connect garner a Commission?  */  
   "WebSaleGetsCommission":boolean,
      /**  Default System Printer where labels are going to be sent if there is no Device available to print labels on the Current Station.  */  
   "DefaultLabelsPrinter":string,
      /**  Default System Printer where forms are going to be sent if there is no Device available to print forms on the Current Station.  */  
   "DefaultFormsPrinter":string,
      /**   Number of lines per page for text report. This value will be written to SysRptLst.TxtLPP. The text based reports (Progress 4gl) generate a print image .txt file. This file contains new page controls characters. The Page size needs to be configurable to handle other paper sizes (ex: A4).
At this time we will allow for a page size setting to be established at the company level.  */  
   "TxtLPP":number,
      /**  Default Miscellaneous Charges Freight Charge Code  */  
   "DefaultMiscFreightChargeCode":string,
      /**  Valid values = "None", "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  If this field is not set or None is selected than PO releases are not created nor are they shipped short.  This is an optional field.  */  
   "PORelShipOption":string,
      /**  Flag to enable VAT taxboxes  */  
   "UseTaxBoxes":boolean,
      /**  Rate Group Code for General applications  */  
   "GenRateGrp":string,
      /**  Rate Group Code for Sales and A/R Invoicing  */  
   "SalesRateGrp":string,
      /**  Currency Rate Group for Purchasing and A/P Invoicing  */  
   "PORateGrp":string,
      /**  Currency Rate Group for Inventory applications  */  
   "InvRateGrp":string,
      /**  Currency Rate Group for Fixed Assets  */  
   "FARateGrp":string,
      /**  Currency Rate Group for Payroll  */  
   "PRRateGrp":string,
      /**  Currency Rate Group for Cash transactions  */  
   "CashRateGrp":string,
      /**   F = Force 1:1 rate for same currencies
C = Use Conversion through base  */  
   "RateLockType":string,
      /**  Indicates if FIFO Cost will be recorded based on Transaction Date or System Date.  By default the UseTranDate is false which means FIFO cost queue will use system date.  */  
   "UseTranDate":boolean,
      /**  Default for Part.LotBatch  */  
   "LotBatch":boolean,
      /**  Default for Part.LotMfgBatch  */  
   "LotMfgBatch":boolean,
      /**  Default for Part.LotMfgLot  */  
   "LotMfgLot":boolean,
      /**  Default for Part.LotHeat  */  
   "LotHeat":boolean,
      /**  Default for Part.LotFirmware  */  
   "LotFirmware":boolean,
      /**  Default for Part.LotBeforeDt  */  
   "LotBeforeDt":boolean,
      /**  Default for Part.LotMfgDt  */  
   "LotMfgDt":boolean,
      /**  Default for Part.LotCureDt  */  
   "LotCureDt":boolean,
      /**  Default for Part.LotExpDt  */  
   "LotExpDt":boolean,
      /**  Controls the number of decimal places that the UI uses to display a "quantiity" field. This only controls the display, the actual number of decimals that can be entered is based on the Unit of Measure. (UomConv.NumOfDec)  */  
   "QtyDsplyDec":number,
      /**  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  */  
   "PORelRcptOption":string,
      /**  If true, then the shipto can be changed on the packing slip to a different shipto than on the Order Release. However, it can only be changed to one of the shipto's that are referenced on the order.  */  
   "AllowShipToChange":boolean,
      /**  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume , Weight, Value, Quantity and Manual.  */  
   "DefDisburseMethod":string,
      /**  Flag to indicate if container shipment lines can be split into another container shipment.  */  
   "AllowSplitContainer":boolean,
      /**  Flag to indicate if Indirect Costs from one container shipment can be transferred to another.  */  
   "AllowTransferIndCost":boolean,
      /**  Flag to indicate if Landed Cost maintenance is allowed in Receipt Entry.  */  
   "AllowReceiptLC":boolean,
      /**  Allow maintenance of Landed Cost after the part is received.  */  
   "AllowLCAfterReceipt":boolean,
      /**  Allow update of PO Transaction Value during Container Landed Cost Entry.  */  
   "AllowUpdTransValue":boolean,
      /**  Do not allow use of Uplift Percent during Landed Cost calculation.  */  
   "DisableLCUplift":boolean,
      /**  Allows entry of restriction types and substances in Part Master, Operation Master, ECO and Job Entry.  */  
   "EnableRoHS":boolean,
      /**  Default value is false. When set to true then all indirect/direct roll-up radio buttons in Part Master and Job Entry should be enabled.  */  
   "AllowDirectRollUp":boolean,
      /**  Synchronize substance weight  */  
   "SyncSubstWeight":boolean,
      /**  Indicates if the RoHS Compliance Process will stop at the first failure it founds.  */  
   "StopAtFirstFailure":boolean,
      /**  Number of days to look back when processing Orders for the Build From Order History  */  
   "OrderHistDays":number,
      /**  Indicates if user is allowed to update the Supplier Price for Receipt created by Purchase Order.  */  
   "AllowUpdSuppPrice":boolean,
      /**  It is used to catch differences between updated Supplier Price for Receipt and PO Unit Price. If no value entered then do not perform percentage check.  */  
   "SuppPerctTolerance":number,
      /**  It is used to catch differences between extended values of updated Supplier Price for Receipt and PO Unit Price. If no value entered then do not perform monetary check.  */  
   "SuppMonetaryTolerance":number,
      /**  Receipt action to value of Supplier Price.  Valid values are "WARN" or "STOP".  WARN means that the user is given a warning, but allowed to proceed (or cancel) the Receipt with that Supplier Price.  STOP means that the Receipt line is not correct and the user should go to PO and update PO Unit Price to make receipt with mentioned price.  */  
   "SuppPriceLimitAction":string,
      /**  The default format code to be used on the Slow Moving Stock Provision report.  */  
   "DefaultSlowMovingFmtCode":string,
      /**  The default format code to be used on the Excess Stock Provision report.  */  
   "DefaultExcessFmtCode":string,
      /**  Indicates whether or not prices for transfer orders are calculated and printed on the packslip.  */  
   "CalcPSPrice":boolean,
      /**  Indicates whether or not taxes are calculated for a customer shipment and printed on the packslip.  */  
   "CalcPSTax":boolean,
      /**  Flag that indicates if a PO should be created when confirm in CTP.  */  
   "RaisePOforCTP":boolean,
      /**  Setting at company level to define if the sales order releases will be created as Make Direct or Buy To Order. Sales order lines for non part master part must be BTO or Make direct.  */  
   "DefaultSORelease":string,
      /**  This would allow the user to receive non traditional payment information (such as post dated checks and bank drafts) and use it in calculating a customer's credit limit  */  
   "EnablePI":boolean,
      /**  If box is checked, then the AP Invoice system will enable the APInvDtl.PurchCode field for European Financial postings  */  
   "APPurchType":boolean,
      /**  Indicates that the discount amount by line needs to be captured to be sent to an external Financials package  */  
   "APDiscount":boolean,
      /**  Flag to decide if the Match By Demand logic is applied to schedules in Demand Mass Review.  */  
   "AutoMatchAll":boolean,
      /**  Allow shipping orders on hold  */  
   "AllowShipOrdHold":boolean,
      /**  Check Unfirm Releasses Schedule  */  
   "ChkUnfirmSched":boolean,
      /**  Check Forcast Schedule  */  
   "ChkForecastSched":boolean,
      /**  Localization Country  */  
   "Localization":string,
      /**  Use Government Uniform Invoices. Taiwan localization flag.  */  
   "UseGUI":boolean,
      /**  Indicates if taxes are calculated in a separate exchange rate  */  
   "UseTaxRate":boolean,
      /**  Currency Rate Group for Taxes  */  
   "TaxRateGrp":string,
      /**  OCR Calculation Type. Localization for Sweden, Finland and Estonia.  */  
   "OCRCalcType":boolean,
      /**  OCR number is derived from either the invoice number or a setting at the customer. Localization for Sweden, Finland and Estonia.  */  
   "OCRNumDrivenFrom":string,
      /**  OCR length is the maximum length an OCR number is allowed to be. Localization setting for Sweden, Finland and Estonia.  */  
   "OCRLength":number,
      /**  The flag to indicate if Account Reference number assigned to the customer should be used as Banking Reference on AR Invoice sent to the customer.  */  
   "UseAcctRef":boolean,
      /**   Malaysia Localization
LMW License Number  */  
   "CSFLMWLcnNbr":string,
      /**   Malaysia Localization
CJ5 License Number  */  
   "CSFCJ5LcnNbr":string,
      /**   Malaysia Localization
CJ5 File Number  */  
   "CSFCJ5FileNbr":string,
      /**  Field to choose between close or delete releases on SO when the demand is process  */  
   "CancelSchedAction":string,
      /**  Document Type for Tax Receipt (Thailand Localization)  */  
   "THTaxRecDocType":string,
      /**  Withholding Tax Document Type (Thailand Localization)  */  
   "THWHTDocType":string,
      /**   Taiwan Localization
Seller City Code  */  
   "GUISellerCityCode":string,
      /**  This field would be true if the system should automatically create a Supplier record for each Employee for processing Expenses.  */  
   "ExpenseAutoSupplier":boolean,
      /**  If the system is setup to automatically create a Supplier record for each Employee for processing Expenses, this field will be the Prefix.  This value will prefix a numeric value and be used for the Supplier ID.  */  
   "ExpenseAutoSupplierPrefix":string,
      /**  Rate Group Code for Employee Expenses  */  
   "ExpenseRateGrp":string,
      /**  Internal sequence for automatic creation of vendors for employees.  */  
   "ExpenseVendorSeq":number,
      /**  If the flag is false then users are allowed to enter  anything in the bank branch ID field in customer bank, supplier bank and BankAcct. The code will still try to do a lookup and retrieve the description of the bank branch ID.  */  
   "ValidateBankBranchID":boolean,
      /**  If the flag is false then users are allowed to enter anything in the bank IBAN (International Bank Account Number) field in customer bank, supplier bank and BankAcct.  If the flag is true, the checksum validation will be performed.  */  
   "ValidateBankIBAN":boolean,
      /**  This is the default used when calculating CTP for multiple lines on an order.  If it is non-blank, then all the CTP jobs will be scheduled to complete at the same time.  It can be overridden at the time CTP is calculated.  */  
   "CTPSchedulingCode":string,
      /**   Used as the collection method for creating Change Log records.
Possible values are: "D" -  Daily (Default Value), one record is created per day and everybody's changes are stored together.  "U" - User, one  record is created per day for each user.  */  
   "ChgLogMethod":string,
      /**  Chief Accountant Name  */  
   "ChiefAcctName":string,
      /**  Cheif Accountant Cell Phone Number  */  
   "ChiefAcctCellPhone":string,
      /**  Cheif Accountant Email Address  */  
   "ChiefAcctEmail":string,
      /**  Tax Return Bank Code  */  
   "TRBankCode":string,
      /**  Tax Return Bank Branch  */  
   "TRBankBranch":string,
      /**  Tax Return Bank Account  */  
   "TRBankAcct":string,
      /**  ID number for consolidation.  */  
   "TotalPayID":string,
      /**  Tax Office Code  */  
   "TaxOfficeCode":string,
      /**  Tax Agent Name  */  
   "TaxAgentName":string,
      /**  Tax Agent Phone  */  
   "TaxAgentPhone":string,
      /**  Tax Agent Tax Region Number  */  
   "TaxAgentTaxRegNo":string,
      /**  Defines the format In which the EDI Outbound Documents will be sent to output.  */  
   "EDIOutboundAs":string,
      /**  Company default Workflow Group. Used to assign to cases.  */  
   "HDDefWFGroupID":string,
      /**  Starting supplier reference ID number  */  
   "StartVendAuditRefID":number,
      /**  IsDiscountforDebitM  */  
   "IsDiscountforDebitM":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  THBranchID  */  
   "THBranchID":string,
      /**  UseInvRateDefTax  */  
   "UseInvRateDefTax":boolean,
      /**  Allow changes to be made to POs that are linked to Intercompany Sales Orders  */  
   "AllowLinkedPOChg":boolean,
      /**  Consider Working Days in the Delivery Days Calculation  */  
   "ConsiderWorkingDays":boolean,
      /**  DeferTaxExchRate  */  
   "DeferTaxExchRate":number,
      /**  PmtTaxUseDate  */  
   "PmtTaxUseDate":number,
      /**  CNAccEntityName  */  
   "CNAccEntityName":string,
      /**  CNAccountStructure  */  
   "CNAccountStructure":string,
      /**  CNAttachment  */  
   "CNAttachment":string,
      /**  CNBaseCurrency  */  
   "CNBaseCurrency":string,
      /**  CNCashier  */  
   "CNCashier":string,
      /**  CNCFICodeCurGainLoss  */  
   "CNCFICodeCurGainLoss":string,
      /**  CNChecker  */  
   "CNChecker":string,
      /**  CNCompType  */  
   "CNCompType":string,
      /**  CNDisableEntryRules  */  
   "CNDisableEntryRules":boolean,
      /**  CNExportPath  */  
   "CNExportPath":string,
      /**  CNGroupName  */  
   "CNGroupName":string,
      /**  CNGTICollector  */  
   "CNGTICollector":string,
      /**  CNGTICommTaxCode  */  
   "CNGTICommTaxCode":string,
      /**  CNGTIDefCCFlag  */  
   "CNGTIDefCCFlag":boolean,
      /**  CNGTIDefINFlag  */  
   "CNGTIDefINFlag":boolean,
      /**  CNGTIDefPath  */  
   "CNGTIDefPath":string,
      /**  CNGTIDefPOFlag  */  
   "CNGTIDefPOFlag":boolean,
      /**  CNGTIDefPTFlag  */  
   "CNGTIDefPTFlag":boolean,
      /**  CNGTIDefSMFlag  */  
   "CNGTIDefSMFlag":boolean,
      /**  CNGTIDefSOFlag  */  
   "CNGTIDefSOFlag":boolean,
      /**  CNGTIManager  */  
   "CNGTIManager":string,
      /**  CNGTIVATCode  */  
   "CNGTIVATCode":string,
      /**  CNGTIVATInvLimit  */  
   "CNGTIVATInvLimit":number,
      /**  CNGTIVATInvLineLimit  */  
   "CNGTIVATInvLineLimit":number,
      /**  CNIndustry  */  
   "CNIndustry":string,
      /**  CNIndustryCode  */  
   "CNIndustryCode":string,
      /**  CNKeeper  */  
   "CNKeeper":string,
      /**  CNMaker  */  
   "CNMaker":string,
      /**  CNOrgCode  */  
   "CNOrgCode":string,
      /**  CNRegionCode  */  
   "CNRegionCode":string,
      /**  JPFiscalCalendarID  */  
   "JPFiscalCalendarID":string,
      /**  TWGUICalendarID  */  
   "TWGUICalendarID":string,
      /**  If the flag is false then users are allowed to enter anything in the Tax ID field in customer and supplier.  If the flag is true, the validation will be performed.  */  
   "ValidateTaxID":boolean,
      /**  MXDebugMode  */  
   "MXDebugMode":boolean,
      /**  MXDocType  */  
   "MXDocType":string,
      /**  MXIEPSTaxType. Obsolete, SalesTax.MXTaxType used instead  */  
   "MXIEPSTaxType":string,
      /**  MXISRTaxType. Obsolete, SalesTax.MXTaxType used instead  */  
   "MXISRTaxType":string,
      /**  MXIVATaxType. Obsolete, SalesTax.MXTaxType used instead  */  
   "MXIVATaxType":string,
      /**  MXPACCode  */  
   "MXPACCode":string,
      /**  MXTaxRcptEFT  */  
   "MXTaxRcptEFT":number,
      /**  MXTaxRcptType  */  
   "MXTaxRcptType":string,
      /**  MXThumbprint  */  
   "MXThumbprint":string,
      /**  MXUseExpedidoEn  */  
   "MXUseExpedidoEn":boolean,
      /**  MXValidFrom  */  
   "MXValidFrom":string,
      /**  MXValidTo  */  
   "MXValidTo":string,
      /**  OCRCalcAlg  */  
   "OCRCalcAlg":string,
      /**  NOThresholdAmt  */  
   "NOThresholdAmt":number,
      /**  EAddress  */  
   "EAddress":string,
      /**  EInvOutputDir  */  
   "EInvOutputDir":string,
      /**  EInvImpFileLocation  */  
   "EInvImpFileLocation":string,
      /**  EInvImpArchiveFileLocation  */  
   "EInvImpArchiveFileLocation":string,
      /**  EInvImpSelectionMethod  */  
   "EInvImpSelectionMethod":string,
      /**  DefaultLineTaxable  */  
   "DefaultLineTaxable":boolean,
      /**  Bill of Exchange Payment Method  */  
   "PEBOEPaymentMethod":number,
      /**  Bill of Exchange Portfolio Status  */  
   "PEBOEPortfolioStatus":string,
      /**  AsyncShip  */  
   "AsyncShip":boolean,
      /**  Within PO Entry when modifying unit price which was derived from a supplier price list, prompt the user to confirm.  */  
   "OverridePriceListPrompt":boolean,
      /**  Disable Override Price List option with PO Entry  */  
   "DisableOverridePriceListOption":boolean,
      /**  DEBundesbankCompanyID  */  
   "DEBundesbankCompanyID":string,
      /**  DEZ4ExportPath  */  
   "DEZ4ExportPath":string,
      /**  Defaults the Warehouse and Bin in Receipt to the last used for the current Part and Pack Slip  */  
   "UseLastWhseBin":boolean,
      /**  Indicates what Qty Option will be defaulted for new PO lines. Options are "Our" and "Supplier".  */  
   "POQtyOption":string,
      /**  Indicates what Qty Option will be defaulted for new Receipt lines. Options are "Our" and "Supplier".  */  
   "ReceiptQtyOption":string,
      /**  CNGTILangID  */  
   "CNGTILangID":string,
      /**  Defines the point at which the PO Releases will be closed. Available options are 'Arrival', 'Receipt', or 'Invoice'.  */  
   "CloseReleaseAt":string,
      /**  SubRateGrp  */  
   "SubRateGrp":string,
      /**  If true and the UOM is set to no rounding and the number of decimals is exceeded, you will get an error. Otherwise the value will be truncated (same as round down currently behaves).  */  
   "StopOnUOMNoRound":boolean,
      /**  MYIndustryCode1  */  
   "MYIndustryCode1":string,
      /**  MYIndustryCode2  */  
   "MYIndustryCode2":string,
      /**  MYIndustryCode3  */  
   "MYIndustryCode3":string,
      /**  MYIndustryCode4  */  
   "MYIndustryCode4":string,
      /**  MYIndustryCode5  */  
   "MYIndustryCode5":string,
      /**  PE Document ID  */  
   "PEDocumentID":string,
      /**  PE Identity Document Type  */  
   "PEIdentityDocType":string,
      /**  CNOurBank  */  
   "CNOurBank":string,
      /**  JobLotDflt  */  
   "JobLotDflt":boolean,
      /**  LACTaxCalcEnabled  */  
   "LACTaxCalcEnabled":boolean,
      /**  TW GUI Code  */  
   "TWGUIRegNum":string,
      /**  NLMessageRefSupplierICP  */  
   "NLMessageRefSupplierICP":string,
      /**  NLDigipoortDeliveryURL  */  
   "NLDigipoortDeliveryURL":string,
      /**  NLDigipoortStatusURL  */  
   "NLDigipoortStatusURL":string,
      /**  NLDigipoortServerThumbprint  */  
   "NLDigipoortServerThumbprint":string,
      /**  NLDigipoortClientThumbprint  */  
   "NLDigipoortClientThumbprint":string,
      /**  Encoding for GTI Export file  */  
   "CNGTIEncodingFormat":number,
      /**  Flag to determine whether PO taxes will be automatically calculated each time a PO line is updated.  */  
   "POTaxReadyToProcess":boolean,
      /**  Flag to determine whether PO taxes will be calculated.  */  
   "POTaxCalculate":boolean,
      /**  PEAddressID  */  
   "PEAddressID":string,
      /**  X509Code  */  
   "X509Code":string,
      /**  COIFRSInterestRate  */  
   "COIFRSInterestRate":number,
      /**  MXCURP  */  
   "MXCURP":string,
      /**  This flag will be used to determine if taxes are calculated for AP Invoices at Document Level (Default, False) or at Line Level (True).  */  
   "APTaxLnLevel":boolean,
      /**  MYLMWLcnPurchaseExpDate  */  
   "MYLMWLcnPurchaseExpDate":string,
      /**  MYLMWPurchaseAddr  */  
   "MYLMWPurchaseAddr":string,
      /**  MYLMWLcnManufacturing  */  
   "MYLMWLcnManufacturing":string,
      /**  MYLMWLcnManufacturingExpDate  */  
   "MYLMWLcnManufacturingExpDate":string,
      /**  MYLMWManufacturingAddr  */  
   "MYLMWManufacturingAddr":string,
      /**  Flag to determine whether Receipt taxes will be calculated.  */  
   "ReceiptTaxCalculate":boolean,
      /**  Flag to determine whether Quote taxes will be calculated.  */  
   "CalcQuoteTax":boolean,
      /**  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttBatch":string,
      /**  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttMfgBatch":string,
      /**  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttMfgLot":string,
      /**  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttHeat":string,
      /**  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttFirmware":string,
      /**  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttBeforeDt":string,
      /**  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttMfgDt":string,
      /**  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttCureDt":string,
      /**  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttExpDt":string,
      /**  PLTaxOfficeCode  */  
   "PLTaxOfficeCode":string,
      /**  PLRegionCode  */  
   "PLRegionCode":string,
      /**  PLProvince  */  
   "PLProvince":string,
      /**  PLDistrict  */  
   "PLDistrict":string,
      /**  PLCommunity  */  
   "PLCommunity":string,
      /**  PLBuildingNum  */  
   "PLBuildingNum":string,
      /**  PLRoomNum  */  
   "PLRoomNum":string,
      /**  PLPostOffice  */  
   "PLPostOffice":string,
      /**  Turnover in Previous Fiscal Year  */  
   "INPrevYearTurnover":number,
      /**  DeferManualEntry  */  
   "DeferManualEntry":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Container Receipt, Receipt Entry.  */  
   "DeferPurchaseReceipt":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Job Receipt to Job, Job Receipt to Salvage, Job Receipt to Inventory, Kanban Receipts.  */  
   "DeferJobReceipt":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Inspection Processing.  */  
   "DeferInspection":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Quantity Adjustment.  */  
   "DeferQtyAdjustment":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Inventory Transfer.  */  
   "DeferInventoryMove":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Customer Shipment Entry, Subcontractor Shipment Entry, Drop Shipment Entry, Order Entry.  */  
   "DeferShipments":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Count Tag Entry.  */  
   "DeferInventoryCounts":boolean,
      /**  DeferAssetDisposal  */  
   "DeferAssetDisposal":boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: RMA Processing.  */  
   "DeferReturnMaterials":boolean,
      /**  Flag to indicate if it is allowed to create employees with Group resource, without a resource defined.  */  
   "AllowEmpWithoutResource":boolean,
      /**  INSingleTaxCatTypeSO  */  
   "INSingleTaxCatTypeSO":boolean,
      /**  INSingleTaxCatTypePO  */  
   "INSingleTaxCatTypePO":boolean,
      /**  BusinessCatID  */  
   "BusinessCatID":string,
      /**  Flag to determine whether Duty will be included on Taxable amount  */  
   "ReceiptIncludeDutyInTax":boolean,
      /**  INAllowChangingPP  */  
   "INAllowChangingPP":boolean,
      /**  Fiscal Unity Tax ID (CSF Netherlands)  */  
   "NLFiscalUnityTaxID":string,
      /**  Prefix for incoming FSA records. To be used to create Cash Receipt groups.  */  
   "FSACashGrpPfx":string,
      /**  Prefix for incoming FSA records. To be used to create AR Invoice groups.  */  
   "FSAARInvGrpPfx":string,
      /**  Indicates if inbound AR Invoices are sent to posting when received from FSA.  */  
   "FSASendARInvToPosting":boolean,
      /**  Reason Code to be used for inbound inventory quantity adjustments received from Epicor FSA.  */  
   "FSAInvQtyAdjustmentReasonCode":string,
      /**  MXLocality  */  
   "MXLocality":string,
      /**  MXMunicipioCode  */  
   "MXMunicipioCode":string,
      /**  RevaluationAR  */  
   "RevaluationAR":string,
      /**  RevaluationAP  */  
   "RevaluationAP":string,
      /**  RevaluationBA  */  
   "RevaluationBA":string,
      /**  RevaluationPCD  */  
   "RevaluationPCD":string,
      /**  GenerateDigitalSignature  */  
   "GenerateDigitalSignature":boolean,
      /**  UseCopyNumInPackSlips  */  
   "UseCopyNumInPackSlips":boolean,
      /**  This is the location of the the EWC generator.  */  
   "EWConfiguratorURL":string,
      /**  NLDigipoortServerCertID  */  
   "NLDigipoortServerCertID":string,
      /**  NLDigipoortClientCertID  */  
   "NLDigipoortClientCertID":string,
      /**  UnapprovedPO  */  
   "UnapprovedPO":string,
      /**  UnconfirmedPO  */  
   "UnconfirmedPO":string,
      /**  Default Ship Via Code for return shipments of RMAs for FSA related transactions  */  
   "FSAShipViaCode":string,
      /**  Default reason code for RMAs from FSA  */  
   "FSARMAReasonCode":string,
      /**  Default payment method for expenses from FSA  */  
   "FSAExpensePMUID":number,
      /**  APPrepayTaxCalc  */  
   "APPrepayTaxCalc":boolean,
      /**  Waste Register Number (CSF Poland)  */  
   "PLWasteRegisterNum":string,
      /**  This is the location of the EWC Runtime.  */  
   "EWCRuntimeURL":string,
      /**  AGAFIPResponsibilityCode  */  
   "AGAFIPResponsibilityCode":string,
      /**  E-Invoice CompanyID Attribute  */  
   "EInvCompanyIDAttr":string,
      /**  E-Invoice EndpointID Attribute  */  
   "EInvEndpointIDAttr":string,
      /**  PriceToleranceOnHigherPrice  */  
   "PriceToleranceOnHigherPrice":boolean,
      /**  URL address to the Quick Ship application  */  
   "QuickShipURL":string,
      /**  Indicates if Quick Ship International Shipments are used.  */  
   "QSUseIntl":boolean,
      /**  Indicates if Quick Ship Bill of Lading  is used.  */  
   "QSUseBOL":boolean,
      /**  Reserved for Future Development  */  
   "QSUseCO":boolean,
      /**  Stores the name of the admin group referring to the security group maintenance.  */  
   "CNGTIAdminGroup":string,
      /**  Define the search sequence  */  
   "CNCheckerSearchSeq":number,
      /**  Define the search sequence  */  
   "CNMakerSearchSeq":number,
      /**  SalesTaxID  */  
   "SalesTaxID":string,
      /**  ServiceTaxID  */  
   "ServiceTaxID":string,
      /**  ELIEinvoice  */  
   "ELIEinvoice":boolean,
      /**  ELIDefReportID  */  
   "ELIDefReportID":string,
      /**  ELIDefStyleNum  */  
   "ELIDefStyleNum":number,
      /**  ELIDefToMail  */  
   "ELIDefToMail":string,
      /**  ELIDefCCMail  */  
   "ELIDefCCMail":string,
      /**  ELIDefMailTempID  */  
   "ELIDefMailTempID":string,
      /**  ELIDefEinvoicePath  */  
   "ELIDefEinvoicePath":string,
      /**  ELIDefDepTranDocTypeID  */  
   "ELIDefDepTranDocTypeID":string,
      /**  Enable Received Date Warning (CSF Poland)  */  
   "PLEnableRcvDateWarning":boolean,
      /**  COOneTimeID  */  
   "COOneTimeID":string,
      /**  COFiscalResp1  */  
   "COFiscalResp1":string,
      /**  COFiscalResp2  */  
   "COFiscalResp2":string,
      /**  COFiscalResp3  */  
   "COFiscalResp3":string,
      /**  Weight UOM Class  */  
   "CNWeightUOMClass":string,
      /**  EORI Number  */  
   "EORINumber":string,
      /**  Enable Netting Transaction Entry  */  
   "EnableNetting":boolean,
      /**  This field indicates that posting of withholding taxes will go through interim accounts when tax timing is partially paid or fully paid.  */  
   "WithholdAcctToInterim":boolean,
      /**  ELIDefFromMail  */  
   "ELIDefFromMail":string,
      /**  This transaction document type will be the one assigned for the netting credit memo created.  */  
   "NetTranDocTypeIDCM":string,
      /**  Description: This transaction document type will be the one assigned for the netting debit memo created  */  
   "NetTranDocTypeIDDM":string,
      /**  Security Group to be used as Tax Declaration Admins  */  
   "TWTaxDeclarationAdminGroup":string,
      /**  Enables/disables Tax Id validation.  */  
   "TaxValidationAllow":boolean,
      /**  Electronic Interface of type Tax Id Validation  */  
   "TaxValidationEFTHeadUID":number,
      /**  Enables/disables automatic Tax Id validation when customer or supplier Tax Id is changed.  */  
   "TaxValidationAutomatic":boolean,
      /**  Action if Invalid Tax ID  */  
   "TaxValidationAction":number,
      /**  RevaluationBAUnrealized  */  
   "RevaluationBAUnrealized":boolean,
      /**  RevaluationPCDUnrealized  */  
   "RevaluationPCDUnrealized":boolean,
      /**  HMRCTaxValidationAllow  */  
   "HMRCTaxValidationAllow":boolean,
      /**  HMRCTaxValidationURL  */  
   "HMRCTaxValidationURL":string,
      /**  HMRCTaxValidationAutomatic  */  
   "HMRCTaxValidationAutomatic":boolean,
      /**  HMRCTaxValidationAction  */  
   "HMRCTaxValidationAction":number,
      /**  Indicates if entry of a County of Origin is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   "AttISOrigCountry":string,
      /**  Company Scheme ID  */  
   "ExternalSchemeID":string,
      /**  Company ID  */  
   "ExternalID":string,
      /**  Indicates site can be used as a legal entity.  */  
   "SiteIsLegalEntity":boolean,
      /**  Tax Rate by Kg  */  
   "MYTaxRateByKg":string,
      /**  Tax Rate by Liter  */  
   "MYTaxRateByLiter":string,
      /**  Encryption Key  */  
   "TWEncryptionKey":string,
      /**  EInvoice Operator Code  */  
   "ELIOperatorCode":string,
      /**  Indicates the logic used to calculate the base/rpt fields.  Currently used by Bank Funds Transfer  */  
   "CurrExDiff":number,
      /**  The document type used to generate the legal number for the invoices generated automatically at the shipment.  */  
   "ERSDocTypeID":string,
      /**  The group prefix used to generated the invoice group for the invoice generated automatically by the system when shipping an ERS PO.  */  
   "ERSInvGrpPrefix":string,
      /**  Default Path where the files will be stored to be read by the Import EDI Process.  */  
   "InboundPath":string,
      /**  ELIERSDocTypeID  */  
   "ELIERSDocTypeID":string,
      /**  ELISendMail  */  
   "ELISendMail":boolean,
      /**  ELISendingOption  */  
   "ELISendingOption":number,
      /**  PlasticTaxUOMCode  */  
   "PlasticTaxUOMCode":string,
      /**  PlasticTaxRate  */  
   "PlasticTaxRate":number,
      /**  CNQuantityControl  */  
   "CNQuantityControl":number,
      /**  QuickShip Registration Code  */  
   "QuickShipRegCode":string,
      /**  URL address to the Quick Ship API  */  
   "QuickShipAPIURL":string,
      /**  Quick Ship User Name  */  
   "QuickShipUserID":string,
      /**  Quick Ship Password  */  
   "QuickShipPassword":string,
      /**  CNBondedWhseControl  */  
   "CNBondedWhseControl":number,
      /**  Freight Service Integration Selection. (AI - REST API Integration, QW - Quick Ship Web Services)  */  
   "FreightSvcInt":string,
      /**  BaseUOMClassID  */  
   "BaseUOMClassID":string,
      /**  Indicates financial groups are automatically locked on selection or creation  */  
   "AutoLockFinGroups":boolean,
      /**  Controls where Attachments are place when CPQ pushes them to Kinetic.  The selected Document Type must be of Server Transfer Type.  If the selected Document Type is Reserved for Specific Tables, the Document Type Control must include the following tables: OrderDtl, QuoteAsm, QuoteDtl, JobAsmbl, JobHead.  If no Document Type is selected, the CPQ Quote Sync will be the master and pull attachments from CPQ and if there is a value CPQ Quote Sync will not run.  */  
   "KBMaxDocTypeID":string,
      /**  Default E-invoice Report Style  */  
   "ELIRcptDefStyleNum":number,
   "CNCFICodeDescription":string,
      /**  CSF China - dynamic field for calculating of the XBSyst.CNCFICodeCurGainLoss field.  */  
   "CNCOACode":string,
      /**  Web-Service URL for E-Invoice.  */  
   "EInvWSURL":string,
   "EnableOCRCalcType":boolean,
      /**   If this flag is true then on Currency Revaluation screen the Reverse checkbox is enabled.
If this flag is false then on Currency Revaluaion screen Reverse checkbox is Read Only and set to true.  */  
   "EnableReverse":boolean,
      /**  Enable calculation of settlement discounts for credit memos in AR  */  
   "IsDiscountforCreditM":boolean,
   "JPFiscalCalDescription":string,
      /**  Peru Collection Agent withholding status  */  
   "PECollectionAgent":boolean,
      /**  Peru Goods Contributor withholding status  */  
   "PEGoodsContributor":boolean,
      /**  Peru No Address Provided withholding status  */  
   "PENoAddress":boolean,
      /**  Peru Not Found withholding status.  */  
   "PENotFound":boolean,
      /**  Peru Withholding Agent withholding status  */  
   "PEWithholdAgent":boolean,
      /**  Display used to for PORelShipOption  */  
   "PORelShipOptDisplay":string,
   "TranDocTypeDescription":string,
      /**  The field for user to input Company Encryption Key  */  
   "TWEncryptionKeyInput":string,
      /**  CSF China - dynamic field for calculating of the XBSyst.CNCFICodeCurGainLoss field.  */  
   "CNSegmentNbr":number,
      /**  Currency Exchange Difference  */  
   "CurrencyExchangeDiff":string,
      /**  URL of the OneEDI API Endpoint to post the demand outbound to  */  
   "OneEDIAPIUrl":string,
      /**  Client Id required to access OneEDI API  */  
   "OneEDIAPIClientId":string,
      /**  Client Secret required to access OneEDI API  */  
   "OneEDIAPIClientSecret":string,
      /**  CPQ Instance URL.  */  
   "KBMaxUrl":string,
      /**  CPQ Username used for communication.  */  
   "KBMaxUsername":string,
      /**  CPQ password used for communication.  */  
   "KBMaxPassword":string,
      /**  CPQ SQL Instance for syncing data between Kinetic and CPQ.  */  
   "KBMaxSqlInstance":string,
   "KBMaxSqlDatabase":string,
   "KBMaxSqlUsername":string,
   "KBMaxSqlPassword":string,
      /**  Indicates if site segements should be inactivated.  */  
   "InactivateSiteSegments":boolean,
   "EDISupplierEnable":boolean,
   "BitFlag":number,
   "BankBankName":string,
   "BankDescription":string,
   "CNOurBankBankAcctDescription":string,
   "CNOurBankBankAcctBankName":string,
   "CurrCashRateGrpDescription":string,
   "CurrExpenseRateGrpDescription":string,
   "CurrFARateGrpDescription":string,
   "CurrGenRateGrpDescription":string,
   "CurrInvRateGrpDescription":string,
   "CurrPORateGrpDescription":string,
   "CurrPRRateGrpDescription":string,
   "CurrSalesRateGrpDescription":string,
   "CurrSubRateGrpDescription":string,
   "CurrTaxRateGrpDescription":string,
   "FSAExpensePMUIDType":number,
   "FSAExpensePMUIDName":string,
   "FSAExpensePMUIDSummarizePerCustomer":boolean,
   "FSARMAReasonCodeDescription":string,
   "FSAShipViaCodeDescription":string,
   "FSAShipViaCodeWebDesc":string,
   "GlobalCurrencyDocumentDesc":string,
   "GlobalCurrencyCurrDesc":string,
   "GlobalCurrencyCurrName":string,
   "GlobalCurrencyCurrencyID":string,
   "GlobalCurrencyCurrSymbol":string,
   "MXDocTypeDescription":string,
   "StockProvFmtExcessDescription":string,
   "StockProvFmtSlowDescription":string,
   "SysFormsPrinterDescription":string,
   "SysLabelsPrinterDescription":string,
   "THTaxRecDocTypeDescription":string,
   "THWHTDocTypeDescription":string,
   "WFGroupDescription":string,
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
      @param ipJPFiscalCalendarID
      @param ds
   */  
export interface ChangeJPFiscalCalendarID_input{
      /**  Proposed input value of Japan Fiscal Calendar  */  
   ipJPFiscalCalendarID:string,
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface ChangeJPFiscalCalendarID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param sendToFSA
      @param ds
   */  
export interface ChangeSendToFSA_input{
      /**  Proposed input value for checkbox Sync to FSA  */  
   sendToFSA:boolean,
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface ChangeSendToFSA_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ipAPTaxLnLevel
      @param ds
   */  
export interface CheckAPTaxLnLevel_input{
      /**  New APTaxLnLevel value  */  
   ipAPTaxLnLevel:boolean,
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface CheckAPTaxLnLevel_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_CompanyTableset,
}
}

export interface CheckARinvcDates_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param cTaxLiabilityCode
   */  
export interface CheckDefTaxLiability_input{
      /**  Default Tax Liability code  */  
   cTaxLiabilityCode:string,
}

export interface CheckDefTaxLiability_output{
}

   /** Required : 
      @param cTaxTypeCode
   */  
export interface CheckDefTaxType_input{
      /**  Default Tax Type code  */  
   cTaxTypeCode:string,
}

export interface CheckDefTaxType_output{
}

   /** Required : 
      @param payrollDate
   */  
export interface CheckPayrollDate_input{
      /**  Payroll Start Date  */  
   payrollDate:string,
}

export interface CheckPayrollDate_output{
parameters : {
      /**  output parameters  */  
   payrollMessage:string,
}
}

   /** Required : 
      @param ipRedStornoOpt
   */  
export interface CheckRedStornoOpt_input{
      /**  proposed red storno option. This needs to run if the option is NP (not permitted)  */  
   ipRedStornoOpt:string,
}

export interface CheckRedStornoOpt_output{
}

   /** Required : 
      @param cCodeTypeID
      @param cCodeID
      @param lPublishEx
   */  
export interface CheckUDCodeEx_input{
      /**  User-defined code type.  */  
   cCodeTypeID:string,
      /**  Code ID for check.  */  
   cCodeID:string,
      /**  If Yes - exception should be raised if UD code does not exist; If No - exception should not be raised.  */  
   lPublishEx:boolean,
}

export interface CheckUDCodeEx_output{
parameters : {
      /**  output parameters  */  
   cDescription:string,
}
}

   /** Required : 
      @param cCodeID
   */  
export interface CheckUDCodesExistence_input{
      /**  Code ID for check.  */  
   cCodeID:string,
}

export interface CheckUDCodesExistence_output{
parameters : {
      /**  output parameters  */  
   lUDCodeExists:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckVATFormat_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface CheckVATFormat_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChgCompanyFisCal_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface ChgCompanyFisCal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChgCountry_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface ChgCountry_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChgJCSystForecastPeriods_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface ChgJCSystForecastPeriods_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
      @param proposedTemplateJobNum
   */  
export interface ChgingMJTemplate_input{
   ds:Erp_Tablesets_CompanyTableset[],
      /**  Proposed input value of the Template Job Num  */  
   proposedTemplateJobNum:string,
}

export interface ChgingMJTemplate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

export interface CleanHCMLink_output{
}

   /** Required : 
      @param company
   */  
export interface CompanyTaxConnectCertCaptureEnabled_input{
      /**  Company  */  
   company:string,
}

export interface CompanyTaxConnectCertCaptureEnabled_output{
   returnObj:boolean,
}

   /** Required : 
      @param company
   */  
export interface CompanyTaxConnectEnabled_input{
      /**  Company  */  
   company:string,
}

export interface CompanyTaxConnectEnabled_output{
   returnObj:boolean,
}

   /** Required : 
      @param company
   */  
export interface DeleteByID_input{
   company:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param vCompany
   */  
export interface DisabledGLFields_input{
      /**  Company number  */  
   vCompany:string,
}

export interface DisabledGLFields_output{
parameters : {
      /**  output parameters  */  
   vFieldList:string,
}
}

   /** Required : 
      @param ds
      @param ds1
      @param companyID
   */  
export interface ETCAfterAddrVal_input{
   ds:Erp_Tablesets_CompanyTableset[],
   ds1:Erp_Tablesets_ETCAddrValidationTableset[],
      /**  Company.CompanyID  */  
   companyID:string,
}

export interface ETCAfterAddrVal_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param companyID
   */  
export interface ETCValidateAddress_input{
      /**  Company.Company  */  
   companyID:string,
}

export interface ETCValidateAddress_output{
   returnObj:Erp_Tablesets_ETCAddrValidationTableset[],
parameters : {
      /**  output parameters  */  
   statusFlag:boolean,
   errorFlag:boolean,
   errorMsg:string,
}
}

export interface Erp_Tablesets_AGCompanyRow{
      /**  Company  */  
   Company:string,
      /**  Generated Files Folder  */  
   GenFilesFolder:string,
      /**  Inventory Movement Mandatory CUIT  */  
   InvMoveMandCUIT:boolean,
      /**  Sales Order Mandatory CUIT  */  
   SOMandCUIT:boolean,
      /**  Default Import Destination  */  
   DefaultDestination:string,
      /**  Transport Key  */  
   TransportKey:string,
      /**  Withholding Certificate Signer  */  
   WHCertificateSigner:string,
      /**  Signer Position  */  
   SignerPosition:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Web Service Code  */  
   WebServiceConfigCode:string,
      /**  ElectronicCreditInvMinAmt  */  
   ElectronicCreditInvMinAmt:number,
      /**  FinOption  */  
   FinOption:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_APSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if Receipt transactions are to be used to create invoices. This flag is used by the Receipt entry program to set the value of the RcvHead.SaveForInvoicing.  Invoice entry pulls in receipt details  Receipt.SaveForInvoicing = Yes and Receipt.Invoiced =  No.  */  
   SaveReceipts:boolean,
      /**  Configures the A/P automatic invoice payment selection process to unconditionally take any available discount amount.  */  
   AlwaysDiscount:boolean,
      /**  Identifies default aging format, the details of which is stored in the AgingRptFmt table.  */  
   FmtCode:string,
      /**  Stores the FmtCode of the AgingRptFmt record that is to be considered the A/P default.  */  
   DefaultFmtCode:string,
      /**  Used by AP Check printing.  It is the line # at which the check perforation is.  */  
   CheckPerforationLineNum:number,
      /**  For internal use only.  Used with CPayCompany to enforce security of the Centralized Payment Parent company.  */  
   CPayParent:string,
      /**  Company that is the Parent of Centralized Payment process.  More than one company can be attached to a serial number that has the Centralized Payment module entered.  This field designates which of those companies is the Central Payment Parent Company and can therefore create invoices flagged for centralized payment.  */  
   CPayCompany:string,
      /**  Indicates if user is allowed to override the Reverse Charge Method in the AP invoice line.  */  
   AllowReverseCharges:boolean,
      /**  It used to catch rounding differences that might occur when vendor invoices are settled in a currency different from the invoice currency  */  
   RoundTolerance:number,
      /**  If the value is true and in case the total balance of an invoice transaction is within the total rounding setup for the currency of the invoice the balance is automatically accepted and booked as a rounding difference.  If the value is false the user has to balance the transaction manually.  */  
   RoundInvoice:boolean,
      /**   Determines how a logged invoice is processed through the accounting system.
TR = Authorization Tracking.  Logged invoices are not processed by the Posting Engine.  Logging invoices is done for tracking purposes.  Full accounting is done when the AP Invoice is created.
TA - Account for Taxes.  When logged invoices are posted, accounts payable and tax amounts are booked directly to the respective accounts, the invoice net amount is posted to a Logged Invoice Suspense Account.  The entry is removed from the suspense account when the logged invoice is converted to an AP Invoice.
S - Book All to a Suspense Account.  When the logged invoice is posted the tax invoice and net amount are posted to a Logged Invoice Suspense Account.  The entry is removed from the suspense account when the logged invoice is voided or converted to a regular AP Invoice.  */  
   LogInvAccting:string,
      /**  List of authorized administrators who are able to mark a logged action as complete.  */  
   AuthAdmins:string,
      /**  Indicates if Logged Invoices are created in an Aprpoved state or if they must be manually approved.  If the Accounting Option is 'Authorization Tracking' logged invoices can not be auto approved.  */  
   LogInvAutoAprv:boolean,
      /**  First G/L Update Stage  */  
   GLStage:string,
      /**  Next available number in PI numbering sequence  */  
   NextPINum:number,
      /**  Number of digits allowed for PI Numbering  */  
   NumDigit:number,
      /**  Next available number sequence for ap invoices created from employee expenses.  */  
   NextExpInvSeq:number,
      /**  This flag will be used to default the InvcHead.ReadyToCalc field when an Account Payable invoice is created. Defaults to No.  */  
   InvcReadyToCalcDflt:boolean,
      /**  Indicates which date to use (Apply/Invoice Date) to calculate exchange rates.  */  
   ExchangeDateToUse:number,
      /**  Invoice Legal Numbers based on “Apply/Invoice” Date for AP invoices and Debit Memos  */  
   LNBasedOnDate:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates that it need to copy exchange Rates during generation of AP Debit Memo.  */  
   CopyExcRateDM:boolean,
      /**  Indicates that it need to copy exchange Rates for creating AP Correction Invoice.  */  
   CopyExcRateCorrInv:boolean,
      /**  The Taxable option from Purchase Order Entry is brought into AP Invoice Entry.  */  
   UsePODtlTaxable:boolean,
      /**  Invoice Legal Number required for AP Invoices and Debit Memos.  */  
   LNReqForInvc:boolean,
      /**  Apply pre-payments on accounts payable (AP) invoices automatically.  */  
   ApplyAPPrePayAuto:boolean,
      /**  Field to enable functionality of Dates Set Up  */  
   DatesSetUp:boolean,
      /**  Field to Allow Amend the Apply Date on AP Invoices  */  
   APAmdApplyDate:boolean,
      /**  Field to Allow Amend the Tax Point Date on AP Invoices  */  
   APAmdTaxPDate:boolean,
      /**  Field to Allow Amend the Tax Rate Date on AP Invoices  */  
   APAmdTaxRateD:boolean,
      /**  Field to default the Apply Date on AP Invoices  */  
   APDefApplyDate:string,
      /**  Field to default the Tax Point Date on AP Invoices  */  
   APDefTaxPDate:string,
      /**  Field to default the Tax Rate Date on AP Invoices  */  
   APDefTaxRateD:string,
      /**  Field to link the Apply Date on AP Invoices  */  
   APLinkApplyDate:string,
      /**  Field to link the Tax Point Date on AP Invoices  */  
   APLinkTaxPDate:string,
      /**  Field to link the Tax Rate Date on AP Invoices  */  
   APLinkTaxRateD:string,
      /**  TWAPLegNumSource  */  
   TWAPLegNumSource:string,
      /**  TWAPThresholdTax  */  
   TWAPThresholdTax:number,
      /**  Current Tax Year  */  
   TaxYear:number,
      /**  Taxpayer Identification Number for Payer  */  
   PayersTIN:string,
      /**  Name Control for 1099 Payer  */  
   NameControl:string,
      /**  Office Code for 1099 Payer  */  
   OfficeCode:string,
      /**  First line of the Payer name  */  
   Name1:string,
      /**  Second line of Payer name  */  
   Name2:string,
      /**  First address line of the Payer address  */  
   Address1:string,
      /**  Second address line of the Payer address  */  
   Address2:string,
      /**  Third address line of the Payer address  */  
   Address3:string,
      /**  City portion of the address of the Payer address  */  
   City:string,
      /**  State portion of the Payer address  */  
   State:string,
      /**  Postal code or zip code portion of the Payer address  */  
   ZIP:string,
      /**  The phone number of the Payer  */  
   PhoneNum:string,
      /**  Transmitter Control Code  */  
   TransControlCode:string,
      /**  COExtWordAmt  */  
   COExtWordAmt:string,
      /**  DeferredExpCurr  */  
   DeferredExpCurr:number,
      /**  Flag that allows to create multiple invoicing of receipts  */  
   AllowMultInvcReceipts:boolean,
      /**  Days outstanding allowed. It is used to validate if the days between the invoice date and receipt date are greater or equal than this value  */  
   DaysOutstanding:number,
      /**  Percentage of tolerance that is allowed in each receipt and its invoiced and not invoiced lines  */  
   PcntTolerance:number,
      /**  Amount of tolerance that is allowed in each receipt and its not invoiced lines  */  
   AmountTolerance:number,
      /**  Type of the Payer  */  
   TaxEntityType:string,
      /**  Subcategory of the Payer  */  
   TaxEntitySubCat:string,
      /**  Contact person name  */  
   ContactPerson:string,
      /**  Role/Designation of the contact person  */  
   RoleCode:string,
      /**  Name of the office branch  */  
   BranchName:string,
      /**  Permanent Account Number for Payer  */  
   PayersPAN:string,
      /**  Contact person email address  */  
   EMailAddress:string,
      /**  Area code for the phone number of the Payer  */  
   AreaCode:string,
      /**  The fax number of the Payer  */  
   FaxNum:string,
      /**  The action to take when an AP Invoice Invoice Date or Apply Date is greater than today plus the days horizon.  Options are (W)arning, (S)top, (N)one  */  
   FutureDateAction:string,
      /**  The number of days beyond today's date that an AP Invoice Invoice Date or Appy Date can be.  */  
   FutureDateDaysHorizon:number,
      /**  Form 1099-K Filer  */  
   US1099KFiler:string,
      /**  Form 1099-K PSE Name  */  
   US1099KPSEName:string,
      /**  Form 1099-K PSE Phone  */  
   US1099KPSEPhone:string,
      /**  Indicates that the exchange rate will be copied when creating an AP Cancellation Invoice.  */  
   CopyExcRateCancelInv:boolean,
      /**  APTaxRoundOption  */  
   APTaxRoundOption:number,
      /**  EInvoice  */  
   EInvoice:boolean,
      /**  TaxRegionCode  */  
   TaxRegionCode:string,
      /**  Centralized Payment  */  
   CentralizedPayment:boolean,
      /**  US1099ReportBySite  */  
   US1099ReportBySite:boolean,
      /**  Indicates which date is used for TaxTran Transaction Date - AP Invoices related records  */  
   APTaxRptDate:number,
   AuthAdminsName:string,
      /**  Indicates which date to use to calculate exchange rates  */  
   ExchangeDate:number,
   TaxRegionCodeDesc:string,
   BitFlag:number,
   AgingRptFmtDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Used to establish the beginning Invoice #. When the system generates a new InvcHead it will assign the greater of (StartInvoiceNum) or (the last Invoice # on file + 1) as the invoice number.  */  
   StartInvoiceNum:number,
      /**  Indicates if Shipment transactions are to be used to create invoices. This flag is used by the Shipping entry program to set the value of the  "Invoiced" flag field. (see ShipHead.Invoiced).  Invoice entry generates invoices for Shipments which contain  "Invoiced" flag =  No.  */  
   SaveShipments:boolean,
      /**  Order Entry action to a Credit Held customer.  Valid values are "WARN" or "STOP".  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the order and customer placed on credit hold.  STOP means that the order line addition/change to the order is not accepted and the order and customer are not placed on credit hold.  */  
   CreditOrderAction:string,
      /**  Shipping Entry action to a Credit Held order.  Valid values are "WARN" or "STOP".  WARN means that the user is warned that the order is on credit hold, but allowed to proceed (or cancel) with the shipment.  STOP means that the shipment for that order is not accepted.  */  
   CreditShipAction:string,
      /**  The Journal Code of the Journal that will be used for A/R invoices. Normally this would be called Sales Journal.  */  
   SJJournalCode:string,
      /**   The Journal Code of the Journal that will be used for A/R adjustments and application of credit memos.
Normally this would be called the Adjustments Journal.  */  
   AJJournalCode:string,
      /**  Use Shipment date for Invoice Date  */  
   UseShipDateForInvDate:boolean,
      /**  Stores the FmtCode of the AgingRptFmt record that is to be considered the A/R default.  */  
   DefaultFmtCode:string,
      /**  Identifies default aging format, the details of which is stored in the AgingRptFmt table.  */  
   FmtCode:string,
      /**  This flag will be used to default the InvcHead.ReadyToCalc field when an invoice is created. Defaults to No  */  
   InvcReadyToCalcDflt:boolean,
      /**  Indicates if user is allowed to override the Reverse Charge Method in the AR invoice line.  */  
   AllowReverseCharges:boolean,
      /**  It is used to catch rounding differences that might occur when customer invoices are settled in a currency different from the invoice currency.  */  
   RoundTolerance:number,
      /**  if Yes it means that tax rounding and calculation level (line or total) are performed according to rules set on each customer, if NO - according to company setup  */  
   TaxARCustomRules:boolean,
      /**  Credit checking relationship  */  
   RlsClassCredit:string,
      /**  Reporting relationship class  */  
   RlsClassReport:string,
      /**  Payer-sold to relationship, lets payer customer pays for the sold to customer, who is billed in the invoice  */  
   RlsClassPayerSold:string,
      /**  Accepts payments from any customer within the same national account, regardless of parent-child status  */  
   AcrossNatAcc:boolean,
      /**  This field is used to enable ability in Cash Receipts to prorate the discount amount back to the original sales accounts instead of the Discount Account of the module or group part.  */  
   ProrateDiscToLine:boolean,
      /**  Indicates if legal numbers are required for invoices.  */  
   LNReqForInvc:boolean,
      /**  Indicates how finance/late charges are calculated and charged with these two options: Percentage on Invoice Amount (Default) or Percentage on Amount Overdue.  */  
   ChargeMethod:boolean,
      /**  Indicates if finance charge shall only be applied once per invoice. In case it?s not checked, finance charges shall be calculated each time the process is executed.  */  
   OncePerInvoice:boolean,
      /**  Indicates that the system will generate a combined reminder letter and finance charge invoice.  */  
   CombWReminder:boolean,
      /**  A/R Clearing Accounting  */  
   ARClearing:boolean,
      /**  Indicates if user is allowed to set Invoice Settlement in Different Currency for Cash Receipts and Credit Memo.  */  
   AllowSettlementInDiffCurr:boolean,
      /**  Field to default the Apply Date on AR Invoices.  */  
   ARDefApplyDate:string,
      /**  Field to default the Shipment Date on AR Invoices.  */  
   ARDefShipDate:string,
      /**  Field to default the Tax Point Date on AR Invoices.  */  
   ARDefTaxPDate:string,
      /**  Field to default the Currency Date on AR Invoices.  */  
   ARDefCurrDate:string,
      /**  Field to default the Tax Rate Date on AR Invoices.  */  
   ARDefTaxRateD:string,
      /**  Field to link the Apply Date on AR Invoices.  */  
   ARLinkApplyDate:string,
      /**  Field to link the Shipment Date on AR Invoices.  */  
   ARLinkShipDate:string,
      /**  Field to link the Tax Point Date on AR Invoices.  */  
   ARLinkTaxPDate:string,
      /**  Field to link the Currency Date Date on AR Invoices.  */  
   ARLinkCurrDate:string,
      /**  Field to link the Tax Rate Date on AR Invoices.  */  
   ARLinkTaxRateD:string,
      /**  Field to Allow Amend the Apply Date on AR Invoices.  */  
   ARAmdApplyDate:boolean,
      /**  Field to Allow Amend the Shipment Date on AR Invoices.  */  
   ARAmdShipDate:boolean,
      /**  Field to Allow Amend the Tax Point Date on AR Invoices.  */  
   ARAmdTaxPDate:boolean,
      /**  Field to Allow Amend the Currency Date on AR Invoices.  */  
   ARAmdCurreDate:boolean,
      /**  Field to Allow Amend the Tax Rate Date on AR Invoices.  */  
   ARAmdTaxRateD:boolean,
      /**  Field to enable funcionality of Dates Set Up  */  
   DatesSetUp:boolean,
      /**  Field to default the Tax Rate Date for cancellation or adjusment credit on AR Invoices.  */  
   ARDefTaxRCrD:string,
      /**  Field to Allow Amend the Tax Rate Date for cancellation or adjusment credit on AR Invoices.  */  
   ARAmdTaxRCrD:boolean,
      /**  This field will hold the default value for InvcHead.UseAltBillTo which indicates if the Alternate Bill To address should be used for taxing instead of the ship to address.  */  
   UseAltBillToAddr:boolean,
      /**  Flag to indicate if the Exchange Rate should be copied from the original Invoice for a Correction Invoice.  */  
   CopyExchangeRate:boolean,
      /**  Indicates first PI stage that updates the G/L  */  
   GLStage:string,
      /**  Endorse AP  */  
   EndorseAP:boolean,
      /**  GL Status  */  
   GLStatus:boolean,
      /**  Unapproved Status  */  
   UnapprovedStatus:string,
      /**  Portfolio Status  */  
   PortfolioStatus:string,
      /**  Bank Status  */  
   BankStatus:string,
      /**  Settled Status  */  
   SettledStatus:string,
      /**  Next available number in PI numbering sequence  */  
   NextPINum:number,
      /**  Number of digits allowed for PI Numbering  */  
   NumDigit:number,
      /**  Cash Receipts from sale preferred bank.  */  
   PreferredBank:string,
      /**  IsDiscountforCreditM  */  
   IsDiscountforCreditM:boolean,
      /**  MandateCounter  */  
   MandateCounter:number,
      /**  SEPADDMsgCounter  */  
   SEPADDMsgCounter:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates that for AR Invoices the confirmation taxes can be used.  */  
   AllowConfirmationTax:boolean,
      /**  UseAltBillToID  */  
   UseAltBillToID:boolean,
      /**  CopyExcRateCancelInv  */  
   CopyExcRateCancelInv:boolean,
      /**  CopyExcRateCM  */  
   CopyExcRateCM:boolean,
      /**  ExchangeDate  */  
   ExchangeDate:number,
      /**  AllowOverpaidInv  */  
   AllowOverpaidInv:boolean,
      /**  AutoARBal  */  
   AutoARBal:boolean,
      /**  CancelledStatus  */  
   CancelledStatus:string,
      /**  AdjDocLevTax  */  
   AdjDocLevTax:boolean,
      /**  RetainCreditOverride  */  
   RetainCreditOverride:boolean,
      /**  LNCashRecForUnappliedRec  */  
   LNCashRecForUnappliedRec:boolean,
      /**  AllowNegativeDiscount  */  
   AllowNegativeDiscount:boolean,
      /**  AllowNegativeQuantity  */  
   AllowNegativeQuantity:boolean,
      /**  UseControlledCM  */  
   UseControlledCM:boolean,
      /**  Use Copy Numbers in AR Invoice  */  
   UseCopyNumInARInv:boolean,
      /**  Miscellaneous AR Invoice action to a Credit Held customer.  Valid values are "WARN" or "STOPENTRY", “STOPPOST”, “IGNORE”.  WARN means that the user is given a warning, but allowed to proceed (or cancel) with the invoice.  STOPENTRY means that the user is given a message that invoice cannot be created.  STOPPOST means the user is giving a message the invoice cannot be created, but it cannot be posted until the customer is removed from credit hold.  IGNORE means no message is received but the invoice will be marked as on credit hold.  */  
   CreditLimitInvoiceAction:string,
      /**  Maximum Write Off Amount  */  
   MaxWriteOffAmt:number,
      /**  Allow Negative Write Off  */  
   AllowNegativeWriteOff:boolean,
      /**  Invoice Deposit Tax Treatment  */  
   DepTaxTreatment:string,
      /**  Can be set = yes, if Deposit Invoice Tax treatment is Tax Shipment Net movement. Allow shipment invoice with negative net tax elements  */  
   DepAllowNegativeTax:boolean,
      /**  Product Tax Category  */  
   DepTaxCatID:string,
      /**  Require Deposit Invoice  */  
   DepInvcRequired:boolean,
      /**  Invoice Days Delay  */  
   DepDaysDelay:number,
      /**  Deposit transaction Document Type of type AR Invoice  */  
   DepTranDocTypeID:string,
      /**  Deposit Invoices show prior linked Deposit Invoices  */  
   DepShowLinkedInvc:boolean,
      /**  MandatoryARRemittanceSlip  */  
   MandatoryARRemittanceSlip:boolean,
      /**  Endorsed to Supplier PI Status  */  
   EndorsedToSupplierStatus:string,
      /**  AllowNegBal  */  
   AllowNegBal:boolean,
      /**  Company that is the Parent of Centralized Collection process.  This field designates which company is the Central Collection Parent Company and can therefore receive and pay the invoices flagged for centralized collection.  */  
   CColCompany:string,
      /**  Flag to indicate if Invoices created automatically will be marked for Central Collection.  */  
   CentralCollectionForAutoInv:boolean,
      /**  Use Bill To Tax ID in Sales List  */  
   UseBillToTaxIDInSL:boolean,
      /**  Split Revenue based on combination of Product Group and Tax Effective Rate GLC  */  
   SplitRevenueByTaxEffRate:boolean,
      /**  EnableSettlementFeature  */  
   EnableSettlementFeature:boolean,
   ARClearingAcctDesc:string,
      /**  XASyst.ARClearingDept  */  
   ARClearingDept:string,
   ARClearingDisplayAccount:string,
      /**  XASyst.ARClearingDiv  */  
   ARClearingDiv:string,
      /**  Indicates which date is used for TaxTran Transaction Date - AR Invoices related records  */  
   ARTaxRptDate:number,
      /**  If yes, enable IntPay acount (from GLSyst)  */  
   ARVoucherInvoices:boolean,
   DEPTaxCatIDDescription:string,
   DepTranDocTypeLinkDescription:string,
   isRlsCreditEmpty:boolean,
   isRlsPayEmpty:boolean,
   isRlsReportEmpty:boolean,
      /**  XASyst.ARClearingChart  */  
   ARClearingChart:string,
   BitFlag:number,
   AgingRptFmtDescription:string,
   AJJournalCodeJrnlDescription:string,
   PIStatusBStatusDesc:string,
   PIStatusCStatusDesc:string,
   PIStatusEToSStatusDesc:string,
   PIStatusPStatusDesc:string,
   PIStatusSStatusDesc:string,
   PIStatusUStatusDesc:string,
   PreferredBankDescription:string,
   PreferredBankBankName:string,
   SJJournalCodeJrnlDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BMSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unapprove part revisions when checked out to ECO.  */  
   UnapproveRevOnCheckout:boolean,
      /**  Indicates if the user's password will be verified during operations such as Rev approve/unapprove, checkout, checkin.  */  
   VerifyPassword:boolean,
      /**  If TRUE then a workflow group and task set is required on ECO Group records.  */  
   WorkflowRequired:boolean,
      /**  If TRUE then the Engineering Workbench is limited to one user per ECO Group.  If FALSE then individual revisions within a group can be locked.  */  
   SingleUser:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_BorderPctRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   DestCountryNum:number,
      /**  This is used to calculate the percentage of the miscellaneous charge to be applied in the Intrastat.  */  
   PctAtBorder:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   DestCountryNumDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CRSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company default Task set.  Used to assign to new lead/opportunity/quote when there isn't a task set for the Sales Territory for the Quote.  */  
   DefTaskSetID:string,
      /**  Company default Marketing Campaign.  Used to assign to a new lead/opportunity/quote.  */  
   DefMktgCampaignID:string,
      /**  Company default Web Marketing Campaign.  Used to assign to a new lead/opportunity/quote.  */  
   DefWebMktgCampaignID:string,
      /**  Default "win" reason Code.  From Reason table with Code type of "w"  */  
   WinReasonCode:string,
      /**  Default "Loss" reason Code.  From Reason table with Code type of "L"  */  
   LossReasonCode:string,
      /**  Default "Task Completion" reason Code.  From Reason table with Code type of "T"  */  
   TaskReasonCode:string,
      /**  Indicates that the win Function will close all open tasks on the LOQ  */  
   CloseTasksWin:boolean,
      /**  Indicates that the Lose Function will close all open tasks on the LOQ  */  
   CloseTasksLose:boolean,
      /**  Company default Sales territory  */  
   TerritoryID:string,
      /**  Company default Inter-Company Marketing Campaign.  Used to assign to a new lead/opportunity/quote.  */  
   DefICMktgCampaignID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This flag indicates if the territory security is applied to sales order. By applying territory security at SO the user only can load sales orders and customers for the territory that his workforce has access.  */  
   UseTerritorySecurity:boolean,
      /**  Number  of calls assigned to the owner that are loaded automatically when opening CRM Call log.  */  
   CRMCallsShown:number,
      /**  This fields defines if the Epicor ERP CRM is integrated to an External CRM.  Only enabled if there is an active license for External CRM Integration.  */  
   ExternalCRMIntegration:boolean,
      /**  This fields define the external software used as the Extenral CRM. The valid option are  S: Salesfore.com .  */  
   ExternalCRMSystem:string,
      /**  This is the URL used to integrate to the External CRM system  */  
   ExternalCRMURL:string,
      /**  This field determines what system is used as the primary master file holder. The valid values are E : Epicor ERP  C: External CRM  */  
   ExternalCRMMasterFile:string,
      /**  This field defines the token used to integrate to the External CRM  */  
   ExternalToken:string,
      /**  This field defines the user id used to integrate to the External CRM  */  
   ExternalCRMLoginID:string,
      /**  This field defines the token password to integrate to the External CRM  */  
   ExternalCRMPassword:string,
      /**  This field defines the time zone used by the External CRM. This is used in cases where the External CRM is located in a different time zone than Epicor ERP.  */  
   ExternalCRMTimeZoneID:string,
      /**  This field defines the default Industry Class Type used by the External CRM. The valid values are all the active Industry Class Type Id defined in Epicor ERP.  */  
   ExternalCRMDefaultICTypeID:string,
      /**  This field defines the last time that the External CRM has been Synchronized to Epicor ERP. This field is maintained by the External CRM Synchronization  process.  */  
   ExternalCRMLastSync:string,
      /**  This field defines the last time that Customer Contacts  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   ExternalCRMLastSyncContact:string,
      /**  This field defines the last time that the Customers  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   ExternalCRMLastSyncCustomer:string,
      /**  This field defines the last time that  Part  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   ExternalCRMLastSyncPart:string,
      /**  This field defines the last time that  Quotes  has been Synchronized between Epicor ERP and the External CRM. This field is maintained by the External CRM Synchronization  process.  */  
   ExternalCRMLastSyncQuote:string,
      /**  This field is used by the External CRM integration only.  */  
   ExternalCRMCreateSO:number,
      /**  External CRM masked password.  */  
   ExternalCRMPasswordMasked:string,
   BitFlag:number,
   DefICMktgCampDescription:string,
   DefMktgCampaignIDCampDescription:string,
   DefTaskSetIDWorkflowType:string,
   DefTaskSetIDTaskSetDescription:string,
   DefWebMtkgCampDescription:string,
   ExternalCRMDefaultICTypeDescription:string,
   LossReasonDescription:string,
   TaskReasonDescription:string,
   TerritoryIDTerritoryDesc:string,
   WinReasonDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CSFSystRow{
      /**  Company Identifier.  */  
   Company:string,
   TaxInfo1:string,
   TaxInfo2:string,
   TaxInfo3:string,
   TaxInfo4:string,
   TaxInfo5:string,
   TaxInfo6:string,
   TaxInfo7:string,
   TaxInfo8:string,
   TaxInfo9:string,
   TaxInfo10:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RedStornoOpt  */  
   RedStornoOpt:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CompanyAttchRow{
   Company:string,
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

export interface Erp_Tablesets_CompanyListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company Name  */  
   Name:string,
      /**  First company address line.  */  
   Address1:string,
      /**  City portion of company address.  */  
   City:string,
      /**  State portion of company address.  */  
   State:string,
      /**  Postal code or zip code portion of company address.  */  
   Zip:string,
      /**  Company phone number  */  
   PhoneNum:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CompanyListTableset{
   CompanyList:Erp_Tablesets_CompanyListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CompanyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Company Name  */  
   Name:string,
      /**  First company address line.  */  
   Address1:string,
      /**  Second company address line.  */  
   Address2:string,
      /**  Third company address line.  */  
   Address3:string,
      /**  City portion of company address.  */  
   City:string,
      /**  State portion of company address.  */  
   State:string,
      /**  Postal code or zip code portion of company address.  */  
   Zip:string,
      /**  Country portion of company address.  */  
   Country:string,
      /**  Company phone number  */  
   PhoneNum:string,
      /**  Company fax number  */  
   FaxNum:string,
      /**  Federal Income Tax Number  */  
   FEIN:string,
      /**  State Tax ID  */  
   StateTaxID:string,
      /**  Current fiscal year  */  
   CurrentFiscalYear:number,
      /**  This is the Trading Partner ID that is used for incoming and outgoing EDI.  */  
   EDICode:string,
      /**  The Tax Region Code for this company. This tax region is used to define the 'interior'. It is used as a default tax region in Vendor Maintenance.  */  
   TaxRegionCode:string,
      /**  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  */  
   CountryNum:number,
      /**  Added for FRx Integration which requires that the company is identified by a unique positive integer, as opposed to a character string.  FRx calls this the entity number.  It is maintained on the General Ledger configuration screen.  */  
   Number:number,
      /**  Data Source Name for the FRx database for this company.  Must be linked to a SQL Server 7.0 database to allow exporting of data for financial reporting using FRx.  This field is maintained on the General Ledger configuration screen for each company.  */  
   FRxDSN:string,
      /**  The file set where the eScheduling XML messages will be sent.  It must be a valid DOS file name.  If eScheduling is being used with the Manufacturing System this field is required.  */  
   EschedFileSet:string,
      /**  Unique identifier from and external G/L interface  */  
   ExternalID:string,
      /**  Name of file that contains the company's logo image.  This can be blank (no logo available).  This is used for Customer/Sales/Supplier Connect.  */  
   LogoFile:string,
      /**  Path the Employee Photos are stored in.  */  
   EmpPhotoPath:string,
      /**   Descriptive Code assigned by the user which uniquely identifies the Calendar.  If this equals "", then the ProdCal record is the Company Level production calendar.
A Production Calendar can be attached to a Resource Group, a Resource, or a Vendor.  */  
   CalendarID:string,
      /**  The User ID for FRx.  */  
   FrxUserid:string,
      /**  FRxUserID password  */  
   FRxPassWord:string,
      /**  The fiscal calendar id for the company.  */  
   FiscalCalendarID:string,
      /**  Company legal name  */  
   LegalName:string,
      /**  Tax Payer Registration Reason Code  */  
   TaxRegReason:string,
      /**  Economic Activity Type  */  
   ActTypeCode:string,
      /**  Organization Registration Code  */  
   OrgRegCode:string,
      /**  Chief Executive Officerr name  */  
   ManagerName:string,
      /**  Chief Financial Officer Name  */  
   ChiefAcctName:string,
      /**  Type of report  */  
   ReportTypePref:string,
      /**  WIApplication  */  
   WIApplication:string,
      /**  WIAutoCreateJob  */  
   WIAutoCreateJob:boolean,
      /**  WIGetDetails  */  
   WIGetDetails:boolean,
      /**  WISchedule  */  
   WISchedule:boolean,
      /**  WIRelease  */  
   WIRelease:boolean,
      /**  WIShippingCosts  */  
   WIShippingCosts:boolean,
      /**  DeepCopy  */  
   DeepCopy:boolean,
      /**  DeepCopyDupOrRevEst  */  
   DeepCopyDupOrRevEst:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MapURL  */  
   MapURL:string,
      /**  MXMunicipio  */  
   MXMunicipio:string,
      /**  APBOE Check  */  
   APBOECheck:number,
      /**  COSequenceCert  */  
   COSequenceCert:number,
      /**  Determines if the Company has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  Epicor client number for CRE  */  
   EpicorAccountNum:number,
      /**  StartDate  */  
   StartDate:string,
      /**  Kind of Employer F - Federal Government, S - State and Local Governmental Employer, T - Tax Exempt Employer, Y - State and Local Tax Exempt Employer, N - None Apply  */  
   KindOfEmp:string,
      /**  Use the Employment Code field to select either the 941 (Option R) tax form or the 944 (Option F) tax form, depending upon the tax form the employer files. This selection is used in the W2 Processing program during W2 form export.  */  
   EmploymentCode:string,
      /**  Purchase Schedule Mode specifies how the related demand requirements should be handled for this company.  */  
   PurchaseScheduleMode:string,
      /**  Currency.BaseCurrCode field  */  
   BaseCurrCode:string,
   ExtPRConfig:boolean,
      /**  Has Currency Transactions  */  
   HasCurrTrans:boolean,
   Intrastat:boolean,
      /**  Name of product (MFGSYS Name)  */  
   ProductName:string,
   AllowSchedulingBeforeToday:boolean,
   BitFlag:number,
   CalendarDescription:string,
   FiscalCalDescription:string,
   TaxRegionDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CompanyTableset{
   Company:Erp_Tablesets_CompanyRow[],
   CompanyAttch:Erp_Tablesets_CompanyAttchRow[],
   AGCompany:Erp_Tablesets_AGCompanyRow[],
   APSyst:Erp_Tablesets_APSystRow[],
   ARSyst:Erp_Tablesets_ARSystRow[],
   BMSyst:Erp_Tablesets_BMSystRow[],
   BorderPct:Erp_Tablesets_BorderPctRow[],
   CRSyst:Erp_Tablesets_CRSystRow[],
   CSFSyst:Erp_Tablesets_CSFSystRow[],
   Currency:Erp_Tablesets_CurrencyRow[],
   CurrRateGrp:Erp_Tablesets_CurrRateGrpRow[],
   EQSyst:Erp_Tablesets_EQSystRow[],
   ExtPRSyst:Erp_Tablesets_ExtPRSystRow[],
   FsSyst:Erp_Tablesets_FsSystRow[],
   GLSyst:Erp_Tablesets_GLSystRow[],
   ISSyst:Erp_Tablesets_ISSystRow[],
   JCSyst:Erp_Tablesets_JCSystRow[],
   MMSyst:Erp_Tablesets_MMSystRow[],
   PDMSyst:Erp_Tablesets_PDMSystRow[],
   PECompWhldHist:Erp_Tablesets_PECompWhldHistRow[],
   PRSyst:Erp_Tablesets_PRSystRow[],
   TaxSvcConfig:Erp_Tablesets_TaxSvcConfigRow[],
   XaSyst:Erp_Tablesets_XaSystRow[],
   XbSyst:Erp_Tablesets_XbSystRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CurrRateGrpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Description  */  
   Description:string,
      /**  Determines if the record is inactive  */  
   Inactive:boolean,
      /**  Determins if there is a base rate group to use if no rules or rates are defined for a currency  */  
   BaseRateGrpCode:string,
      /**  Currency to use during single or double currency conversions  */  
   CrossCurrCode:string,
      /**  Determine if rounding should be done after conversion  */  
   CrossRound:boolean,
      /**  Number of decimals to use during rounding  */  
   CrossRoundDec:number,
      /**  Currency used for double currency conversions  */  
   AltCrossCurrCode:string,
      /**  Determine if rounding should be done after conversion  */  
   AltCrossRound:boolean,
      /**  Number of decimals to use during rounding  */  
   AltCrossRoundDec:number,
      /**  Determines whether or not this rate group is shared between more than one company.  */  
   GlobalGrp:boolean,
      /**  Determines whether or not this record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Number of decimals for the exchange rates  */  
   RateNumDec:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  control when the GlobalGrp field should be enabled.  */  
   EnableGlobalGrp:boolean,
      /**  Control when the GlobalLock field should be enabled.  */  
   EnableGlobalLock:boolean,
      /**  Indicates if the Currency is Global (master or linked)  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany and GlbRateGrpCode that is linking to this Rate Group.  */  
   GlbLink:string,
      /**  Company Name from linked global rate group.  */  
   GlbCompanyName:string,
      /**  Rate group Code from linked global rate group.  */  
   GlbRateGrpCode:string,
      /**  Description from linked global rate group.  */  
   GlbRateGrpDesc:string,
      /**  Company ID from linked global rate group.  */  
   GlbCompanyID:string,
   BitFlag:number,
   AltCrossCurrCurrName:string,
   AltCrossCurrCurrDesc:string,
   AltCrossCurrCurrencyID:string,
   AltCrossCurrDocumentDesc:string,
   AltCrossCurrCurrSymbol:string,
   BaseRateGrpDescDescription:string,
   CrossCurrCurrDesc:string,
   CrossCurrCurrName:string,
   CrossCurrCurrencyID:string,
   CrossCurrDocumentDesc:string,
   CrossCurrCurrSymbol:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CurrencyRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Description of the currency  */  
   CurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   CurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   DocumentDesc:string,
      /**  Notes the about the Currency.  */  
   Note:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   CurrName:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   CurrencyID:string,
      /**  Number of decimals used for any types of amounts where they entered, printed, displayed, except unit price and unit cost, according to the table zFieldDecimal where ValueType = "G"  */  
   DecimalsGeneral:number,
      /**  Indicates if the currency is active  */  
   Inactive:boolean,
      /**  Number of decimals used for any unit prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "P"  */  
   DecimalsPrice:number,
      /**  Can only maintain exchange rates for currencies with this flag checked  */  
   MaintRate:boolean,
      /**  Number of decimals used for any cost prices where they entered, printed, displayed, according to the table zFieldDecimal where ValueType = "C"  */  
   DecimalsCost:number,
      /**  Indicates if this is the base currency.  Only one base currency is allowed  */  
   BaseCurr:boolean,
      /**  Define multiple that Unit Prices for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpUnitPrice:number,
      /**  Indicates if this is a reporting currency  */  
   ReportCurr:boolean,
      /**  Define multiple that Unit Tax for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpUnitTax:number,
      /**  Define multiple that Extended Prices (total line amount) for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpExtPrice:number,
      /**  Define multiple that Extended Tax (total line tax) for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpExtTax:number,
      /**  Define multiple that Total amount for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpTotalAmt:number,
      /**  Determines whether or not this currency is shared between more than one company.  */  
   GlobalCurr:boolean,
      /**  Define multiple that Total Tax amount for sales related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpTotalTax:number,
      /**  Determines whether or not this currency record will receive global updates.  */  
   GlobalLock:boolean,
      /**  Define the rule how Unit Price for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleUnitPrice:number,
      /**  Display factor for exchange rates  */  
   ScaleFactor:number,
      /**  Define the rule how Unit Tax for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleUnitTax:number,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   CountryNum:number,
      /**  Define the rule how Extended Prices (total line amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleExtPrice:number,
      /**  Indicates which reporting amount field (Rpt1, Rpt2, or Rpt3) stores this currency.  System field.  */  
   ReportCurrPos:number,
      /**  Define the rule how Extended Tax (total tax amount) for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleExtTax:number,
      /**  Define the rule how total amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleTotalAmt:number,
      /**  Define the rule how total tax amount for sales related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleTotalTax:number,
      /**  It used in AP Invoice, if the rounding amount remaining is less or equal to the tolerance, the remaining amount is automatically booked.  */  
   RoundTolerance:number,
      /**  ISO unique identifier  */  
   ISONumber:number,
      /**  Store ID for Credit Card Processing  */  
   StoreID:string,
      /**  Define multiple that Annual Depreciation Charge for asset related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpAnnualCharge:number,
      /**  Define multiple that Period Depreciation Charge for asset  related documents shall be rounded to, 0- no rounding.  */  
   RoundMltpPeriodCharge:number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRuleAnnualCharge:number,
      /**  Define the rule how Annual Depreciation Charge for asset related documents shall be rounded to the defined multiplier: 0 - no rounding, 1 - Round up, 2 - Round down, 3 - Rounding to the nearest.  */  
   RoundRulePeriodCharge:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AGAFIPCode  */  
   AGAFIPCode:string,
      /**  This Currency Code is used for CRE Processors.  */  
   ISOCurrCode:string,
      /**  ProcessorNum  */  
   ProcessorNum:number,
   BookCurr:boolean,
   CompanyBase:boolean,
      /**  Name of Country.  */  
   CountryName:string,
      /**  Control when the Base Currency should be enable.  */  
   EnableBaseCurr:boolean,
      /**  If currency exist in any transaction the decimals fields should be disables.  */  
   EnableDecimals:boolean,
      /**  control when the Global Currency field should be enable.  */  
   EnableGlobalCurr:boolean,
      /**  Control when the GlobalLock field should be enable.  */  
   EnableGlobalLock:boolean,
      /**  Control when the Inactive field should be enable.  */  
   EnableInactive:boolean,
      /**  GlbCompany that is linked to this currency  */  
   GlbCompany:string,
      /**  GlbCompany Name that is linked to this currency  */  
   GlbCompanyName:string,
      /**  GlbCurrency Description that is linked to this currency  */  
   GlbCurrDesc:string,
      /**  GlbCurrency Code that is linked to this currency  */  
   GlbCurrencyCode:string,
      /**  GlbCurrency ID that is linked to this currency  */  
   GlbCurrencyID:string,
      /**  GlbCurrency Symbol that is linked to this currency  */  
   GlbCurrSymbol:string,
      /**  Indicates if the Currency is Global (master or linked)  */  
   GlbFlag:boolean,
      /**  Delimited list of GlbCompany and GlbCurrencyCode that is linking to this currency  */  
   GlbLink:string,
   HasCCInterface:boolean,
      /**  This field store the RowID of the record that is marked as Base Currency.  */  
   BaseRowRowID:string,
   BitFlag:number,
   CountryDescription:string,
   CreditCardProcessorDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_EQSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Used to establish the beginning Sales Order #. When the system generates a new order it will assign the greater of (StartOrderNum) or (the last orders # on file + 1) as the order number.  */  
   StartQuoteNum:number,
      /**  A integer that express the # of days from the date quoted that someone should follow up with the customer concerning the quote. This is used by quote entry to calculate a default follow up date (QuoteHed.FollowUpDate). Default follow up date is QuoteHed.DateQuoted + EQSyst.FollowUpDays  */  
   FollowUpDays:number,
      /**  An integer that express the # of days from the quoted date when quotes will expire. This is used by quote entry to calculate the QuoteHed.ExpirationDate  */  
   ExpirationDays:number,
      /**  An integer that defines the # of days in which the quoting process needs to be completed in. Quote entry uses this in calculating the QuoteHed.DueDate.  */  
   QuoteDueDays:number,
      /**  Label used for the QuoteHed.CheckOff1 field.  There are 5 CheckOffLabel fields. They are all optional. If entered then the corresponding QuoteHed.CheckOff fields become active.  */  
   CheckOff1Label:string,
      /**  Label used for the QuoteHed.CheckOff2 field.  */  
   CheckOff2Label:string,
      /**  Label used for the QuoteHed.CheckOff3 field.  */  
   CheckOff3Label:string,
      /**  Label used for theQuoteHed.CheckOff4 field.  */  
   CheckOff4Label:string,
      /**  Label used for the QuoteHed.CheckOff5 field.  */  
   CheckOff5Label:string,
      /**  The ID that establishes link to the default QMarkUp record which was indicated as the System Wide default. Provides default markup percents used by quote entry when none are associated to the specific customer. This ID is not directly entered. Instead it is updated by the user checking a toggle box during QMarkUp maintenance indicating "System Default". This may be left blank, which indicates there are no defaults.  */  
   MarkUpID:string,
      /**  Footer message for bottom of quote form  */  
   Message1:string,
      /**  Footer message for bottom of quote form  */  
   Message2:string,
      /**  If set to Yes, the user must change the Quote "Quoted"  flag to No before they are allowed to make any changes.  */  
   PreventQQChange:boolean,
      /**  If this is Yes, then when Quotes are set to "Quoted"  or any header flag is changed on a "Planned" job the user will be prompted to enter a description of the changes.  This option is only available when "PreventQQChange" = Yes.  */  
   LogChanges:boolean,
      /**  System Option to generate all the quantities from the price breaks in quote detail entry.  */  
   GenQuoteQtys:boolean,
      /**  This flag will be used to default the QuoteHed.ReadyToCalc field when an invoice is created. Defaults to No  */  
   QuoReadyToCalcDflt:boolean,
      /**  Option to keep the Quote Detail quantity constant.  */  
   ReduceRelQty:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Refresh Worksheet on Demand . If this flag is check the Quote Worksheet will automatically refresh and it will only refresh if the user manually select the action in Quote Entry.  */  
   RefreshWorksheetOD:boolean,
      /**  GetCostsFromInventory  */  
   GetCostsFromInventory:boolean,
      /**  DfltExpectedQtyTo  */  
   DfltExpectedQtyTo:string,
      /**  DfltOrderQtyToExpQty  */  
   DfltOrderQtyToExpQty:boolean,
      /**  SellingExpectedQty  */  
   SellingExpectedQty:number,
      /**  Quotes can be used as souce BOM if true  */  
   UseQuoteBOM:boolean,
      /**   If true, the system will defer update of Required Qty when the QuoteAsm QtyPer field is updated 
*** FUTURE USE  */  
   DeferQtyUpd:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ETCAddrValidationTableset{
   ETCAddress:Erp_Tablesets_ETCAddressRow[],
   ETCMessage:Erp_Tablesets_ETCMessageRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ETCAddressRow{
      /**  Company  */  
   Company:string,
      /**  City name  */  
   City:string,
      /**  Country name  */  
   Country:string,
      /**  Address line 1  */  
   Line1:string,
      /**  Address line 2  */  
   Line2:string,
      /**  Address line 3  */  
   Line3:string,
      /**  Postal or ZIP code  */  
   PostalCode:string,
      /**  State or province name  */  
   Region:string,
      /**  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  */  
   AddrSource:string,
      /**  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  */  
   AddrSourceID:string,
      /**  This is an additional field that will be set if the user has indicated that the Vantage address should be updated from the address validation results.  */  
   UpdateAddr:boolean,
      /**  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCValidAddress and ETCMessage rows to ETCAddress.  */  
   TransactionID:string,
      /**  This field will be set if by the process calling address validation to indicate whether the user should have the option to update the original address within the address validation UI.  */  
   UpdateAllowed:boolean,
      /**  Programmatically assign unique key to tie the ETCAddress table, the ETCValidAddress table and the ETCMessages table together.  */  
   RequestID:string,
      /**  Programmatically determined value used internally by the adapter. Defaults to the hash code of the Address object.  */  
   AddressCode:string,
      /**  The type of address that was coded (PO Box, Rural Route, and so on), using the input address. This probably needs Code/desc data  Avalara will return F = Firm or company address; G = General Delivery address; H= High-rise or business complex; P = PO Box address; R = Rural route address; S = Street or residential address  */  
   AddressType:string,
      /**  The carrier route associated with the input address (USA). This probably needs Code/desc data  Avalara will return B = PO Box; C = City Delivery; G= General Delivery; H = Highway Contract; R = Rural route.  */  
   CarrierRoute:string,
      /**  City name  */  
   ValidCity:string,
      /**  Country name  */  
   ValidCountry:string,
      /**  County name  */  
   County:string,
      /**  Federal Information Processing Standards Code (USA). This is a unique code representing each geographic combination of state, county, and city. The code is made up of the Federal Information Processing Code (FIPS) that uniquely identifies each state, county, and city in the U.S. See Federal Information Processing Standards (FIPS) Codes for more details. Digits 1-2 are the state code, digits 3-5 are the county code and digits 6-10 are the city code.  */  
   FipsCode:string,
      /**  Line one of the valid address returned by the tax integration.  */  
   ValidLine1:string,
      /**  Line two of the valid address returned by the tax integration.  */  
   ValidLine2:string,
      /**  Line three of the valid address returned by the tax integration.  */  
   ValidLine3:string,
      /**  Line four of the valid address returned by the tax integration.  */  
   ValidLine4:string,
      /**  Postal code returned by the tax integration.  */  
   ValidPostalCode:string,
      /**  A 12-digit POSTNet barcode (USA). Digits 1-5 = ZIP code, digits 6-9 = Plus4 Code, digits 10-11 = delivery point, digit 12 = check digit  */  
   PostNet:string,
      /**  State or province name or abbreviation returned by the tax integration.  */  
   ValidRegion:string,
      /**  This needs Code/desc data.  Avalara will return a single code for each address validation request. We will include the result code in each ETCValidAddress row. Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  */  
   ResultCode:string,
      /**  This is an additional field to set a unique sequence for each ValidMessage returned for a specific TransactionId.  */  
   ResultSeq:number,
      /**  Carrier Route description  */  
   CarrierRouteDesc:string,
      /**  Address type description  */  
   AddressTypeDesc:string,
   OTSCountry:string,
      /**  A  unique integer assigned by the system to new countries by the  maintenance program. This field is used as the foreign key to identify the country in other files such as Customer, or vendor. The end user should never need to know about the value of this field.  */  
   CountryNum:number,
      /**  Foreign key to the InvcHead.  */  
   InvoiceNum:number,
      /**  This field along with Company and InvoiceNum make up the unique key to the table.  The system generates this number during entry of new detail records.  The system determines next available number by finding the last InvcDtl record for the Invoice and adding 1 to it.  */  
   InvoiceLine:number,
      /**   Auto consume window percentage: this is a percentage to calculate the auto consume window days  that scheduling engine will take in consideration to look for available quantity to consume.
The purpose of this is to look ahead for a few days that will save more time than building the goods, so unless we get the full qty “current date” we need to use the window to look for the remaining.  */  
   ACWPercentage:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ETCMessageRow{
      /**  Company  */  
   Company:string,
   Details:string,
      /**  URL to help page for this message  */  
   Helplink:string,
      /**  Gets the name of the message  */  
   Name:string,
      /**  The item the message refers to, if applicable. Used to indicate a missing or incorrect value  */  
   RefersTo:string,
      /**  This probably needs Code/desc data  Avalara will return Success = Operation Succeeded; Warning = Warnings occured, operation succeeded, Error = Errors occured, operation failed; Exception = Unexpected exceptions occurred, operation failed.  */  
   Severity:string,
      /**  source of the message  */  
   Source:string,
      /**  concise summary of the message  */  
   Summary:string,
      /**  This value will come from Avalara ValidateResult TransactionID and identifies a unique specific request/response set. It will be used to tie the ETCMessage row to ETCAddress.  */  
   TransactionID:string,
      /**  This is an additional field that will be required to designate the type of address that is being validated (customer, plant, etc)  */  
   AddrSource:string,
      /**  This is an additional field to contain an appropriate piece of data to be used with the AddrSource for display in the UI to clarify for the user what data the validated address relates to. Such as AddrSource = Customer and AddrSourceID = ?Addison?  */  
   AddrSourceID:string,
      /**  Programitically assigned.  */  
   RequestID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
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

export interface Erp_Tablesets_ExtPRSystRow{
      /**  Company ID  */  
   Company:string,
      /**  Default File  */  
   FilePath:string,
      /**  3rd Party Payroll provider assigned company identifier  */  
   ExtIntCompID:string,
      /**  Consolidates single entry per employee  */  
   ConsHrs:boolean,
      /**  Indicates if an identifier is required in the export file  */  
   TempD:boolean,
      /**  Export Zero Hours as Blank  */  
   ZeroNul:boolean,
      /**  Indicates that only child records will be sent to the export file  */  
   SupHead:boolean,
      /**  2nd Period Start Day  */  
   SemiMonthDay:number,
      /**  Indicates which normal character will separate each field  */  
   Delimiter:string,
      /**  Total hours for Base, OT and premium per line  */  
   TotalAllHrs:boolean,
      /**  Group hours by pay type  */  
   GrpPayTypeID:boolean,
      /**  Default Export Layout  */  
   PayExportLayoutID:string,
      /**  Detailed Labor Hours  */  
   DetailHours:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  When checked, separate lines are created for Base, Overtime and Other (Premium) hours in Export File  */  
   SplitExportLines:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_FsSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Used to establish the beginning Service Contract Number. When the system generates a new Contract it will assign the greater of (StartContractNum) or (the last Contract Num. on file + 1) as the Contract number.  */  
   StartContractNum:number,
      /**  Used to establish the beginning Service Call Number. When the system generates a new Service Call it will assign the greater of (StartServiceCallNum) or (the last Service Call Number on file + 1) as the Service Call number.  */  
   StartServiceCallNum:number,
      /**  This is the window of days that is used to determine if a service contract is going to expire soon.  If the current date plus the expire horizon is greater than or equal to the entered expire date on a contract, the contract is considered to be expiring soon.  */  
   ExpireHorizon:number,
      /**  This flag is used when printing service call tickets.  If "YES" then labor and material pricing will print on the ticket.  */  
   PrintPrice:boolean,
      /**  Product Group Code. This will be used as a default for service calls.  This can be blank or must be valid in the ProdGrup table.  */  
   CallProdCode:string,
      /**  This prefix will be used for service call job.  The service call job will be the prefix + service call number + service call Line number.  */  
   CallJobPrefix:string,
      /**  This flag is to be set to 'YES' during intial startup. When this flag is set to 'YES' all Service Contracts will be created as active invoiced and shipped.  The idea is that a cusomter that purchases FS may already have active service contracts that have been invoiced.  */  
   ContractStartup:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This field stores the allowed Contract Renewal Period which is used to determine how long a contract/renewal can be renewed past its expiration date.  If the RenewalPeriod = 0 then it means that ALL expired contracts can still be renewed anytime.  */  
   RenewalPeriod:number,
   BitFlag:number,
   CallProdDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Maintained through Category Maintenance.  The sales category may be used in the Financial Statements to compare Income Statement accounts against.  */  
   SalesCategory:string,
      /**  Indicates if the A/R module is interfaced with General Ledger.  When interfaced A/R posting routines will automatically create "posted" journal  entries in G/L.  */  
   ARInterfaced:boolean,
      /**  Indicates if the Accounts Payable module is interfaced with General Ledger.  When interfaced A/P posting routines will automatically create "posted" journal  entries in G/L.  */  
   APInterfaced:boolean,
      /**  Indicates if the Payroll module is interfaced with General Ledger.  When interfaced, P/R posting routines will automatically create "posted" journal  entries in G/L.  */  
   PRInterfaced:boolean,
      /**  Configuration option which controls if the user has the option in the periodic Inventory/Wip/Cost of sales calculation process to post the results to general ledger.  If this is set to No then the user will not have the option to post to G/L.  */  
   PostInvtyWipCos:boolean,
      /**  The Journal Code of the Journal that will be used for Journal entry transactions. Manual Journal entries.  */  
   GJJournalCode:string,
      /**   Indicates if the user wants to use Vouchering for A/R Invoices.  Only available if the G/L module is installed.
If yes then the system will do the following
- Print a Voucher # on the invoice.
- When invoices are printed they will be automatically posted. .  The "Voucher number" is actually the Journal Number to which the invoice posted.  */  
   ARVoucherInvoices:boolean,
      /**   Indicates if the user wants to use Vouchering for A/P Invoices.  Only available if the G/L module is installed.
If yes then the system will print a Voucher assignment log when A/P invoices are posted.  The "Voucher number" is actually the Journal Number to which the invoice posted.  */  
   APVoucherInvoices:boolean,
      /**  Allow unbalanced entries to be entered in General Journal Entry with a warning.  */  
   AllowUnBalancedEntries:boolean,
      /**  Allow manual General Journal entries to be made for System Accounts.  */  
   AllowManualGJEntries:boolean,
      /**  Flag to indicate that an External GL interface is being used  */  
   ExtGL:boolean,
      /**  Identifies the Master COA for the company  */  
   MasterCOA:string,
      /**   Indicates if GL balances are maintained real time or in batch. If Yes, the GLJrnDtl write trigger does NOT update the GLPeriodBal table.
If No, the GLJrnDtl write trigger updates the GLPeriod table.  The default value is no.  */  
   BatchGLBalances:boolean,
      /**   If BatchGLBalances = yes the users have the ability to have the daily balances updated in batch mode.  This option is only available if BatchGLBalances equals Yes.
A Yes in this field indicates the GLJrnDtl write trigger does not update the GLDailyBal table.
If No, the GLJrnDtl write trigger updates the GLDailyBalTable.
The default value is No.  */  
   BatchGLDailyBal:boolean,
      /**   This option determines which date gets stored in the GLJrnDtl.MatchDate field when GL transactions are matched.

If true, then the date that the transactions are matched is used.  If false, then the latest apply date of the matched transactions is used.  */  
   MatchUsingCurrentDate:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  It is used to store default Book Mode in GL Journal Entry.  */  
   DefaultBookMode:string,
      /**  The Journal Code of the Journal that will be used for Opening Journal entry transactions. Manual Journal entries.  */  
   GJJournalCodeOpen:string,
      /**  The Journal Code of the Journal that will be used for Clousing Journal entry transactions. Manual Journal entries.  */  
   GJJournalCodeClose:string,
      /**  It is used to store tax entry mode for GL Journal header. Possible values: 0`No Taxes~1`Taxable Journal Lines~2`Taxable Journal Lines or Tax adjustment Journal.  */  
   TaxEntryMode:string,
      /**  It is used to store default value of tax liability for tax line in GL Journal entry routine.  */  
   DefaultTaxLiability:string,
      /**  It is used to store default value of tax type for tax line in GL Journal entry routine.  */  
   DefaultTaxType:string,
      /**  If the flag is on then posting rules conversion program creates a copy of current active revision before merging with the revision provided in the update/upgrade.  */  
   KeepRevisionHistory:boolean,
   FormatSelection:string,
   DisplayGLFormat:string,
   JournalCodeJrnlDescription:string,
   DefaultTaxLiabilityDescription:string,
   DefaultTaxTypeDescription:string,
      /**  The list of tax codes for Default Tax Liability  */  
   TaxLiabilityTaxCodes:string,
   BitFlag:number,
   COADescription:string,
   GJJournalJrnlDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ISSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Enable Harbor Flag  */  
   EnableHarbour:boolean,
      /**  Countries may differ in the way periods are reported.  */  
   PeriodFormat:string,
      /**  Description Type  */  
   DescType:string,
      /**  Intrastat Region  */  
   DefISRegion:string,
      /**  Country of Origin required  */  
   ISOrigCountryReq:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  APRGFlow2  */  
   APRGFlow2:string,
      /**  APRGFlowSpec2  */  
   APRGFlowSpec2:string,
      /**  APRGTranType2  */  
   APRGTranType2:string,
      /**  ARRGFlow2  */  
   ARRGFlow2:string,
      /**  ARRGFlowSpec2  */  
   ARRGFlowSpec2:string,
      /**  ARRGTranType2  */  
   ARRGTranType2:string,
      /**  Generate2APRGLine  */  
   Generate2APRGLine:boolean,
      /**  Generate2ARRGLine  */  
   Generate2ARRGLine:boolean,
      /**  Flow1Desc  */  
   Flow1Desc:string,
      /**  Flow2Desc  */  
   Flow2Desc:string,
      /**  StartIstatNum  */  
   StartIstatNum:number,
      /**  APFlow  */  
   APFlow:string,
      /**  APFlowSpec  */  
   APFlowSpec:string,
      /**  APTranType  */  
   APTranType:string,
      /**  APRGFlow  */  
   APRGFlow:string,
      /**  APRGFlowSpec  */  
   APRGFlowSpec:string,
      /**  APRGTranType  */  
   APRGTranType:string,
      /**  ARFlow  */  
   ARFlow:string,
      /**  ARFlowSpec  */  
   ARFlowSpec:string,
      /**  ARTranType  */  
   ARTranType:string,
      /**  ARRGFlow  */  
   ARRGFlow:string,
      /**  ARRGFlowSpec  */  
   ARRGFlowSpec:string,
      /**  ARRGTranType  */  
   ARRGTranType:string,
      /**  ISCurrency  */  
   ISCurrency:string,
      /**  APExtraTradeCommodityFlow  */  
   APExtraTradeCommodityFlow:string,
      /**  APExtraTradeTranType  */  
   APExtraTradeTranType:string,
      /**  APExtraTradeCustomsProcedure  */  
   APExtraTradeCustomsProcedure:string,
      /**  APExtraTradeISCustomsDeclCountry  */  
   APExtraTradeISCustomsDeclCountry:string,
      /**  APExtraTradeISEUBorderCrossingCountry  */  
   APExtraTradeISEUBorderCrossingCountry:string,
      /**  APRGExtraTradeCommodityFlow  */  
   APRGExtraTradeCommodityFlow:string,
      /**  APRGExtraTradeTranType  */  
   APRGExtraTradeTranType:string,
      /**  APRGExtraTradeCustomsProcedure  */  
   APRGExtraTradeCustomsProcedure:string,
      /**  APRGExtraTradeISCustomsDeclCountry  */  
   APRGExtraTradeISCustomsDeclCountry:string,
      /**  APRGExtraTradeISEUBorderCrossingCountry  */  
   APRGExtraTradeISEUBorderCrossingCountry:string,
      /**  Shipping Returned 2  */  
   ARRGFlowSpec2Descr:string,
      /**  Shipping Returned  */  
   ARRGFlowSpecDescr:string,
      /**  Generate2APRGExtraTradeLine  */  
   Generate2APRGExtraTradeLine:boolean,
      /**  Shipping Returned 2  */  
   ARRGTranType2Descr:string,
      /**  APRGExtraTradeCommodityFlow2  */  
   APRGExtraTradeCommodityFlow2:string,
      /**  APRGExtraTradeTranType2  */  
   APRGExtraTradeTranType2:string,
      /**  Shipping Returned  */  
   ARRGTranTypeDescr:string,
      /**  Shipping Normal  */  
   ARTranTypeDescr:string,
      /**  APRGExtraTradeCustomsProcedure2  */  
   APRGExtraTradeCustomsProcedure2:string,
      /**  APRGExtraTradeISCustomsDeclCountry2  */  
   APRGExtraTradeISCustomsDeclCountry2:string,
      /**  Intrastat Region Description  */  
   RegionDesc:string,
      /**  APRGExtraTradeISEUBorderCrossingCountry2  */  
   APRGExtraTradeISEUBorderCrossingCountry2:string,
      /**  Receipt Normal  */  
   APFlowSpecDescr:string,
      /**  Receipt Returned 2  */  
   APRGFlowSpec2Descr:string,
      /**  ARExtraTradeCommodityFlow  */  
   ARExtraTradeCommodityFlow:string,
      /**  ARExtraTradeTranType  */  
   ARExtraTradeTranType:string,
      /**  Receipt Returned  */  
   APRGFlowSpecDescr:string,
      /**  Receipt Returned 2  */  
   APRGTranType2Descr:string,
      /**  ARExtraTradeCustomsProcedure  */  
   ARExtraTradeCustomsProcedure:string,
      /**  ARExtraTradeISCustomsDeclCountry  */  
   ARExtraTradeISCustomsDeclCountry:string,
      /**  Receipt Returned  */  
   APRGTranTypeDescr:string,
      /**  ARExtraTradeISEUBorderCrossingCountry  */  
   ARExtraTradeISEUBorderCrossingCountry:string,
      /**  Receipt Normal  */  
   APTranTypeDescr:string,
      /**  Shipping Normal  */  
   ARFlowSpecDescr:string,
      /**  ARRGExtraTradeCommodityFlow  */  
   ARRGExtraTradeCommodityFlow:string,
      /**  ARRGExtraTradeTranType  */  
   ARRGExtraTradeTranType:string,
      /**  Used to populate the Intrastat Flow combos  */  
   FlowList:string,
      /**  ARRGExtraTradeCustomsProcedure  */  
   ARRGExtraTradeCustomsProcedure:string,
      /**  ARRGExtraTradeISCustomsDeclCountry  */  
   ARRGExtraTradeISCustomsDeclCountry:string,
      /**  ARRGExtraTradeISEUBorderCrossingCountry  */  
   ARRGExtraTradeISEUBorderCrossingCountry:string,
      /**  Generate2ARRGExtraTradeLine  */  
   Generate2ARRGExtraTradeLine:boolean,
      /**  ARRGExtraTradeCommodityFlow2  */  
   ARRGExtraTradeCommodityFlow2:string,
      /**  ARRGExtraTradeTranType2  */  
   ARRGExtraTradeTranType2:string,
      /**  ARRGExtraTradeCustomsProcedure2  */  
   ARRGExtraTradeCustomsProcedure2:string,
      /**  ARRGExtraTradeISCustomsDeclCountry2  */  
   ARRGExtraTradeISCustomsDeclCountry2:string,
      /**  ARRGExtraTradeISEUBorderCrossingCountry2  */  
   ARRGExtraTradeISEUBorderCrossingCountry2:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_JCSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Label used for the JobHead.CheckOff1 field.  There are 5 CheckOffLabel fields.  They are all optional.  If entered then the corresponding JobHead.CheckOff fields become active.  */  
   CheckOff1Label:string,
      /**  Label used for the JobHead.CheckOff2 field.  */  
   CheckOff2Label:string,
      /**  Label used for the JobHead.CheckOff3 field.  */  
   CheckOff3Label:string,
      /**  Label used for the JobHead.CheckOff4 field.  */  
   CheckOff4Label:string,
      /**  Label used for the JobHead.CheckOff5 field.  */  
   CheckOff5Label:string,
      /**  Indicates the format of how labor time is entered.  It can be entered as (M) - hours/minutes or (H) - Hours/Hundredths.  */  
   ClockFormat:string,
      /**  Indicates if the labor entry details will be transferred to the Payroll system.  This is used to set the value of LaborDtl.Payroll flag.  */  
   FeedPayroll:boolean,
      /**  Controls how shop load is removed.  It can either be by Actual Hours  "H" or based on quantity completed "Q".  */  
   RemoveLoad:string,
      /**  Controls whether or not entry of a Machine ID will be prompted for in Labor Entry and Labor Collection.  */  
   MachinePrompt:boolean,
      /**  Indicates if system should prompt for entry of a Rework Reason code for rework transactions during Labor Collection or Labor Entry.  */  
   ReworkReasons:boolean,
      /**  Indicates if system should prompt user to enter a Scrap Reason code for labor transactions where the scrap quantity is not zero during Labor Entry or Labor Collection.  */  
   ScrapReasons:boolean,
      /**  Indicates the maximum number of digits to be entered into the JCSyst.NextJobNum field.  This also controls the number of digits that the system will generate when the user requests a "Next Job Number" while creating a new job number.  */  
   JobSeqLength:number,
      /**  The value in this field represents the next default job sequence number.  The number of digits that can be entered is controlled by JCSyst.JobSeqLength.  Example of how the system uses these fields to generate a number that is inserted as part of the Job number when the user requests "Next Job Number" while creating a new job number would be: JobSeqLength = 6 and NextJobNumber = 100.  Then the system would try to insert  "000100" into the job number at the current insertion point.  */  
   NextJobNumber:number,
      /**  Grace Period, stored as Hours/Hundredths  */  
   Grace:number,
      /**   Default qualifier for the Production Standard field.  This is used as a default to the qualifier field in operation details when there is no related  OpStd record.  The valid qualifiers are:
"HP" - Hours/Piece, "MP" - minutes/piece, "PH" - pieces/hour, "PM" - Pieces/Minute, "OH" - Operations/Hour, "OM"  - Operations/minute, HR - Fixed Hours.  */  
   StdFormat:string,
      /**   Default standard basis is to be used to with standards that are time per piece (HP & MP).  The basis is a Divisor.  Valid codes are E-Eaches, C=100's, M=1000's, T=10,000.
This field is used in the formula for calculating the estimated production hours.  The operation quantity is divided by the basis value and then multiplied by the standard to result in hours.  */  
   StdBasis:string,
      /**  Default for the JobOper and QuoteOpr.EstScrapType fields  */  
   EstScrapType:string,
      /**  Indicates if system should prompt user to enter an Inventory Adjustment Reason code for quantity and cost adjustments.  */  
   InvAdjReasons:boolean,
      /**  SchedPri.SchedCode value that is marked as the default scheduling code in the Scheduling Priority Code master file.  */  
   SchedCode:string,
      /**  Default for scheduling operations that have been started.  A started operation is one with labor reported to it.  Global Scheduling uses this value.  */  
   SchedStartedOps:boolean,
      /**  The number of weeks labor warning detail is stored until they are purged.  */  
   WksLaborHistWarn:number,
      /**  This option controls whether or not the labor warnings messages are generated/reported.  When this option is turned on labor warning records are created and the labor edit list and/or entry/tracker programs report these warnings.  When it is turned off the labor edit list performs its own warning checking and no warnings are reported in the entry/tracker programs.  This option should only be turned on between labor periods (i.e. after all of the labor has been reported, but before the next periods information has been entered).  Only maintainable if the Data Collection module has been installed.  */  
   GenLaborWarnMsg:boolean,
      /**  If set to Yes, the user must change the Job Engineered flag to No before they are allowed to make any changes to a Job.  */  
   PreventPJChange:boolean,
      /**  If this is Yes, then when Jobs are set to "Planned"  or any header flag is changed on a "Planned" job the user will be prompted to enter a description of the changes.  This option is only available when "PreventPJChange" = Yes.  */  
   LogChanges:boolean,
      /**  Number of minutes used by data collection to determine the time frame in which early clock in times are to be adjusted forward to the shift start time.  If clock in time falls within the  time range of (Shift Start - Allowance) to Shift Start then the clock in time will set to Shift Start time.  */  
   EarlyClockInAllowance:number,
      /**  Number of minutes used by data collection to determine the time frame in which late clock in times are to be adjusted backwards to the shift start time.  If clock in time falls within the  time range of Shift Start to (Shift Start + Allowance)  then the clock in time will set to Shift Start time.  */  
   LateClockInAllowance:number,
      /**  Number of minutes used by data collection to determine the time frame in which early clock out times are to be adjusted forward to the shift end time.  If clock out time falls within the  time range of (Shift End - Allowance) to Shift End  then the clock out time will set to Shift end.  */  
   EarlyClockOutAllowance:number,
      /**  Minutes used to determine the time frame in which late clock out times are to be adjusted backwards to the shift end time.  If clock out time falls within the  time range of Shift end to (Shift Start + Allowance) then the clock out time will set to Shift End time.  */  
   LateClockOutAllowance:number,
      /**  Default for "Floating " the part revision.  To "Float" the revision of unfirm jobs to the revision in effect at the time of the requirement.  */  
   FloatPartRev:boolean,
      /**   Number of days before the forecast date in which any sales orders that exist should reduce the forecast quantity.
Ex: Forecast date of 3/31/98, Days before of 10, then any orders that have a date of 3/21/98 to 3/31/98 would reduce the forecast.  */  
   ForecastDaysBefore:number,
      /**   Number of days after the forecast date in which any sales orders that exist should reduce the forecast quantity.
Ex: Forecast date of 3/31/98, Days after  of 10, then any orders that have a date of 4/01/98 to 4/10/98 would reduce the forecast.  */  
   ForecastDaysAfter:number,
      /**   Indicates if the LateClockIn or EarlyClockOut grace period should be applied to the labor detail transactions.
Ex: 10 minute LateClockIn, Shift Start = 8:00am, Employee clocks in and starts an activity  at 8:05.  If DetailGrace = Yes then StartTime on the detail will be adjusted to 8:00.  If DetailGrace = No then StartTime remains as 8:05 and an the 5 minutes will be included in the  idle time.  This setting does NOT affect how Start/End times are adjusted for the timecard record.  In both cases for this example the start time for the timecard will be 8:00.  */  
   DetailGrace:boolean,
      /**  If set to Yes, the user is unable to start production work for an operation which is waiting for First Article approval.  */  
   PreventFABypass:boolean,
      /**  Used to get a value for jobs not referencing a sales order.  If a part in not in the price list then use Part.UnitPrice.  */  
   ChgImpactPriceListCode:string,
      /**   Used in conjunction with the Late Grace Period to determine if a job is early, on-time or late.  Example: Early Grace Period is 4, Late Grace Period is 1, Job Required Date is 05/20/02: If the job is
scheduled to be completed before 05/16/02 it is Early.  If the job is
scheduled to be completed anywhere from 05/16/02 through 05/21/02 it is on-time.  If the job is scheduled to be completed after 05/21/02 it is late.  */  
   EarlyGracePeriod:number,
      /**   Used in conjunction with the Early Grace Period to determine if a job is early, on-time or late.  Example: Early Grace Period is 4, Late Grace Period is 1, Job Required Date is 05/20/02: If the job is
scheduled to be completed before 05/16/02 it is Early.  If the job is
scheduled to be completed anywhere from 05/16/02 through 05/21/02 it is on-time.  If the job is scheduled to be completed after 05/21/02 it is late.  */  
   LateGracePeriod:number,
      /**   NJ - Next Job
OR - Order Release  */  
   QuickJobID:string,
      /**  KanBanPrefix  */  
   KanBanPrefix:string,
      /**  The value in this field represents the next default transfer Order sequence number.  The number of digits that can be entered is controlled by JCSyst.OrderSeqLength.  Example of how the system uses these fields to generate a number that is inserted as part of the Transfer Order number when the user requests "Next Order Number" while creating a new Transfer Order number would be: OrderSeqLength = 6 and NextOrderNumber = 100.  Then the system would try to insert  "000100" into the Order number at the current insertion point.  */  
   NextOrderNumber:number,
      /**  Indicates the maximum number of digits to be entered into the JCSyst.NextOrderNum field.  This also controls the number of digits that the system will generate when the user requests a "Next Order Number" while creating a new order number.  */  
   OrderSeqLength:number,
      /**  The value in this field represents the next default transfer Order Line sequence number.  The number of digits that can be entered is controlled by JCSyst.OrderSeqLength.  Example of how the system uses these fields to generate a number that is inserted as part of the Transfer Detail Line number when the user requests "Next Line Number" when converting an MRP Transfer Line number would be: OrderSeqLength = 6 and NextTranLineNumber = 100.  Then the system would try to insert  "000100" into the Line Number at the current insertion point.  */  
   NextTranLineNumber:number,
      /**  Determines if a scheduler is allowed to schedule/reschedule jobs/operations (from the Scheduling Boards) to do work before today.  */  
   AllowSchedulingBeforeToday:boolean,
      /**  Indicates where to post all variances on a job that shipped direct for a standard cost part.  M = to the Product Group, C = to the Cost of Sales.  */  
   DirectShipVar:string,
      /**  Flag to indicate how to split the manufacturing cost elements when a manufactured material is issued to the job.  If flag is set to true, the cost of the issued material will be split into individual manufacturing cost elements. If set to false, the cost of the issued material is added to the manufacturing material cost element only.  */  
   SplitMfgCostElements:boolean,
      /**  This flag is used by ATP to determine if Unfirm Jobs should be considered in ATP calculations.  */  
   UnfirmATP:boolean,
      /**   The ForecastPeriods field defines the forecast periods that are used with the import and export process.

Examples: Year, Semester, Quarter, Month, Week, Day

This field is used with the ForecastPeriodsPerYear field.  */  
   ForecastPeriods:string,
      /**   The ForecastPeriodsPerYear field defines the number of forecast periods per year.

This field is used with the ForecastPeriods field.  */  
   ForecastPeriodsPerYear:number,
      /**   The ReplaceMissingValues field is used to determine how periods with zero demand should be exported when exporting forecast data.

If yes, then zero demand will be replaced with the string "MISSING" as long as there is no demand in previous periods.  If previous periods have some demand, then zero demand will be left as zero.

If the value of this field is no, then zero demand will be left as zero when exporting demand.  */  
   ReplaceMissingValues:boolean,
      /**   The ForecastImportDay field is used by the forecast import process to determine the forecast date for each forecast period.

The valid values for this field are dependent on the value in the ForecastPeriods field.  */  
   ForecastImportDay:number,
      /**  If false then when an employee is booking hours to a job they can enter any Project Role code that has been set up on the employee. When the field is set to true then the Project Role entered MUST be one of the Project Role codes that have been assigned to the operation.  */  
   ChkEmpPrjRole:boolean,
      /**   Defines where the default role code will be obtained.
The options are ?
Operation: Project Role code from the operation will be used.
Employee. Project Role Code from the Employee will be used.  */  
   DfltPrjRoleLoc:string,
      /**  Defines the default revenue recognition method to be used in project entry.The options are Default =  (blank).Code/Desc: INV = On Invoice, LBR = Labor Booking, MAN = Manual, BDN = Actual Burden, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery  */  
   DfltRevRecMthd:string,
      /**  Indicates whether the revenue recognition method can be changed on the project.  */  
   AllowRevRecChg:boolean,
      /**  When set to Reserve following month the journal created will be flagged as a reversing journal.PCL = Reverse on Project Close, MON = Reverse Following Month  */  
   RevRecJrnlReverse:string,
      /**  Defines where the invoice process will obtain the Project Role Rates from. Hierarchical works as defined for Invoice Preparation. All of the others will ONLY obtain the rates from the area defined. HIER = Hierarchical, PROJ = Project Only, EMPL = Employee Only, ROLE = Project Role Only  */  
   DfltPrjRtSrc:string,
      /**  True indicates the user can change the Derive Project Rates from at the project level.  */  
   AllowPrjRtSrcChg:boolean,
      /**  The default format to use when importing forecast data from external forecast solutions.  */  
   ExtFcstImpFormat:string,
      /**  The default format to use when exporting sales history data to external forecast solutions.  */  
   ExtFcstExpFormat:string,
      /**   Default of Invoicing Method of new Project. If advanced billing is not licensed the only options are CS and MB. Code/Desc:
CS = Customer Shipment, 
MB = Milestone Billing, 
FF = Fixed Fee;
CP = Cost Plus;
TM = Time and Material;
PP = Progress payment;

The default is Customer Shipment.  */  
   ConInvMeth:string,
      /**  Tax Category to default into Project. MtlTaxCatID.  */  
   MtlTaxCatID:string,
      /**  Tax Category to default into Project LbrTaxCatID.  */  
   LbrTaxCatID:string,
      /**  Tax Category to default into Project. FeeTaxCatID.  */  
   FeeTaxCatID:string,
      /**  Tax Category to default into Project. ODCaxCatID.  */  
   ODCTaxCatID:string,
      /**  Tax Category to default into Project. SubTaxCatID.  */  
   SubTaxCatID:string,
      /**  Tax Category to default into Project. BdnTaxCatID.  */  
   BdnTaxCatID:string,
      /**  Tax Category to default into Project. TaxOnNetOfRet.  */  
   TaxOnNetOfRet:boolean,
      /**  indicates if the company setting for ChkEmpPrjRole can be overridden at the project level.  */  
   AllowChkEmpPrjRoleChg:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  AdvancedLaborRate  */  
   AdvancedLaborRate:boolean,
      /**  CapRevID  */  
   CapRevID:number,
      /**  AutoReceipt  */  
   AutoReceipt:boolean,
      /**  MRPJobID  */  
   MRPJobID:string,
      /**  Tax Category to default into Project. PbsTaxCatID. (Billing Schedule)  */  
   PbsTaxCatID:string,
      /**  True indicates the user can link a sales order per wbs phase on project.  */  
   SOAllowWBSPhase:boolean,
      /**  SOAutoRelWBSPhase  */  
   SOAutoRelWBSPhase:boolean,
      /**  SchedAnUnEngineered  */  
   SchedAnUnEngineered:boolean,
      /**  GetCostsFromTemplate  */  
   GetCostsFromTemplate:boolean,
      /**  Allows moving Jobs across sites within the company and not only for the site where user is logged on.  */  
   AllowMoveJobsAcrossPlants:boolean,
      /**  MPSOnly  */  
   MPSOnly:boolean,
      /**  EnableSchedDebugLog  */  
   EnableSchedDebugLog:boolean,
      /**  IncludeExtraDetailsLog  */  
   IncludeExtraDetailsLog:boolean,
      /**  MtlQtyParentDefault  */  
   MtlQtyParentDefault:number,
      /**  AssignPrimarySupplier  */  
   AssignPrimarySupplier:boolean,
      /**  AvoidIncludeQuotePrjRevenue  */  
   AvoidIncludeQuotePrjRevenue:boolean,
      /**  Number of pieces created per cycle if Cycle/Minute or Cycle/Hour is selected  */  
   QtyPerCycle:number,
      /**  MaxLogDay  */  
   MaxLogDay:number,
      /**  Default Option to activate Revenue Recognition at WBS Phase level  */  
   DefaultRecognizeRevenueAtPhaseLevel:boolean,
      /**  EnableShipTo  */  
   EnableShipTo:boolean,
   StdFormatDesc:string,
   TaxCatPbsDescription:string,
      /**  Include quotes without link to SO to Projected Revenue  */  
   IncludeQuotePrjRevenue:boolean,
   BitFlag:number,
   ChgImpactPriceLstListDescription:string,
   TaxCatBdnDescription:string,
   TaxCatFeeDescription:string,
   TaxCatLbrDescription:string,
   TaxCatMtlDescription:string,
   TaxCatODCDescription:string,
   TaxCatSubDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MMSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Identifies the EquipStatusID that is to be used as the default for Equip.StatusID. This may be blank. Not directly maintainable. It gets set by Equipment Status maintenance when the user checks the "Default" box.  */  
   DefaultStatusID:string,
      /**  Template Job to be used when creating a Maintenace Job for Maintenance Request / Maintenance Plan. If entered, it must be a valid Job with JobHead.Template = Yes, JobType = "MM" and JobHead.Site must be this Site. System uses hierarchy when determining th  */  
   TemplateJobNum:string,
      /**  Prefix that will be used when generating  Maintenance Job numbers for this company. Note this may be overridden at the Site level (see SiteConfCntrl.MaintJobPrefix)  */  
   JobPrefix:string,
      /**  MMSyst.MaintBuffer, default for EquipPlan.MaintBuffer  */  
   MaintBuffer:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   JobHeadPartDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PDMSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  PDM Export directory  */  
   PDMExportDir:string,
      /**  PDM Import Directory  */  
   PDMImportDir:string,
      /**  Document Export Directory  */  
   DocExportDir:string,
      /**  Document Import Directory  */  
   DocImportDir:string,
      /**  The default Group id for the ECO Group  */  
   ECOGroupID:string,
      /**  Default pdm revision number  */  
   RevisionNum:string,
      /**  The default pdm searchword for new parts.  */  
   SearchWord:string,
      /**  File number used for identification of integration files.  */  
   FileNum:number,
      /**  File name prefix for parts.  */  
   PartPrefix:string,
      /**  File name prefix for Boms.  */  
   BomPrefix:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PLM process will consider two types of revision. Current Revision: last approved revision with effective date less or equal than today. Last approved revision: (no matter the effective date) so if the customer has multiple revisions and one is approved, even if it’s for a future date, we will send this one.  */  
   PLMRevision:string,
   BitFlag:number,
   ECOGroupIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PECompWhldHistRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Record Sequence  */  
   RecordSeq:number,
      /**  Create Date  */  
   CreateDate:string,
      /**  User Identifier.  */  
   UserID:string,
      /**  Good Contributor  */  
   GoodContributor:boolean,
      /**  Indicates the status of Withholding Agent.  */  
   WithholdingAgent:boolean,
      /**  Collection Agent withholding status.  */  
   CollectionAgent:boolean,
      /**  Not Found withholding status.  */  
   NotFound:boolean,
      /**  No Address Provided withholding status.  */  
   NoAddress:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PRSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  During Payroll Class maintenance the user is prompted for a password.  The entered password is encoded and then compared to this string.  An encoded string that is checked before allowing access to the payroll class maintenance program.  If blank then user is prompted to enter a password before allowing access to PRClass maintenance.  It does not matter what security level the user is, they just need to know this password in order to gain access.  */  
   Password:string,
      /**   Controls the order in which checks are printed. Valid options are;
"SuperID", "Name", "EmpID","Dept".  */  
   CheckSort:string,
      /**  Identifies the day of the month which the 2nd period starts for semimonthly payroll runs.  */  
   SemiDay:number,
      /**  Date that the Manufacturing System payroll will become effective.  When initially starting up payroll the user enters the employee year to date information as of (PRStartDate - 1day).  If the user wants the initial quarter to date figures to be correct they should start payroll at the beginning of a quarter and enter that start date here.  */  
   PRStartDate:string,
      /**   Encoded field which indicates if Payroll Managers have been set up.
(Blank = Not a PR manager).  Only users that are Payroll managers are allowed access to payroll class maintenance where they can establish the list of authorized users for the class.
There must always be at least one user where DspPayrollMgr = Yes.  */  
   NoPRMgr:string,
      /**  Enable/Disable the HCM Integration. May be License specific (TBD)  */  
   HCMEnabled:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PrintRates  */  
   PrintRates:boolean,
      /**  If enabled the user is able to enter a max pay rate of 999999.9999 in Payroll Employee, currently the system only allows a max of 9999.9999.  */  
   AllowHighPayRate:boolean,
      /**  Payroll checks exist for this company  */  
   PRChecksExist:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxSvcConfigRow{
      /**  Company Identifier  */  
   Company:string,
      /**  The location of the AvaTax service when the address will not change between the client and web service.  */  
   URL:string,
      /**  The intermediary server, for example a firewall, for the AvaTax service.  */  
   ViaURL:string,
      /**  Stores the text case used for address validation. Possible values are Default, Upper, and Mixed  */  
   TextCase:string,
      /**  The unique account number provided by Avalara for verification against the service. May also contain a username.  */  
   Account:string,
      /**  The unique alpha-numeric key for the account provided by Avalara for verification against the service. May also contain a password if Account contains a username.  */  
   Key:string,
      /**  Indicates whether the Epicor Tax Connect interface is active for this company. If false, no Tax Connect address validation or tax calculations will take place regardless of how the company flags are set for those functions.  */  
   TaxConnectEnabled:boolean,
      /**   Indicates whether the system can perform address validation via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if address validations are authorized/available via the
Epicor Tax Connect. If false no address validation logic will be executed.  */  
   AddrValEnabled:boolean,
      /**  Indicates whether the system should perform tax calculations via Epicor Tax Connect. If TaxConnectEnabled flag = true this flag will be checked to see if tax calculations are authorized/available via Epicor Tax Connect. If false the base Epicor tax calculations will take place.  */  
   TaxCalcEnabled:boolean,
      /**  The Prefix to be used in conjunction with the SalesTaxSeq database sequence for automatically created SalesTax records  */  
   TaxIdPrefix:string,
      /**  Request timeout value for tax connect requests, in seconds.  */  
   RequestTimeOut:number,
      /**  The default tax category to assign to a Sales Order/Quote/Invoice  record if tax connect is enabled and no tax category is defaulted via the standard tax category default logic.  */  
   DefaultTaxCatID:string,
      /**  This records the last document id retrieved from a ReconcileTaxHistory call to Avalara. It will be used to default the starting document ID in the Get Tax History action in Tax Reconciliation process.  */  
   LastDocId:number,
      /**  Specifies if Tax Connect will run in Debug Mode. When TRUE the input-output XML files sent and received to Avalara will NOT be deleted so they can be reviewed.  */  
   DebugMode:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ValidateISOCode  */  
   ValidateISOCode:boolean,
      /**  Indicates whether the system can perform CertCapture transactions. If CertCaptureEnabled is true, CertCapture features will be available. Otherwise, they won't.  */  
   CertCaptureEnabled:boolean,
   APTaxDisplayAccount:string,
   APTaxAcctDesc:string,
   ARTaxDisplayAccount:string,
   ARTaxAcctDesc:string,
      /**  External field to be used to indicate that the Tax Connect service is off line. This filed can be set by the BL when a communication failure with tax connect occurs, or can be set manually in the UI when the user indicates that tax connect is offline. If set to true then the BL will not attempt any communication with the tax service. This is used to save unnecessary processing delays trying to communicate with the tax service when it is known that the service is unavailable.  */  
   ETCOffline:boolean,
   BitFlag:number,
   TaxCatDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtCompanyTableset{
   Company:Erp_Tablesets_CompanyRow[],
   CompanyAttch:Erp_Tablesets_CompanyAttchRow[],
   AGCompany:Erp_Tablesets_AGCompanyRow[],
   APSyst:Erp_Tablesets_APSystRow[],
   ARSyst:Erp_Tablesets_ARSystRow[],
   BMSyst:Erp_Tablesets_BMSystRow[],
   BorderPct:Erp_Tablesets_BorderPctRow[],
   CRSyst:Erp_Tablesets_CRSystRow[],
   CSFSyst:Erp_Tablesets_CSFSystRow[],
   Currency:Erp_Tablesets_CurrencyRow[],
   CurrRateGrp:Erp_Tablesets_CurrRateGrpRow[],
   EQSyst:Erp_Tablesets_EQSystRow[],
   ExtPRSyst:Erp_Tablesets_ExtPRSystRow[],
   FsSyst:Erp_Tablesets_FsSystRow[],
   GLSyst:Erp_Tablesets_GLSystRow[],
   ISSyst:Erp_Tablesets_ISSystRow[],
   JCSyst:Erp_Tablesets_JCSystRow[],
   MMSyst:Erp_Tablesets_MMSystRow[],
   PDMSyst:Erp_Tablesets_PDMSystRow[],
   PECompWhldHist:Erp_Tablesets_PECompWhldHistRow[],
   PRSyst:Erp_Tablesets_PRSystRow[],
   TaxSvcConfig:Erp_Tablesets_TaxSvcConfigRow[],
   XaSyst:Erp_Tablesets_XaSystRow[],
   XbSyst:Erp_Tablesets_XbSystRow[],
   EntityGLC:Erp_Tablesets_EntityGLCRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_XaSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The default Unit of Measure that will be used when creating a part.  */  
   DefaultUM:string,
      /**  Used as the default costing method when creating new parts in Part Master Maintenance. Remember that each Part defines its own costing method. The possible values are "A" - Average, "L" - Last or  "S" - standard.  */  
   CostMethod:string,
      /**  Establishes the default Site ID to be used as the default for a Part's Primary Site field during Part maintenance.  The Default Warehouse must be in the DefaultSite.  */  
   DefaultPlant:string,
      /**  Indicates if Company Name & Address should print on forms.  */  
   PrintCompanyName:boolean,
      /**  Used to establish the beginning Sales Order #. When the system generates a new order it will assign the greater of (StartOrderNum) or (the last orders # on file + 1) as the order number.  */  
   StartOrderNum:number,
      /**  Used to establish the beginning Purchase Order #. When the system generates a new PO, it will assign the greater of (StartPONum) or (the last orders # on file + 1) as the PO number.  */  
   StartPONum:number,
      /**  Used to establish the beginning Packing Slip #. When the system generates a new packing slip it will assign the greater of (StartPSNum) or (the last Packing Slips  # on file + 1) as the PS number.  */  
   StartPSNum:number,
      /**  Identifies the Terms master that is to be used as the default when creating customer masters. This can be left blank if there is no one best terms default. Otherwise it gets set via terms maintenance when the user checks the "Default" box.  */  
   TermsCode:string,
      /**  Controls the entry of ship from job quantity in shipping entry program. If set to "yes" then job quantity field is enabled regardless of the order being linked to a job. This is intended only to be set to "yes" during the initial system implementation period. So that users can create and ship orders for manufactured items without forcing them to have established jobs  */  
   ShipNoJob:boolean,
      /**  This field indicates if the system should generate sales order booking records. Booking tables are used to store changes in sales volume. See BookOrd & BookDtl for more info.  */  
   BookOrders:boolean,
      /**  Option that controls the sensitivity of Bar Code Printing options.  */  
   PrintBarCodes:boolean,
      /**  Used to establish the beginning RMA#. When the system generates a new RMA it will assign the greater of (StartRMANum) or (the last RMA # on file + 1) as the RMA number.  */  
   StartRMANum:number,
      /**  Identifies the ShipVia master that is to be used as the default when creating Purchase Orders. This may be blank if there is no one normal ship via. Not directly maintainable. It gets set by Ship Via maintenance when the user checks the "Default" box.  */  
   DefaultShipViaCode:string,
      /**  Used to establish the beginning PurchaseRFQ #. When the system generates a new RFQ it will assign the greater of (StartRFQNum) or (the last RFQ # on file + 1) as the RFQ number.  */  
   StartRFQNum:number,
      /**  Label used for the DMRHead.CheckOff1 field.  There are 5 CheckOffLabel fields. They are all optional. If entered then the corresponding CheckOff fields become active.  */  
   CheckOff1Label:string,
      /**  Label used for the DMRHead.CheckOff2 field.  */  
   CheckOff2Label:string,
      /**  Label used for the DMRHead.CheckOff3 field.  */  
   CheckOff3Label:string,
      /**  Label used for the DMR.CheckOff4 field.  */  
   CheckOff4Label:string,
      /**  Label used for the DMRHead.CheckOff5 field.  */  
   CheckOff5Label:string,
      /**  Global SN  */  
   GlobalSN:boolean,
      /**  The Journal Code of the Journal that will be used for Inventory/WIP transactions. The Job management Calculate WIP/COS process creates entries in this journal.  */  
   IJJournalCode:string,
      /**  Starting ID number for non-conformance records.  */  
   StartNonConfID:number,
      /**  Starting ID number for non-conformance records.  */  
   StartCorrActID:number,
      /**  Option to keep the Sales Order Detail quantity constant.  */  
   ReduceRelQty:boolean,
      /**  System default buyer id.  This identifies the buyer that will be used during the auto po generation process when no buyer is defined by the PartClass or OpCode records.  */  
   SysBuyerID:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available number is assigned by the system. The system generates a number by finding the order number of the last record on file and then a 1 to it.  */  
   StartTFOrderNum:number,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   AutoOrderBasedDisc:boolean,
      /**  The default shipvia code for the Counter Sales order.  */  
   ShipViaCode:string,
      /**  The invoice group prefix for counter sales orders. The invoice group id is based on this prefix plus two digits of today's month  plus two digits of the today's daynumber.  */  
   InvcGrpPfx:string,
      /**  If a Site does not have a specified SiteCostID, use this one instead  */  
   PlantCostID:string,
      /**  The default task set for use in the Help Desk.  */  
   HDDefaultTaskSetID:string,
      /**  If true, users can auto-complete Help Desk tasks by changing the current workflow stage.  */  
   HDAutoCompleteTasks:boolean,
      /**  Indicates whether to use the shipping staging logic  */  
   StagingReq:boolean,
      /**  True value indicates that the Epicor Advanced Quality module is active.  Related to IQS integration.  */  
   EAQActive:boolean,
      /**  This field will hold the default URL for the Service Connect input channel.  This is only used as the default as the user can specify the individual URLs for data element to be passed to amd from the IQS application.  */  
   DftInputChannel:string,
      /**  This field will hold the default URL for the Service Connect output channel.  This is only used as the default as the user can specify the individual URLs for data element to be passed to amd from the IQS application.  */  
   DftOutputChannel:string,
      /**  Default Miscellaneous Freight Charge Customer Connect  */  
   DefaultMiscFreightCC:string,
      /**  This flag will be used to default the OrderHed.ReadyToCalc field when an invoice is created. Defaults to No.  */  
   SOReadyToCalcDflt:boolean,
      /**  Specifies if line discounts shall be applied to the unit price or the line value.  */  
   SODiscountUnitPrice:boolean,
      /**   Default Unit of Measure Class. Used as the default value when creating new Part masters.
Must be  valid in the UOMClass table.
The UOMClass has a default UOMCode which replaces the 8.3 XASyst.DefaultUM.  */  
   DefUOMClassID:string,
      /**  The character that will represent the place holder for any alphanumeric character ((e.g. 5 / A / a). Default is "&"  */  
   AlphaNumeric:string,
      /**  Indicates the string to use when constructing an Example for a serial mask in Serial Mask Maintenance and the AlphaNumeric character is part of the mask. The default is "A".  */  
   AlphaNumExample:string,
      /**  This is the character used to represent alpha characters (e.g. [a to z] or [A to Z]). Default is "@"  */  
   AlphaOnly:string,
      /**  Indicates the string to use when constructing an Example for a serial mask in Serial Mask Maintenance and the AlphaOnly character is part of the mask. The default will be "B".  */  
   AlphaOnlyExample:string,
      /**  This is the character used to represent a numeric character (e.g. [0 to 9]). Default is "#".  */  
   NumericOnly:string,
      /**  This is the character used to represent a mandatory variable that can be any alphanumeric character. Therefore if the user enters 2 followed by this character in the mask then when a serial number is created these charaters must be replaced with any single character. Default is "?"  */  
   AnyMandatory:string,
      /**  This character is used to represent an optional variable that can be any alphanumeric character. NOTE this character can ONLY be added as the last characters in the mask. Default is "!"  */  
   OptionalAlphaNumeric:string,
      /**  This character is used to represent the characters that are to be stripped off when the internal serial number is created. This character can ONLY be at the front or back of the mask. The default is "~"  */  
   StripChar:string,
      /**  When this character is entered in the mask surrounded by <> characters then a day number as a 2 numeric value will be automatically inserted into the serial number at that position. This will consume 2 characters of the serial number string. (Only allowed for auto generation masks). The default is "D"  */  
   DayChar:string,
      /**  When this character  is entered in the mask surrounded by <> characters this will then automatically enter into the serial number the month number as a 2 numeric value. This will consume 2 characters of the serial number string. (Only allowed for auto generation masks). The default is "M"  */  
   MonthChar:string,
      /**  When this is 2 character string is entered in the mask surrounded by <> characters this will then automatically enter into the serial number the last 2 numeric values of the current calendar year. This must be entered as 2 identical  characters and will consume 2 characters of the serial number string. (Only allowed for auto generation masks). The default is "YY"  */  
   Year2Char:string,
      /**  When this 4 character string is entered in the mask surrounded by < > characters this will then automatically enter into the serial number the full value of the year. This must be entered as 4 identical  characters and will consume 4 characters of the serial number string. (Only allowed for auto generation masks) The default is "YYYY"  */  
   Year4Char:string,
      /**  If this is entered in the mask it must be followed by a hard coded numeric value indicating the number of characters of the part number that will be included in the serial number. The PartChar and the hard coded number should be encased in <> characters when building the mask. E.g. if the part representation  character is entered as "P" and the part number is DS4000-1 and <P6> is entered in the mask then DS4000 will be included in the serial number. The default is "P". (Only allowed for auto generation masks)  */  
   PartChar:string,
      /**  Indicates the string to use when constructing an Example for a serial mask in Serial Mask Maintenance and the PartChar character is part of the mask. The default will be  ?EPICORSERIALNUMBERMASKFORMATEXAMPLE?.  */  
   PartCharExample:string,
      /**  Discount rounding option: NE - Round net price by extended amount, NP - Round net price by unit price,  EP - Round discount by extended amount; UP - Round discount by unit price.  */  
   SODiscountRound:string,
      /**  Pack Slip counter used for generating new automatic SMI PO Receipts.  */  
   SMIPackSlip:number,
      /**  This field holds the current year that is used as part of the key when generating an auto generated receipt for supplier managed inventories.  This is used in the program im/GenSMIReceipt.p  */  
   SMIYear:number,
      /**  Default is blank.  Values include active shifts.  Selected value is used as the default value for Shift in Employee Maintenance.  */  
   DefaultShift:number,
      /**  Select this checkbox to enable the AQM Integration. This checkbox enables movement of data in both directions, from the Epicor application to AQM and vice versa.  */  
   IQSActive:boolean,
      /**  Specifies a selected folder path where the data will be exported. For example, C:\Epicor3Data\ServiceConnect\AQM\DataExportOut. Only enable if AQM integration is active.  */  
   IQSOutputDir:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  StartBOLNum  */  
   StartBOLNum:number,
      /**  Allow Project/WBS phase to be defined  */  
   PrjAllowWBSPhase:boolean,
      /**  Default Job Type of Sales Order line.  */  
   PrjJobType:string,
      /**  Use reference invoice costs for RMA  */  
   RMAUseRefCosts:boolean,
      /**  Used for Sales Order to give the ability to find price lists using the base currency if the customer currency if foreign.  */  
   UseOMBaseCurr:boolean,
      /**  PassedReqMove  */  
   PassedReqMove:boolean,
      /**  FailedReqMove  */  
   FailedReqMove:boolean,
      /**  PassedRMAReqMove  */  
   PassedRMAReqMove:boolean,
      /**  FailedRMAReqMove  */  
   FailedRMAReqMove:boolean,
      /**  QuoteToSOReadyToCalcDflt  */  
   QuoteToSOReadyToCalcDflt:boolean,
      /**  This flag will be used to default the OrderHed.ReadyToFulfill field when a sales order is created.  */  
   SOReadyToFulfillDflt:boolean,
      /**  Indicates the maximum number of levels of parent/child nesting allowed.  */  
   MaxPCIDParentChildLevels:number,
      /**  Default Amount of Rows by Page to display in the MES Work Queue UI at Startup. Set it to ZERO to retrieve all the Work Queue records at once, into one single page.  */  
   MaxWorkQueueRecords:number,
      /**  RMAAllowMultipleCredInv  */  
   RMAAllowMultipleCredInv:boolean,
      /**  Specifies a legal number that will default when AR invoices import from Epicor FSA.  */  
   FSATranDocTypeID:string,
      /**  FSAPromptForInstallation  */  
   FSAPromptForInstallation:boolean,
      /**  Specifies a legal number that will default when Credit Memos import from Epicor FSA.  */  
   FSATranDocTypeIDCreditMemo:string,
      /**  TransactionRetrievalDays  */  
   TransactionRetrievalDays:number,
      /**  This field defines the format that will be used to export the data in the AQM Synchronization Process. The valid options are Extended: Extended version and Compact: Compact version. Only enabled if AQM integration is active.  */  
   IQSOutputFormat:string,
      /**  This flag will be used to default the ReadyToFulfill field for jobs.  */  
   JobReadyToFulfillDflt:boolean,
      /**  This flag will be used to default the ReadyToFulfill field for transfer orders.  */  
   TransferReadyToFulfillDflt:boolean,
   EnableSNMaskFields:boolean,
   FSACMemoTranDocDesc:string,
   FSAInvoiceTranDocDesc:string,
   InvcTranType:string,
      /**  A temporary field for the UI for starting order number until the db StartOrderNum field format can be changed to contain 9 digits.  */  
   TmpStartOrderNum:number,
   CMTranType:string,
      /**  FSMDocTypeID (Attachment Document Type).  */  
   FSMDocTypeID:string,
      /**  Company flag to enable FSM sync of Analysis Code  */  
   FSMSyncAnalysisCd:boolean,
      /**  Company flag to enable FSM sync of Employee (Service Tech)  */  
   FSMSyncEmpBasic:boolean,
      /**  Company flag to enable FSM sync of Asset Class (Equipment Type)  */  
   FSMSyncFSAssetClass:boolean,
      /**  Company flag to enable FSM sync of Asset Class (Work Code)  */  
   FSMSyncIndirect:boolean,
      /**  Company flag to enable FSM sync of Operation (Condition)  */  
   FSMSyncOpMaster:boolean,
      /**  Company flag to enable FSM sync of Part Class  */  
   FSMSyncPartClass:boolean,
      /**  Company flag to enable FSM sync of Site (Dispatch Location)  */  
   FSMSyncPlant:boolean,
      /**  Company flag to enable FSM sync of Serial Number (Equipment)  */  
   FSMSyncSerialNo:boolean,
      /**  Company flag to enable FSM sync of UOM  */  
   FSMSyncUOM:boolean,
      /**  Company flag to enable FSM sync of Warehouse  */  
   FSMSyncWarehse:boolean,
   BitFlag:number,
   DefaultPlantName:string,
   HDTaskTaskSetDescription:string,
   HDTaskWorkflowType:string,
   IJJournalJrnlDescription:string,
   PlantCostDescription:string,
   ShiftDescription:string,
   ShipViaDescription:string,
   ShipViaWebDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_XbSystRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Contains the Label used for the user defined field in the Purchase Order Master.  */  
   POUserChar1Label:string,
      /**  Contains the Label used for the 2nd user defined character  field in the Purchase Order Master.  */  
   POUserChar2Label:string,
      /**  Contains the Label used for the 3rd user defined character field in the Purchase Order Master.  */  
   POUserChar3Label:string,
      /**  Contains the Label used for the 4th user defined character field in the Purchase Order Master.  */  
   POUserChar4Label:string,
      /**  Contains the Label used for the 1st user defined date field in the Purchase Order Master..  */  
   POUserDate1Label:string,
      /**  Contains the Label used for the 2nd user defined date field in the Purchase Order Master.  */  
   POUserDate2Label:string,
      /**  Contains the Label used for the 3rd user defined date field in the Purchase Order Master.  */  
   POUserDate3Label:string,
      /**  Contains the Label used for the 4th user defined date  field in the Purchase Order Master.  */  
   POUserDate4Label:string,
      /**  Contains the Label used for the 1st user defined decimal field in the Purchase Order Master..  */  
   POUserDec1Label:string,
      /**  Contains the Label used for the 2nd user defined decimal field in the Purchase Order Master.  */  
   POUserDec2Label:string,
      /**  Contains the Label used for the 1st user defined field in the Purchase Order Master.  */  
   POUserInt1Label:string,
      /**  Contains the Label used for the 2nd user defined field in the Purchase Order Master.  */  
   POUserInt2Label:string,
      /**  Company that is the Parent of Consolidated Purchasing.  More than one company can be attached to a serial number that has the Consolidated Purchasing module entered.  This field designates which of those companies is the parent of Consolidated Purchasing and can therefore create Consolidated Purchase Orders.  */  
   ConsolidatedPurchasingCompany:string,
      /**  Holds the Currency.CurrencyCode value in which Consolidated Purchasing data will be exchanged.  */  
   GlobalCurrencyCode:string,
      /**  Allow Express Part Checkout.  */  
   ExpPartCKOut:boolean,
      /**  For internal use only.  Used with ConsolidatedPurchasingCompany to enforce security of the Consolidated Purchasing Parent company.  */  
   ConsPurchasingParent:string,
      /**  Determines if a new PO release is created at receipt when the quantity received is less than the quantity shipped.  The new PO Rel quantity is the difference between the ship quantity and the receipt quantity.  */  
   NewPoRelAtReceipt:boolean,
      /**  Use when creating payment records from credit card payments automatically from Sales Order or from Customer Shipment  */  
   CashGrpPfx:string,
      /**  Invoice Group Prefix used for credit card groups  */  
   CCInvPfx:string,
      /**  Bank Account code to be used when creating credit card payments  */  
   DefBankAcctID:string,
      /**  Indicates whether or not Container Tracking is to calculate landed cost.  If yes, landed costs are calculated at the time the container is received.  The cubic sq feet of a container cannot be zero.  If no, landed costs are NOT calculated.  */  
   SkipLandedCostCalc:boolean,
      /**  Does a sale that originated via Customer Connect garner a Commission?  */  
   WebSaleGetsCommission:boolean,
      /**  Default System Printer where labels are going to be sent if there is no Device available to print labels on the Current Station.  */  
   DefaultLabelsPrinter:string,
      /**  Default System Printer where forms are going to be sent if there is no Device available to print forms on the Current Station.  */  
   DefaultFormsPrinter:string,
      /**   Number of lines per page for text report. This value will be written to SysRptLst.TxtLPP. The text based reports (Progress 4gl) generate a print image .txt file. This file contains new page controls characters. The Page size needs to be configurable to handle other paper sizes (ex: A4).
At this time we will allow for a page size setting to be established at the company level.  */  
   TxtLPP:number,
      /**  Default Miscellaneous Charges Freight Charge Code  */  
   DefaultMiscFreightChargeCode:string,
      /**  Valid values = "None", "Short" and "Create".   At the time a container is shipped, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the shipping quantity and a new PO release is created for the difference between the original po release quantity and the ship quantity.  If this field is not set or None is selected than PO releases are not created nor are they shipped short.  This is an optional field.  */  
   PORelShipOption:string,
      /**  Flag to enable VAT taxboxes  */  
   UseTaxBoxes:boolean,
      /**  Rate Group Code for General applications  */  
   GenRateGrp:string,
      /**  Rate Group Code for Sales and A/R Invoicing  */  
   SalesRateGrp:string,
      /**  Currency Rate Group for Purchasing and A/P Invoicing  */  
   PORateGrp:string,
      /**  Currency Rate Group for Inventory applications  */  
   InvRateGrp:string,
      /**  Currency Rate Group for Fixed Assets  */  
   FARateGrp:string,
      /**  Currency Rate Group for Payroll  */  
   PRRateGrp:string,
      /**  Currency Rate Group for Cash transactions  */  
   CashRateGrp:string,
      /**   F = Force 1:1 rate for same currencies
C = Use Conversion through base  */  
   RateLockType:string,
      /**  Indicates if FIFO Cost will be recorded based on Transaction Date or System Date.  By default the UseTranDate is false which means FIFO cost queue will use system date.  */  
   UseTranDate:boolean,
      /**  Default for Part.LotBatch  */  
   LotBatch:boolean,
      /**  Default for Part.LotMfgBatch  */  
   LotMfgBatch:boolean,
      /**  Default for Part.LotMfgLot  */  
   LotMfgLot:boolean,
      /**  Default for Part.LotHeat  */  
   LotHeat:boolean,
      /**  Default for Part.LotFirmware  */  
   LotFirmware:boolean,
      /**  Default for Part.LotBeforeDt  */  
   LotBeforeDt:boolean,
      /**  Default for Part.LotMfgDt  */  
   LotMfgDt:boolean,
      /**  Default for Part.LotCureDt  */  
   LotCureDt:boolean,
      /**  Default for Part.LotExpDt  */  
   LotExpDt:boolean,
      /**  Controls the number of decimal places that the UI uses to display a "quantiity" field. This only controls the display, the actual number of decimals that can be entered is based on the Unit of Measure. (UomConv.NumOfDec)  */  
   QtyDsplyDec:number,
      /**  Valid values = "Short" and "Create".   When the container arrives, if this option is set to "Short", the PO release quantity is reduced. If this option is set to "Create" the PO release quantity is reduced to the arrived quantity and a new PO release is created for the difference between the original po release quantity and the arrived quantity.  This is an optional field.  */  
   PORelRcptOption:string,
      /**  If true, then the shipto can be changed on the packing slip to a different shipto than on the Order Release. However, it can only be changed to one of the shipto's that are referenced on the order.  */  
   AllowShipToChange:boolean,
      /**  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume , Weight, Value, Quantity and Manual.  */  
   DefDisburseMethod:string,
      /**  Flag to indicate if container shipment lines can be split into another container shipment.  */  
   AllowSplitContainer:boolean,
      /**  Flag to indicate if Indirect Costs from one container shipment can be transferred to another.  */  
   AllowTransferIndCost:boolean,
      /**  Flag to indicate if Landed Cost maintenance is allowed in Receipt Entry.  */  
   AllowReceiptLC:boolean,
      /**  Allow maintenance of Landed Cost after the part is received.  */  
   AllowLCAfterReceipt:boolean,
      /**  Allow update of PO Transaction Value during Container Landed Cost Entry.  */  
   AllowUpdTransValue:boolean,
      /**  Do not allow use of Uplift Percent during Landed Cost calculation.  */  
   DisableLCUplift:boolean,
      /**  Allows entry of restriction types and substances in Part Master, Operation Master, ECO and Job Entry.  */  
   EnableRoHS:boolean,
      /**  Default value is false. When set to true then all indirect/direct roll-up radio buttons in Part Master and Job Entry should be enabled.  */  
   AllowDirectRollUp:boolean,
      /**  Synchronize substance weight  */  
   SyncSubstWeight:boolean,
      /**  Indicates if the RoHS Compliance Process will stop at the first failure it founds.  */  
   StopAtFirstFailure:boolean,
      /**  Number of days to look back when processing Orders for the Build From Order History  */  
   OrderHistDays:number,
      /**  Indicates if user is allowed to update the Supplier Price for Receipt created by Purchase Order.  */  
   AllowUpdSuppPrice:boolean,
      /**  It is used to catch differences between updated Supplier Price for Receipt and PO Unit Price. If no value entered then do not perform percentage check.  */  
   SuppPerctTolerance:number,
      /**  It is used to catch differences between extended values of updated Supplier Price for Receipt and PO Unit Price. If no value entered then do not perform monetary check.  */  
   SuppMonetaryTolerance:number,
      /**  Receipt action to value of Supplier Price.  Valid values are "WARN" or "STOP".  WARN means that the user is given a warning, but allowed to proceed (or cancel) the Receipt with that Supplier Price.  STOP means that the Receipt line is not correct and the user should go to PO and update PO Unit Price to make receipt with mentioned price.  */  
   SuppPriceLimitAction:string,
      /**  The default format code to be used on the Slow Moving Stock Provision report.  */  
   DefaultSlowMovingFmtCode:string,
      /**  The default format code to be used on the Excess Stock Provision report.  */  
   DefaultExcessFmtCode:string,
      /**  Indicates whether or not prices for transfer orders are calculated and printed on the packslip.  */  
   CalcPSPrice:boolean,
      /**  Indicates whether or not taxes are calculated for a customer shipment and printed on the packslip.  */  
   CalcPSTax:boolean,
      /**  Flag that indicates if a PO should be created when confirm in CTP.  */  
   RaisePOforCTP:boolean,
      /**  Setting at company level to define if the sales order releases will be created as Make Direct or Buy To Order. Sales order lines for non part master part must be BTO or Make direct.  */  
   DefaultSORelease:string,
      /**  This would allow the user to receive non traditional payment information (such as post dated checks and bank drafts) and use it in calculating a customer's credit limit  */  
   EnablePI:boolean,
      /**  If box is checked, then the AP Invoice system will enable the APInvDtl.PurchCode field for European Financial postings  */  
   APPurchType:boolean,
      /**  Indicates that the discount amount by line needs to be captured to be sent to an external Financials package  */  
   APDiscount:boolean,
      /**  Flag to decide if the Match By Demand logic is applied to schedules in Demand Mass Review.  */  
   AutoMatchAll:boolean,
      /**  Allow shipping orders on hold  */  
   AllowShipOrdHold:boolean,
      /**  Check Unfirm Releasses Schedule  */  
   ChkUnfirmSched:boolean,
      /**  Check Forcast Schedule  */  
   ChkForecastSched:boolean,
      /**  Localization Country  */  
   Localization:string,
      /**  Use Government Uniform Invoices. Taiwan localization flag.  */  
   UseGUI:boolean,
      /**  Indicates if taxes are calculated in a separate exchange rate  */  
   UseTaxRate:boolean,
      /**  Currency Rate Group for Taxes  */  
   TaxRateGrp:string,
      /**  OCR Calculation Type. Localization for Sweden, Finland and Estonia.  */  
   OCRCalcType:boolean,
      /**  OCR number is derived from either the invoice number or a setting at the customer. Localization for Sweden, Finland and Estonia.  */  
   OCRNumDrivenFrom:string,
      /**  OCR length is the maximum length an OCR number is allowed to be. Localization setting for Sweden, Finland and Estonia.  */  
   OCRLength:number,
      /**  The flag to indicate if Account Reference number assigned to the customer should be used as Banking Reference on AR Invoice sent to the customer.  */  
   UseAcctRef:boolean,
      /**   Malaysia Localization
LMW License Number  */  
   CSFLMWLcnNbr:string,
      /**   Malaysia Localization
CJ5 License Number  */  
   CSFCJ5LcnNbr:string,
      /**   Malaysia Localization
CJ5 File Number  */  
   CSFCJ5FileNbr:string,
      /**  Field to choose between close or delete releases on SO when the demand is process  */  
   CancelSchedAction:string,
      /**  Document Type for Tax Receipt (Thailand Localization)  */  
   THTaxRecDocType:string,
      /**  Withholding Tax Document Type (Thailand Localization)  */  
   THWHTDocType:string,
      /**   Taiwan Localization
Seller City Code  */  
   GUISellerCityCode:string,
      /**  This field would be true if the system should automatically create a Supplier record for each Employee for processing Expenses.  */  
   ExpenseAutoSupplier:boolean,
      /**  If the system is setup to automatically create a Supplier record for each Employee for processing Expenses, this field will be the Prefix.  This value will prefix a numeric value and be used for the Supplier ID.  */  
   ExpenseAutoSupplierPrefix:string,
      /**  Rate Group Code for Employee Expenses  */  
   ExpenseRateGrp:string,
      /**  Internal sequence for automatic creation of vendors for employees.  */  
   ExpenseVendorSeq:number,
      /**  If the flag is false then users are allowed to enter  anything in the bank branch ID field in customer bank, supplier bank and BankAcct. The code will still try to do a lookup and retrieve the description of the bank branch ID.  */  
   ValidateBankBranchID:boolean,
      /**  If the flag is false then users are allowed to enter anything in the bank IBAN (International Bank Account Number) field in customer bank, supplier bank and BankAcct.  If the flag is true, the checksum validation will be performed.  */  
   ValidateBankIBAN:boolean,
      /**  This is the default used when calculating CTP for multiple lines on an order.  If it is non-blank, then all the CTP jobs will be scheduled to complete at the same time.  It can be overridden at the time CTP is calculated.  */  
   CTPSchedulingCode:string,
      /**   Used as the collection method for creating Change Log records.
Possible values are: "D" -  Daily (Default Value), one record is created per day and everybody's changes are stored together.  "U" - User, one  record is created per day for each user.  */  
   ChgLogMethod:string,
      /**  Chief Accountant Name  */  
   ChiefAcctName:string,
      /**  Cheif Accountant Cell Phone Number  */  
   ChiefAcctCellPhone:string,
      /**  Cheif Accountant Email Address  */  
   ChiefAcctEmail:string,
      /**  Tax Return Bank Code  */  
   TRBankCode:string,
      /**  Tax Return Bank Branch  */  
   TRBankBranch:string,
      /**  Tax Return Bank Account  */  
   TRBankAcct:string,
      /**  ID number for consolidation.  */  
   TotalPayID:string,
      /**  Tax Office Code  */  
   TaxOfficeCode:string,
      /**  Tax Agent Name  */  
   TaxAgentName:string,
      /**  Tax Agent Phone  */  
   TaxAgentPhone:string,
      /**  Tax Agent Tax Region Number  */  
   TaxAgentTaxRegNo:string,
      /**  Defines the format In which the EDI Outbound Documents will be sent to output.  */  
   EDIOutboundAs:string,
      /**  Company default Workflow Group. Used to assign to cases.  */  
   HDDefWFGroupID:string,
      /**  Starting supplier reference ID number  */  
   StartVendAuditRefID:number,
      /**  IsDiscountforDebitM  */  
   IsDiscountforDebitM:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  THBranchID  */  
   THBranchID:string,
      /**  UseInvRateDefTax  */  
   UseInvRateDefTax:boolean,
      /**  Allow changes to be made to POs that are linked to Intercompany Sales Orders  */  
   AllowLinkedPOChg:boolean,
      /**  Consider Working Days in the Delivery Days Calculation  */  
   ConsiderWorkingDays:boolean,
      /**  DeferTaxExchRate  */  
   DeferTaxExchRate:number,
      /**  PmtTaxUseDate  */  
   PmtTaxUseDate:number,
      /**  CNAccEntityName  */  
   CNAccEntityName:string,
      /**  CNAccountStructure  */  
   CNAccountStructure:string,
      /**  CNAttachment  */  
   CNAttachment:string,
      /**  CNBaseCurrency  */  
   CNBaseCurrency:string,
      /**  CNCashier  */  
   CNCashier:string,
      /**  CNCFICodeCurGainLoss  */  
   CNCFICodeCurGainLoss:string,
      /**  CNChecker  */  
   CNChecker:string,
      /**  CNCompType  */  
   CNCompType:string,
      /**  CNDisableEntryRules  */  
   CNDisableEntryRules:boolean,
      /**  CNExportPath  */  
   CNExportPath:string,
      /**  CNGroupName  */  
   CNGroupName:string,
      /**  CNGTICollector  */  
   CNGTICollector:string,
      /**  CNGTICommTaxCode  */  
   CNGTICommTaxCode:string,
      /**  CNGTIDefCCFlag  */  
   CNGTIDefCCFlag:boolean,
      /**  CNGTIDefINFlag  */  
   CNGTIDefINFlag:boolean,
      /**  CNGTIDefPath  */  
   CNGTIDefPath:string,
      /**  CNGTIDefPOFlag  */  
   CNGTIDefPOFlag:boolean,
      /**  CNGTIDefPTFlag  */  
   CNGTIDefPTFlag:boolean,
      /**  CNGTIDefSMFlag  */  
   CNGTIDefSMFlag:boolean,
      /**  CNGTIDefSOFlag  */  
   CNGTIDefSOFlag:boolean,
      /**  CNGTIManager  */  
   CNGTIManager:string,
      /**  CNGTIVATCode  */  
   CNGTIVATCode:string,
      /**  CNGTIVATInvLimit  */  
   CNGTIVATInvLimit:number,
      /**  CNGTIVATInvLineLimit  */  
   CNGTIVATInvLineLimit:number,
      /**  CNIndustry  */  
   CNIndustry:string,
      /**  CNIndustryCode  */  
   CNIndustryCode:string,
      /**  CNKeeper  */  
   CNKeeper:string,
      /**  CNMaker  */  
   CNMaker:string,
      /**  CNOrgCode  */  
   CNOrgCode:string,
      /**  CNRegionCode  */  
   CNRegionCode:string,
      /**  JPFiscalCalendarID  */  
   JPFiscalCalendarID:string,
      /**  TWGUICalendarID  */  
   TWGUICalendarID:string,
      /**  If the flag is false then users are allowed to enter anything in the Tax ID field in customer and supplier.  If the flag is true, the validation will be performed.  */  
   ValidateTaxID:boolean,
      /**  MXDebugMode  */  
   MXDebugMode:boolean,
      /**  MXDocType  */  
   MXDocType:string,
      /**  MXIEPSTaxType. Obsolete, SalesTax.MXTaxType used instead  */  
   MXIEPSTaxType:string,
      /**  MXISRTaxType. Obsolete, SalesTax.MXTaxType used instead  */  
   MXISRTaxType:string,
      /**  MXIVATaxType. Obsolete, SalesTax.MXTaxType used instead  */  
   MXIVATaxType:string,
      /**  MXPACCode  */  
   MXPACCode:string,
      /**  MXTaxRcptEFT  */  
   MXTaxRcptEFT:number,
      /**  MXTaxRcptType  */  
   MXTaxRcptType:string,
      /**  MXThumbprint  */  
   MXThumbprint:string,
      /**  MXUseExpedidoEn  */  
   MXUseExpedidoEn:boolean,
      /**  MXValidFrom  */  
   MXValidFrom:string,
      /**  MXValidTo  */  
   MXValidTo:string,
      /**  OCRCalcAlg  */  
   OCRCalcAlg:string,
      /**  NOThresholdAmt  */  
   NOThresholdAmt:number,
      /**  EAddress  */  
   EAddress:string,
      /**  EInvOutputDir  */  
   EInvOutputDir:string,
      /**  EInvImpFileLocation  */  
   EInvImpFileLocation:string,
      /**  EInvImpArchiveFileLocation  */  
   EInvImpArchiveFileLocation:string,
      /**  EInvImpSelectionMethod  */  
   EInvImpSelectionMethod:string,
      /**  DefaultLineTaxable  */  
   DefaultLineTaxable:boolean,
      /**  Bill of Exchange Payment Method  */  
   PEBOEPaymentMethod:number,
      /**  Bill of Exchange Portfolio Status  */  
   PEBOEPortfolioStatus:string,
      /**  AsyncShip  */  
   AsyncShip:boolean,
      /**  Within PO Entry when modifying unit price which was derived from a supplier price list, prompt the user to confirm.  */  
   OverridePriceListPrompt:boolean,
      /**  Disable Override Price List option with PO Entry  */  
   DisableOverridePriceListOption:boolean,
      /**  DEBundesbankCompanyID  */  
   DEBundesbankCompanyID:string,
      /**  DEZ4ExportPath  */  
   DEZ4ExportPath:string,
      /**  Defaults the Warehouse and Bin in Receipt to the last used for the current Part and Pack Slip  */  
   UseLastWhseBin:boolean,
      /**  Indicates what Qty Option will be defaulted for new PO lines. Options are "Our" and "Supplier".  */  
   POQtyOption:string,
      /**  Indicates what Qty Option will be defaulted for new Receipt lines. Options are "Our" and "Supplier".  */  
   ReceiptQtyOption:string,
      /**  CNGTILangID  */  
   CNGTILangID:string,
      /**  Defines the point at which the PO Releases will be closed. Available options are 'Arrival', 'Receipt', or 'Invoice'.  */  
   CloseReleaseAt:string,
      /**  SubRateGrp  */  
   SubRateGrp:string,
      /**  If true and the UOM is set to no rounding and the number of decimals is exceeded, you will get an error. Otherwise the value will be truncated (same as round down currently behaves).  */  
   StopOnUOMNoRound:boolean,
      /**  MYIndustryCode1  */  
   MYIndustryCode1:string,
      /**  MYIndustryCode2  */  
   MYIndustryCode2:string,
      /**  MYIndustryCode3  */  
   MYIndustryCode3:string,
      /**  MYIndustryCode4  */  
   MYIndustryCode4:string,
      /**  MYIndustryCode5  */  
   MYIndustryCode5:string,
      /**  PE Document ID  */  
   PEDocumentID:string,
      /**  PE Identity Document Type  */  
   PEIdentityDocType:string,
      /**  CNOurBank  */  
   CNOurBank:string,
      /**  JobLotDflt  */  
   JobLotDflt:boolean,
      /**  LACTaxCalcEnabled  */  
   LACTaxCalcEnabled:boolean,
      /**  TW GUI Code  */  
   TWGUIRegNum:string,
      /**  NLMessageRefSupplierICP  */  
   NLMessageRefSupplierICP:string,
      /**  NLDigipoortDeliveryURL  */  
   NLDigipoortDeliveryURL:string,
      /**  NLDigipoortStatusURL  */  
   NLDigipoortStatusURL:string,
      /**  NLDigipoortServerThumbprint  */  
   NLDigipoortServerThumbprint:string,
      /**  NLDigipoortClientThumbprint  */  
   NLDigipoortClientThumbprint:string,
      /**  Encoding for GTI Export file  */  
   CNGTIEncodingFormat:number,
      /**  Flag to determine whether PO taxes will be automatically calculated each time a PO line is updated.  */  
   POTaxReadyToProcess:boolean,
      /**  Flag to determine whether PO taxes will be calculated.  */  
   POTaxCalculate:boolean,
      /**  PEAddressID  */  
   PEAddressID:string,
      /**  X509Code  */  
   X509Code:string,
      /**  COIFRSInterestRate  */  
   COIFRSInterestRate:number,
      /**  MXCURP  */  
   MXCURP:string,
      /**  This flag will be used to determine if taxes are calculated for AP Invoices at Document Level (Default, False) or at Line Level (True).  */  
   APTaxLnLevel:boolean,
      /**  MYLMWLcnPurchaseExpDate  */  
   MYLMWLcnPurchaseExpDate:string,
      /**  MYLMWPurchaseAddr  */  
   MYLMWPurchaseAddr:string,
      /**  MYLMWLcnManufacturing  */  
   MYLMWLcnManufacturing:string,
      /**  MYLMWLcnManufacturingExpDate  */  
   MYLMWLcnManufacturingExpDate:string,
      /**  MYLMWManufacturingAddr  */  
   MYLMWManufacturingAddr:string,
      /**  Flag to determine whether Receipt taxes will be calculated.  */  
   ReceiptTaxCalculate:boolean,
      /**  Flag to determine whether Quote taxes will be calculated.  */  
   CalcQuoteTax:boolean,
      /**  Indicates if entry of a BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttBatch:string,
      /**  Indicates if entry of a MFG BATCH is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttMfgBatch:string,
      /**  Indicates if entry of a MFG Lot is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttMfgLot:string,
      /**  Indicates if entry of a Heat Number  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttHeat:string,
      /**  Indicates if entry of FIRMWARE is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttFirmware:string,
      /**  Indicates if entry of a Best Before Date is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttBeforeDt:string,
      /**  Indicates if entry of a Original Manufacture Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttMfgDt:string,
      /**  Indicates if entry of a CURE DATE  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttCureDt:string,
      /**  Indicates if entry of an Expiration Date  is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttExpDt:string,
      /**  PLTaxOfficeCode  */  
   PLTaxOfficeCode:string,
      /**  PLRegionCode  */  
   PLRegionCode:string,
      /**  PLProvince  */  
   PLProvince:string,
      /**  PLDistrict  */  
   PLDistrict:string,
      /**  PLCommunity  */  
   PLCommunity:string,
      /**  PLBuildingNum  */  
   PLBuildingNum:string,
      /**  PLRoomNum  */  
   PLRoomNum:string,
      /**  PLPostOffice  */  
   PLPostOffice:string,
      /**  Turnover in Previous Fiscal Year  */  
   INPrevYearTurnover:number,
      /**  DeferManualEntry  */  
   DeferManualEntry:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Container Receipt, Receipt Entry.  */  
   DeferPurchaseReceipt:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Job Receipt to Job, Job Receipt to Salvage, Job Receipt to Inventory, Kanban Receipts.  */  
   DeferJobReceipt:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Inspection Processing.  */  
   DeferInspection:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: Quantity Adjustment.  */  
   DeferQtyAdjustment:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Inventory Transfer.  */  
   DeferInventoryMove:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Customer Shipment Entry, Subcontractor Shipment Entry, Drop Shipment Entry, Order Entry.  */  
   DeferShipments:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later. This flag is used for following screens: Count Tag Entry.  */  
   DeferInventoryCounts:boolean,
      /**  DeferAssetDisposal  */  
   DeferAssetDisposal:boolean,
      /**  This flag indicates if the Lots attributes are necessary to be entered in the creation of the lot or could be entered later.  This flag is used for following screens: RMA Processing.  */  
   DeferReturnMaterials:boolean,
      /**  Flag to indicate if it is allowed to create employees with Group resource, without a resource defined.  */  
   AllowEmpWithoutResource:boolean,
      /**  INSingleTaxCatTypeSO  */  
   INSingleTaxCatTypeSO:boolean,
      /**  INSingleTaxCatTypePO  */  
   INSingleTaxCatTypePO:boolean,
      /**  BusinessCatID  */  
   BusinessCatID:string,
      /**  Flag to determine whether Duty will be included on Taxable amount  */  
   ReceiptIncludeDutyInTax:boolean,
      /**  INAllowChangingPP  */  
   INAllowChangingPP:boolean,
      /**  Fiscal Unity Tax ID (CSF Netherlands)  */  
   NLFiscalUnityTaxID:string,
      /**  Prefix for incoming FSA records. To be used to create Cash Receipt groups.  */  
   FSACashGrpPfx:string,
      /**  Prefix for incoming FSA records. To be used to create AR Invoice groups.  */  
   FSAARInvGrpPfx:string,
      /**  Indicates if inbound AR Invoices are sent to posting when received from FSA.  */  
   FSASendARInvToPosting:boolean,
      /**  Reason Code to be used for inbound inventory quantity adjustments received from Epicor FSA.  */  
   FSAInvQtyAdjustmentReasonCode:string,
      /**  MXLocality  */  
   MXLocality:string,
      /**  MXMunicipioCode  */  
   MXMunicipioCode:string,
      /**  RevaluationAR  */  
   RevaluationAR:string,
      /**  RevaluationAP  */  
   RevaluationAP:string,
      /**  RevaluationBA  */  
   RevaluationBA:string,
      /**  RevaluationPCD  */  
   RevaluationPCD:string,
      /**  GenerateDigitalSignature  */  
   GenerateDigitalSignature:boolean,
      /**  UseCopyNumInPackSlips  */  
   UseCopyNumInPackSlips:boolean,
      /**  This is the location of the the EWC generator.  */  
   EWConfiguratorURL:string,
      /**  NLDigipoortServerCertID  */  
   NLDigipoortServerCertID:string,
      /**  NLDigipoortClientCertID  */  
   NLDigipoortClientCertID:string,
      /**  UnapprovedPO  */  
   UnapprovedPO:string,
      /**  UnconfirmedPO  */  
   UnconfirmedPO:string,
      /**  Default Ship Via Code for return shipments of RMAs for FSA related transactions  */  
   FSAShipViaCode:string,
      /**  Default reason code for RMAs from FSA  */  
   FSARMAReasonCode:string,
      /**  Default payment method for expenses from FSA  */  
   FSAExpensePMUID:number,
      /**  APPrepayTaxCalc  */  
   APPrepayTaxCalc:boolean,
      /**  Waste Register Number (CSF Poland)  */  
   PLWasteRegisterNum:string,
      /**  This is the location of the EWC Runtime.  */  
   EWCRuntimeURL:string,
      /**  AGAFIPResponsibilityCode  */  
   AGAFIPResponsibilityCode:string,
      /**  E-Invoice CompanyID Attribute  */  
   EInvCompanyIDAttr:string,
      /**  E-Invoice EndpointID Attribute  */  
   EInvEndpointIDAttr:string,
      /**  PriceToleranceOnHigherPrice  */  
   PriceToleranceOnHigherPrice:boolean,
      /**  URL address to the Quick Ship application  */  
   QuickShipURL:string,
      /**  Indicates if Quick Ship International Shipments are used.  */  
   QSUseIntl:boolean,
      /**  Indicates if Quick Ship Bill of Lading  is used.  */  
   QSUseBOL:boolean,
      /**  Reserved for Future Development  */  
   QSUseCO:boolean,
      /**  Stores the name of the admin group referring to the security group maintenance.  */  
   CNGTIAdminGroup:string,
      /**  Define the search sequence  */  
   CNCheckerSearchSeq:number,
      /**  Define the search sequence  */  
   CNMakerSearchSeq:number,
      /**  SalesTaxID  */  
   SalesTaxID:string,
      /**  ServiceTaxID  */  
   ServiceTaxID:string,
      /**  ELIEinvoice  */  
   ELIEinvoice:boolean,
      /**  ELIDefReportID  */  
   ELIDefReportID:string,
      /**  ELIDefStyleNum  */  
   ELIDefStyleNum:number,
      /**  ELIDefToMail  */  
   ELIDefToMail:string,
      /**  ELIDefCCMail  */  
   ELIDefCCMail:string,
      /**  ELIDefMailTempID  */  
   ELIDefMailTempID:string,
      /**  ELIDefEinvoicePath  */  
   ELIDefEinvoicePath:string,
      /**  ELIDefDepTranDocTypeID  */  
   ELIDefDepTranDocTypeID:string,
      /**  Enable Received Date Warning (CSF Poland)  */  
   PLEnableRcvDateWarning:boolean,
      /**  COOneTimeID  */  
   COOneTimeID:string,
      /**  COFiscalResp1  */  
   COFiscalResp1:string,
      /**  COFiscalResp2  */  
   COFiscalResp2:string,
      /**  COFiscalResp3  */  
   COFiscalResp3:string,
      /**  Weight UOM Class  */  
   CNWeightUOMClass:string,
      /**  EORI Number  */  
   EORINumber:string,
      /**  Enable Netting Transaction Entry  */  
   EnableNetting:boolean,
      /**  This field indicates that posting of withholding taxes will go through interim accounts when tax timing is partially paid or fully paid.  */  
   WithholdAcctToInterim:boolean,
      /**  ELIDefFromMail  */  
   ELIDefFromMail:string,
      /**  This transaction document type will be the one assigned for the netting credit memo created.  */  
   NetTranDocTypeIDCM:string,
      /**  Description: This transaction document type will be the one assigned for the netting debit memo created  */  
   NetTranDocTypeIDDM:string,
      /**  Security Group to be used as Tax Declaration Admins  */  
   TWTaxDeclarationAdminGroup:string,
      /**  Enables/disables Tax Id validation.  */  
   TaxValidationAllow:boolean,
      /**  Electronic Interface of type Tax Id Validation  */  
   TaxValidationEFTHeadUID:number,
      /**  Enables/disables automatic Tax Id validation when customer or supplier Tax Id is changed.  */  
   TaxValidationAutomatic:boolean,
      /**  Action if Invalid Tax ID  */  
   TaxValidationAction:number,
      /**  RevaluationBAUnrealized  */  
   RevaluationBAUnrealized:boolean,
      /**  RevaluationPCDUnrealized  */  
   RevaluationPCDUnrealized:boolean,
      /**  HMRCTaxValidationAllow  */  
   HMRCTaxValidationAllow:boolean,
      /**  HMRCTaxValidationURL  */  
   HMRCTaxValidationURL:string,
      /**  HMRCTaxValidationAutomatic  */  
   HMRCTaxValidationAutomatic:boolean,
      /**  HMRCTaxValidationAction  */  
   HMRCTaxValidationAction:number,
      /**  Indicates if entry of a County of Origin is required for Lots of this Part. Pertinent only for lot tracked parts. Accepted values are N="Not Tracked", T = "Tracked" and M = "Mandatory".  */  
   AttISOrigCountry:string,
      /**  Company Scheme ID  */  
   ExternalSchemeID:string,
      /**  Company ID  */  
   ExternalID:string,
      /**  Indicates site can be used as a legal entity.  */  
   SiteIsLegalEntity:boolean,
      /**  Tax Rate by Kg  */  
   MYTaxRateByKg:string,
      /**  Tax Rate by Liter  */  
   MYTaxRateByLiter:string,
      /**  Encryption Key  */  
   TWEncryptionKey:string,
      /**  EInvoice Operator Code  */  
   ELIOperatorCode:string,
      /**  Indicates the logic used to calculate the base/rpt fields.  Currently used by Bank Funds Transfer  */  
   CurrExDiff:number,
      /**  The document type used to generate the legal number for the invoices generated automatically at the shipment.  */  
   ERSDocTypeID:string,
      /**  The group prefix used to generated the invoice group for the invoice generated automatically by the system when shipping an ERS PO.  */  
   ERSInvGrpPrefix:string,
      /**  Default Path where the files will be stored to be read by the Import EDI Process.  */  
   InboundPath:string,
      /**  ELIERSDocTypeID  */  
   ELIERSDocTypeID:string,
      /**  ELISendMail  */  
   ELISendMail:boolean,
      /**  ELISendingOption  */  
   ELISendingOption:number,
      /**  PlasticTaxUOMCode  */  
   PlasticTaxUOMCode:string,
      /**  PlasticTaxRate  */  
   PlasticTaxRate:number,
      /**  CNQuantityControl  */  
   CNQuantityControl:number,
      /**  QuickShip Registration Code  */  
   QuickShipRegCode:string,
      /**  URL address to the Quick Ship API  */  
   QuickShipAPIURL:string,
      /**  Quick Ship User Name  */  
   QuickShipUserID:string,
      /**  Quick Ship Password  */  
   QuickShipPassword:string,
      /**  CNBondedWhseControl  */  
   CNBondedWhseControl:number,
      /**  Freight Service Integration Selection. (AI - REST API Integration, QW - Quick Ship Web Services)  */  
   FreightSvcInt:string,
      /**  BaseUOMClassID  */  
   BaseUOMClassID:string,
      /**  Indicates financial groups are automatically locked on selection or creation  */  
   AutoLockFinGroups:boolean,
      /**  Controls where Attachments are place when CPQ pushes them to Kinetic.  The selected Document Type must be of Server Transfer Type.  If the selected Document Type is Reserved for Specific Tables, the Document Type Control must include the following tables: OrderDtl, QuoteAsm, QuoteDtl, JobAsmbl, JobHead.  If no Document Type is selected, the CPQ Quote Sync will be the master and pull attachments from CPQ and if there is a value CPQ Quote Sync will not run.  */  
   KBMaxDocTypeID:string,
      /**  Default E-invoice Report Style  */  
   ELIRcptDefStyleNum:number,
   CNCFICodeDescription:string,
      /**  CSF China - dynamic field for calculating of the XBSyst.CNCFICodeCurGainLoss field.  */  
   CNCOACode:string,
      /**  Web-Service URL for E-Invoice.  */  
   EInvWSURL:string,
   EnableOCRCalcType:boolean,
      /**   If this flag is true then on Currency Revaluation screen the Reverse checkbox is enabled.
If this flag is false then on Currency Revaluaion screen Reverse checkbox is Read Only and set to true.  */  
   EnableReverse:boolean,
      /**  Enable calculation of settlement discounts for credit memos in AR  */  
   IsDiscountforCreditM:boolean,
   JPFiscalCalDescription:string,
      /**  Peru Collection Agent withholding status  */  
   PECollectionAgent:boolean,
      /**  Peru Goods Contributor withholding status  */  
   PEGoodsContributor:boolean,
      /**  Peru No Address Provided withholding status  */  
   PENoAddress:boolean,
      /**  Peru Not Found withholding status.  */  
   PENotFound:boolean,
      /**  Peru Withholding Agent withholding status  */  
   PEWithholdAgent:boolean,
      /**  Display used to for PORelShipOption  */  
   PORelShipOptDisplay:string,
   TranDocTypeDescription:string,
      /**  The field for user to input Company Encryption Key  */  
   TWEncryptionKeyInput:string,
      /**  CSF China - dynamic field for calculating of the XBSyst.CNCFICodeCurGainLoss field.  */  
   CNSegmentNbr:number,
      /**  Currency Exchange Difference  */  
   CurrencyExchangeDiff:string,
      /**  URL of the OneEDI API Endpoint to post the demand outbound to  */  
   OneEDIAPIUrl:string,
      /**  Client Id required to access OneEDI API  */  
   OneEDIAPIClientId:string,
      /**  Client Secret required to access OneEDI API  */  
   OneEDIAPIClientSecret:string,
      /**  CPQ Instance URL.  */  
   KBMaxUrl:string,
      /**  CPQ Username used for communication.  */  
   KBMaxUsername:string,
      /**  CPQ password used for communication.  */  
   KBMaxPassword:string,
      /**  CPQ SQL Instance for syncing data between Kinetic and CPQ.  */  
   KBMaxSqlInstance:string,
   KBMaxSqlDatabase:string,
   KBMaxSqlUsername:string,
   KBMaxSqlPassword:string,
      /**  Indicates if site segements should be inactivated.  */  
   InactivateSiteSegments:boolean,
   EDISupplierEnable:boolean,
   BitFlag:number,
   BankBankName:string,
   BankDescription:string,
   CNOurBankBankAcctDescription:string,
   CNOurBankBankAcctBankName:string,
   CurrCashRateGrpDescription:string,
   CurrExpenseRateGrpDescription:string,
   CurrFARateGrpDescription:string,
   CurrGenRateGrpDescription:string,
   CurrInvRateGrpDescription:string,
   CurrPORateGrpDescription:string,
   CurrPRRateGrpDescription:string,
   CurrSalesRateGrpDescription:string,
   CurrSubRateGrpDescription:string,
   CurrTaxRateGrpDescription:string,
   FSAExpensePMUIDType:number,
   FSAExpensePMUIDName:string,
   FSAExpensePMUIDSummarizePerCustomer:boolean,
   FSARMAReasonCodeDescription:string,
   FSAShipViaCodeDescription:string,
   FSAShipViaCodeWebDesc:string,
   GlobalCurrencyDocumentDesc:string,
   GlobalCurrencyCurrDesc:string,
   GlobalCurrencyCurrName:string,
   GlobalCurrencyCurrencyID:string,
   GlobalCurrencyCurrSymbol:string,
   MXDocTypeDescription:string,
   StockProvFmtExcessDescription:string,
   StockProvFmtSlowDescription:string,
   SysFormsPrinterDescription:string,
   SysLabelsPrinterDescription:string,
   THTaxRecDocTypeDescription:string,
   THWHTDocTypeDescription:string,
   WFGroupDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param vCompany
   */  
export interface FormatList_input{
      /**  Company number  */  
   vCompany:string,
}

export interface FormatList_output{
parameters : {
      /**  output parameters  */  
   formatList:string,
}
}

export interface GetBookMethodList_output{
parameters : {
      /**  output parameters  */  
   strList:string,
}
}

   /** Required : 
      @param company
   */  
export interface GetByID_input{
   company:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CompanyTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CompanyTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CompanyTableset[],
}

export interface GetCPayCompanyList_output{
parameters : {
      /**  output parameters  */  
   cpayCompanyList:string,
}
}

   /** Required : 
      @param appName
   */  
export interface GetCheckOffLabels_input{
      /**  Either Job, Quote or DMR  */  
   appName:string,
}

export interface GetCheckOffLabels_output{
parameters : {
      /**  output parameters  */  
   labelList:string,
}
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
   returnObj:string,
}

export interface GetInitialPath_output{
      /**  A string containing the default path  */  
   returnObj:string,
}

   /** Required : 
      @param transType
   */  
export interface GetLegalNumbers_input{
   transType:string,
}

export interface GetLegalNumbers_output{
   returnObj:string,
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
   returnObj:Erp_Tablesets_CompanyListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetMaxWorkQueueRecords_output{
   returnObj:number,
}

   /** Required : 
      @param vCompany
   */  
export interface GetModLicensing_input{
      /**  Company number  */  
   vCompany:string,
}

export interface GetModLicensing_output{
parameters : {
      /**  output parameters  */  
   vModules:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewAGCompany_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewAGCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewAPSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewAPSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewARSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewARSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewBMSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewBMSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
      @param company
   */  
export interface GetNewBorderPct_input{
   ds:Erp_Tablesets_CompanyTableset[],
   company:string,
}

export interface GetNewBorderPct_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
      @param company
   */  
export interface GetNewBorderPercent_input{
   ds:Erp_Tablesets_CompanyTableset[],
      /**  The company ID  */  
   company:string,
}

export interface GetNewBorderPercent_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCRSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewCRSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCSFSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewCSFSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
      @param company
   */  
export interface GetNewCompanyAttch_input{
   ds:Erp_Tablesets_CompanyTableset[],
   company:string,
}

export interface GetNewCompanyAttch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCompany_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
      @param company
   */  
export interface GetNewCurrRateGrp_input{
   ds:Erp_Tablesets_CompanyTableset[],
   company:string,
}

export interface GetNewCurrRateGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
      @param company
   */  
export interface GetNewCurrency_input{
   ds:Erp_Tablesets_CompanyTableset[],
   company:string,
}

export interface GetNewCurrency_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewEQSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewEQSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
      @param company
      @param relatedToFile
      @param key1
      @param key2
      @param key3
      @param key4
      @param key5
      @param key6
   */  
export interface GetNewEntityGLC_input{
   ds:Erp_Tablesets_CompanyTableset[],
   company:string,
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
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewExtPRSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewExtPRSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewFsSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewFsSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewGLSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewGLSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewISSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewISSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewJCSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewJCSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewMMSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewMMSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPDMSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewPDMSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
      @param company
   */  
export interface GetNewPECompWhldHist_input{
   ds:Erp_Tablesets_CompanyTableset[],
   company:string,
}

export interface GetNewPECompWhldHist_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPRSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewPRSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTaxSvcConfig_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewTaxSvcConfig_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewXaSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewXaSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewXbSyst_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface GetNewXbSyst_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

export interface GetOCRAlgorithmList_output{
parameters : {
      /**  output parameters  */  
   cOCRAlgorithmList:string,
}
}

export interface GetQuickShipURL_output{
      /**  The value of the QuickShipURL (string).  */  
   returnObj:string,
}

   /** Required : 
      @param whereClauseCompany
      @param whereClauseCompanyAttch
      @param whereClauseAGCompany
      @param whereClauseAPSyst
      @param whereClauseARSyst
      @param whereClauseBMSyst
      @param whereClauseBorderPct
      @param whereClauseCRSyst
      @param whereClauseCSFSyst
      @param whereClauseCurrency
      @param whereClauseCurrRateGrp
      @param whereClauseEQSyst
      @param whereClauseExtPRSyst
      @param whereClauseFsSyst
      @param whereClauseGLSyst
      @param whereClauseISSyst
      @param whereClauseJCSyst
      @param whereClauseMMSyst
      @param whereClausePDMSyst
      @param whereClausePECompWhldHist
      @param whereClausePRSyst
      @param whereClauseTaxSvcConfig
      @param whereClauseXaSyst
      @param whereClauseXbSyst
      @param whereClauseEntityGLC
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCompany:string,
   whereClauseCompanyAttch:string,
   whereClauseAGCompany:string,
   whereClauseAPSyst:string,
   whereClauseARSyst:string,
   whereClauseBMSyst:string,
   whereClauseBorderPct:string,
   whereClauseCRSyst:string,
   whereClauseCSFSyst:string,
   whereClauseCurrency:string,
   whereClauseCurrRateGrp:string,
   whereClauseEQSyst:string,
   whereClauseExtPRSyst:string,
   whereClauseFsSyst:string,
   whereClauseGLSyst:string,
   whereClauseISSyst:string,
   whereClauseJCSyst:string,
   whereClauseMMSyst:string,
   whereClausePDMSyst:string,
   whereClausePECompWhldHist:string,
   whereClausePRSyst:string,
   whereClauseTaxSvcConfig:string,
   whereClauseXaSyst:string,
   whereClauseXbSyst:string,
   whereClauseEntityGLC:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CompanyTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface GetSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   serialList:string,
}
}

export interface GetSystemTimeZoneList_output{
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

   /** Required : 
      @param companyID
      @param baseCurrencyCode
      @param decimalsCost
      @param decimalsPrice
      @param decimalsGeneral
   */  
export interface InitializeCompany_input{
   companyID:string,
   baseCurrencyCode:string,
   decimalsCost:number,
   decimalsPrice:number,
   decimalsGeneral:number,
}

export interface InitializeCompany_output{
}

export interface NLCopyDigipoortSettingToAllCompanies_output{
      /**  Companies have been modified  */  
   returnObj:string,
}

   /** Required : 
      @param ipBankAcctID
      @param ds
   */  
export interface OnChangeARBankAcctID_input{
   ipBankAcctID:string,
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface OnChangeARBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param AddrValEnabled
      @param ds
   */  
export interface OnChangeAddrValEnabled_input{
   AddrValEnabled:boolean,
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface OnChangeAddrValEnabled_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ipBankAcctID
      @param ds
   */  
export interface OnChangeBankAcctID_input{
   ipBankAcctID:string,
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface OnChangeBankAcctID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ipProposedCColCompany
      @param ds
   */  
export interface OnChangeCentralCollectionParentCompany_input{
      /**  Central Collection Parent Company value  */  
   ipProposedCColCompany:string,
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface OnChangeCentralCollectionParentCompany_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface OnChangeDefTaxLiability_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface OnChangeDefTaxLiability_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param eliDefEinvoicePath
      @param ds
   */  
export interface OnChangeELIDefEinvoicePath_input{
   eliDefEinvoicePath:string,
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface OnChangeELIDefEinvoicePath_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param eliDefReportID
      @param ds
   */  
export interface OnChangeELIDefReportID_input{
   eliDefReportID:string,
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface OnChangeELIDefReportID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param cFlowCode
      @param lIsFlowArrival
      @param ds
   */  
export interface OnChangeFlow_input{
      /**  Flow code.  */  
   cFlowCode:string,
      /**  Flag, showed which flow code has been changing: True - Arrival; False - Despatch.  */  
   lIsFlowArrival:boolean,
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface OnChangeFlow_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param cGJJournalCode
   */  
export interface OnChangeGJJournalCode_input{
      /**  Proposed GJJournalCode  */  
   cGJJournalCode:string,
}

export interface OnChangeGJJournalCode_output{
}

   /** Required : 
      @param currMasterChart
      @param newMasterChart
   */  
export interface OnChangeMasterChart_input{
      /**  Current value of MasterChart  */  
   currMasterChart:string,
      /**  Proposed value of MasterChart  */  
   newMasterChart:string,
}

export interface OnChangeMasterChart_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
}
}

   /** Required : 
      @param ipSiteIsLegalEntity
      @param ds
   */  
export interface OnChangeSiteIsLegalEntity_input{
   ipSiteIsLegalEntity:boolean,
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface OnChangeSiteIsLegalEntity_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param ipTranDocTypeID
      @param ds
   */  
export interface OnChangeTranDocType_input{
   ipTranDocTypeID:string,
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface OnChangeTranDocType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param UseAltBillToAddr
      @param ds
   */  
export interface OnChangeUseAltBillToAddr_input{
   UseAltBillToAddr:boolean,
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface OnChangeUseAltBillToAddr_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param pDestCountryNum
      @param bBorderPctSysRowID
   */  
export interface OnChangingDestCountryNum_input{
      /**  Proposed DestCountryNum  */  
   pDestCountryNum:number,
      /**  Current SysRowID  */  
   bBorderPctSysRowID:string,
}

export interface OnChangingDestCountryNum_output{
}

   /** Required : 
      @param pSubRateGrp
   */  
export interface OnChangingSubRateGrp_input{
      /**  Proposed SubRateGrp  */  
   pSubRateGrp:string,
}

export interface OnChangingSubRateGrp_output{
}

export interface SiteIsLegalEntity_output{
   returnObj:boolean,
}

export interface TestExtCRMConnection_output{
parameters : {
      /**  output parameters  */  
   msgConnection:string,
}
}

   /** Required : 
      @param svcURL
      @param svcAccount
      @param svcLicense
   */  
export interface TestTaxConnection_input{
      /**  SvcURL  */  
   svcURL:string,
      /**  SvcAccount  */  
   svcAccount:string,
      /**  SvcLicense  */  
   svcLicense:string,
}

export interface TestTaxConnection_output{
parameters : {
      /**  output parameters  */  
   testResult:boolean,
   testMessage:string,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCompanyTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCompanyTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CompanyTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CompanyTableset,
}
}

   /** Required : 
      @param countryNum
   */  
export interface ValidateIntrastatCodeForCompany_input{
      /**  Country for Current Company  */  
   countryNum:number,
}

export interface ValidateIntrastatCodeForCompany_output{
   returnObj:boolean,
}

   /** Required : 
      @param proposedCodeID
      @param proposedCodeValue
      @param industryCode1
      @param industryCode2
      @param industryCode3
      @param industryCode4
      @param industryCode5
   */  
export interface ValidateMYIndustryCodeOnChanging_input{
      /**  zero-based order number of industry codes  */  
   proposedCodeID:number,
      /**  proposed value  */  
   proposedCodeValue:string,
      /**  industry code 1  */  
   industryCode1:string,
      /**  industry code 2  */  
   industryCode2:string,
      /**  industry code 3  */  
   industryCode3:string,
      /**  industry code 4  */  
   industryCode4:string,
      /**  industry code 5  */  
   industryCode5:string,
}

export interface ValidateMYIndustryCodeOnChanging_output{
   returnObj:string,
}

   /** Required : 
      @param companyId
      @param sendToFSA
   */  
export interface ValidateSendToFSA_input{
      /**  Current Company  */  
   companyId:string,
      /**  Sync to FSA flag for Current Company  */  
   sendToFSA:boolean,
}

export interface ValidateSendToFSA_output{
   returnObj:boolean,
}

