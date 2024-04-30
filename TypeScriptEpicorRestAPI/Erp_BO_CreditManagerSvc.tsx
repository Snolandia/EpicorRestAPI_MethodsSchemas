import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.CreditManagerSvc
// Description: Customer Credit Manager Business Object
           Notes : The logic for the update of the Customer Credit Information is copied
           from the Customer Business Object.  Limit the fields to be maintained
           for Customer since validation is limited to just the update of credit
           information.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get CreditManagers items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CreditManagers
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CMCustomerRow
   */  
export function get_CreditManagers(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CMCustomerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CMCustomerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CreditManagers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CMCustomerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CMCustomerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreditManagers(requestBody:Erp_Tablesets_CMCustomerRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CreditManager item
   Description: Calls GetByID to retrieve the CreditManager item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CreditManager
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CMCustomerRow
   */  
export function get_CreditManagers_Company_CustNum(Company:string, CustNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CMCustomerRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_CMCustomerRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CreditManager for the service
   Description: Calls UpdateExt to update CreditManager. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CreditManager
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CMCustomerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CreditManagers_Company_CustNum(Company:string, CustNum:string, requestBody:Erp_Tablesets_CMCustomerRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")", {
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
   Summary: Call UpdateExt to delete CreditManager item
   Description: Call UpdateExt to delete CreditManager item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CreditManager
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CreditManagers_Company_CustNum(Company:string, CustNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")", {
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
   Description: Get CustomCrdPools items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CustomCrdPools1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustomCrdPoolRow
   */  
export function get_CreditManagers_Company_CustNum_CustomCrdPools(Company:string, CustNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustomCrdPoolRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")/CustomCrdPools", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustomCrdPoolRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the CustomCrdPool item
   Description: Calls GetByID to retrieve the CustomCrdPool item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustomCrdPool1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CustomCrdPoolRow
   */  
export function get_CreditManagers_Company_CustNum_CustomCrdPools_SysRowID(Company:string, CustNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CustomCrdPoolRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")/CustomCrdPools(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_CustomCrdPoolRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get GlbCustCreds items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_GlbCustCreds1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCustCredRow
   */  
export function get_CreditManagers_Company_CustNum_GlbCustCreds(Company:string, CustNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustCredRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")/GlbCustCreds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustCredRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the GlbCustCred item
   Description: Calls GetByID to retrieve the GlbCustCred item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCustCred1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ExtCompany Desc: ExtCompany   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GlbCustCredRow
   */  
export function get_CreditManagers_Company_CustNum_GlbCustCreds_Company_CustNum_ExtCompany(Company:string, CustNum:string, ExtCompany:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbCustCredRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CreditManagers(" + Company + "," + CustNum + ")/GlbCustCreds(" + Company + "," + CustNum + "," + ExtCompany + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbCustCredRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get CustomCrdPools items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustomCrdPools
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustomCrdPoolRow
   */  
export function get_CustomCrdPools(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustomCrdPoolRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CustomCrdPools", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustomCrdPoolRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustomCrdPools
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustomCrdPoolRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.CustomCrdPoolRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomCrdPools(requestBody:Erp_Tablesets_CustomCrdPoolRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CustomCrdPools", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the CustomCrdPool item
   Description: Calls GetByID to retrieve the CustomCrdPool item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustomCrdPool
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.CustomCrdPoolRow
   */  
export function get_CustomCrdPools_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CustomCrdPoolRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CustomCrdPools(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_CustomCrdPoolRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CustomCrdPool for the service
   Description: Calls UpdateExt to update CustomCrdPool. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustomCrdPool
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustomCrdPoolRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CustomCrdPools_SysRowID(SysRowID:string, requestBody:Erp_Tablesets_CustomCrdPoolRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CustomCrdPools(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete CustomCrdPool item
   Description: Call UpdateExt to delete CustomCrdPool item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustomCrdPool
      @param SysRowID Desc: SysRowID   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CustomCrdPools_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CustomCrdPools(" + SysRowID + ")", {
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
   Description: Get GlbCustCreds items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbCustCreds
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbCustCredRow
   */  
export function get_GlbCustCreds(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustCredRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GlbCustCreds", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustCredRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbCustCreds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbCustCredRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GlbCustCredRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbCustCreds(requestBody:Erp_Tablesets_GlbCustCredRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GlbCustCreds", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the GlbCustCred item
   Description: Calls GetByID to retrieve the GlbCustCred item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbCustCred
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ExtCompany Desc: ExtCompany   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GlbCustCredRow
   */  
export function get_GlbCustCreds_Company_CustNum_ExtCompany(Company:string, CustNum:string, ExtCompany:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbCustCredRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GlbCustCreds(" + Company + "," + CustNum + "," + ExtCompany + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbCustCredRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlbCustCred for the service
   Description: Calls UpdateExt to update GlbCustCred. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbCustCred
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ExtCompany Desc: ExtCompany   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbCustCredRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlbCustCreds_Company_CustNum_ExtCompany(Company:string, CustNum:string, ExtCompany:string, requestBody:Erp_Tablesets_GlbCustCredRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GlbCustCreds(" + Company + "," + CustNum + "," + ExtCompany + ")", {
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
   Summary: Call UpdateExt to delete GlbCustCred item
   Description: Call UpdateExt to delete GlbCustCred item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbCustCred
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ExtCompany Desc: ExtCompany   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlbCustCreds_Company_CustNum_ExtCompany(Company:string, CustNum:string, ExtCompany:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GlbCustCreds(" + Company + "," + CustNum + "," + ExtCompany + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CMCustomerListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CMCustomerListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CMCustomerListRow)
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
export function get_GetRows(whereClauseCMCustomer:string, whereClauseCustomCrdPool:string, whereClauseGlbCustCred:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCMCustomer!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCMCustomer=" + whereClauseCMCustomer
   }
   if(typeof whereClauseCustomCrdPool!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCustomCrdPool=" + whereClauseCustomCrdPool
   }
   if(typeof whereClauseGlbCustCred!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlbCustCred=" + whereClauseGlbCustCred
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(custNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof custNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "custNum=" + custNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method isNAGlobalCustomer
   OperationID: isNAGlobalCustomer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/isNAGlobalCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/isNAGlobalCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_isNAGlobalCustomer(requestBody:isNAGlobalCustomer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<isNAGlobalCustomer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/isNAGlobalCustomer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as isNAGlobalCustomer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCustomerGlobalFields
   OperationID: GetCustomerGlobalFields
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCustomerGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomerGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustomerGlobalFields(requestBody:GetCustomerGlobalFields_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCustomerGlobalFields_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetCustomerGlobalFields", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetCustomerGlobalFields_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetCodeDescList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method ChangeCollections
   Description: Purpose:
Parameters:
<param name="ipInCollections">switch identifying whether or not the customer is in collections</param><param name="ds">The CreditManager data set</param>
Notes:
   OperationID: ChangeCollections
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeCollections_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCollections_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeCollections(requestBody:ChangeCollections_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeCollections_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/ChangeCollections", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeCollections_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOrderCreditHold
   Description: Call this method when the user updates the order's credit hold field.  This will calculate
or reset the default Credit Override Limit of a particular order.  The toggling of the
credit hold check box will determine when OrderHed.CreditOverrideLimit should be enabled.
The Credit Override Limit should be enabled if the Credit Hold field is unchecked.
Conversely, Credit Override Limit is disabled if Credit Hold is checked.
   OperationID: ChangeOrderCreditHold
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOrderCreditHold_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderCreditHold_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOrderCreditHold(requestBody:ChangeOrderCreditHold_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOrderCreditHold_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/ChangeOrderCreditHold", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeOrderCreditHold_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeInvoiceCreditHold
   Description: Validates the Credit Hold change. If valid updates it in the DB.
   OperationID: ChangeInvoiceCreditHold
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceCreditHold_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceCreditHold_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeInvoiceCreditHold(requestBody:ChangeInvoiceCreditHold_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeInvoiceCreditHold_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/ChangeInvoiceCreditHold", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeInvoiceCreditHold_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeInvoiceCreditHoldByInvoiceNum
   Description: Validates the change of Credit Hold in selected InvoiceNum. If Credit hold is valid, it gets updated in the DB.
   OperationID: ChangeInvoiceCreditHoldByInvoiceNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeInvoiceCreditHoldByInvoiceNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInvoiceCreditHoldByInvoiceNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeInvoiceCreditHoldByInvoiceNum(requestBody:ChangeInvoiceCreditHoldByInvoiceNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeInvoiceCreditHoldByInvoiceNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/ChangeInvoiceCreditHoldByInvoiceNum", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeInvoiceCreditHoldByInvoiceNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCreditHold
   Description: This method checks if customer will go on credit hold.  Then asks if the user
wants all orders to go on credit hold.  To be called right before update.  If the user
answers yes to putting orders on hold then the ApplyHoldToOrder field needs to be populated.
   OperationID: CheckCreditHold
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCreditHold_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCreditHold_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCreditHold(requestBody:CheckCreditHold_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCreditHold_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/CheckCreditHold", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckCreditHold_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportCustCredit
   Description: Call this method to export customer credit information.  This method accepts
an input parameter to exclude or include customer with credit limit of zero.
This method returns the data table ttExportCustCred containing all valid
customer credit information.  The resulting records from the ttExportCustCred
will then need to be outputted as a CSV file (comma delimited) with the first
output line containing the description or label of all fields.
   OperationID: ExportCustCredit
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportCustCredit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportCustCredit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportCustCredit(requestBody:ExportCustCredit_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportCustCredit_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/ExportCustCredit", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExportCustCredit_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportCustCreditFile
   Description: Call this method to export customer credit information.  This method accepts
an input parameter to exclude or include customer with credit limit of zero.
This method returns the data table ttExportCustCred containing all valid
customer credit information and create a CSV file (comma delimited).
   OperationID: ExportCustCreditFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportCustCreditFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportCustCreditFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportCustCreditFile(requestBody:ExportCustCreditFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportCustCreditFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/ExportCustCreditFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExportCustCreditFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetARLOC
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><returns>The ARLOCDataSet data set</returns>
   OperationID: GetARLOC
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetARLOC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetARLOC_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetARLOC(requestBody:GetARLOC_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetARLOC_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetARLOC", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetARLOC_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByCustID
   Description: This method finds the customer record by CustId instead of CustNum
   OperationID: GetByCustID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByCustID(requestBody:GetByCustID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByCustID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetByCustID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByCustID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCashDeposits
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><returns>The InvcHeadDataSet data set</returns>
   OperationID: GetCashDeposits
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCashDeposits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCashDeposits_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCashDeposits(requestBody:GetCashDeposits_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCashDeposits_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetCashDeposits", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetCashDeposits_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetContacts
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><returns>The CustCntDataSet data set</returns>
   OperationID: GetContacts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetContacts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetContacts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetContacts(requestBody:GetContacts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetContacts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetContacts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetContacts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvoicedDeposits
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><param name="ds"></param><param name="ds1"></param>
   OperationID: GetInvoicedDeposits
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInvoicedDeposits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvoicedDeposits_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvoicedDeposits(requestBody:GetInvoicedDeposits_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInvoicedDeposits_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetInvoicedDeposits", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetInvoicedDeposits_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvoices
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><param name="ds"></param><returns>The InvcHeadDataSet data set</returns>
   OperationID: GetInvoices
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvoices(requestBody:GetInvoices_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInvoices_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetInvoices_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvoicesEx
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><param name="mode">Valid options are All, Open, Closed, OpenWithDep (GetInvoices original behavior)</param><param name="fromDays">the amount of days to get a date from which the invoices will be selected.</param><param name="inRange">if the invoices will be selected from an specific date.</param><param name="ds"></param><returns>The InvcHeadDataSet data set</returns>
   OperationID: GetInvoicesEx
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInvoicesEx_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvoicesEx_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvoicesEx(requestBody:GetInvoicesEx_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInvoicesEx_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetInvoicesEx", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetInvoicesEx_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOrders
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><returns>The CMOrderHedDataSet data set</returns>
   OperationID: GetOrders
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetOrders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrders_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrders(requestBody:GetOrders_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetOrders_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetOrders", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetOrders_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPayIns
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><returns>The ARPNHeadDataSet data set</returns>
   OperationID: GetPayIns
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPayIns_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPayIns_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPayIns(requestBody:GetPayIns_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPayIns_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetPayIns", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPayIns_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPayments
   Description: Purpose:
Parameters:  none
Notes:
<param name="ipCustID">The customer character ID</param><param name="ds"></param><returns>The CashHeadDataSet data set</returns>
   OperationID: GetPayments
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPayments_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPayments_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPayments(requestBody:GetPayments_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPayments_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetPayments", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPayments_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPaymentsHeaders
   Description: Get list of Payments (CashHead) for the selected customer.
   OperationID: GetPaymentsHeaders
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPaymentsHeaders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPaymentsHeaders_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPaymentsHeaders(requestBody:GetPaymentsHeaders_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPaymentsHeaders_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetPaymentsHeaders", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPaymentsHeaders_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPaymentsDetails
   Description: Receives GroupID and HeadNum and returns all CashDetails related to this filters.
   OperationID: GetPaymentsDetails
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPaymentsDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPaymentsDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPaymentsDetails(requestBody:GetPaymentsDetails_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPaymentsDetails_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetPaymentsDetails", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetPaymentsDetails_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCustomerBalance
   Description: Purpose: Retrieves the total unallocated amount of a customer
Parameters:  none
Notes:
<param name="custNum">the customer numeric ID</param><param name="balance">balance in favor of the customer in base currency</param><param name="rpt1Balance">balance in favor of the customer in reporting currency 1</param><param name="rpt2Balance">balance in favor of the customer in reporting currency 2</param><param name="rpt3Balance">balance in favor of the customer in reporting currency 3</param><returns>nothing</returns>
   OperationID: GetCustomerBalance
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCustomerBalance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCustomerBalance_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCustomerBalance(requestBody:GetCustomerBalance_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCustomerBalance_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetCustomerBalance", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetCustomerBalance_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportCustCredit
   Description: Call this method to import customer credit information into the database.
This method expects an input data table ttImportCustCred with data coming
from an external comma delimited file.
   OperationID: ImportCustCredit
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportCustCredit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportCustCredit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportCustCredit(requestBody:ImportCustCredit_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportCustCredit_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/ImportCustCredit", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportCustCredit_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportCustCreditCsv
   Description: Call this method to import customer credit information into the database.
This method expects the input File to exist in the server with data coming
from an external comma delimited file.
   OperationID: ImportCustCreditCsv
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportCustCreditCsv_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportCustCreditCsv_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportCustCreditCsv(requestBody:ImportCustCreditCsv_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportCustCreditCsv_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/ImportCustCreditCsv", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportCustCreditCsv_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateCMOrderHed
   Description: This method updates the ttCMOrderHed's physical table
   OperationID: UpdateCMOrderHed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateCMOrderHed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCMOrderHed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateCMOrderHed(requestBody:UpdateCMOrderHed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateCMOrderHed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/UpdateCMOrderHed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateCMOrderHed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateNACreditPrc
   Description: This method reset NACreditPrc when its status changes, based in its Used/Shared.
   OperationID: UpdateNACreditPrc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateNACreditPrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateNACreditPrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateNACreditPrc(requestBody:UpdateNACreditPrc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateNACreditPrc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/UpdateNACreditPrc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateNACreditPrc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateCreditTotals
   Description: This method updates the TotOpenCredit and TotGlobalCredit fields.  To be called when
the include credit flags are changed.
   OperationID: UpdateCreditTotals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateCreditTotals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCreditTotals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateCreditTotals(requestBody:UpdateCreditTotals_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateCreditTotals_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/UpdateCreditTotals", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateCreditTotals_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateGlobalLimits
   Description: This method converts the global credit limit from the global currency value to
the local currency value.  To be used when the global currency code changes or
when the global credit limits are changed.
   OperationID: UpdateGlobalLimits
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateGlobalLimits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateGlobalLimits_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateGlobalLimits(requestBody:UpdateGlobalLimits_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateGlobalLimits_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/UpdateGlobalLimits", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateGlobalLimits_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateNAParentCreditPrc
   Description: This method validates the NA parent credit percentage.
   OperationID: ValidateNAParentCreditPrc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateNAParentCreditPrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNAParentCreditPrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateNAParentCreditPrc(requestBody:ValidateNAParentCreditPrc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateNAParentCreditPrc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/ValidateNAParentCreditPrc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateNAParentCreditPrc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateNACreditSharedPrc
   Description: This method validate the NA credit shared percentage.
   OperationID: ValidateNACreditSharedPrc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateNACreditSharedPrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNACreditSharedPrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateNACreditSharedPrc(requestBody:ValidateNACreditSharedPrc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateNACreditSharedPrc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/ValidateNACreditSharedPrc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateNACreditSharedPrc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateGlbNAParentCreditPrc
   Description: This method validates the global NA parent credit percentage.
   OperationID: ValidateGlbNAParentCreditPrc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateGlbNAParentCreditPrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGlbNAParentCreditPrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateGlbNAParentCreditPrc(requestBody:ValidateGlbNAParentCreditPrc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateGlbNAParentCreditPrc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/ValidateGlbNAParentCreditPrc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateGlbNAParentCreditPrc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateGlbNACreditSharedPrc
   Description: This method validate the global NA credit shared percentage.
   OperationID: ValidateGlbNACreditSharedPrc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateGlbNACreditSharedPrc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateGlbNACreditSharedPrc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateGlbNACreditSharedPrc(requestBody:ValidateGlbNACreditSharedPrc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateGlbNACreditSharedPrc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/ValidateGlbNACreditSharedPrc", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateGlbNACreditSharedPrc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateAgingCode
   Description: Validates Aging Code.
   OperationID: ValidateAgingCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateAgingCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateAgingCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateAgingCode(requestBody:ValidateAgingCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateAgingCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/ValidateAgingCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ValidateAgingCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetOrdersCreditOverride
   OperationID: SetOrdersCreditOverride
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetOrdersCreditOverride_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetOrdersCreditOverride_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetOrdersCreditOverride(requestBody:SetOrdersCreditOverride_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetOrdersCreditOverride_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/SetOrdersCreditOverride", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as SetOrdersCreditOverride_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PESelectInvoices
   Description: This procedure returns Open balance invoices
   OperationID: PESelectInvoices
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PESelectInvoices_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PESelectInvoices_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PESelectInvoices(requestBody:PESelectInvoices_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PESelectInvoices_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/PESelectInvoices", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PESelectInvoices_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PEUpdateInvcHeadRecords
   Description: This procedure updates selected InvcHead
   OperationID: PEUpdateInvcHeadRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PEUpdateInvcHeadRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PEUpdateInvcHeadRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PEUpdateInvcHeadRecords(requestBody:PEUpdateInvcHeadRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PEUpdateInvcHeadRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/PEUpdateInvcHeadRecords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PEUpdateInvcHeadRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewCMCustomer
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCMCustomer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewCMCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCMCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCMCustomer(requestBody:GetNewCMCustomer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewCMCustomer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetNewCMCustomer", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewCMCustomer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGlbCustCred
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbCustCred
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGlbCustCred_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbCustCred_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlbCustCred(requestBody:GetNewGlbCustCred_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGlbCustCred_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetNewGlbCustCred", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewGlbCustCred_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CreditManagerSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CMCustomerListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CMCustomerListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CMCustomerRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CMCustomerRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustomCrdPoolRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CustomCrdPoolRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbCustCredRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbCustCredRow,
}

export interface Erp_Tablesets_CMCustomerListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   "CustID":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   "CustNum":number,
      /**  The full name of the customer.  */  
   "Name":string,
      /**  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  */  
   "CreditHold":boolean,
      /**  Contains the default FOB.FOB value of the FOB policy for this  customers orders.  Default used in sales order entry for this customer.  */  
   "DefaultFOB":string,
      /**  Determines whether or not Open Sales Orders are to be included in the credit limit checking process for the customer. This checkbox will also include open service contracts.  */  
   "CreditIncludeOrders":boolean,
      /**  Date on which the next credit review should be conducted for the customer.  */  
   "CreditReviewDate":string,
      /**  Date on which the customer was last placed on credit hold. This field is maintained by the system.  */  
   "CreditHoldDate":string,
      /**  Indicates how the customer was placed on credit hold.  Valid values are "MANUAL", "INVOICES", "ORDERS", and "CONTRACTS".  "MANUAL" means that the user placed the customer on hold.  INVOICES means that the customer's open A/R balance exceeded the credit limit.  ORDERS means that the sum of the open A/R and the open orders exceeded the credit limit. This field is maintained by the system.  */  
   "CreditHoldSource":string,
      /**  The UserFile.DCDUSERID value of the user that last cleared the customer's credit hold. This field is maintained by the system.  */  
   "CreditClearUserID":string,
      /**  The date that the user last cleared the customer's credit hold. This field is maintained by the system.  */  
   "CreditClearDate":string,
      /**  The time that the user last cleared the customer's credit hold in HH:MM:SS format. This field is maintained by the system.  */  
   "CreditClearTime":string,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   "EDICode":string,
      /**  The Customer.CustNum value of the customer's parent company.  */  
   "ParentCustNum":number,
      /**  Determines whether or not this customer is an inter-company customer.  */  
   "ICCust":boolean,
      /**  BillFrequency  */  
   "BillFrequency":string,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   "CreditIncludePI":boolean,
      /**  Determines whether or not this customer is shared between more than one company.  */  
   "GlobalCust":boolean,
      /**  Indicates if this customer participates in the Inter-Company Trading.  */  
   "ICTrader":boolean,
      /**  Determines whether or not Open Orders are to be included in the global credit limit checking process. This checkbox will also include open service contracts.  */  
   "GlobalCredIncOrd":boolean,
      /**  Indicates whether or not Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking process.  */  
   "GlobalCredIncPI":boolean,
      /**  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  */  
   "GlobalCurrencyCode":string,
      /**  Determines whether or not the customer has been placed into a "Global Credit Hold" status.  Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  */  
   "GlobalCreditHold":string,
      /**  Determines whether or not this customer record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit.  A credit limit of zero is considered as having unlimited credit.  */  
   "CreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  */  
   "CustPILimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit Limit.  A credit limit of zero is considered as having unlimited credit.  */  
   "GlobalCreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  */  
   "GlobalPILimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  */  
   "DocGlobalCreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  */  
   "DocGlobalPILimit":number,
      /**  allow use Parent Credit in National Account  */  
   "NAParentCreditIsUsed":boolean,
      /**  allow/deny to a customer share his own credit with other customers within the National account  */  
   "NACreditIsShare":boolean,
      /**  define what type of credit will be used first when the customer  */  
   "NACreditPreferenceList":string,
      /**  Max Percent of Parent Credit to Use  */  
   "NAParentCreditPrc":number,
      /**  Percentage of the customer credit shared to his Children.  */  
   "NACreditSharedPrc":number,
      /**  allow use Global Parent Credit in National Account  */  
   "GlbNAParentCreditIsUsed":boolean,
      /**  allow/deny to a customer share his own credit with other customers within the Global National account  */  
   "GlbNACreditIsShare":boolean,
      /**  Max Percent of Global Parent Credit to Use  */  
   "GlbNAParentCreditPrc":number,
      /**  Percentage of the customer credit shared to his Global Children.  */  
   "GlbNACreditSharedPrc":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Total number of open invoices  */  
   "TotOpenInvoices":number,
      /**  Total number of open orders  */  
   "TotOpenOrders":number,
      /**  Total number of open Payment Instruments  */  
   "TotOpenPI":number,
   "TotInvoiceCredit":number,
   "TotOrderCredit":number,
   "TotPICredit":number,
      /**  Total Credit based on CredInc flags  */  
   "TotOpenCredit":number,
      /**  Total Global Invoice Credit (including current company)  */  
   "TotGlbInvoiceCredit":number,
      /**  Total Global Order Credit (including current company)  */  
   "TotGlbOrderCredit":number,
      /**  Total Global Payment Instruments Credit (including current company)  */  
   "TotGlbPICredit":number,
      /**  Total Global Open Credit (based on GlbCredInc flags)  */  
   "TotGlbOpenCredit":number,
      /**  Indicates if the Customer is Global (master or linked)  */  
   "GlbFlag":boolean,
      /**  Indicates whether PI fields should be enabled or not  */  
   "PIFlag":boolean,
      /**  Apply credit hold status to orders  */  
   "ApplyHoldToOrders":boolean,
   "FxdTotOrders":number,
   "FxdTotPI":number,
   "FxdOrderCredit":number,
   "FxdPICredit":number,
   "FxdGlbOrdCredit":number,
   "FxdGlbPICredit":number,
      /**  Same value as GlobalCredIncOrd except if customer not global, value is no.  */  
   "DspGlobalCredIncOrd":boolean,
   "EDITest":boolean,
   "EDITranslator":string,
      /**  Own Credit Available  */  
   "NAOwnCreditAvail":number,
   "NAOwnCreditUsedDsp":number,
      /**  Available Parent?s Credit in National Accout  */  
   "NAParentCrdAvail":number,
   "NAPoolCreditUsed":number,
   "NASharedCreditUsedDsp":number,
      /**  Available credit from credit pools to be used by this customer in National account.  */  
   "NAPoolCrdAvail":number,
      /**  Customer?s credit available to be shared with his Children in National Account  */  
   "NAChildCrdAvail":number,
   "NAParentsCreditUsedDsp":number,
      /**  Global Shared Credit Available  */  
   "GlbNAChildCrdAvail":number,
   "GlbNAOwnCreditUsedDsp":number,
      /**  Global Parents Credit Available  */  
   "GlbNAParentCrdAvail":number,
   "GlbNAPoolCreditUsed":number,
   "GlbNAParentsCreditUsedDsp":number,
   "GlbNAPoolCrdAvail":number,
   "GlbNASharedCreditUsedDsp":number,
      /**  Global Own Credit Available  */  
   "GlbNAOwnCreditAvail":number,
      /**  National Credit data has been updated and recalculation is needed  */  
   "NACreditUpdated":boolean,
      /**  Total Credit available in the National Account  */  
   "NATotalCreditAvail":number,
   "NATotalCreditUsed":number,
      /**  Is the customer in the National Account of Credit Checking  */  
   "NACreditCust":boolean,
   "TotLCCredit":number,
      /**  Total open order value against LC/ECG  */  
   "TotLCOpenOrders":number,
      /**  Total cumulative invoices against LC/ECG  */  
   "TotLCCumInvoices":number,
      /**  Total invoice balance against LC/ECG  */  
   "TotLCInvoiceBal":number,
      /**  Total LC/ECG credit used.  */  
   "TotLCUsed":number,
      /**  Total number of open LC/ECG.  */  
   "TotOpenLC":number,
      /**  Total number of open orders against LC/ECG.  */  
   "TotOpenOrderLC":number,
      /**  Total number of open invoices against LC/ECG.  */  
   "TotOpenInvoicesLC":number,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "GlobalCurrencyCurrencyID":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "GlobalCurrencyDocumentDesc":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "GlobalCurrencyCurrName":string,
      /**  Description of the currency  */  
   "GlobalCurrencyCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "GlobalCurrencyCurrSymbol":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CMCustomerRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   "CustID":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   "CustNum":number,
      /**  The full name of the customer.  */  
   "Name":string,
      /**  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  */  
   "CreditHold":boolean,
      /**  Contains the default FOB.FOB value of the FOB policy for this  customers orders.  Default used in sales order entry for this customer.  */  
   "DefaultFOB":string,
      /**  Determines whether or not Open Sales Orders are to be included in the credit limit checking process for the customer. This checkbox will also include open service contracts.  */  
   "CreditIncludeOrders":boolean,
      /**  Date on which the next credit review should be conducted for the customer.  */  
   "CreditReviewDate":string,
      /**  Date on which the customer was last placed on credit hold. This field is maintained by the system.  */  
   "CreditHoldDate":string,
      /**  Indicates how the customer was placed on credit hold.  Valid values are "MANUAL", "INVOICES", "ORDERS", and "CONTRACTS".  "MANUAL" means that the user placed the customer on hold.  INVOICES means that the customer's open A/R balance exceeded the credit limit.  ORDERS means that the sum of the open A/R and the open orders exceeded the credit limit. This field is maintained by the system.  */  
   "CreditHoldSource":string,
      /**  The UserFile.DCDUSERID value of the user that last cleared the customer's credit hold. This field is maintained by the system.  */  
   "CreditClearUserID":string,
      /**  The date that the user last cleared the customer's credit hold. This field is maintained by the system.  */  
   "CreditClearDate":string,
      /**  The time that the user last cleared the customer's credit hold in HH:MM:SS format. This field is maintained by the system.  */  
   "CreditClearTime":string,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   "EDICode":string,
      /**  The Customer.CustNum value of the customer's parent company.  */  
   "ParentCustNum":number,
      /**  Determines whether or not this customer is an inter-company customer.  */  
   "ICCust":boolean,
      /**  BillFrequency  */  
   "BillFrequency":string,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   "CreditIncludePI":boolean,
      /**  Determines whether or not this customer is shared between more than one company.  */  
   "GlobalCust":boolean,
      /**  Indicates if this customer participates in the Inter-Company Trading.  */  
   "ICTrader":boolean,
      /**  Determines whether or not Open Orders are to be included in the global credit limit checking process. This checkbox will also include open service contracts.  */  
   "GlobalCredIncOrd":boolean,
      /**  Indicates whether or not Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking process.  */  
   "GlobalCredIncPI":boolean,
      /**  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  */  
   "GlobalCurrencyCode":string,
      /**  Determines whether or not the customer has been placed into a "Global Credit Hold" status.  Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  */  
   "GlobalCreditHold":string,
      /**  Determines whether or not this customer record will receive global updates.  */  
   "GlobalLock":boolean,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit.  A credit limit of zero is considered as having unlimited credit.  */  
   "CreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  */  
   "CustPILimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit Limit.  A credit limit of zero is considered as having unlimited credit.  */  
   "GlobalCreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  */  
   "GlobalPILimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  */  
   "DocGlobalCreditLimit":number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  */  
   "DocGlobalPILimit":number,
      /**  allow use Parent Credit in National Account  */  
   "NAParentCreditIsUsed":boolean,
      /**  allow/deny to a customer share his own credit with other customers within the National account  */  
   "NACreditIsShare":boolean,
      /**  define what type of credit will be used first when the customer  */  
   "NACreditPreferenceList":string,
      /**  Max Percent of Parent Credit to Use  */  
   "NAParentCreditPrc":number,
      /**  Percentage of the customer credit shared to his Children.  */  
   "NACreditSharedPrc":number,
      /**  allow use Global Parent Credit in National Account  */  
   "GlbNAParentCreditIsUsed":boolean,
      /**  allow/deny to a customer share his own credit with other customers within the Global National account  */  
   "GlbNACreditIsShare":boolean,
      /**  Max Percent of Global Parent Credit to Use  */  
   "GlbNAParentCreditPrc":number,
      /**  Percentage of the customer credit shared to his Global Children.  */  
   "GlbNACreditSharedPrc":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  In Collections  */  
   "Collections":boolean,
      /**  CollectionsDate  */  
   "CollectionsDate":string,
      /**  Date Collection Posted  */  
   "DateCollectionPosted":string,
      /**  Indicates if customer has been placed into an "Aging Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  */  
   "AgingCreditHold":boolean,
      /**  Date on which the customer was last placed on aging hold. This field is maintained by the system.  */  
   "AgingCreditHoldDate":string,
      /**  Indicates how the customer was placed on aging hold.  Valid values are "MANUAL" and "PROCESS".  "MANUAL" means that the user placed the customer on hold.  “PROCESS” means that the Mass Credit Information Update Process places the customer on aging hold.  This field is maintained by the system.  */  
   "AgingCreditHoldSource":string,
      /**  The UserFile.DCDUSERID value of the user that last cleared the customer's aging hold. This field is maintained by the system.  */  
   "AgingCreditClearUserID":string,
      /**  The date that the user last cleared the customer's aging hold. This field is maintained by the system.  */  
   "AgingCreditClearDate":string,
      /**  The aging code assigned to the customer.  */  
   "AgingCreditCode":string,
      /**  Indicates if the record is inactive.  */  
   "Inactive":boolean,
      /**  Total number of open invoices  */  
   "TotOpenInvoices":number,
      /**  Total number of open orders  */  
   "TotOpenOrders":number,
      /**  Total number of open Payment Instruments  */  
   "TotOpenPI":number,
   "TotInvoiceCredit":number,
   "TotOrderCredit":number,
   "TotPICredit":number,
      /**  Total Credit based on CredInc flags  */  
   "TotOpenCredit":number,
      /**  Total Global Invoice Credit (including current company)  */  
   "TotGlbInvoiceCredit":number,
      /**  Total Global Order Credit (including current company)  */  
   "TotGlbOrderCredit":number,
      /**  Total Global Payment Instruments Credit (including current company)  */  
   "TotGlbPICredit":number,
      /**  Total Global Open Credit (based on GlbCredInc flags)  */  
   "TotGlbOpenCredit":number,
      /**  Indicates if the Customer is Global (master or linked)  */  
   "GlbFlag":boolean,
      /**  Indicates whether PI fields should be enabled or not  */  
   "PIFlag":boolean,
      /**  Apply credit hold status to orders  */  
   "ApplyHoldToOrders":boolean,
   "FxdTotOrders":number,
   "FxdTotPI":number,
   "FxdOrderCredit":number,
   "FxdPICredit":number,
   "FxdGlbOrdCredit":number,
   "FxdGlbPICredit":number,
      /**  Same value as GlobalCredIncOrd except if customer not global, value is no.  */  
   "DspGlobalCredIncOrd":boolean,
   "EDITest":boolean,
   "EDITranslator":string,
      /**  Own Credit Available  */  
   "NAOwnCreditAvail":number,
   "NAOwnCreditUsedDsp":number,
      /**  Available Parent?s Credit in National Accout  */  
   "NAParentCrdAvail":number,
   "NAPoolCreditUsed":number,
   "NASharedCreditUsedDsp":number,
      /**  Available credit from credit pools to be used by this customer in National account.  */  
   "NAPoolCrdAvail":number,
      /**  Customer?s credit available to be shared with his Children in National Account  */  
   "NAChildCrdAvail":number,
   "NAParentsCreditUsedDsp":number,
      /**  Global Shared Credit Available  */  
   "GlbNAChildCrdAvail":number,
   "GlbNAOwnCreditUsedDsp":number,
      /**  Global Parents Credit Available  */  
   "GlbNAParentCrdAvail":number,
   "GlbNAPoolCreditUsed":number,
   "GlbNAParentsCreditUsedDsp":number,
   "GlbNAPoolCrdAvail":number,
   "GlbNASharedCreditUsedDsp":number,
      /**  Global Own Credit Available  */  
   "GlbNAOwnCreditAvail":number,
      /**  National Credit data has been updated and recalculation is needed  */  
   "NACreditUpdated":boolean,
      /**  Total Credit available in the National Account  */  
   "NATotalCreditAvail":number,
   "NATotalCreditUsed":number,
      /**  Is the customer in the National Account of Credit Checking  */  
   "NACreditCust":boolean,
   "TotLCCredit":number,
      /**  Total open order value against LC/ECG  */  
   "TotLCOpenOrders":number,
      /**  Total cumulative invoices against LC/ECG  */  
   "TotLCCumInvoices":number,
      /**  Total invoice balance against LC/ECG  */  
   "TotLCInvoiceBal":number,
      /**  Total LC/ECG credit used.  */  
   "TotLCUsed":number,
      /**  Total number of open LC/ECG.  */  
   "TotOpenLC":number,
      /**  Total number of open orders against LC/ECG.  */  
   "TotOpenOrderLC":number,
      /**  Total number of open invoices against LC/ECG.  */  
   "TotOpenInvoicesLC":number,
      /**   Indicates ift the Collections was changed by the user but not posted yet.
Used in Peru localization.  */  
   "CollectionsChanged":boolean,
      /**   Indicates if Post Collections option in Actions menu is supposed to be visible.
Post Collections is used by Peru Localization  */  
   "CollectionsPostVisible":boolean,
   "BitFlag":number,
   "AgingCreditDescription":string,
   "GlobalCurrencyCurrDesc":string,
   "GlobalCurrencyDocumentDesc":string,
   "GlobalCurrencyCurrName":string,
   "GlobalCurrencyCurrSymbol":string,
   "GlobalCurrencyCurrencyID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CustomCrdPoolRow{
      /**  Company  */  
   "Company":string,
   "CustNum":number,
   "CrdPoolCode":string,
   "CreditUsed":number,
   "CreditAvailable":number,
      /**  Global Pool - shows if the pool belongs to Global National Account  */  
   "GlobalNA":boolean,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlbCustCredRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   "CustNum":number,
      /**  Company credit totals came from (not just owner of the global customer)  */  
   "ExtCompany":string,
   "ExtCompName":string,
      /**  Date the credit was last updated  */  
   "UpdateDate":string,
      /**  Open AR Credit in Global Currency  */  
   "DocARTotal":number,
      /**  Open Order Credit in Global Currency  */  
   "DocSOTotal":number,
      /**  Open PI Credit in Global Currency  */  
   "DocPITotal":number,
      /**  AR Credit in local companies base currency  */  
   "ARTotal":number,
      /**  SO Credit in local companies base currency  */  
   "SOTotal":number,
      /**  PI Credit in local companies base currency  */  
   "PITotal":number,
      /**  Holds connection and exchange rate error messages  */  
   "ErrorMsg":string,
      /**  This field holds the associated Global Customer number.  If this is the "parent" customer then it will match the CustNum field.  0 indicates that this is not a global customer at all  */  
   "GlbCustNum":number,
      /**  The Customer.CustNum value of the customer's parent company.  */  
   "ParentCustNum":number,
      /**  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  */  
   "GlobalCurrencyCode":string,
      /**  Total Number of Open Invoices  */  
   "TotalInvoices":number,
      /**  Total Number of Open Orders  */  
   "TotalOrders":number,
      /**  Total Number of open Payment Instruments  */  
   "TotalPayIns":number,
      /**  Parent's Credit used by this customer  */  
   "NAParentsCreditUsed":number,
      /**  Shared Credit used by children  */  
   "NASharedCreditUsed":number,
      /**  Own Credit used by himself  */  
   "NAOwnCreditUsed":number,
      /**  Global Parent's Credit used by this customer  */  
   "GlbNAParentsCreditUsed":number,
      /**  Shared Credit used by Global children  */  
   "GlbNASharedCreditUsed":number,
      /**  Pool Credit used  */  
   "NAPoolCreditUsed":number,
      /**  Global Credit Pool used  */  
   "GlbNAPoolCreditUsed":number,
      /**  Own Credit used by himself  */  
   "GlbNAOwnCreditUsed":number,
      /**  Allocated Credit exceed Credit Limit  */  
   "NAExceedLimit":number,
      /**  Allocated Credit exceed Global Credit Limit  */  
   "GlbNAExceedLimit":number,
      /**  AR Letter of Credit Credit in local companies base currency  */  
   "ARLOCTotal":number,
      /**  Open AR Letter of Credit Credit in Global Currency  */  
   "DocARLOCTotal":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Currency Code of the related record  */  
   "CurrencyCode":string,
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
      @param ipInCollections
      @param ds
   */  
export interface ChangeCollections_input{
   ipInCollections:boolean,
   ds:Erp_Tablesets_CreditManagerTableset[],
}

export interface ChangeCollections_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditManagerTableset,
}
}

   /** Required : 
      @param invoiceNum
      @param ds
   */  
export interface ChangeInvoiceCreditHoldByInvoiceNum_input{
      /**  Invoice Number being validated  */  
   invoiceNum:number,
   ds:Erp_Tablesets_InvcHeadTableset[],
}

export interface ChangeInvoiceCreditHoldByInvoiceNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvcHeadTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeInvoiceCreditHold_input{
   ds:Erp_Tablesets_InvcHeadTableset[],
}

export interface ChangeInvoiceCreditHold_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvcHeadTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeOrderCreditHold_input{
   ds:Erp_Tablesets_CMOrderHedTableset[],
}

export interface ChangeOrderCreditHold_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CMOrderHedTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface CheckCreditHold_input{
   ds:Erp_Tablesets_CreditManagerTableset[],
}

export interface CheckCreditHold_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditManagerTableset,
   vMessage:string,
}
}

   /** Required : 
      @param custNum
   */  
export interface DeleteByID_input{
   custNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_ARLOCAttchRow{
   Company:string,
   LCID:string,
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

export interface Erp_Tablesets_ARLOCRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Letter of Credit ID.  */  
   LCID:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Monetary value of the Letter of Credit.  */  
   LCValue:number,
      /**  Monetary value of the Letter of Credit. Report Currency 1.  */  
   Rpt1LCValue:number,
      /**  Monetary value of the Letter of Credit. Report Currency 2.  */  
   Rpt2LCValue:number,
      /**  Monetary value of the Letter of Credit. Report Currency 3.  */  
   Rpt3LCValue:number,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Exchange Rate  */  
   ExchangeRate:number,
      /**  Exchange Rate Lock flag  */  
   RateLocked:boolean,
      /**  Date that Letter of Credit was issued.  */  
   IssueDate:string,
      /**  Valid From date.  */  
   FromDate:string,
      /**  Valid To date.  */  
   ToDate:string,
      /**  Letter of Credit Description.  */  
   Description:string,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  Name of the Letter of Credit Guarantor.  */  
   GuarantorName:string,
      /**  Terms code  */  
   TermsCode:string,
      /**  Ship Complete flag  */  
   ShipComplete:boolean,
      /**  If true, no more commitments to this Letter of Credit.  */  
   Inactive:boolean,
      /**  Reason Letter of Credit was marked Inactive (entered by user).  */  
   InactiveReason:string,
      /**  If true, Letter of Credit is closed.  */  
   Closed:boolean,
      /**  Optional.  */  
   FOB:string,
      /**  Free form text.  */  
   IssuanceType:string,
      /**  Free form text.  */  
   PackListCopies:string,
      /**  Free form text.  */  
   PlaceOfLoading:string,
      /**  Free form text comments.  */  
   Comment:string,
      /**  Unique identifier.  */  
   RateGrpCode:string,
      /**  LC = Letter of Credit, ECG = Export Credit Guarantee  */  
   Type:string,
      /**  Monetary value of the Letter of Credit in bank's currency.  */  
   DocLCValue:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Delimited list of available bill to customers (CustID`CustomerName~CustID`CustomerName)  */  
   AvailBTCustList:string,
      /**  Bill To Customer ID  */  
   BTCustID:string,
   BaseCurrencyID:string,
   BaseCurrSymbol:string,
   CurrencySwitch:boolean,
      /**  if 'yes', Letter of Credit is used on at least one Sales Order or Invoice.  */  
   InUse:boolean,
   OpenLCCredit:number,
   OpenOrderValue:number,
   CumInvoices:number,
      /**  Cumulative Invoices  */  
   DocCumInvoices:number,
      /**  Invoices Balance  */  
   DocInvoiceBal:number,
      /**  Open LC Credit  */  
   DocOpenLCCredit:number,
      /**  Open Order Value  */  
   DocOpenOrderValue:number,
      /**  Paid Invoice Value  */  
   DocPaidInvoiceValue:number,
      /**  Total Order Value  */  
   DocTotalOrderValue:number,
      /**  Invoices Balance  */  
   InvoiceBal:number,
      /**  Paid Invoice Value  */  
   PaidInvoiceValue:number,
      /**  Total Order Value  */  
   TotalOrderValue:number,
      /**  Cumulative Invoices  */  
   Rpt1CumInvoices:number,
      /**  Cumulative Invoices  */  
   Rpt2CumInvoices:number,
      /**  Cumulative Invoices  */  
   Rpt3CumInvoices:number,
      /**  Invoices Balance  */  
   Rpt1InvoiceBal:number,
      /**  Invoices Balance  */  
   Rpt2InvoiceBal:number,
      /**  Invoices Balance  */  
   Rpt3InvoiceBal:number,
      /**  Open LC Credit  */  
   Rpt1OpenLCCredit:number,
      /**  Open LC Credit  */  
   Rpt2OpenLCCredit:number,
      /**  Open LC Credit  */  
   Rpt3OpenLCCredit:number,
      /**  Open Order Value  */  
   Rpt2OpenOrderValue:number,
      /**  Open Order Value  */  
   Rpt1OpenOrderValue:number,
      /**  Open Order Value  */  
   Rpt3OpenOrderValue:number,
      /**  Paid Invoice Value  */  
   Rpt1PaidInvoiceValue:number,
      /**  Paid Invoice Value  */  
   Rpt2PaidInvoiceValue:number,
      /**  Paid Invoice Value  */  
   Rpt3PaidInvoiceValue:number,
      /**  Total Order Value  */  
   Rpt1TotalOrderValue:number,
      /**  Total Order Value  */  
   Rpt2TotalOrderValue:number,
      /**  Total Order Value  */  
   Rpt3TotalOrderValue:number,
   TermsCodeDescription:string,
   Currency:string,
   UseExchangeRate:string,
      /**  Letter of Credit value in base currency converted from document currency using current (today) exchange rate  */  
   LCValueCurrent:number,
      /**  Open LOC Credit in base currency converted from Open LOC Credit in Document currency using current (today) exchange rate  */  
   OpenLCCreditCurrent:number,
      /**  Open Order Value in base currency converted from the amount in document currency using the current (now) exchange rate  */  
   OpenOrderValueCurrent:number,
   CumInvoicesCurrent:number,
      /**  Invoices Balance converted from document cuurency using current (today) exchange rate  */  
   InvoiceBalCurrent:number,
      /**  Paid Invoice Value in base currency converted from amount in doc currency using the current (now) exchange rate  */  
   PaidInvoiceValueCurrent:number,
      /**  Total Order value converted from amount in doc currency using current (now) exchange rate  */  
   TotalOrderValueCurrent:number,
      /**  Letter of Credit value in Rpt1 currency converted from document currency using current (today) exchange rate  */  
   Rpt1LCValueCurrent:number,
      /**  Letter of Credit value in Rpt2 currency converted from document currency using current (today) exchange rate  */  
   Rpt2LCValueCurrent:number,
      /**  Letter of Credit value in Rpt3 currency converted from document currency using current (today) exchange rate  */  
   Rpt3LCValueCurrent:number,
   BitFlag:number,
   BaseCurrCurrSymbol:string,
   BaseCurrCurrName:string,
   BaseCurrDocumentDesc:string,
   BaseCurrCurrencyID:string,
   BaseCurrCurrDesc:string,
   BTCustNumBTName:string,
   BTCustNumCustID:string,
   BTCustNumName:string,
   CurrencyCodeBaseCurr:boolean,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrencyID:string,
   CustomerCustID:string,
   CustomerName:string,
   FOBDescription:string,
   ReasonDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARLOCTableset{
   ARLOC:Erp_Tablesets_ARLOCRow[],
   ARLOCAttch:Erp_Tablesets_ARLOCAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_ARPNHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Transaction Amount  */  
   TranAmt:number,
      /**  Applied Amount  */  
   AppliedAmt:number,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Bank Amount  */  
   BankAmount:number,
      /**  Bank Slip Number of the promissory note.  */  
   BankSlip:string,
      /**  Base Amount  */  
   BaseAmount:number,
      /**  When creating a new CashBdtl, the next available # is assigned by the system.  The system generates a number by finding the last CashBdtl of a cashbhed and uses its CashBookLine + 1. Not directly entered by the user.  */  
   CashbookLine:number,
      /**  Company Bank Account ID  */  
   CompBankAcctID:string,
      /**  Currency Code  */  
   CurrencyCode:string,
      /**  Customer Bank Account ID  */  
   CustBankAcctID:string,
      /**  Customer ID  */  
   CustID:string,
      /**  Customer Number  */  
   CustNum:number,
      /**  Description  */  
   Description:string,
      /**  Discount Amount. Base Currency.  */  
   DiscountAmt:number,
      /**  Applied Amount. Document Currency.  */  
   DocAppliedAmt:number,
      /**  Unapplied Amount. Document Currency.  */  
   DocUnAppliedAmt:number,
      /**  Tax Amount. Document Currency.  */  
   DocTaxAmt:number,
      /**  Transaction Amount. Document Currency.  */  
   DocTranAmt:number,
      /**  Withholding Amount. Document Currency.  */  
   DocWithholdAmt:number,
      /**  Exchange Rate  */  
   ExchangeRate:number,
      /**  Get Default Tax ID's flag.  */  
   GetDfltTaxIds:boolean,
      /**  Posted to GL flag  */  
   GLPosted:boolean,
      /**  Legal Number  */  
   LegalNumber:string,
      /**  Paid flag  */  
   Paid:boolean,
      /**  Posted flag  */  
   Posted:boolean,
      /**  Process Card  */  
   ProcessCard:string,
      /**  Rate Group code  */  
   RateGrpCode:string,
      /**  Recalculated before posting.  */  
   RecalcBeforePost:boolean,
      /**  Applied Amount. Report Currency 1.  */  
   Rpt1AppliedAmt:number,
      /**  Tax Amount. Report Currency 1.  */  
   Rpt1TaxAmt:number,
      /**  Transaction Amount. Report Currency 1.  */  
   Rpt1TranAmt:number,
      /**  Unapplied Amount. Report Currency 1.  */  
   Rpt1UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 1.  */  
   Rpt1WithholdAmt:number,
      /**  Applied Amount. Report Currency 2.  */  
   Rpt2AppliedAmt:number,
      /**  Tax Amount. Report Currency 2.  */  
   Rpt2TaxAmt:number,
      /**  Transaction Amount. Report Currency 2.  */  
   Rpt2TranAmt:number,
      /**  Unapplied Amount. Report Currency 2.  */  
   Rpt2UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 2.  */  
   Rpt2WithholdAmt:number,
      /**  Applied Amount. Report Currency 3.  */  
   Rpt3AppliedAmt:number,
      /**  Tax Amount. Report Currency 3.  */  
   Rpt3TaxAmt:number,
      /**  Transaction Amount. Report Currency 3.  */  
   Rpt3TranAmt:number,
      /**  Unapplied Amount. Report Currency 3.  */  
   Rpt3UnappliedAmt:number,
      /**  Withholding Amount. Report Currency 3.  */  
   Rpt3WithholdAmt:number,
      /**  Signed flag  */  
   Signed:boolean,
      /**  Tax Amount. Base Currency.  */  
   TaxAmt:number,
      /**  Tax Liability  */  
   TaxRegionCode:string,
      /**  Total AR Amount  */  
   TotalARAmt:number,
      /**  Transaction Date  */  
   TransDate:string,
      /**  Unapplied Amount. Base Currency.  */  
   UnappliedAmt:number,
      /**  Voided Flag  */  
   Voided:boolean,
      /**  Withholding Amount. Base Currency.  */  
   WithholdAmt:number,
      /**  Company Name  */  
   CompanyName:string,
      /**  First company address line.  */  
   CompanyAddr1:string,
      /**  Second company address line.  */  
   CompanyAddr2:string,
      /**  Third company address line.  */  
   CompanyAddr3:string,
      /**  Company City portion of the address.  */  
   CompanyCity:string,
      /**  Company State portion of the address.  */  
   CompanyState:string,
      /**  Company Postal Code or Zip Code portion of the address.  */  
   CompanyPostalCode:string,
      /**  Company Country portion of the address.  */  
   CompanyCountry:string,
      /**  Company Name  */  
   CustomerName:string,
      /**  First customer address line.  */  
   CustomerAddr1:string,
      /**  Second customer address line.  */  
   CustomerAddr2:string,
      /**  Third customer address line.  */  
   CustomerAddr3:string,
      /**  Customer Stateportion of the address.  */  
   CustomerState:string,
      /**  Customer City portion of the address.  */  
   CustomerPostalCode:string,
      /**  Customer Postal Code or Zip Code portion of the address.  */  
   CustomerCity:string,
      /**  Before allowing transaction entry the user establishes a "Group ID". All transactions belong to a group. This current GroupID is assigned by the user.  Once created, it cannot be changed.  The Group ID is used to Selectively print and post the transactions.  */  
   GroupID:string,
      /**  An integer automatically assigned by the system using the database sequence called "CashHeadSeq". Which along with company and BatchID creates a unique key for the record. This is for internal control only the user never needs to reference.  */  
   HeadNum:number,
      /**  Reference to  invchead  */  
   InvoiceNum:number,
      /**  AR Payment Instrument ID  */  
   ARPromNoteID:string,
      /**  Fiscal Year. This is not entered by the user on each record. Duplicated in from the CashGroup.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashGroup.FiscalPeriod.  */  
   FiscalPeriod:number,
      /**  The unique identifier of the fiscal calendar.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Transaction Type  */  
   TranType:string,
      /**  Sent Flag  */  
   Sent:boolean,
      /**  Type  */  
   Type:string,
      /**  Issue Date  */  
   IssueDate:string,
      /**  Due date of the promissory note.  */  
   DueDate:string,
      /**  Bank/Branch Code for company's bank.  */  
   CompBankBranchCode:string,
      /**  IBANCode for company's bank.  */  
   CompIBANCode:string,
      /**  Bank/Branch Code for customer's bank.  */  
   CustBankBranchCode:string,
      /**  IBAN Code for customer's bank.  */  
   CustIBANCode:string,
      /**  Indicates whether Payment Instrument was auto-generated from AR Invoice Entry.  */  
   AutoGenerated:boolean,
      /**  If true, indicates that Customer is flagged as Direct Deposit. Comes from field Customer.DirectDeposit.  */  
   DirectDeposit:boolean,
      /**  Amount that the bank cleared the payment instrument for.  */  
   ClearedAmt:number,
      /**  Date that the payment instrument was cleared in the system (System Set).  */  
   ClearedDate:string,
      /**  Indicates that the payment instrument is in the process of being cleared.  When the Bank Statement is posted all Pending Transactions and Checks are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPending:boolean,
      /**  Person who cleared the payment instrument (System Set).  */  
   ClearedPerson:string,
      /**  Indicates the Payment Instrument's cleared status.  When the Bank Statement is posted all Pending Transactions and Payment Instruments are flagged as Cleared and any variances are posted to the Bank Account's Cash and Cleared Variance Accounts.  */  
   ClearedPI:boolean,
      /**  End Date of the Statement that the payment instrument was cleared on.  */  
   ClearedStmtEndDate:string,
      /**  Time that the payment instrument was cleared in the system - in HH:MM:SS format (System Set).  */  
   ClearedTime:string,
      /**  Amount that the bank cleared the check for.(Vendors Currency)  */  
   DocClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2ClearedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3ClearedAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Customer's country code  */  
   CustCountryCode:number,
      /**  Customer country portion of the address.  */  
   CustomerCountry:string,
      /**  Promissory Note Status  */  
   PIStatus:string,
      /**  Current Group  */  
   CurGroupID:string,
      /**  Stage  */  
   PIStage:string,
      /**  Reason to change Company or Customer information  */  
   ChgComment:string,
      /**  Hold from Application reason  */  
   HoldReason:string,
      /**  Lock Exchange Rate  */  
   LockRate:boolean,
      /**  Reference to reversed PI  */  
   ReferseRef:number,
      /**  Reverse Date  */  
   ReverseDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  BankClearedAmt  */  
   BankClearedAmt:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  TotalBankFee  */  
   TotalBankFee:number,
      /**  DocTotalBankFee  */  
   DocTotalBankFee:number,
      /**  Rpt1TotalBankFee  */  
   Rpt1TotalBankFee:number,
      /**  Rpt2TotalBankFee  */  
   Rpt2TotalBankFee:number,
      /**  Rpt3TotalBankFee  */  
   Rpt3TotalBankFee:number,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  Issuer Name  */  
   IssuerName:string,
      /**  Signed By  */  
   SignedBy:string,
      /**  Signed Date  */  
   SignedDate:string,
      /**  Signee Address 1  */  
   SigneeAddr1:string,
      /**  Signee Address 2  */  
   SigneeAddr2:string,
      /**  Signee Address 3  */  
   SigneeAddr3:string,
      /**  Signee City  */  
   SigneeCity:string,
      /**  Signee State  */  
   SigneeState:string,
      /**  Signee Postal Code  */  
   SigneeZip:string,
      /**  Signee Country Number  */  
   SigneeCountryNum:number,
      /**  Signee Phone  */  
   SigneePhoneNum:string,
      /**  Signee Email Address  */  
   SigneeEMailAddress:string,
      /**  Signee Comment  */  
   SigneeComment:string,
      /**  DiscountChargeAmt  */  
   DiscountChargeAmt:number,
      /**  DocDiscountChargeAmt  */  
   DocDiscountChargeAmt:number,
      /**  Rpt1DiscountChargeAmt  */  
   Rpt1DiscountChargeAmt:number,
      /**  Rpt2DiscountChargeAmt  */  
   Rpt2DiscountChargeAmt:number,
      /**  Rpt3DiscountChargeAmt  */  
   Rpt3DiscountChargeAmt:number,
      /**  Signee Bank Name  */  
   SigneeBankName:string,
      /**  Signee Bank Account Number  */  
   SigneeBankAcct:string,
      /**  Signee Bank Identifier  */  
   SigneeBankIdentifier:string,
      /**  Signee IBAN Code  */  
   SigneeIBANCode:string,
      /**  Signee Bank BranchCode  */  
   SigneeBankBranchCode:string,
      /**  DiscountCashDate  */  
   DiscountCashDate:string,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
   ApplyDate:string,
   BankCurrencyCode:string,
   BankCurrSymbol:string,
   BankRecGainLoss:number,
      /**  Indicates if rate was calculates from TranAmt field instead of CurrExRate table  */  
   calcRate:boolean,
   CompanyBankAcct:string,
   CompanyBankIdentifier:string,
   CompanyBankName:string,
   CompBankBranchCodeDesc:string,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
   CurrencyDesc:string,
   CurrencySwitch:boolean,
   CustBankBranchCodeDesc:string,
   CustomerBankAcct:string,
   CustomerBankIdentifier:string,
   CustomerBankName:string,
   DisableBankAcctIDPI:boolean,
      /**   The flag to indicate if BankClearedAmt is not available to make changes.
(If Bank currency equals transaction currency this flag is true)  */  
   DisableBankAmt:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocBankRecGainLoss:number,
   DocDiscount:number,
   DocDiscountAmt:number,
   DocGainLossReal:number,
   DocGainLossUnreal:number,
   DocReceipt:number,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
   FullyPaid:boolean,
   GainLossReal:number,
   GainLossUnreal:number,
      /**  Indicates if a legal number configuration exists for miscellaneous shipments  */  
   HasLegNumCnfg:boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumMessage:string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   PIStatusDesc:string,
      /**  like PIType.Initiation  */  
   PITypeInitiation:string,
   Receipt:number,
   RevalueDate:string,
   Rpt1BankRecGainLoss:number,
   Rpt1DiscountAmt:number,
   Rpt1GainLossReal:number,
   Rpt1GainLossUnreal:number,
   Rpt1Receipt:number,
   Rpt1TranTaxAmt:number,
   Rpt2BankRecGainLoss:number,
   Rpt2DiscountAmt:number,
   Rpt2GainLossReal:number,
   Rpt2GainLossUnreal:number,
   Rpt2Receipt:number,
   Rpt2TranTaxAmt:number,
   Rpt3BankRecGainLoss:number,
   Rpt3DiscountAmt:number,
   Rpt3GainLossReal:number,
   Rpt3GainLossUnreal:number,
   Rpt3Receipt:number,
   Rpt3TranTaxAmt:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   StatusChgLegalNum:string,
   StatusChgTranDocType:string,
   TermsDesc:string,
   TotalCashReceived:number,
   TotalRoundDiff:number,
   TranTaxAmt:number,
   TypeDesc:string,
   XRateLabel:string,
   BankTotalAmount:number,
   BaseCurrencyCode:string,
   BaseCurrencyDesc:string,
   BaseCurrSymbol:string,
   BillToName:string,
   DocDiscountedAmt:number,
      /**  for kinetic purposes  */  
   ARPNDtlExists:boolean,
      /**  for kinetic purposes  */  
   ARPNDtlInvoicePosted:boolean,
   BitFlag:number,
   BankAcctDescription:string,
   BankAcctBankName:string,
   CashbookLineDescription:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CustNumInactive:boolean,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   PIStatusStatusDesc:string,
   PITypeDescription:string,
   RateGrpDescription:string,
   TaxRegionCodeDescription:string,
   TranDocTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ARPNHeadTableset{
   ARPNHead:Erp_Tablesets_ARPNHeadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_AllocDepositTrkRow{
      /**  Company  */  
   Company:string,
   CurrencyCode:string,
      /**  "0 - Prepaid Invoiced Deposit   1 - Cash Deposit 2 - Reverse Cash Deposit"  */  
   PrePayType:number,
      /**  Deposit Invoice Number  */  
   DepInvoiceNum:number,
      /**  Group ID of deposit payment  */  
   DepGroupID:string,
      /**  Identification of Deposit Payment  */  
   DepHeadNum:number,
      /**  Apply Date of Deposit Invoice  */  
   DepApplyDate:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  "0 - Unrecognized               1 - Partial Recognized 2 - Full Recognized"  */  
   PrePayStatus:number,
      /**  Allocated Amount  */  
   DocAllocAmt:number,
   AllocAmt:number,
   Rpt1AllocAmt:number,
   Rpt2AllocAmt:number,
   Rpt3AllocAmt:number,
      /**  Allocated Balance  */  
   DocAllocBal:number,
   AllocBal:number,
   Rpt1AllocBal:number,
   Rpt2AllocBal:number,
   Rpt3AllocBal:number,
      /**  Total Tax Amount of Deposit  */  
   DocTaxAmt:number,
   TaxAmt:number,
   Rpt1TaxAmt:number,
   Rpt2TaxAmt:number,
   Rpt3TaxAmt:number,
      /**  Remaining Tax Amount of Deposit  */  
   DocAllocTaxBal:number,
   AllocTaxBal:number,
   Rpt1AllocTaxBal:number,
   Rpt2AllocTaxBal:number,
   Rpt3AllocTaxBal:number,
      /**  Shipment Invoice Number for which this Deposit is allocated  */  
   InvoiceNum:number,
   DepCheckRef:string,
      /**  Currency switch used to determine what currency to display amounts in.  */  
   CurrencySwitch:boolean,
      /**  Original Amt  */  
   DocOriginalAmt:number,
   OriginalAmt:number,
   Rpt1OriginalAmt:number,
   Rpt2OriginalAmt:number,
   Rpt3OriginalAmt:number,
      /**  Original Tax Amt  */  
   DocOriginalTaxAmt:number,
   OriginalTaxAmt:number,
   Rpt1OriginalTaxAmt:number,
   Rpt2OriginalTaxAmt:number,
   Rpt3OriginalTaxAmt:number,
   CustNum:number,
   LegalNumber:string,
   Reference:string,
      /**  IsDepCM to distinguish between Deposit Billing Invoices and Deposit Billing Credit Memos  */  
   IsDepCM:boolean,
   DepInvoiceDate:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_AllocDepositsTableset{
   AllocDepositTrk:Erp_Tablesets_AllocDepositTrkRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CMCustomerListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  The full name of the customer.  */  
   Name:string,
      /**  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  */  
   CreditHold:boolean,
      /**  Contains the default FOB.FOB value of the FOB policy for this  customers orders.  Default used in sales order entry for this customer.  */  
   DefaultFOB:string,
      /**  Determines whether or not Open Sales Orders are to be included in the credit limit checking process for the customer. This checkbox will also include open service contracts.  */  
   CreditIncludeOrders:boolean,
      /**  Date on which the next credit review should be conducted for the customer.  */  
   CreditReviewDate:string,
      /**  Date on which the customer was last placed on credit hold. This field is maintained by the system.  */  
   CreditHoldDate:string,
      /**  Indicates how the customer was placed on credit hold.  Valid values are "MANUAL", "INVOICES", "ORDERS", and "CONTRACTS".  "MANUAL" means that the user placed the customer on hold.  INVOICES means that the customer's open A/R balance exceeded the credit limit.  ORDERS means that the sum of the open A/R and the open orders exceeded the credit limit. This field is maintained by the system.  */  
   CreditHoldSource:string,
      /**  The UserFile.DCDUSERID value of the user that last cleared the customer's credit hold. This field is maintained by the system.  */  
   CreditClearUserID:string,
      /**  The date that the user last cleared the customer's credit hold. This field is maintained by the system.  */  
   CreditClearDate:string,
      /**  The time that the user last cleared the customer's credit hold in HH:MM:SS format. This field is maintained by the system.  */  
   CreditClearTime:string,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   EDICode:string,
      /**  The Customer.CustNum value of the customer's parent company.  */  
   ParentCustNum:number,
      /**  Determines whether or not this customer is an inter-company customer.  */  
   ICCust:boolean,
      /**  BillFrequency  */  
   BillFrequency:string,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   CreditIncludePI:boolean,
      /**  Determines whether or not this customer is shared between more than one company.  */  
   GlobalCust:boolean,
      /**  Indicates if this customer participates in the Inter-Company Trading.  */  
   ICTrader:boolean,
      /**  Determines whether or not Open Orders are to be included in the global credit limit checking process. This checkbox will also include open service contracts.  */  
   GlobalCredIncOrd:boolean,
      /**  Indicates whether or not Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking process.  */  
   GlobalCredIncPI:boolean,
      /**  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  */  
   GlobalCurrencyCode:string,
      /**  Determines whether or not the customer has been placed into a "Global Credit Hold" status.  Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  */  
   GlobalCreditHold:string,
      /**  Determines whether or not this customer record will receive global updates.  */  
   GlobalLock:boolean,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit.  A credit limit of zero is considered as having unlimited credit.  */  
   CreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  */  
   CustPILimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit Limit.  A credit limit of zero is considered as having unlimited credit.  */  
   GlobalCreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  */  
   GlobalPILimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  */  
   DocGlobalCreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  */  
   DocGlobalPILimit:number,
      /**  allow use Parent Credit in National Account  */  
   NAParentCreditIsUsed:boolean,
      /**  allow/deny to a customer share his own credit with other customers within the National account  */  
   NACreditIsShare:boolean,
      /**  define what type of credit will be used first when the customer  */  
   NACreditPreferenceList:string,
      /**  Max Percent of Parent Credit to Use  */  
   NAParentCreditPrc:number,
      /**  Percentage of the customer credit shared to his Children.  */  
   NACreditSharedPrc:number,
      /**  allow use Global Parent Credit in National Account  */  
   GlbNAParentCreditIsUsed:boolean,
      /**  allow/deny to a customer share his own credit with other customers within the Global National account  */  
   GlbNACreditIsShare:boolean,
      /**  Max Percent of Global Parent Credit to Use  */  
   GlbNAParentCreditPrc:number,
      /**  Percentage of the customer credit shared to his Global Children.  */  
   GlbNACreditSharedPrc:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Total number of open invoices  */  
   TotOpenInvoices:number,
      /**  Total number of open orders  */  
   TotOpenOrders:number,
      /**  Total number of open Payment Instruments  */  
   TotOpenPI:number,
   TotInvoiceCredit:number,
   TotOrderCredit:number,
   TotPICredit:number,
      /**  Total Credit based on CredInc flags  */  
   TotOpenCredit:number,
      /**  Total Global Invoice Credit (including current company)  */  
   TotGlbInvoiceCredit:number,
      /**  Total Global Order Credit (including current company)  */  
   TotGlbOrderCredit:number,
      /**  Total Global Payment Instruments Credit (including current company)  */  
   TotGlbPICredit:number,
      /**  Total Global Open Credit (based on GlbCredInc flags)  */  
   TotGlbOpenCredit:number,
      /**  Indicates if the Customer is Global (master or linked)  */  
   GlbFlag:boolean,
      /**  Indicates whether PI fields should be enabled or not  */  
   PIFlag:boolean,
      /**  Apply credit hold status to orders  */  
   ApplyHoldToOrders:boolean,
   FxdTotOrders:number,
   FxdTotPI:number,
   FxdOrderCredit:number,
   FxdPICredit:number,
   FxdGlbOrdCredit:number,
   FxdGlbPICredit:number,
      /**  Same value as GlobalCredIncOrd except if customer not global, value is no.  */  
   DspGlobalCredIncOrd:boolean,
   EDITest:boolean,
   EDITranslator:string,
      /**  Own Credit Available  */  
   NAOwnCreditAvail:number,
   NAOwnCreditUsedDsp:number,
      /**  Available Parent?s Credit in National Accout  */  
   NAParentCrdAvail:number,
   NAPoolCreditUsed:number,
   NASharedCreditUsedDsp:number,
      /**  Available credit from credit pools to be used by this customer in National account.  */  
   NAPoolCrdAvail:number,
      /**  Customer?s credit available to be shared with his Children in National Account  */  
   NAChildCrdAvail:number,
   NAParentsCreditUsedDsp:number,
      /**  Global Shared Credit Available  */  
   GlbNAChildCrdAvail:number,
   GlbNAOwnCreditUsedDsp:number,
      /**  Global Parents Credit Available  */  
   GlbNAParentCrdAvail:number,
   GlbNAPoolCreditUsed:number,
   GlbNAParentsCreditUsedDsp:number,
   GlbNAPoolCrdAvail:number,
   GlbNASharedCreditUsedDsp:number,
      /**  Global Own Credit Available  */  
   GlbNAOwnCreditAvail:number,
      /**  National Credit data has been updated and recalculation is needed  */  
   NACreditUpdated:boolean,
      /**  Total Credit available in the National Account  */  
   NATotalCreditAvail:number,
   NATotalCreditUsed:number,
      /**  Is the customer in the National Account of Credit Checking  */  
   NACreditCust:boolean,
   TotLCCredit:number,
      /**  Total open order value against LC/ECG  */  
   TotLCOpenOrders:number,
      /**  Total cumulative invoices against LC/ECG  */  
   TotLCCumInvoices:number,
      /**  Total invoice balance against LC/ECG  */  
   TotLCInvoiceBal:number,
      /**  Total LC/ECG credit used.  */  
   TotLCUsed:number,
      /**  Total number of open LC/ECG.  */  
   TotOpenLC:number,
      /**  Total number of open orders against LC/ECG.  */  
   TotOpenOrderLC:number,
      /**  Total number of open invoices against LC/ECG.  */  
   TotOpenInvoicesLC:number,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   GlobalCurrencyCurrencyID:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   GlobalCurrencyDocumentDesc:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   GlobalCurrencyCurrName:string,
      /**  Description of the currency  */  
   GlobalCurrencyCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   GlobalCurrencyCurrSymbol:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CMCustomerListTableset{
   CMCustomerList:Erp_Tablesets_CMCustomerListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CMCustomerRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  */  
   CustID:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  The full name of the customer.  */  
   Name:string,
      /**  Indicates if customer has been placed into a "Credit Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  */  
   CreditHold:boolean,
      /**  Contains the default FOB.FOB value of the FOB policy for this  customers orders.  Default used in sales order entry for this customer.  */  
   DefaultFOB:string,
      /**  Determines whether or not Open Sales Orders are to be included in the credit limit checking process for the customer. This checkbox will also include open service contracts.  */  
   CreditIncludeOrders:boolean,
      /**  Date on which the next credit review should be conducted for the customer.  */  
   CreditReviewDate:string,
      /**  Date on which the customer was last placed on credit hold. This field is maintained by the system.  */  
   CreditHoldDate:string,
      /**  Indicates how the customer was placed on credit hold.  Valid values are "MANUAL", "INVOICES", "ORDERS", and "CONTRACTS".  "MANUAL" means that the user placed the customer on hold.  INVOICES means that the customer's open A/R balance exceeded the credit limit.  ORDERS means that the sum of the open A/R and the open orders exceeded the credit limit. This field is maintained by the system.  */  
   CreditHoldSource:string,
      /**  The UserFile.DCDUSERID value of the user that last cleared the customer's credit hold. This field is maintained by the system.  */  
   CreditClearUserID:string,
      /**  The date that the user last cleared the customer's credit hold. This field is maintained by the system.  */  
   CreditClearDate:string,
      /**  The time that the user last cleared the customer's credit hold in HH:MM:SS format. This field is maintained by the system.  */  
   CreditClearTime:string,
      /**  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  */  
   EDICode:string,
      /**  The Customer.CustNum value of the customer's parent company.  */  
   ParentCustNum:number,
      /**  Determines whether or not this customer is an inter-company customer.  */  
   ICCust:boolean,
      /**  BillFrequency  */  
   BillFrequency:string,
      /**  Indicates that Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking.  */  
   CreditIncludePI:boolean,
      /**  Determines whether or not this customer is shared between more than one company.  */  
   GlobalCust:boolean,
      /**  Indicates if this customer participates in the Inter-Company Trading.  */  
   ICTrader:boolean,
      /**  Determines whether or not Open Orders are to be included in the global credit limit checking process. This checkbox will also include open service contracts.  */  
   GlobalCredIncOrd:boolean,
      /**  Indicates whether or not Payment Instruments (bank drafts, post dated checks) are to be included in the credit limit checking process.  */  
   GlobalCredIncPI:boolean,
      /**  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  */  
   GlobalCurrencyCode:string,
      /**  Determines whether or not the customer has been placed into a "Global Credit Hold" status.  Any non-blank value will trigger notification of this condition in Order Entry and Shipping.  */  
   GlobalCreditHold:string,
      /**  Determines whether or not this customer record will receive global updates.  */  
   GlobalLock:boolean,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit.  A credit limit of zero is considered as having unlimited credit.  */  
   CreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  */  
   CustPILimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit Limit.  A credit limit of zero is considered as having unlimited credit.  */  
   GlobalCreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a credit limit for payment instruments such as post dated checks or bank drafts.  A credit limit of zero is considered as having unlimited credit.  */  
   GlobalPILimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Global Credit limit.  Credit limit of zero is considered as having unlimited credit. Stored in Global Currency.  */  
   DocGlobalCreditLimit:number,
      /**  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit. Stored in Global currency  */  
   DocGlobalPILimit:number,
      /**  allow use Parent Credit in National Account  */  
   NAParentCreditIsUsed:boolean,
      /**  allow/deny to a customer share his own credit with other customers within the National account  */  
   NACreditIsShare:boolean,
      /**  define what type of credit will be used first when the customer  */  
   NACreditPreferenceList:string,
      /**  Max Percent of Parent Credit to Use  */  
   NAParentCreditPrc:number,
      /**  Percentage of the customer credit shared to his Children.  */  
   NACreditSharedPrc:number,
      /**  allow use Global Parent Credit in National Account  */  
   GlbNAParentCreditIsUsed:boolean,
      /**  allow/deny to a customer share his own credit with other customers within the Global National account  */  
   GlbNACreditIsShare:boolean,
      /**  Max Percent of Global Parent Credit to Use  */  
   GlbNAParentCreditPrc:number,
      /**  Percentage of the customer credit shared to his Global Children.  */  
   GlbNACreditSharedPrc:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  In Collections  */  
   Collections:boolean,
      /**  CollectionsDate  */  
   CollectionsDate:string,
      /**  Date Collection Posted  */  
   DateCollectionPosted:string,
      /**  Indicates if customer has been placed into an "Aging Hold" status. A "yes" will trigger notification of this condition in Order Entry and Shipping.  */  
   AgingCreditHold:boolean,
      /**  Date on which the customer was last placed on aging hold. This field is maintained by the system.  */  
   AgingCreditHoldDate:string,
      /**  Indicates how the customer was placed on aging hold.  Valid values are "MANUAL" and "PROCESS".  "MANUAL" means that the user placed the customer on hold.  “PROCESS” means that the Mass Credit Information Update Process places the customer on aging hold.  This field is maintained by the system.  */  
   AgingCreditHoldSource:string,
      /**  The UserFile.DCDUSERID value of the user that last cleared the customer's aging hold. This field is maintained by the system.  */  
   AgingCreditClearUserID:string,
      /**  The date that the user last cleared the customer's aging hold. This field is maintained by the system.  */  
   AgingCreditClearDate:string,
      /**  The aging code assigned to the customer.  */  
   AgingCreditCode:string,
      /**  Indicates if the record is inactive.  */  
   Inactive:boolean,
      /**  Total number of open invoices  */  
   TotOpenInvoices:number,
      /**  Total number of open orders  */  
   TotOpenOrders:number,
      /**  Total number of open Payment Instruments  */  
   TotOpenPI:number,
   TotInvoiceCredit:number,
   TotOrderCredit:number,
   TotPICredit:number,
      /**  Total Credit based on CredInc flags  */  
   TotOpenCredit:number,
      /**  Total Global Invoice Credit (including current company)  */  
   TotGlbInvoiceCredit:number,
      /**  Total Global Order Credit (including current company)  */  
   TotGlbOrderCredit:number,
      /**  Total Global Payment Instruments Credit (including current company)  */  
   TotGlbPICredit:number,
      /**  Total Global Open Credit (based on GlbCredInc flags)  */  
   TotGlbOpenCredit:number,
      /**  Indicates if the Customer is Global (master or linked)  */  
   GlbFlag:boolean,
      /**  Indicates whether PI fields should be enabled or not  */  
   PIFlag:boolean,
      /**  Apply credit hold status to orders  */  
   ApplyHoldToOrders:boolean,
   FxdTotOrders:number,
   FxdTotPI:number,
   FxdOrderCredit:number,
   FxdPICredit:number,
   FxdGlbOrdCredit:number,
   FxdGlbPICredit:number,
      /**  Same value as GlobalCredIncOrd except if customer not global, value is no.  */  
   DspGlobalCredIncOrd:boolean,
   EDITest:boolean,
   EDITranslator:string,
      /**  Own Credit Available  */  
   NAOwnCreditAvail:number,
   NAOwnCreditUsedDsp:number,
      /**  Available Parent?s Credit in National Accout  */  
   NAParentCrdAvail:number,
   NAPoolCreditUsed:number,
   NASharedCreditUsedDsp:number,
      /**  Available credit from credit pools to be used by this customer in National account.  */  
   NAPoolCrdAvail:number,
      /**  Customer?s credit available to be shared with his Children in National Account  */  
   NAChildCrdAvail:number,
   NAParentsCreditUsedDsp:number,
      /**  Global Shared Credit Available  */  
   GlbNAChildCrdAvail:number,
   GlbNAOwnCreditUsedDsp:number,
      /**  Global Parents Credit Available  */  
   GlbNAParentCrdAvail:number,
   GlbNAPoolCreditUsed:number,
   GlbNAParentsCreditUsedDsp:number,
   GlbNAPoolCrdAvail:number,
   GlbNASharedCreditUsedDsp:number,
      /**  Global Own Credit Available  */  
   GlbNAOwnCreditAvail:number,
      /**  National Credit data has been updated and recalculation is needed  */  
   NACreditUpdated:boolean,
      /**  Total Credit available in the National Account  */  
   NATotalCreditAvail:number,
   NATotalCreditUsed:number,
      /**  Is the customer in the National Account of Credit Checking  */  
   NACreditCust:boolean,
   TotLCCredit:number,
      /**  Total open order value against LC/ECG  */  
   TotLCOpenOrders:number,
      /**  Total cumulative invoices against LC/ECG  */  
   TotLCCumInvoices:number,
      /**  Total invoice balance against LC/ECG  */  
   TotLCInvoiceBal:number,
      /**  Total LC/ECG credit used.  */  
   TotLCUsed:number,
      /**  Total number of open LC/ECG.  */  
   TotOpenLC:number,
      /**  Total number of open orders against LC/ECG.  */  
   TotOpenOrderLC:number,
      /**  Total number of open invoices against LC/ECG.  */  
   TotOpenInvoicesLC:number,
      /**   Indicates ift the Collections was changed by the user but not posted yet.
Used in Peru localization.  */  
   CollectionsChanged:boolean,
      /**   Indicates if Post Collections option in Actions menu is supposed to be visible.
Post Collections is used by Peru Localization  */  
   CollectionsPostVisible:boolean,
   BitFlag:number,
   AgingCreditDescription:string,
   GlobalCurrencyCurrDesc:string,
   GlobalCurrencyDocumentDesc:string,
   GlobalCurrencyCurrName:string,
   GlobalCurrencyCurrSymbol:string,
   GlobalCurrencyCurrencyID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CMOrderHedRow{
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   OrderNum:number,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  */  
   PONum:string,
      /**   This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.

On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  */  
   RequestDate:string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   OrderDate:string,
      /**  Credit Hold flag to indicate when to override credit and set limit.  */  
   CreditHold:boolean,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of ORDERHED.CUSTNUM use the CUSTOMER.TERMS

field as the default.  */  
   TermsCode:string,
      /**  Order Total  */  
   OrderTotal:number,
      /**  Open Order Balance  */  
   OrderBalance:number,
      /**  Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   DepositBal:number,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   NeedByDate:string,
      /**  Indicates that the credit hold was overridden for this order.  */  
   CreditOverride:boolean,
      /**  The authorized maximum dollar limit that an order for a credit held customer is approved for.  Initially defaulted to the current order amount when the order is credit hold overridden.  The order amount is calculated by using line information only (i.e. extended amount and discounts) - deposits, advance billings, shipments and miscellaneous charges are NOT considered.  */  
   CreditOverrideLimit:number,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalCharges:number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalMisc:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalDiscount:number,
      /**  Total Advance Billable Balance  */  
   TotalAdvBill:number,
      /**   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalTax:number,
      /**  Total amount of order that has been invoiced  */  
   TotalInvoiced:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  OrderOpenCredit  */  
   OrderOpenCredit:number,
   CustomerCustID:string,
   CustomerBTName:string,
   CustomerName:string,
   ShipViaWebDesc:string,
   ShipViaDescription:string,
   TermsDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CMOrderHedTableset{
   CMOrderHed:Erp_Tablesets_CMOrderHedRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CashDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The data entry "Group" to which is transaction is assigned. This is not user maintainable. It is duplicated from the corresponding CashHead record.  */  
   GroupID:string,
      /**  The foreign key that relates this detail record to a CashHead record. Duplicated from CashHead.HeadNum when record is created. Not applicable to user interface.  */  
   HeadNum:number,
      /**  The open A/R invoice # that the transaction applies against. Not used by the MisPay trantype. In the case of PayInv, or CMemo transaction this must be a valid InvcHead record where InvcHead.CreditMemo = No. In case of "Adjust" transactions this can be either a invoice or a credit memo reference. Note: The "Apply Credit Memo" program automatically creates an additional CashDtl records for each invoice to which the credit memo is applied.  In this additional record this field contains the credit memo's number.  */  
   InvoiceNum:number,
      /**  Applicable to CMemo transaction types only. The "Apply Credit Memo" program creates two CashDtl records for each invoice that a credit memo is applied to. One record for the <credit> to the invoice and a second record for the debit to the credit memo. In the first record this field is the InvoiceNum of the Credit memo. In the second record it is the InvoiceNum of the invoice that the credit memo was applied to.  */  
   InvoiceRef:number,
      /**   Identifies the type of transaction. Adjust = Adjustment, CMemo = Credit Memo Transfer, PrePay = Pre Payment, MisPay = Misc Payment, PayInv = Payment on Invoices. This is  duplicated from the CashHead.TranType, not user maintainable.
Note: For currency gain/loss it will be "Adjust". Both the Debit/Credit GL# will be used. Debit is A/R account. Credit is gain/loss account.  */  
   TranType:string,
      /**  A flag that indicates if this transaction has been posted. A posted transaction cannot be maintained; it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Fiscal Year. This is not entered by the user on each record. Instead as part of the posting process it is duplicated in from the CashBatc.FiscalYear. Therefore each batch is posted to a single fiscal period.  */  
   FiscalYear:number,
      /**  Fiscal period for the transaction. Not directly entered by the user. Duplicated from the CashBatc.FiscalPeriod at time of posting.  */  
   FiscalPeriod:number,
      /**  Indicates if this transaction has been posted to the General Ledger Module.  */  
   GLPosted:boolean,
      /**  Transaction Date. Duplicated from the CashBatc.TranDate. Not user maintainable. This is refreshed as part of the post process.  */  
   TranDate:string,
      /**   The customer's Check number of the receipt transaction. Duplicated from CashHead.CheckRef. This is a mandatory field used only for Cash Receipt type of translations.  Primarily used as a reference. The only validation is that it can't be blank.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   CheckRef:string,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.
For records based in Debit Note applied  it carries a negative sign.  */  
   TranAmt:number,
      /**   Amount of transaction that is being applied.  Default as the lesser of IncvHead.InvoiceBal or CashHead.Outstanding.
Notes on sign of field: For Cash receipt transaction, it carries a positive sign. For Adjustments it carries the sign entered by the user (negatives reduce A/R). For disbursement of a credit memo against invoices (CMEMO) the transactions against the invoice carry a negative sign and the transactions generated against the credit memo carry a positive sign.  */  
   DocTranAmt:number,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   CustNum:number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   Discount:number,
      /**   Prompt Payment Discount given for this invoice. Only applicable for PayInv trantype.  The (TranAmt - Discount) reduces the Outstanding amount of the CashHead.TranAmt left to be applied.
This can't be > TranAmt.  */  
   DocDiscount:number,
      /**  Allows user to enter comments about the transaction. This is only applicable with TranType = "Adjust".  */  
   Comment:string,
      /**  Allows user to enter a short descriptive reference for the transaction. This is useful with Miscellaneous Cash Receipts.  */  
   Reference:string,
      /**   Exchange rate that will be used for this CashDtl, only differs from cashead when the invoice is locked.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
      /**  The internally set flag to indicate if this detail line of the Cash payment is Debit Note type.  */  
   DebitNote:boolean,
      /**  Debit Note Detail Comments.  */  
   DNComments:string,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   DNAmount:number,
      /**  The total debit note value applied for the invoice selected for the payment during the payment transaction.  */  
   DocDnAmount:number,
      /**  The Debit Note Number assigned by the customer.  */  
   DNCustNbr:string,
      /**  Rounding difference arises when invoice in one currency are settled in another currency  */  
   RoundDiff:number,
      /**  Reporting currency value of this field  */  
   Rpt1Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt2Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt3Discount:number,
      /**  Reporting currency value of this field  */  
   Rpt1DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt2DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt3DnAmount:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Fiscal Year Suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Tax Amount in the vendors currency.  */  
   DocTaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Red Storno Flag  */  
   RedStorno:boolean,
      /**  Tax Receipt Date (Thailand Localization)  */  
   TaxReceiptDate:string,
      /**  Tax Receipt No. (Thailand Localization)  */  
   TaxReceiptNo:string,
      /**  Withholding Tax Certificate Date  (Thailand Localization)  */  
   WHTCertificateDate:string,
      /**  Withholding Tax Certificate No. (Thailand Localization)  */  
   WHTCertificateNo:string,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  "R" for realized or "U" for unrealized Gain/Loss  */  
   GainLossType:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Indicates if it's a reversing Gain/Loss adjustment  */  
   ReverseGL:boolean,
      /**  Revaluation date that generated the gain/loss record  */  
   RevalueDate:string,
      /**  Invoice Balance at the time of revaluation  */  
   RevalueBal:number,
      /**  Document currency Invoice Balance at the time of revaluation  */  
   DocRevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt1RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt2RevalueBal:number,
      /**  Reporting currency Invoice Balance at the time of revaluation  */  
   Rpt3RevalueBal:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Tax Remarks  */  
   TaxRemarks:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  SEPADDMsgID  */  
   SEPADDMsgID:string,
      /**  SEPADDPmtID  */  
   SEPADDPmtID:string,
      /**  PmtDueDate  */  
   PmtDueDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  MX Payment Number for AR Invoice  */  
   MXPaymentNum:number,
      /**  Reference to HeadNum of main CashHead record.  */  
   WriteOffHeadNumRef:number,
      /**  EpicorFSA  */  
   EpicorFSA:boolean,
      /**  Taxable Adjustment  */  
   TaxableAdjustment:boolean,
   ApplyDate:string,
      /**  Adjustment amount in Base Currency  */  
   BaseAdjAmt:number,
   BaseCurrDesc:string,
      /**  Currency.CurrSymbol for BASE  */  
   BaseCurrSymbol:string,
      /**  The Billing Contact Number.  Obtained from InvcHead.BillConNum.  */  
   BillConNum:number,
      /**  If this flag is true the AR Invoice exchange rates is used when the Adjustment is applied and no currency Gain/Loss is calculated  */  
   CopyRate:boolean,
      /**  Indicates if invoice related to  this detail line is Correction invoice with negatice balance  */  
   CorrectionInv:boolean,
   CreditMemo:boolean,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencyDescription:string,
   CurrencySwitch:boolean,
      /**  Currency.CurrSymbol  */  
   CurrSymbol:string,
      /**  This field displays all Debit Note customer defined numbers applied.  */  
   DebitNotesApplied:string,
   DispDocSelfAssessAmt:number,
   DispDocWithholdAmt:number,
      /**  Display gl account  */  
   DispGLAcct:string,
   DispSelfAssessAmt:number,
   DispTranAmt:number,
   DispWithholdAmt:number,
   DocDispTranAmt:number,
      /**  Doc Invoice Amount  */  
   DocInvoiceAmt:number,
      /**  Doc Invoice Balance  */  
   DocInvoiceBal:number,
   DocNetCash:number,
      /**  Doc New Invoice Balance  */  
   DocNewBalance:number,
      /**  Write Off Amount  */  
   DocWriteOffAmount:number,
      /**  If this flag is true then CopyRate checkbox is Read Only  */  
   DsblCopyRate:boolean,
      /**  Legal Number Field  */  
   EnableAssignLegNum:boolean,
   EnableTranDocType:boolean,
      /**  Legal Number Field  */  
   EnableVoidLegNum:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency.  */  
   FullyPaid:boolean,
   GainLossAmt:number,
      /**  G/L Reference Code Description  */  
   GLRefCodeDesc:string,
      /**  Legal Number Field  */  
   HasLegNumCnfg:boolean,
   InvDiscountDate:string,
   InvDueDate:string,
      /**  Invoice Exchange Rate  */  
   InvExchRate:number,
   InvLegalNumber:string,
   InvLockRate:boolean,
      /**  Invoice Amount  */  
   InvoiceAmt:number,
      /**  Invoice Balance  */  
   InvoiceBal:number,
   InvTermsCode:string,
   InvXRateLabel:string,
      /**  This flag is used to differentiate between a normal Invoice Credit Memo and a Credit Payment.  */  
   IsCreditPayment:boolean,
   IsDiscountforCreditM:boolean,
   LegalNumMessage:string,
   LegalNumStyle:string,
   NetCash:number,
      /**  New Invoice Balance  */  
   NewBalance:number,
   OldGainLoss:number,
      /**  The related order number (InvcHead.OrderNum)  */  
   OrderNum:number,
      /**  Processing company's Reference ID, unique to each transaction  */  
   PNRef:string,
      /**  Indicates if posting GL transactions  */  
   PostToGL:boolean,
      /**  Whether to recalculate the CashDtl.TranAmt and all related columns prior to saving.  */  
   RecalcTranAmt:boolean,
   RedStornoOpt:string,
      /**  Indicates if Reference Code is (M)andatory, (O)ptional, (E)xcluded or Blank.  Enable Reference Code if "M" or "O".  */  
   RefCodeStatus:string,
      /**  This will indicate the information on this CashDtl record will not be included in the Cash Receipt Adjustment.  */  
   RemoveForAdjustment:boolean,
   Rpt1DispTranAmt:number,
   Rpt1GainLossAmt:number,
   Rpt1InvoiceAmt:number,
   Rpt1InvoiceBal:number,
   Rpt1NetCash:number,
   Rpt1NewBalance:number,
   Rpt1OldGainLoss:number,
      /**  Write Off Amount  */  
   Rpt1WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   Rpt1WriteOffGainLossAmt:number,
   Rpt2DispTranAmt:number,
   Rpt2GainLossAmt:number,
   Rpt2InvoiceAmt:number,
   Rpt2InvoiceBal:number,
   Rpt2NetCash:number,
   Rpt2NewBalance:number,
   Rpt2OldGainLoss:number,
      /**  Write Off Amount  */  
   Rpt2WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   Rpt2WriteOffGainLossAmt:number,
   Rpt3DispTranAmt:number,
   Rpt3GainLossAmt:number,
   Rpt3InvoiceAmt:number,
   Rpt3InvoiceBal:number,
   Rpt3NetCash:number,
   Rpt3NewBalance:number,
   Rpt3OldGainLoss:number,
      /**  Write Off Amount  */  
   Rpt3WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   Rpt3WriteOffGainLossAmt:number,
      /**  CustID associated with CashDtl.SoldToCustNum  */  
   SoldToCustID:string,
      /**  Populated from InvcHead.SoldToCustNum.  */  
   SoldToCustNum:number,
      /**  CustName associated with CashDtl.SoldToCustNum  */  
   SoldToCustomerName:string,
      /**  Legal Number Field  */  
   SystemTranType:string,
      /**  Description of the Tran Type  */  
   TranTypeDesc:string,
      /**  This field shows if this CashDtl line is 'Debit Note' type , created as a result of Debit Note(s) applied.  */  
   Type:string,
      /**  Write Off  */  
   WriteOff:boolean,
      /**  Write Off Account  */  
   WriteOffAccount:string,
      /**  Write Off Account Description  */  
   WriteOffAccountDesc:string,
      /**  Write Off Amount  */  
   WriteOffAmount:number,
      /**  Write Off Gain Loss Amount  */  
   WriteOffGainLossAmt:number,
   XRateLabel:string,
      /**  Legal Number Field  */  
   AllowChgAfterPrint:boolean,
      /**  Write Off Amount  */  
   OldWriteOffAmount:number,
   WriteOffAccountDisp:string,
   TaxableWriteOff:boolean,
      /**  Total Gain Loss Amount  */  
   TotalGainLossAmt:number,
      /**  Write Off Amount  */  
   OldWriteOffGainLossAmt:number,
      /**  Write Off Amount  */  
   Rpt1OldWriteOffGainLossAmt:number,
      /**  Write Off Amount  */  
   Rpt2OldWriteOffGainLossAmt:number,
      /**  Write Off Amount  */  
   Rpt3OldWriteOffGainLossAmt:number,
      /**  Total Gain Loss Amount  */  
   Rpt1TotalGainLossAmt:number,
      /**  Total Gain Loss Amount  */  
   Rpt2TotalGainLossAmt:number,
      /**  Total Gain Loss Amount  */  
   Rpt3TotalGainLossAmt:number,
      /**  Write Off Amount  */  
   DocOldWriteOffAmount:number,
      /**  Write Off Amount  */  
   Rpt1OldWriteOffAmount:number,
      /**  Write Off Amount  */  
   Rpt2OldWriteOffAmount:number,
      /**  Write Off Amount  */  
   Rpt3OldWriteOffAmount:number,
      /**  Allows uset to enter comment for Write Off.  */  
   WriteOffComment:string,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
   ReferenceTranDate:string,
   ReferenceTranNum:number,
   ReferenceTranTime:number,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   EnableManualWHTax:boolean,
      /**  Indicates if the withholding amount tax was manually modified.  */  
   WHTaxManualChange:boolean,
   BitFlag:number,
   CustNumCustID:string,
   CustNumName:string,
   CustNumBTName:string,
   InvoiceNumInvoiceType:string,
   InvoiceNumCardMemberName:string,
   InvoiceNumTermsCode:string,
   RateGrpDescription:string,
   TaxRgnDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashDtlTableset{
   CashDtl:Erp_Tablesets_CashDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CashHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Displays the ID of the group the transaction is assigned to.  */  
   GroupID:string,
      /**  Displays the receipt header number used for internal reference.  */  
   HeadNum:number,
      /**  A flag that indicates if this transaction has been posted. A posted transaction can not be maintained, it is considered as being committed. This flag is not directly set by the user for each transaction. Instead it is set via a "post function" which processes all the transactions in the batch.  */  
   Posted:boolean,
      /**  Displays the transaction type.  */  
   TranType:string,
      /**  Displays the number of the check.  */  
   CheckRef:string,
      /**  Sales Order #.  This is only used by the PrePay transaction. It must be a valid order found in OrderHed.  */  
   OrderNum:number,
      /**  The invoice # that is to be adjusted or the invoice number of a credit memo that is to be applied. This field is only used when TranType = CMemo or Adjust. It must be a valid open invoice memo found in the InvcHead file.  */  
   InvoiceNum:number,
      /**  Displays the transaction amount.  */  
   TranAmt:number,
      /**  Displays the transaction amount in customer currency.  */  
   DocTranAmt:number,
      /**  Displays the customer ID.  */  
   CustID:string,
      /**  Displays the date of the transaction.  */  
   TranDate:string,
      /**  Contains the Customer number that the transaction is for.  This must be valid in the Customer table.  Not entered for miscellaneous receipts.  */  
   CustNum:number,
      /**  Displays the unapplied amount.  */  
   UnAppliedAmt:number,
      /**  Displays the unapplied amount in base currency.  */  
   DocUnAppliedAmt:number,
      /**  Displays the amount applied to invoices.  */  
   AppliedAmt:number,
      /**  Displays the amount in document currency applied to invoices.  */  
   DocAppliedAmt:number,
      /**  Displays the fiscal year that the check is posted to.  */  
   FiscalYear:number,
      /**  Displays the fiscal period that the check is posted to.  */  
   FiscalPeriod:number,
      /**  Displays any reference.  */  
   Reference:string,
      /**  Indicates if this transaction has been posted.  */  
   GLPosted:boolean,
      /**  The invoice number that was used to create the credit memo for the unapplied cash receipt. This is updated during the cash receipt posting process and is used to link to the invchead.  */  
   CreditMemoNum:number,
      /**  Displays the customer currency.  */  
   CurrencyCode:string,
      /**  Displays the exchange rate that is used for this check.  */  
   ExchangeRate:number,
      /**  The Tax Region for this payment.  */  
   TaxRegionCode:string,
      /**  Total Tax Amount.  */  
   TaxAmt:number,
      /**  Displays the tax amount.  */  
   DocTaxAmt:number,
      /**  This field identifies a bankslip.  */  
   CashBookNum:number,
      /**  This field identifies a line of a bankslip.  */  
   CashbookLine:number,
      /**  Displays the legal number of the check.  */  
   LegalNumber:string,
      /**  External ID  */  
   ExternalID:string,
      /**  Link to the related GLRefTyp.RefType.  */  
   GLRefType:string,
      /**  Link to the related Code in GLRefCod.RefCode  */  
   GLRefCode:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   CCAmount:number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   CCFreight:number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   CCTax:number,
      /**  Total amount being sent to the credit card processor  */  
   CCTotal:number,
      /**  See CCAmount  */  
   CCDocAmount:number,
      /**  See CCFreight  */  
   CCDocFreight:number,
      /**  See CCTax  */  
   CCDocTax:number,
      /**  See CCTotal  */  
   CCDocTotal:number,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Indicates whether or not the bank account assigned for the Cash Receipt group  is for Debit Notes only.  If this flag is yes the new Deposit and new Misc payment options will be not available. If this flag is yes the check amount is 0 (no cash processed) and the check number is not assigned by the user.  */  
   DebNoteOnly:boolean,
      /**  Reporting currency value of this field  */  
   Rpt1AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3AppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TaxAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3TranAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnAppliedAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnAppliedAmt:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  See CCAmount  */  
   Rpt1CCAmount:number,
      /**  See CCAmount  */  
   Rpt2CCAmount:number,
      /**  See CCAmount  */  
   Rpt3CCAmount:number,
      /**  See CCFreight  */  
   Rpt1CCFreight:number,
      /**  See CCFreight  */  
   Rpt2CCFreight:number,
      /**  See CCFreight  */  
   Rpt3CCFreight:number,
      /**  See CCTax  */  
   Rpt1CCTax:number,
      /**  See CCTax  */  
   Rpt2CCTax:number,
      /**  See CCTax  */  
   Rpt3CCTax:number,
      /**  See CCTotal  */  
   Rpt1CCTotal:number,
      /**  See CCTotal  */  
   Rpt2CCTotal:number,
      /**  See CCTotal  */  
   Rpt3CCTotal:number,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the line before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Self Assessment Tax Amount.  */  
   SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   DocSelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt1SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt2SelfAssessAmt:number,
      /**  Self Assessment Tax Amount.  */  
   Rpt3SelfAssessAmt:number,
      /**  The unique code of Receipt Currency.  */  
   ReceiptCurrencyCode:string,
      /**  Amount of Receipt in Receipt Currency.  */  
   ReceiptAmt:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Bank Currency.  */  
   BankRcptExchangeRate:number,
      /**  Exchange rate that will be used for the Receipt from Receipt Currency to Settlement Currency.  */  
   SettlementExchangeRate:number,
      /**  The unique Currency code for Credit Memo.  */  
   CMCurrencyCode:string,
      /**  Amount of Credit Memo in CM Currency.  */  
   CMAmount:number,
      /**  Reference to cash receipt which had been reversed.  */  
   ReverseRef:number,
      /**  Date when cash receipt had been reversed  */  
   ReverseDate:string,
      /**  Bank Account ID  */  
   BankAcctID:string,
      /**  Withhold Tax  */  
   TaxWhld:number,
      /**  Dsicount Date  */  
   DiscountDate:string,
      /**  Calculate Withhold Tax  */  
   TaxWhldCalc:number,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  Site ID (Used Primary for Thailand Localization)  */  
   Plant:string,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Base currency.  */  
   UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Document currency.  */  
   DocUnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt1 currency.  */  
   Rpt1UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt2 currency.  */  
   Rpt2UnallocatedAmt:number,
      /**  Used for deposit payments. It is not equal zero if there is no sales order for the particular deposit payment. Rpt3 currency.  */  
   Rpt3UnallocatedAmt:number,
      /**  Number of the unallocated deposit payment to be apply.  */  
   ApplyHeadNum:number,
      /**  Used during the allocation process of the unallocated deposit payment. Base currency.  */  
   AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Document currency.  */  
   DocAllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt1 currency.  */  
   Rpt1AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt2 currency.  */  
   Rpt2AllocatedAmt:number,
      /**  Used during the allocation process of the unallocated deposit payment. Rpt3 currency.  */  
   Rpt3AllocatedAmt:number,
      /**  Comments related to the cash receipt.  */  
   Comment:string,
      /**  Payment Method Unique Identifier  */  
   PMUID:number,
      /**  Unique identifier of Petty Cash Desk  */  
   PCashDeskID:string,
      /**  ID Given by the Bank assigned during matching  */  
   BankTranID:string,
      /**  Reference Number, unique identifier of Petty Cash Document  */  
   PCashRefNum:number,
      /**  Transaction Document Type for the record.  */  
   TranDocTypeID:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Invoice Date  */  
   InvoiceDate:string,
      /**  Tax Remarks  */  
   TaxRemarks:string,
      /**  Non Deductable Code  */  
   NonDeductCode:string,
      /**  Non Deductable Amount  */  
   NonDeductAmt:number,
      /**  Non Deductable Doc Amount  */  
   NonDeductDocAmt:number,
      /**  Non Deductable Rpt1 Amount  */  
   NonDeductRpt1Amt:number,
      /**  Non Deductable Rpt2 Amount  */  
   NonDeductRpt2Amt:number,
      /**  Non Deductable Rpt3 Amount  */  
   NonDeductRpt3Amt:number,
      /**  Asset Type Code  */  
   AssetTypeCode:string,
      /**  Cash  */  
   Cash:boolean,
      /**  Credit Card  */  
   CreditCard:boolean,
      /**  Normal  */  
   Normal:boolean,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  Bank Transaction Date  */  
   BankTransDate:string,
      /**  Payee  */  
   Payee:string,
      /**  AccountNumber  */  
   AccountNumber:string,
      /**  OtherDetails  */  
   OtherDetails:string,
      /**  MandateReference  */  
   MandateReference:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  SEPADDExportDate  */  
   SEPADDExportDate:string,
      /**  BOE Invoice Number  */  
   BOEInvoiceNum:number,
      /**  MXRecDate  */  
   MXRecDate:string,
      /**  OwnReference  */  
   OwnReference:string,
      /**  DocumentType  */  
   DocumentType:string,
      /**  ABTUID  */  
   ABTUID:string,
      /**  BankRcptExchangeRate10D  */  
   BankRcptExchangeRate10D:number,
      /**  SettlementExchangeRate10D  */  
   SettlementExchangeRate10D:number,
      /**  Indicates that cash receipt is currently excluded from batch in Bank Statement Processing.  */  
   BankBatchExcluded:boolean,
      /**  BankBatchSysRowID  */  
   BankBatchSysRowID:string,
      /**  PayMethodReference  */  
   PayMethodReference:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangeDate  */  
   ChangeDate:string,
      /**  OnAccount  */  
   OnAccount:boolean,
      /**  The amount of the cash receipt applied to invoices in receipt currency  */  
   RcptCurAppliedAmt:number,
      /**  The amount of the cash receipt that is unapplied in receipt currency  */  
   RcptCurUnAppliedAmt:number,
      /**  MXAccountNumber  */  
   MXAccountNumber:string,
      /**  MX Method of Payment: single, multiple, etc.  */  
   MXPaidAs:string,
      /**  If TRUE then MX Electronic Payment XML is required  */  
   MXPaySupplementFlag:boolean,
      /**  LockboxID  */  
   LockboxID:string,
      /**  MX Receipt’s Fiscal Folio (UUID)  */  
   MXFiscalFolio:string,
      /**  MX UUID of the original Receipt being corrected  */  
   MXOriginalCheckRef:string,
      /**  MX Confirmation Code for special Cash Receipts  */  
   MXConfirmationCode:string,
      /**  MX Customer’s Bank ID  */  
   MXBankID:string,
      /**  Text entered by the user to indicate the reason Cash receipt was Reversed.  */  
   ReversedReason:string,
      /**  Credit Card Holder City.  */  
   CCCity:string,
      /**  Credit Card Holder State.  */  
   CCState:string,
      /**  ccToken  */  
   ccToken:string,
      /**  DepositBalance  */  
   DepositBalance:number,
      /**  DocDepositBalance  */  
   DocDepositBalance:number,
      /**  Rpt1DepositBalance  */  
   Rpt1DepositBalance:number,
      /**  Rpt2DepositBalance  */  
   Rpt2DepositBalance:number,
      /**  Rpt3DepositBalance  */  
   Rpt3DepositBalance:number,
      /**  Indicates this record is an adjustment CashHead.  */  
   Adjustment:boolean,
      /**  Reference to cash receipt which had been adjusted.  */  
   AdjustmentRef:number,
      /**  The reason for the adjustment entered by the user  */  
   AdjustmentReason:string,
      /**  Total Check Write Off Amount  */  
   WriteOffAmount:number,
      /**  DocWriteOffAmount  */  
   DocWriteOffAmount:number,
      /**  Rpt1WriteOffAmount  */  
   Rpt1WriteOffAmount:number,
      /**  Rpt2WriteOffAmount  */  
   Rpt2WriteOffAmount:number,
      /**  Rpt3WriteOffAmount  */  
   Rpt3WriteOffAmount:number,
      /**  Mexico Certified Timestamp  */  
   MXCertifiedTimestamp:string,
      /**  Mexico SAT Seal  */  
   MXSATSeal:string,
      /**  Mexico Digital Seal  */  
   MXDigitalSeal:string,
      /**  Mexico SAT Certificate Serial Number  */  
   MXSATCertificateSN:string,
      /**  Mexico Original String Timbre Fiscal Digital  */  
   MXOriginalStringTFD:string,
      /**  Mexico Certificate  */  
   MXCertificate:string,
      /**  Mexico Certificate Serial Number  */  
   MXCertificateSN:string,
      /**  SourceGroupID  */  
   SourceGroupID:string,
      /**  SourceHeadNum  */  
   SourceHeadNum:number,
      /**  Standard Entry Class Code  */  
   SEC:string,
      /**  ACH Transaction Code  */  
   ACHTranCode:number,
      /**  ID of the Customer's bank.  */  
   CustomerBankID:string,
      /**  The Bank account number for the Customer.  */  
   CustomerBankAcctNumber:string,
      /**  CustomerBankSwiftNum  */  
   CustomerBankSwiftNum:string,
      /**  The Bank account IBAN Code  */  
   CustomerBankIBANCode:string,
      /**  Name on the Bank Account.  */  
   CustomerBankNameOnAccount:string,
      /**  First address line of customer bank.  */  
   CustomerBankAddress1:string,
      /**  Second address line of customer bank.  */  
   CustomerBankAddress2:string,
      /**  Third address line of customer bank.  */  
   CustomerBankAddress3:string,
      /**  Bank City  */  
   CustomerBankCity:string,
      /**  Bank State/Prov  */  
   CustomerBankState:string,
      /**  Postal Code or zip code  */  
   CustomerBankPostalCode:string,
      /**  Bank account Country Number.  */  
   CustomerBankCountryNum:number,
      /**  ARRemittanceSlipPrinted  */  
   ARRemittanceSlipPrinted:boolean,
      /**  Customer Bank Name  */  
   CustomerBankName:string,
      /**  MXPostedTimeStamp  */  
   MXPostedTimeStamp:string,
      /**  MXSerie  */  
   MXSerie:string,
      /**  MXFolio  */  
   MXFolio:string,
      /**  MXEPaymentType  */  
   MXEPaymentType:string,
      /**  MXEPaymentCertificateNumber  */  
   MXEPaymentCertificateNumber:string,
      /**  MXEPaymentOriginalString  */  
   MXEPaymentOriginalString:string,
      /**  MXEPaymentDigitalSeal  */  
   MXEPaymentDigitalSeal:string,
      /**  Source  */  
   Source:string,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  GL Description for the Reverse process  */  
   RevDescription:string,
      /**  GL Description for AR - Apply Credit Memo  */  
   CMDescription:string,
      /**  Receipt Amount in Bank Currency  */  
   BankReceiptAmt:number,
      /**  MXCancelReasonCode  */  
   MXCancelReasonCode:string,
      /**  MXSubstHeadNum  */  
   MXSubstHeadNum:number,
      /**  MXCancellationMode  */  
   MXCancellationMode:string,
      /**  E-invoice error description.  */  
   ELIEInvException:string,
      /**  EInvoice ID  */  
   ELIEInvID:string,
      /**  E-invoice  */  
   ELIEInvoice:boolean,
      /**  E-invoice Service Provider Status  */  
   ELIEInvServiceProviderStatus:number,
      /**  E-invoice Status  */  
   ELIEInvStatus:number,
      /**  User Id of the person generated E-invoice.  */  
   ELIEInvUpdatedBy:string,
      /**  E-invoice Updated On  */  
   ELIEInvUpdatedOn:string,
      /**  Adjustment Customer Name  */  
   AdjustmentCustName:string,
      /**  Customer to which the new invoices will be applied.  */  
   AdjustmentCustNum:number,
      /**  Date the adjustment was made.  */  
   AdjustmentDate:string,
      /**  Displays the amount available to apply to the invoices.  */  
   AdjustmentDocUnAppliedAmt:number,
      /**  On Account  */  
   AdjustmentOnAccount:boolean,
      /**  Temp TranDocTypeID used when adjusting a Cash Rececipt  */  
   AdjustmentTranDocTypeID:string,
   AllocDepBal:number,
   AllowChgAfterPrint:boolean,
      /**  For TranType = "PayInv" it is true only if ARSyst.AllowSettlementInDiffCurr is true. For other types it is true always.  */  
   AllowUpdSettlementCurr:boolean,
      /**  Amount to Allocate  */  
   AmtToAlloc:number,
   ApplyDate:string,
      /**  AVSADDR returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) address test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSAddr:string,
      /**  AVSZIP returned by a 3rd party credit card processing company  for a credit card transaction. This value represents the results of the Address Verification System (AVS) zip code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   AVSZip:string,
      /**  Bank Currency Value  */  
   BankAmount:number,
   BankBaseXRateLabel:string,
   BankCurrencyCode:string,
      /**  Bank Currency Symbol  */  
   BankCurrSymbol:string,
   BankExchangeRate:number,
   BankRcptXRateLabel:string,
   BaseCurrencyCode:string,
      /**  Base Currency Symbol  */  
   BaseCurrSymbol:string,
      /**  Bill To Name  */  
   BillToName:string,
      /**  Indicates if rate was calculated from TranAmt fields instead of CurrExRate table  */  
   calcRate:boolean,
      /**  Stored Credit Card Number  */  
   CardStore:string,
      /**  Field to enable/disable the Sale and Deposit Buttons in the Credit Card Tab. This button will depend in the status of the AllowDepPay in CreditCardProc.  */  
   CCAllowSales:boolean,
   CCApprovalNum:string,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention  */  
   CCCSCID:string,
      /**  Tokenized value of CSCID  */  
   CCCSCIDToken:string,
      /**  Field to enable/disable the Customer Address fields in the Credit Card Tab. This button will depend in the status of the UseAVSin CreditCardProc.  */  
   CCEnableAddress:boolean,
      /**  s fields in the Credit Card Tab. This button will depend in the status of the UseCSC in CreditCardProc.  */  
   CCEnableCSC:boolean,
      /**   Indicates if the credit card setup will be using a testing Paygate instance for transactions.
Force requests to use Paygate test url: paygate-test1.eaglesoa.com  */  
   CCIsTraining:boolean,
      /**  RESPMSG returned by  a 3rd party credit card processing company for a credit card transaction. This is a brief description of the status of the credit card transaction.  */  
   CCResponse:string,
      /**  PNREF returned by a 3rd party credit card processing company for a credit card transaction. This is a unique number that identifies the transaction and is often referenced we performing related transactions.  */  
   CCTranID:string,
      /**  Credit Card Transaction Type  */  
   CCTranType:string,
      /**  Check Box on the UI to filter records by Central Collection flag  */  
   CentralCollectionCheck:boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Correction Invoice with negative amount  */  
   CorrectionInv:boolean,
      /**  Customer Credit Hold flag  */  
   CreditHold:boolean,
      /**  If the user selects Credit Memo/Correction Invoice document type this flag indicates that this is Credit Memo  */  
   CreditMemo:boolean,
      /**  CREProcessor is true when Credit Card Configuration is CRE Server.  */  
   CREProcessor:boolean,
      /**  CVV2MATCH returned by a 3rd party credit card processing company for a credit card transaction. This value represents the results of the Card Security Code test. The result in this field does not affect the outcome of the transaction and is supplied for advisory purposes only.  */  
   CSCResult:string,
      /**  Current Amount Selected on Invoice Select Tab  */  
   CurrAmtSelected:number,
   CurrencySwitch:boolean,
      /**  Displays the address of the customer that paid the receipt.  */  
   CustFullAddr:string,
   CustomerName:string,
   DisableFieldsForPCashDoc:boolean,
      /**  Display GL Account  */  
   DispGLAcct:string,
   DocAllocDepBal:number,
      /**  Doc Amount to Allocate  */  
   DocAmtToAlloc:number,
      /**  Displays the discount applied to the receipt.  */  
   DocDiscount:number,
      /**  Displays the invoice amount paid by this receipt. The amount includes both discount and payment amounts.  */  
   DocReceipt:number,
      /**  Transaction Amount less Tax Amount  */  
   DocTranTaxAmt:number,
      /**  Document number: Invoice Number if source document is AR Invoice or HeadNum if source document is Deposit Payment.  */  
   DocumentNum:number,
   DocWhldTax:number,
   DspBankBatchID:string,
      /**  Amount of Credit Memo in CM Currency.  */  
   DspCMAmount:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   DspDocTranAmt:number,
   DspSalesOrderValue:number,
      /**  Amount of check, credit memo, or adjustment depending on the transaction type. For CMemo this is the total amount of the credit memo that was applied, in this case it is not entered by the user, instead it is updated as the credit memo is applied to invoices. For all other transactions the user  */  
   DspTranAmt:number,
   EnableAssignLegNum:boolean,
      /**  Indicates if the option to get the default account is enable.  */  
   EnableGetDefaultAcct:boolean,
   EnableTranDocType:boolean,
   EnableTransactionDate:boolean,
   EnableVoidLegNum:boolean,
      /**  Invoice is considered as fully paid in case the absolute value of unapplied amout is less than tolerance defined for the currency, it's used to show the status of invoice.  */  
   FullyPaid:boolean,
   GLRefCodeDescription:string,
   HasLegNumCnfg:boolean,
      /**  The InvcHead legal number  */  
   InvcLegalNumber:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
   LegalNumberDsp:string,
   LegalNumMessage:string,
      /**  Copied from OrderHed.LockRate  */  
   LockRate:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
   ManualTaxAdj:boolean,
      /**  MXCancellationID  */  
   MXCancellationID:string,
   MXCancellationStatus:string,
      /**  MXECEPXml  */  
   MXECEPXml:string,
      /**  Mexico Calculated field - shows Check Reference number of the original Receipt being corrected  */  
   MXOriginalRefNum:string,
      /**  Host Address for the Paygate Hosted Token Service.  */  
   PayGateHostAddress:string,
      /**  NameSpace for the Paygate Hosted Token Service.  */  
   PayGateNameSpace:string,
      /**  Public Key for the Paygate Hosted Token Service EWA component.  */  
   PayGatePublicKey:string,
      /**  This column is used within cash receipt tracker to show either the receipt date or the source/ original receipt date if the cash receipt has been adjusted.  */  
   ReceiptDate:string,
      /**  PNRef number referred to in the transaction.  If Deposit transaction must referenece prior Authorization using the PNRef  */  
   ReferencePNRef:string,
   Rpt1AllocDepBal:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt1TranTaxAmt:number,
   Rpt1WhldTax:number,
   Rpt2AllocDepBal:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt2TranTaxAmt:number,
   Rpt2WhldTax:number,
   Rpt3AllocDepBal:number,
      /**  Transaction Amount less Tax Amount  */  
   Rpt3TranTaxAmt:number,
   Rpt3WhldTax:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
   SalesOrderValue:number,
   SettlementXRateLabel:string,
      /**  Name of the Sold To customer if this is a Deposit (created using an OrderHed).  */  
   SoldToCustomerName:string,
   SystemTranType:string,
      /**  Sum of all rounding differences of the payments for one Cash Receipt and one Check  */  
   TotalRoundDiff:number,
      /**  Transaction Amount less Tax Amount  */  
   TranTaxAmt:number,
      /**  Description of TranType  */  
   TranTypeDesc:string,
      /**  Yes if Cash Receipt has Unapplied amount but credit memo is applied.  */  
   UnappliedAmountApplied:boolean,
   WhldTax:number,
   XRateLabel:string,
      /**  Displays the customer ID.  */  
   AdjustmentCustID:string,
   ReferenceTranDate:string,
   ReferenceTranNum:number,
   ReferenceTranTime:number,
      /**  Displays the address of the customer that paid the receipt with newline delimiter.  */  
   CustFullAddrFormatted:string,
      /**  Indicates if the user can manually modify the applied withholding tax of the invoice. Used in Apply Credit Memo when withholding tax was not posted through an interim account.  */  
   EnableManualWHTax:boolean,
      /**  Indicates if the withholding tax was manually modified.  */  
   WHTaxManualChange:boolean,
      /**  Payment type description, displayed in the Details page header.  */  
   TranTypeDescCaption:string,
   AdjustmentCustAddress:string,
      /**  Substitution Cash Receipt Group ID  */  
   MXSubstGroupId:string,
      /**  Substitution Cash Receipt CheckRef  */  
   MXSubstCheckRef:string,
      /**  Substitution Cash Receipt UUID  */  
   MXSubstFiscalFolio:string,
   BitFlag:number,
   BankAcctIDDescription:string,
   BankAcctIDBankName:string,
   CardTypeDescription:string,
   CashBHedPosted:boolean,
   CashBHedCashBookNum:number,
   CashbookLineDescription:string,
   CMCurrencyCodeDocumentDesc:string,
   CMCurrencyCodeCurrName:string,
   CMCurrencyCodeCurrSymbol:string,
   CMCurrencyCodeCurrDesc:string,
   CMCurrencyCodeCurrencyID:string,
   CurrencyCodeDocumentDesc:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrName:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CustNumInactive:boolean,
   CustNumName:string,
   CustNumBTName:string,
   CustNumCustID:string,
   InvoiceNumTermsCode:string,
   InvoiceNumCardMemberName:string,
   OrderNumCardMemberName:string,
   OrderNumCurrencyCode:string,
   PCashDocDirection:string,
   PMUIDName:string,
   PMUIDMXSATCode:string,
   PMUIDSummarizePerCustomer:boolean,
   PMUIDType:number,
   RateGrpDescription:string,
   RcptCurrencyCodeCurrencyID:string,
   RcptCurrencyCodeDocumentDesc:string,
   RcptCurrencyCodeCurrDesc:string,
   RcptCurrencyCodeCurrSymbol:string,
   RcptCurrencyCodeCurrName:string,
   ReverseMXCancelReasonCode:string,
   ReverseMXCancellationMode:string,
   SourceTranDateTranDate:string,
   TaxRegionCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CashHeadTableset{
   CashHead:Erp_Tablesets_CashHeadRow[],
   CashDtl:Erp_Tablesets_CashDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CreditManagerTableset{
   CMCustomer:Erp_Tablesets_CMCustomerRow[],
   CustomCrdPool:Erp_Tablesets_CustomCrdPoolRow[],
   GlbCustCred:Erp_Tablesets_GlbCustCredRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CustCntAttchRow{
   Company:string,
   CustNum:number,
   ShipToNum:string,
   ConNum:number,
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

export interface Erp_Tablesets_CustCntRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  The Customer.CustNum value of the customer that the contact is related to.  */  
   CustNum:number,
      /**  The ShipTo.ShipToNum of the Ship To that the customer  */  
   ShipToNum:string,
      /**  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  */  
   ConNum:number,
      /**  Full name of the contact.  */  
   Name:string,
      /**  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  */  
   Func:string,
      /**  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  */  
   FaxNum:string,
      /**  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  */  
   PhoneNum:string,
      /**  A logical flag that indicates if this contact has a mailing address different from the one found in the associated Customer master. This flag is only applicable to contacts related to the Customer. That is where CustCnt.ShipToNum = "". During maintenance if this flag is Yes then access is allowed to the Address, City, State, Zip and Country fields. Otherwise those fields are protected. During maintenance when SpecialAddress is toggled to Yes and the address1 field is blank the program defaults all the address fields equal to the customers, thinking that much of it will be the same, saving keying time. When it's toggled to "No", then program sets all the address field to blank.  */  
   SpecialAddress:boolean,
      /**  Line 1 of the contact's mailing address if different from that of the customer. The contacts associated with a customer (not ship to) are allowed to have address, city, state, zip and country fields that are different from that of their associated customer. If not blank, these address fields are printed on the Quote form; otherwise the customer address is used.  */  
   Address1:string,
      /**  Line 2 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  */  
   Address2:string,
      /**  Line 3 of the contact's mailing address if different from that of the customer. (See Address1 for additional information).  */  
   Address3:string,
      /**  The city portion of the contact's mailing address. (See Address1 for additional information).  */  
   City:string,
      /**  The state or province portion of the contact's mailing address. (See Address1 for additional information).  */  
   State:string,
      /**  The zip or postal code portion of the contact's mailing address. (See Address1 for additional information).  */  
   Zip:string,
      /**  The Country portion of the contact's mailing address. (See Address1 for additional information).  */  
   Country:string,
      /**  The company name of the contact's mailing address. (See Address1 for additional information).  */  
   CorpName:string,
      /**  The contact's email address.  */  
   EMailAddress:string,
      /**  The Country.CountryNum value of the country selected for the contact's mailing address.  */  
   CountryNum:number,
      /**  Customer Connect password for this contact.  */  
   SFPortalPassword:string,
      /**  Indicates if able to create Orders  */  
   SFUser:boolean,
      /**  Indicates if "Order History" is functional  */  
   PortalUser:boolean,
      /**  RoleCD.RoleCode value of the role assigned to the contact.  */  
   RoleCode:string,
      /**  The contact's cell phone number.  */  
   CellPhoneNum:string,
      /**  The contact's pager number.  */  
   PagerNum:string,
      /**  The contact's Home number.  */  
   HomeNum:string,
      /**  The contact's alternate phone number.  */  
   AltNum:string,
      /**  The contact's title.  */  
   ContactTitle:string,
      /**  The name of the person this contact reports to.  */  
   ReportsTo:string,
      /**  Comments are intended to be internal comments about a specific contact.  */  
   Comment:string,
      /**  Indicates whether or not this contact should be included in marketing lists.  */  
   NoContact:boolean,
      /**  The date that the contact was entered into the database.  */  
   CreateDate:string,
      /**  The UserFile.DCDUserID of the user that entered the contact into the database.  */  
   CreateDcdUserID:string,
      /**  **NOTE cannot find any code that maintains this field.  */  
   ChangeDate:string,
      /**  **NOTE cannot find any code that maintains this field.  */  
   ChangeDcdUserID:string,
      /**  Determines whether or not this contact can be referenced on a quote, order, packing slip or invoice.  */  
   Inactive:boolean,
      /**  Contact's first name.  */  
   FirstName:string,
      /**  Contact's middle name.  */  
   MiddleName:string,
      /**  Contact's last name.  */  
   LastName:string,
      /**  Contact's prefix.  */  
   Prefix:string,
      /**  Contact's suffix.  */  
   Suffix:string,
      /**  Contact's initials.  */  
   Initials:string,
      /**  External ID  */  
   ExternalID:string,
      /**  Determines whether or not this record receives global updates  */  
   GlobalLock:boolean,
      /**  If TRUE then the input prices will be shown in the Customer Connect Configuration Review.  */  
   ShowInputPrice:boolean,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  Pertains to Alternate Shipto. Contains the CustNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterCustNum:number,
      /**  Pertains to Alternate Shipto. Contains the ShipToNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterShipToNum:string,
      /**  Pertains to Alternate Shipto. Contains the ConNum of the CustCnt record that is the "Master". Changes made to the Master, are replicated to the alternates.  */  
   MasterConNum:number,
      /**  Unique identifier for a PerCon record.  */  
   PerConID:number,
      /**  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  */  
   SyncNameToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Address fields on PerCon won't affect this record and visa versa.  */  
   SyncAddressToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  */  
   SyncPhoneToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  */  
   SyncEmailToPerCon:boolean,
      /**  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  */  
   SyncLinksToPerCon:boolean,
      /**  Contact's Website.  */  
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
      /**  Indicates if the Person/Contact address should be used as the Special Quoting Address.  */  
   PerConAddress:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  This field defines if the customer contact  is synchronized to an External CRM.  */  
   SyncToExternalCRM:boolean,
      /**  This field holds the id of this customer in the External CRM  */  
   ExternalCRMCustomerID:string,
      /**  This field holds the id of this customer contact in the External CRM  */  
   ExternalCRMContactID:string,
   RoleDescription:string,
      /**   This check box indicates that this contact is the customer's main billing contact. 
When an AR invoice is created for this customer, this contact's name will automatically appear on the invoice.  */  
   PrimaryBilling:boolean,
      /**   This check box indicates that this contact is the customer's main purchasing contact. 
When a quote or sales order is created for this customer, this contact's name will automatically appear on the order or quote.  */  
   PrimaryPurchasing:boolean,
      /**   This check box indicates that this contact is the customer's main shipping contact. 
When a packing slip is created for this customer, this contact's name will automatically appear on the slip.  */  
   PrimaryShipping:boolean,
      /**  Indicates if the Contact is global (Master or Linked)  */  
   GlbFlag:boolean,
      /**  delimited list of CustCnAttr codes  */  
   AttrCodeList:string,
      /**  GlbCustCnt fields in a linked list to find the linking record  */  
   GlbLink:string,
      /**  Used for ContactTracker.  This is needed so the UI can relate the Contact Tracker tables together.  */  
   ContactName:string,
   PerConName:string,
   BitFlag:number,
   CustNumName:string,
   CustNumBTName:string,
   CustNumCustID:string,
   MasterCustNumBTName:string,
   MasterCustNumName:string,
   MasterCustNumCustID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CustCntTableset{
   CustCnt:Erp_Tablesets_CustCntRow[],
   CustCntAttch:Erp_Tablesets_CustCntAttchRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CustomCrdPoolRow{
      /**  Company  */  
   Company:string,
   CustNum:number,
   CrdPoolCode:string,
   CreditUsed:number,
   CreditAvailable:number,
      /**  Global Pool - shows if the pool belongs to Global National Account  */  
   GlobalNA:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExportCustCredRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Customer ID  */  
   CustID:string,
      /**  Customer Type  */  
   CustomerType:string,
      /**  Customer Name  */  
   CustName:string,
      /**  Credit Limit  */  
   CreditLimit:number,
      /**  Credit Review Date stored as character  */  
   CreditReviewDate:string,
      /**  Total invoice credit amount  */  
   InvoiceCreditTot:number,
      /**  Total order credit amount  */  
   OrderCreditTot:number,
      /**  Total credit amount  */  
   CreditTot:number,
      /**  Total number of invoices  */  
   NumInvoice:number,
      /**  Total number of orders  */  
   NumOrder:number,
      /**  Credit Hold values: 1 = Customer on credit hold; 0 = Not on hold  */  
   CreditHold:number,
      /**  Credit Include Order values: 1 = Include Orders; 0 = Exclude Orders  */  
   CreditIncludeOrders:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ExportCustCredTableset{
   ExportCustCred:Erp_Tablesets_ExportCustCredRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlbCustCredRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   CustNum:number,
      /**  Company credit totals came from (not just owner of the global customer)  */  
   ExtCompany:string,
   ExtCompName:string,
      /**  Date the credit was last updated  */  
   UpdateDate:string,
      /**  Open AR Credit in Global Currency  */  
   DocARTotal:number,
      /**  Open Order Credit in Global Currency  */  
   DocSOTotal:number,
      /**  Open PI Credit in Global Currency  */  
   DocPITotal:number,
      /**  AR Credit in local companies base currency  */  
   ARTotal:number,
      /**  SO Credit in local companies base currency  */  
   SOTotal:number,
      /**  PI Credit in local companies base currency  */  
   PITotal:number,
      /**  Holds connection and exchange rate error messages  */  
   ErrorMsg:string,
      /**  This field holds the associated Global Customer number.  If this is the "parent" customer then it will match the CustNum field.  0 indicates that this is not a global customer at all  */  
   GlbCustNum:number,
      /**  The Customer.CustNum value of the customer's parent company.  */  
   ParentCustNum:number,
      /**  Holds the Currency.CurrencyCode value of that the global customer will exchange data in.  */  
   GlobalCurrencyCode:string,
      /**  Total Number of Open Invoices  */  
   TotalInvoices:number,
      /**  Total Number of Open Orders  */  
   TotalOrders:number,
      /**  Total Number of open Payment Instruments  */  
   TotalPayIns:number,
      /**  Parent's Credit used by this customer  */  
   NAParentsCreditUsed:number,
      /**  Shared Credit used by children  */  
   NASharedCreditUsed:number,
      /**  Own Credit used by himself  */  
   NAOwnCreditUsed:number,
      /**  Global Parent's Credit used by this customer  */  
   GlbNAParentsCreditUsed:number,
      /**  Shared Credit used by Global children  */  
   GlbNASharedCreditUsed:number,
      /**  Pool Credit used  */  
   NAPoolCreditUsed:number,
      /**  Global Credit Pool used  */  
   GlbNAPoolCreditUsed:number,
      /**  Own Credit used by himself  */  
   GlbNAOwnCreditUsed:number,
      /**  Allocated Credit exceed Credit Limit  */  
   NAExceedLimit:number,
      /**  Allocated Credit exceed Global Credit Limit  */  
   GlbNAExceedLimit:number,
      /**  AR Letter of Credit Credit in local companies base currency  */  
   ARLOCTotal:number,
      /**  Open AR Letter of Credit Credit in Global Currency  */  
   DocARLOCTotal:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ImportCustCredRow{
      /**  Company Identifier  */  
   Company:string,
      /**  Customer ID  */  
   CustID:string,
   CustomerType:string,
   CustName:string,
      /**  Customer Credit Limit  */  
   CreditLimit:number,
      /**  Credit Review Date  */  
   CreditReviewDate:string,
      /**  Credit Hold values: 1 = Customer is on hold; 0 = Not on hold  */  
   CreditHold:number,
      /**  Credit Include Order values: 1 = Include orders; 0 = Exclude orders  */  
   CreditIncludeOrders:number,
      /**  Total invoice credit amount  */  
   InvoiceCreditTot:number,
      /**  Total order credit amount  */  
   OrderCreditTot:number,
      /**  Total credit amount  */  
   CreditTot:number,
      /**  Total number of invoices  */  
   NumInvoice:number,
      /**  Total number of orders  */  
   NumOrder:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ImportCustCredTableset{
   ImportCustCred:Erp_Tablesets_ImportCustCredRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InvcHeadRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Indicates if invoice is "open".  */  
   OpenInvoice:boolean,
      /**  The latest transaction date (CashDtl) which was available when the invoice was closed. This is used to improve record selection performance when selecting invoices that were open as of a certain date. (Used by the aged invoice report). This is updated during the CashReceipt posting process, Adjustment entry or Apply Credit memos programs..  */  
   ClosedDate:string,
      /**   Indicates the type of document. Yes = Credit Memo No= Invoice. This value can't be changed after the record has been created.
Credit memos affect the way detail quantities and amounts are stored in the database. They will always be stored with a negative sign but will entered as a positive.
Credit Memos created by invoice entry also set the InvoiceSuffix field = "CM"  */  
   CreditMemo:boolean,
      /**  An internal flag that represents Credit Memo was due to Unapplied Receipts. Created by the Cash Receipts Entry program.   This is only applicable with CreditMemo = Yes.  */  
   UnappliedCash:boolean,
      /**   The Check reference number that the Unapplied Receipt Credit Memo was created from. Cash receipts entry sets this field equal to the CashHead.CheckRef when it creates the Unapplied Receipt Credit Memo.  Primarily used as a reference.
This is used when TranType = PrePay, MisPay or PayInv.  */  
   CheckRef:string,
      /**  An internally assigned field that further identifies an invoice. This field will be displayed as a suffix to the invoice number.  The possible values are "CM" = Credit memo created by invoice entry, UR = Unapplied Receipt Credit Memo,  DN = Debit Note, and FC = Finance Charge invoice.  */  
   InvoiceSuffix:string,
      /**  The Group that the invoice was associated with  during the data entry process. This field is not directly maintainable, it is assigned by the invoice entry program using the BatchID of the "current " batch that the user is working with.  */  
   GroupID:string,
      /**  Indicates if this invoice has been Posted to the receivables file.    Only invoices that have been Posted (true) will be included as part of the open receivables, that is they will not appear on reports or inquiries other than those used within invoice entry. Otherwise they are considered as still being in data entry. This field is always "no" when the invoice is created. It is set to "yes"  by the  "Post function". Once an invoice is posted it can't be maintained via data entry.  */  
   Posted:boolean,
      /**  If this field is left blank the system assigns the next available #. The next available # is the greater of last # on file plus one or the XaSyst.StartInvNum.  */  
   InvoiceNum:number,
      /**  There are four types of invoices:  "Shp" = Invoice for Shipment, "Adv" = Advanced Billing, "Dep" = For Deposit Payments, "Mis" = Miscellaneous.  The setting of this field affects invoice entry:  "Shipments" - These are generated by the "Get Shipments function" and is not selectable directly by the user.  "Advanced"  - Must have a sales order reference. The detail lines on this type of invoice update the OrderDtl.AdvanceBillBal. Also the user indicates if this should be considered as deferred revenue. Which changes which G/L accounts are used for the line item credits.  "Deposit" - invoices are used to request a "deposit" on an order. A Sales Order is mandatory. No line items or Miscellaneous records are allowed. The user enters a flat amount on the header (InvcHead.PrePayAmt) which will be printed in the body of the invoice. This also updates the OrderHed.PrePayBal field.   "Miscellaneous" - These invoices may or may not reference a Sales Order.  If Invoice is generated in Project Billing then there are following options: "PFF" - Fixed Fee project;  "PCP" - Cost Plus project;  "PTM" - Time and Material project;  "PPP" - Progress Payment project.  */  
   InvoiceType:string,
      /**  Only used when InvoiceType = "Adv" (Advanced Billing).  Indicates if the detail line amounts are to be considered as sales or deferred revenue.  If "No" then the G/L accounts on the detail lines are the Sales Accounts otherwise they will be set to the Deferred Revenue accounts established in the ARSyst/ARAcct files.  */  
   DeferredRevenue:boolean,
      /**  Sales Order #. This is a mandatory entry for all InvoiceType except "Miscellaneous". If entered it must be valid in the OrderHed file. The OrderHed supplies the invoice with many defaults, including; CustNum, PONum, TermsCode,  FOB, RepRate, RepSplit, SalesRepList, InvoiceComments  */  
   OrderNum:number,
      /**  The CustNum field is the internal # that is used to link the invoice to the Customer master file.  This field is not directly maintained by the user.  In most cases it will be duplicated from the referenced OrderHed. For "Miscellaneous" invoices the user can enter either a Sales Order Number or a Customer ID which will supply the CustNum.  */  
   CustNum:number,
      /**  Customer's PO#.   This is a reference field which will be printed on the invoice. Defaults from the OrderHed.PONum.  */  
   PONum:string,
      /**  User ID that entered the invoice. This is not maintainable by the user.  */  
   EntryPerson:string,
      /**  Defaults from sales order ORderHed.FOB  */  
   FOB:string,
      /**  Contains the foreign key to the TERMS master file.  Defaults from OrderHed if OrderNum > 0 else from the Customer master. This IS A MANDATORY ENTRY. User maintainable via a combo-box for terms description.  */  
   TermsCode:string,
      /**  Invoice date is duplicated from the InvcGrp record.  */  
   InvoiceDate:string,
      /**  The due date of the earlist unpaid scheduled payment amount. Normally invoices only have a single due date and amount. However we provide for installment payments which have multiple due dates and associated amounts. When invoices are first created this date will always be equal to the first entry in the DateDueList. Then as transactions are applied this "Current" Due Date is refreshed by figuring out which is the earliest unpaid scheduled payment.  */  
   DueDate:string,
      /**  Fiscal Year is duplicated from the related InvcGrp or based on ShipDate of Packing Slip. This is also refreshed if the InvoiceDate is changed.  */  
   FiscalYear:number,
      /**  Fiscal period of invoice. This is duplicated in from the InvcBatc or during the "get shipments" function it is determined based on the ShipDate of the packing slip or when the invoice date is changed. It is overrideable.  */  
   FiscalPeriod:number,
      /**  Once posted, maintenance is not allowed.  */  
   GLPosted:boolean,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   InvoiceAmt:number,
      /**  Total invoice Amount. This field is an accumulation of the extended net amounts of the detail line items (InvcDtl) and of the miscellaneous charges/credits (InvcMisc) records.  This field has a true sign. (credit memos are negative).  */  
   DocInvoiceAmt:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   InvoiceBal:number,
      /**  Current outstanding balance. Carries a true sign. (Credit memos are negative).  */  
   DocInvoiceBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   UnpostedBal:number,
      /**  Current outstanding balance which includes the unposted cash receipt amounts. This balance is updated immediately as cash is applied to the invoice, while the InvoiceBal field is not updated until the cash is posted.  Used by cash receipts to validate  online that an invoice is not over paid. Carries a true sign. (Credit memos are negative).  */  
   DocUnpostedBal:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DepositCredit:number,
      /**  Amount to be credited against the invoice total due to deposit payments against the sales order. This can be defaulted from OrderHed.DepositBal. This will be printed on the invoice as a separate line "Less Deposit of:"  This value updates the OrderHed.DepositBal. Do not allow OrderHed.DepositBal to become negative.  */  
   DocDepositCredit:number,
      /**  Stores the Sales Rep Codes for the invoice. Up to five codes can be  established. This field is not directly maintainable.  Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The defaults are based on the OrderHed.SalesRepList if a valid Order is referenced or first one is defaulted from the Customer master if ship to is blank else from the ShipTo.  */  
   SalesRepList:string,
      /**   This field is maintainable/viewable only for Credit Memos. It represents the invoice # that this credit memo relates to. It can be left blank. If entered it must be a valid InvcHead record where the InvcHead.CreditMemo = No. This field is also used to order the invoices when printing aging reports. The idea is to be able to print the credit memos next to their corresponding invoice. Therefore, this field will always have a value.

For Invoices it is equal to the InvoiceNum.

For Credit memos where they are not related to an invoice it is also set equal to the credit memo's InvoiceNum. In this later case when InvcHead.Credit = Yes and InvcHead.InvoiceNum = InvcHead.InvoiceRef the InvoiceRef is reset to zero before being displayed, then when written back to the database it is set = to the InvoiceNum if the user did not enter a related invoice.  */  
   InvoiceRef:number,
      /**  Value of this field is reference to invoice which has been cancelled by current invoice.  */  
   RefCancelled:number,
      /**  Value of this field is reference to invoice that cancelled this invoice.  */  
   RefCancelledBy:number,
      /**  An internal flag to indicate if this invoice was created by the Open Invoice Load program.  These records are not maintainable/viewable via invoice entry.  */  
   StartUp:boolean,
      /**  Contains the "list" of due dates for the scheduled payments. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDates:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   PayAmounts:string,
      /**  The scheduled payment amounts. Corresponds with the PayDates list. Delimited by the character defined in the "list-delim" variable.  */  
   DocPayAmounts:string,
      /**  Prompt payment discount date. This is calculated based on the Invoice date + Terms.DiscountDays. Not user maintainable. This will default into the cash receipt record if the scheduled due amount is being paid in full.  */  
   PayDiscDate:string,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   PayDiscAmt:number,
      /**  Amount of discount that would be given if paid on or before the specified PayDiscDate. Calculated using the Terms.DiscountPercent X Invoice total amount.  */  
   DocPayDiscAmt:number,
      /**  Contains the key  value for the Billing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMBCON as the default.  */  
   BillConNum:number,
      /**  Invoices that are within a data entry group can be put on "Hold". They will not be posted until InvoiceHeld=No.  This flag can be used for whatever the reason the user may wish to keep an invoice in a data entry group from being posted.  The Manufacturing System sets this flag when creating invoices for order line items which had been flagged for "Time & Material Invoicing" (OrderDtl.TMBilling)  */  
   InvoiceHeld:boolean,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**   Exchange rate that will be used for this invoice.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**   Journal number that invoice was posted to.  This can also be thought of as the Voucher Number. If ARSyst.ARVoucherInvoices = Yes then this value will be printed on the Invoice.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Journal that invoice was posted to.  */  
   JournalCode:string,
      /**  Used to differentiate between invoiced with standard lines which are for parts "PART"  and lines for service calls  "CALL" .  */  
   LineType:string,
      /**   The RMA number which generated this Credit Memo.
Note: This only applies to Credit Memos. 
It is assigned as part of the Request Credit process for an RMA and is not directly maintainable by Invoice Entry.  */  
   RMANum:number,
      /**  The Site that the invoice is relate to.  */  
   Plant:string,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**  External Identifier  */  
   ExternalID:string,
      /**  Cross reference invoice number used when converting data from another ERP system when the previous system data has alphanumeric content.  This field is not used by MfgSys.  This field can be used in searches and can be added to screens through customization.  */  
   XRefInvoiceNum:string,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   DepGainLoss:number,
      /**  For the Debit Note invoices this field contains the detail comments for the Debit Note. For the regular invoices this field contains the list of Debit Notes related to this invoice.  */  
   DNComments:string,
      /**  For the Debit Note invoice this field contains A Debit Note number assigned by the customer. The Debit Note number is supposed to be unique for the customer.  */  
   DNCustNbr:string,
      /**   Indicates the type of documents. Yes = Debit Note. This value can't be changed (the record is created on Invoice payment posting).
Debit Notes  also have the InvoiceSuffix field = "DN".  */  
   DebitNote:boolean,
      /**  This is populated from ShipHead.CustNum representing the Sold To customer.  */  
   SoldToCustNum:number,
      /**  Default is false.  This is only set to true if this invoice was generated via Get Shipments and shipments were combined based on common Bill To customer.  This is used by ARInvoice Entry to properly enable/disable Bill To customer field (InvcHead.CustNum) and to identify the record as a consolidated Invoice.  */  
   Consolidated:boolean,
      /**  If InvcHead.CustNum (BillTo) is different from InvcHead.SoldToCustNum (SoldTo), then this field defaults to the CustBillTo (Alt BillTo). InvoiceAddress status and SoldToInvoiceAddress is set to the opposite status.  */  
   BillToInvoiceAddress:boolean,
      /**  Always the opposite status of BillToInvoiceAddress.  If true, Invoice address for printing will use the Bill To address on the Sold-to customer.  If false, will use the Bill To address of the Bill to customer.  */  
   SoldToInvoiceAddress:boolean,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm1:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm2:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm3:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm4:number,
      /**  Contains the total commission amount for the corresponding sales rep (SalesRepList). This total is NOT MAINTAINABLE. It is updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain this total;  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount) * RepSplit) * RepRate).  */  
   RepComm5:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate1:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate2:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate3:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate4:number,
      /**  Establishes the default commission rates used for invoice line items. Defaults to OrderHed.RepRate if related to sales order.  */  
   RepRate5:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales1:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales2:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales3:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales4:number,
      /**  An array of five elements containing the total invoice sales amount for the corresponding sales reps (SalesRepList). These totals are NOT MAINTAINABLE. They are updated via write triggers on the InvcDtl record.  The following basic formula is used to maintain these totals:  If InvcDtl.Commissionable = Yes then the sales amount to accumulate is calculated as (((ShipQty/PriceFactor) * UnitPrice) - Discount . NOTE: miscellaneous charges/credits are NOT part of the sales total.  */  
   RepSales5:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit1:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit2:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit3:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit4:number,
      /**  Default Split percent for the invoice detail lines.  If related to a sales order then defaults to the OrderHed.RepSplit.  */  
   RepSplit5:number,
      /**  Indicates if the Credit Memo is for a Rebate  */  
   CMType:string,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  This flag will be used to indicate if the invoice is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the invoice which could affect taxes (InvcDtl, InvcHead, InvcMisc, etc). It defaults from ARSyst.InvcReadyToCalcDflt field when an invoice is created.  */  
   ReadyToCalc:boolean,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  used to force the recalc of an invoice before posting due to changes in tax connect data that could not be resolved at the time the change was made to the Epicor data.  */  
   RecalcBeforePost:boolean,
      /**  Rounding in Base is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Rounding in Customer currency  */  
   DocRounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt2DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt3DepositCredit:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3InvoiceBal:number,
      /**  Reporting currency value of this field  */  
   Rpt1PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt2PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt3PayAmounts:string,
      /**  Reporting currency value of this field  */  
   Rpt1PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3PayDiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt1UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt2UnpostedBal:number,
      /**  Reporting currency value of this field  */  
   Rpt3UnpostedBal:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Amount of deposit applied  */  
   DocDepApplied:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt1DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt2DepGainLoss:number,
      /**  Wherever the Less Advanced or Less Deposited is calculated, put any gain-loss difference into this field.  */  
   Rpt3DepGainLoss:number,
      /**  The date this invoice will get applied to the books when it is posted.  */  
   ApplyDate:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Tax point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  The last date finance/late charges have been calculated for this invoice.  */  
   LastChrgCalcDate:string,
      /**  Transaction document type id.  */  
   TranDocTypeID:string,
      /**  Total Finance Charge amount.  */  
   TotFinChrg:number,
      /**  Indicates if the document has been printed.  */  
   DocumentPrinted:boolean,
      /**  Contains the "list" of pay discount days for the scheduled discounts. Delimited by the character defined in the "List-Delim" variable.  */  
   PayDiscDays:string,
      /**  The discount percents. Corresponds with the PayDisDays list. Delimited by the character defined in the "list-delim" variable.  */  
   PayDiscPer:string,
      /**  Blocks certain invoice from generating finance/later charge.  */  
   BlockedFinChrg:boolean,
      /**  Reason why invoice has been blocked generating finance/later charge and only is enabled if the invoice is blocked.  */  
   BlockedFinChrgReason:string,
      /**  Withholding Tax Amount.  */  
   WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   DocWithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt1WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt2WithholdAmt:number,
      /**  Withholding Tax Amount.  */  
   Rpt3WithholdAmt:number,
      /**  Blocks certain invoice from being printed on reminder letters.  */  
   BlockedRemLetters:boolean,
      /**  Field to define when apply the discount percentage, can be when invoice is paid in full or Cash amount  */  
   PayDiscPartPay:boolean,
      /**  Reason why invoice has been blocked from being printed on reminder letters and only is enabled if the invoice is blocked.  */  
   BlockedRemLettersReason:string,
      /**  The actual ship date for the packing slip. Default as system date.  */  
   ShipDate:string,
      /**  Currency Rate Date  */  
   CurrRateDate:string,
      /**   Indicates if the invoice has been paid by a Payment Instrument.
Values:
blank = Not linked to a Payment Instrument
"O" = Paid by outstanding Payment Instrument
"C" = Paid by colledted Payment instument  */  
   PIPayment:string,
      /**  Unique identifier of the payment method  */  
   PMUID:number,
      /**  If TRUE taxes will be calculated based on the Alternate Bill To, if FALSE it will proceed normally.  */  
   UseAltBillTo:boolean,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Will be se to Yes if the Invoice was created by the Correction (Reversing) logic.  */  
   CorrectionInv:boolean,
      /**  Tax Rate Group Code  */  
   TaxRateGrpCode:string,
      /**  Locks Tax Rate and allows user to edit the tax exchange rate  */  
   LockTaxRate:boolean,
      /**  Sweden Finland Localization field - Banking Reference  */  
   SEBankRef:string,
      /**  Government Uniform Invoice Tax Type Code (Taiwan Localization field)  */  
   GUITaxTypeCode:string,
      /**  Government Uniform Invoice Format Code (Taiwan Localization field)  */  
   GUIFormatCode:string,
      /**  Government Uniform Invoice Deduct Code (Taiwan Localization field)  */  
   GUIDeductCode:string,
      /**  Reversal Doucment Amount  */  
   ReversalDocAmount:number,
      /**  Original Due Date at posting time  */  
   OrigDueDate:string,
      /**  The reference to CashHead.HeadNum.Used in deposit invoices  */  
   HeadNum:number,
      /**  Letter of Credit ID.  */  
   ARLOCID:string,
      /**  The free text field which can contain reference (such as Contract)  */  
   ContractRef:string,
      /**  Bank for Cash receipts. For Shipment Invoices it comes from Packing Slip. For Deposit Invoices created based on deposit payments it is actual bank money are received to. For other  Invoice types, default comes from 1) Sales Order 2) Bill To Customer 3) System default (Company).  */  
   OurBank:string,
      /**  Addition to Contract  */  
   ContractDate:string,
      /**  If the invoice was generated in Project Billing then it is reference to the project.  */  
   PBProjectID:string,
      /**  Deposit amount is transaction amount of deposit payment  */  
   DepositAmt:number,
      /**   Taiwan Localization
Export Bill Number  */  
   GUIExportBillNumber:string,
      /**  Deposit amount is transaction amount of deposit payment in document currency  */  
   DocDepositAmt:number,
      /**   Taiwan Localization
Date of Export  */  
   GUIDateOfExport:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt1 currency  */  
   Rpt1DepositAmt:number,
      /**   Taiwan Localization
Export Type  */  
   GUIExportType:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt2 currency  */  
   Rpt2DepositAmt:number,
      /**   Taiwan Localization
Export Mark  */  
   GUIExportMark:string,
      /**  Deposit amount is transaction amount of deposit payment in Rpt23currency  */  
   Rpt3DepositAmt:number,
      /**   Taiwan Localization
Export Bill Type  */  
   GUIExportBillType:string,
      /**  Deposit unallocated amount in base currency  */  
   DepUnallocatedAmt:number,
      /**  Day when a company sums up accounts receivables for each customer.  */  
   SummarizationDate:string,
      /**  Deposit unallocated amount in document currency  */  
   DocDepUnallocatedAmt:number,
      /**  Date when a company bills the customer  */  
   BillingDate:string,
      /**  Deposit unallocated amount in Rpt1 currency  */  
   Rpt1DepUnallocatedAmt:number,
      /**  Billing Number to be generated from Legal Numbering upon printing of billing statement.  */  
   BillingNumber:string,
      /**  Deposit unallocated amount in Rpt2 currency  */  
   Rpt2DepUnallocatedAmt:number,
      /**  Only records ready to bill will be printed in the Billing Statement  */  
   ReadyToBill:boolean,
      /**  Deposit unallocated amount in Rpt3 currency  */  
   Rpt3DepUnallocatedAmt:number,
      /**  Flag to indicate if the DefTaxDate will be overwritten when Tax Point change on Invoice Header.  */  
   OvrDefTaxDate:boolean,
      /**  Cross Reference Contract Number.  */  
   XRefContractNum:string,
      /**  Cross Reference Contract Date.  */  
   XRefContractDate:string,
      /**  Main Site  */  
   MainSite:boolean,
      /**  Site Code  */  
   SiteCode:string,
      /**  Branch ID  */  
   BranchID:string,
      /**  Customer Agent Name  */  
   CustAgentName:string,
      /**  Customer Agent Tax Region Number  */  
   CustAgentTaxRegNo:string,
      /**  Export Type: 0-No Export, 1-Normal Export(S04), 2-Material Export(S05), 3-Service Export(S06)  */  
   ExportType:string,
      /**  Export Report Number  */  
   ExportReportNo:string,
      /**  Real Estate Number  */  
   RealEstateNo:string,
      /**  Excluded  */  
   Excluded:boolean,
      /**  Deferred  */  
   Deferred:boolean,
      /**  CycleCode  */  
   CycleCode:string,
      /**  Duration  */  
   Duration:number,
      /**  EndDate  */  
   EndDate:string,
      /**  MaxValueAmt  */  
   MaxValueAmt:number,
      /**  DocMaxValueAmt  */  
   DocMaxValueAmt:number,
      /**  Rpt1MaxValueAmt  */  
   Rpt1MaxValueAmt:number,
      /**  Rpt2MaxValueAmt  */  
   Rpt2MaxValueAmt:number,
      /**  Rpt3MaxValueAmt  */  
   Rpt3MaxValueAmt:number,
      /**  HoldInvoice  */  
   HoldInvoice:boolean,
      /**  CopyLatestInvoice  */  
   CopyLatestInvoice:boolean,
      /**  OverrideEndDate  */  
   OverrideEndDate:boolean,
      /**  CycleInactive  */  
   CycleInactive:boolean,
      /**  RecurSource  */  
   RecurSource:boolean,
      /**  InstanceNum  */  
   InstanceNum:number,
      /**  RecurBalance  */  
   RecurBalance:number,
      /**  DocRecurBalance  */  
   DocRecurBalance:number,
      /**  Rpt1RecurBalance  */  
   Rpt1RecurBalance:number,
      /**  Rpt2RecurBalance  */  
   Rpt2RecurBalance:number,
      /**  Rpt3RecurBalance  */  
   Rpt3RecurBalance:number,
      /**  LastDate  */  
   LastDate:string,
      /**  RecurringState  */  
   RecurringState:string,
      /**  IsRecurring  */  
   IsRecurring:boolean,
      /**  InvoiceNumList  */  
   InvoiceNumList:string,
      /**  IsAddedToGTI  */  
   IsAddedToGTI:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  CHISRCodeLine  */  
   CHISRCodeLine:string,
      /**  CMReason  */  
   CMReason:string,
      /**  THIsImmatAdjustment  */  
   THIsImmatAdjustment:boolean,
      /**  AGAuthorizationCode  */  
   AGAuthorizationCode:string,
      /**  AGAuthorizationDate  */  
   AGAuthorizationDate:string,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  AGDocumentLetter  */  
   AGDocumentLetter:string,
      /**  AGInvoicingPoint  */  
   AGInvoicingPoint:string,
      /**  AGLegalNumber  */  
   AGLegalNumber:string,
      /**  AGPrintingControlType  */  
   AGPrintingControlType:string,
      /**  RevisionDate  */  
   RevisionDate:string,
      /**  RevisionNum  */  
   RevisionNum:number,
      /**  TWDeclareYear  */  
   TWDeclareYear:number,
      /**  TWDeclarePeriod  */  
   TWDeclarePeriod:number,
      /**  TWGenerationType  */  
   TWGenerationType:string,
      /**  TWGUIGroup  */  
   TWGUIGroup:string,
      /**  TWPeriodPrefix  */  
   TWPeriodPrefix:string,
      /**  Indicates if the Invoice is in Collections status  */  
   InvInCollections:boolean,
      /**   Indicates if the Customer of the Invoice is in Collections
(Peru Localization)  */  
   CollectionsCust:boolean,
      /**  A counter of the number of times an AR Invoice has been transmitted via EDI.  The counter is automatically incremented each time the EDIReady flag changes from False to True.  */  
   CounterARForm:number,
      /**  flag indicates if Revenue of the invoice has been already posted  */  
   PostedRecog:boolean,
      /**  Confirmation Date  */  
   CNConfirmDate:string,
      /**  MXSATSeal  */  
   MXSATSeal:string,
      /**  MXSerie  */  
   MXSerie:string,
      /**  MXTaxRcptType  */  
   MXTaxRcptType:string,
      /**  MXFiscalFolio  */  
   MXFiscalFolio:string,
      /**  MXTotalPayments  */  
   MXTotalPayments:number,
      /**  MXFolio  */  
   MXFolio:string,
      /**  MXCertifiedTimestamp  */  
   MXCertifiedTimestamp:string,
      /**  MXSATCertificateSN  */  
   MXSATCertificateSN:string,
      /**  MXDigitalSeal  */  
   MXDigitalSeal:string,
      /**  MXPostedTimeStamp  */  
   MXPostedTimeStamp:string,
      /**  MXCertificate  */  
   MXCertificate:string,
      /**  MXApprovalYear  */  
   MXApprovalYear:number,
      /**  MXCBB  */  
   MXCBB:string,
      /**  MXApprovalNum  */  
   MXApprovalNum:number,
      /**  MXOriginalStringTFD  */  
   MXOriginalStringTFD:string,
      /**  MXPaymentNum  */  
   MXPaymentNum:number,
      /**  MXPaidAs  */  
   MXPaidAs:string,
      /**  MXCertificateSN  */  
   MXCertificateSN:string,
      /**  MXOriginalAmount  */  
   MXOriginalAmount:number,
      /**  MXAccountNumber  */  
   MXAccountNumber:string,
      /**  MXOriginalDate  */  
   MXOriginalDate:string,
      /**  MXOriginalSeries  */  
   MXOriginalSeries:string,
      /**  MXOriginalFolio  */  
   MXOriginalFolio:string,
      /**  MXTaxRegime  */  
   MXTaxRegime:string,
      /**  MXOriginalString  */  
   MXOriginalString:string,
      /**  MXPaymentName  */  
   MXPaymentName:string,
      /**  EInvoice  */  
   EInvoice:boolean,
      /**  EInvStatus  */  
   EInvStatus:number,
      /**  EInvTimestamp  */  
   EInvTimestamp:string,
      /**  EInvUpdatedBy  */  
   EInvUpdatedBy:string,
      /**  EInvException  */  
   EInvException:string,
      /**  Flagged that this invoice has taxes which were necessary or is necessary now.  */  
   WithTaxConfirm:boolean,
      /**  UseAltBillToID  */  
   UseAltBillToID:boolean,
      /**  MXCancelledDate  */  
   MXCancelledDate:string,
      /**  Overpaid  */  
   Overpaid:boolean,
      /**  OrdExchangeRate  */  
   OrdExchangeRate:number,
      /**  PEAPPayNum  */  
   PEAPPayNum:number,
      /**  PEBankNumber  */  
   PEBankNumber:string,
      /**  PECharges  */  
   PECharges:number,
      /**  PECommissions  */  
   PECommissions:number,
      /**  PEDetTaxAmt  */  
   PEDetTaxAmt:number,
      /**  PEDetTaxCurrencyCode  */  
   PEDetTaxCurrencyCode:string,
      /**  PEDischargeAmt  */  
   PEDischargeAmt:number,
      /**  PEDischargeDate  */  
   PEDischargeDate:string,
      /**  PEInterest  */  
   PEInterest:number,
      /**  PENoPayPenalty  */  
   PENoPayPenalty:number,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   PESUNATDepAmt:number,
      /**  CSF Peru - SUNAT Deposit Date  */  
   PESUNATDepDate:string,
      /**  CSF Peru -  SUNAT Deposit Number  */  
   PESUNATDepNum:string,
      /**  PEBOEPosted  */  
   PEBOEPosted:boolean,
      /**  DocPEInterest  */  
   DocPEInterest:number,
      /**  DocPECommissions  */  
   DocPECommissions:number,
      /**  DocPECharges  */  
   DocPECharges:number,
      /**  DocPENoPayPenalty  */  
   DocPENoPayPenalty:number,
      /**  DocPEDischargeAmt  */  
   DocPEDischargeAmt:number,
      /**  DocPEDetTaxAmt  */  
   DocPEDetTaxAmt:number,
      /**  Rpt1PEInterest  */  
   Rpt1PEInterest:number,
      /**  Rpt1PECommissions  */  
   Rpt1PECommissions:number,
      /**  Rpt1PECharges  */  
   Rpt1PECharges:number,
      /**  Rpt1PENoPayPenalty  */  
   Rpt1PENoPayPenalty:number,
      /**  Rpt1PEDischargeAmt  */  
   Rpt1PEDischargeAmt:number,
      /**  Rpt2PEInterest  */  
   Rpt2PEInterest:number,
      /**  Rpt2PECommissions  */  
   Rpt2PECommissions:number,
      /**  Rpt2PECharges  */  
   Rpt2PECharges:number,
      /**  Rpt2PENoPayPenalty  */  
   Rpt2PENoPayPenalty:number,
      /**  Rpt2PEDischargeAmt  */  
   Rpt2PEDischargeAmt:number,
      /**  Rpt3PEInterest  */  
   Rpt3PEInterest:number,
      /**  Rpt3PECommissions  */  
   Rpt3PECommissions:number,
      /**  Rpt3PECharges  */  
   Rpt3PECharges:number,
      /**  Rpt3PENoPayPenalty  */  
   Rpt3PENoPayPenalty:number,
      /**  Rpt3PEDischargeAmt  */  
   Rpt3PEDischargeAmt:number,
      /**  Our Supplier Code  */  
   OurSupplierCode:string,
      /**  PEGuaranteeName  */  
   PEGuaranteeName:string,
      /**  PEGuaranteeAddress1  */  
   PEGuaranteeAddress1:string,
      /**  PEGuaranteeAddress2  */  
   PEGuaranteeAddress2:string,
      /**  PEGuaranteeAddress3  */  
   PEGuaranteeAddress3:string,
      /**  PEGuaranteeCity  */  
   PEGuaranteeCity:string,
      /**  PEGuaranteeState  */  
   PEGuaranteeState:string,
      /**  PEGuaranteeZip  */  
   PEGuaranteeZip:string,
      /**  PEGuaranteeCountry  */  
   PEGuaranteeCountry:string,
      /**  PEGuaranteeTaxID  */  
   PEGuaranteeTaxID:string,
      /**  PEGuaranteePhoneNum  */  
   PEGuaranteePhoneNum:string,
      /**  PEBOEStatus  */  
   PEBOEStatus:string,
      /**  PEBOEIsMultiGen  */  
   PEBOEIsMultiGen:boolean,
      /**  PE Reference Document ID  */  
   PERefDocID:string,
      /**  PE Reason Code  */  
   PEReasonCode:string,
      /**  PE Reason Description  */  
   PEReasonDesc:string,
      /**  TW GUI Code Seller  */  
   TWGUIRegNumSeller:string,
      /**  TW GUI Code Buyer  */  
   TWGUIRegNumBuyer:string,
      /**  Document Name  */  
   TWGUIExportDocumentName:string,
      /**  Remarks  */  
   TWGUIExportRemarks:string,
      /**  Verification  */  
   TWGUIExportVerification:string,
      /**  PEDebitNoteReasonCode  */  
   PEDebitNoteReasonCode:string,
      /**  PEDebitNote  */  
   PEDebitNote:boolean,
      /**  MXPartPmt  */  
   MXPartPmt:boolean,
      /**  Tax Invoice Type  */  
   CNTaxInvoiceType:number,
      /**  MXExportOperationType  */  
   MXExportOperationType:string,
      /**  MXExportCustDocCode  */  
   MXExportCustDocCode:string,
      /**  MXExportCertOriginNum  */  
   MXExportCertOriginNum:string,
      /**  MXExportConfNum  */  
   MXExportConfNum:string,
      /**  MXExportCertOrigin  */  
   MXExportCertOrigin:boolean,
      /**  MXIncoterm  */  
   MXIncoterm:string,
      /**  AGDocConcept  */  
   AGDocConcept:number,
      /**  Electronic Invoice reference number  */  
   EInvRefNum:string,
      /**  Export document reference number  */  
   ExportDocRefNum:string,
      /**  Export document date  */  
   ExportDocDate:string,
      /**  Tax Transaction ID  */  
   INTaxTransactionID:string,
      /**  MXMovingReasonFlag  */  
   MXMovingReasonFlag:boolean,
      /**  MXMovingReason  */  
   MXMovingReason:string,
      /**  MXNumRegIdTrib  */  
   MXNumRegIdTrib:string,
      /**  MXResidenCountryNum  */  
   MXResidenCountryNum:number,
      /**  MXPurchaseType  */  
   MXPurchaseType:string,
      /**  MXConfirmationCode  */  
   MXConfirmationCode:string,
      /**  MXExternalCode  */  
   MXExternalCode:string,
      /**  This invoice was created via an integration with a third-party field service.  */  
   ServiceInvoice:boolean,
      /**  MXDomesticTransfer  */  
   MXDomesticTransfer:boolean,
      /**  MXCancellationMode  */  
   MXCancellationMode:string,
      /**  Shipping Port Code  */  
   INShippingPortCode:string,
      /**  Export Procedure  */  
   INExportProcedure:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  DigitalSignature  */  
   DigitalSignature:string,
      /**  SignedOn  */  
   SignedOn:string,
      /**  SignedBy  */  
   SignedBy:string,
      /**  FirstPrintDate  */  
   FirstPrintDate:string,
      /**  DocCopyNum  */  
   DocCopyNum:number,
      /**  DepositBalance  */  
   DepositBalance:number,
      /**  DocDepositBalance  */  
   DocDepositBalance:number,
      /**  Rpt1DepositBalance  */  
   Rpt1DepositBalance:number,
      /**  Rpt2DepositBalance  */  
   Rpt2DepositBalance:number,
      /**  Rpt3DepositBalance  */  
   Rpt3DepositBalance:number,
      /**  Quote number to which this invoice record is associated with.  */  
   QuoteNum:number,
      /**  The help desk case related to this invoice.  */  
   HDCaseNum:number,
      /**  Indicates that the credit hold was overridden for this invoice.  */  
   CreditOverride:boolean,
      /**  Description	Indicates that the credit hold was overridden for this invoice.	The date and time the user override the invoice credit hold.  */  
   CreditOverrideDate:string,
      /**  The user id that override the invoice credit hold.  */  
   CreditOverrideUserID:string,
      /**  Indicates the invoice is on credit hold.  Applicable to miscellaneous invoices only.  */  
   CreditHold:boolean,
      /**  Peru Electronic Invoice XML Type  */  
   PEXMLType:number,
      /**  COCreditMemoReasonCode  */  
   COCreditMemoReasonCode:string,
      /**  CODebitMemoReasonCode  */  
   CODebitMemoReasonCode:string,
      /**  COReasonDesc  */  
   COReasonDesc:string,
      /**  CODebitNote  */  
   CODebitNote:boolean,
      /**  PEDetractionTranNum  */  
   PEDetractionTranNum:number,
      /**  PEProductCode  */  
   PEProductCode:string,
      /**  PECollectionGroupID  */  
   PECollectionGroupID:string,
      /**  PE Caption Code  */  
   PECaptionCode:string,
      /**  PE Caption Code Description  */  
   PECaption:string,
      /**  PE Reference DocumentType 1  */  
   PERefDocumentType:string,
      /**  PE Reference Document Number 1  */  
   PERefDocumentNumber:string,
      /**  PE Detraction good or service code  */  
   PEDetrGoodServiceCode:string,
      /**  PE Reference DocumentType 2  */  
   PERefDocumentType2:string,
      /**  PE Reference DocumentType 3  */  
   PERefDocumentType3:string,
      /**  PE Reference DocumentType 4  */  
   PERefDocumentType4:string,
      /**  PE Reference DocumentType 5  */  
   PERefDocumentType5:string,
      /**  PE Reference Document Number 2  */  
   PERefDocumentNumber2:string,
      /**  PE Reference Document Number 3  */  
   PERefDocumentNumber3:string,
      /**  PE Reference Document Number 4  */  
   PERefDocumentNumber4:string,
      /**  PE Reference Document Number 5  */  
   PERefDocumentNumber5:string,
      /**  E-invoice  */  
   ELIEInvoice:boolean,
      /**  Status of E-invoice (1 - Open, 2 - Generated, 3 - Sent, 4 - Error).  */  
   ELIEInvStatus:number,
      /**  User Id of the person generated E-invoice.  */  
   ELIEInvUpdatedBy:string,
      /**  E-invoice error description.  */  
   ELIEInvException:string,
      /**  Date and Time of E-invoice generation.  */  
   ELIEInvUpdatedOn:string,
      /**  COOperType  */  
   COOperType:string,
      /**  Flag that indicates if the Invoice is for Central Collection.  */  
   CentralCollection:boolean,
      /**  Company that created this invoice.  */  
   CColChildCompany:string,
      /**  Central Collection company.  */  
   CColParentCompany:string,
      /**  Order number on the invoicing company.  */  
   CColOrderNum:number,
      /**  Invoice number on the invoicing company.  */  
   CColChildInvoiceNum:number,
      /**  Invoice number on central collection company  */  
   CColInvoiceNum:number,
      /**  Legal number on the invoicing company invoice.  */  
   CColChildLegalNumber:string,
      /**  Legal number on central collection company.  */  
   CColLegalNumber:string,
      /**  Invoice reference on the Invoicing Company.  */  
   CColInvoiceRef:number,
      /**  Invoice Balance in the Central Collection company.  */  
   CColInvBal:number,
      /**  Central Collection Doc Invoice Balance.  */  
   DocCColInvBal:number,
      /**  Invoice Amount on the Invoicing Company.  */  
   CColInvAmt:number,
      /**  Invoice Amount on the Invoicing Company.  */  
   DocCColInvAmt:number,
      /**  Rpt 1 Parent Invoice Balance  */  
   Rpt1CColInvBal:number,
      /**  Rpt 2 Parent Invoice Balance  */  
   Rpt2CColInvBal:number,
      /**  Rpt 3 Parent Invoice Balance  */  
   Rpt3CColInvBal:number,
      /**  Rpt 1 Child Invoice Amount  */  
   Rpt1CColInvAmt:number,
      /**  Rpt 2 Child Invoice Amount  */  
   Rpt2CColInvAmt:number,
      /**  Rpt 3 Child Invoice Amount  */  
   Rpt3CColInvAmt:number,
      /**  Id of the netting transaction that generated this document.  */  
   NettingID:number,
      /**  User terminal name  */  
   ELIEInvTerminalName:string,
      /**  User terminal IP  */  
   ELIEInvTerminalIP:string,
      /**  GL Description  */  
   Description:string,
      /**  WithholdAcctToInterim  */  
   WithholdAcctToInterim:boolean,
      /**  Indicates if the Central Collection parent invoice is open.  */  
   CColOpenInvoice:boolean,
      /**  AGQRCodeData  */  
   AGQRCodeData:string,
      /**  Exempt Reason Code  */  
   ExemptReasonCode:string,
      /**  EInvoice ID  */  
   ELIEInvID:string,
      /**  this is a link to the service call that this invoice is for.  Linetype = "CALL"  */  
   CallNum:number,
      /**  this is a link to the service call line that this invoice is for.  Linetype = "CALL"  */  
   CallLine:number,
      /**  Associates the Call Line record back its linked jobnum  */  
   JobNum:string,
      /**  MXCancelReasonCode  */  
   MXCancelReasonCode:string,
      /**  MXSubstInvoiceNum  */  
   MXSubstInvoiceNum:number,
      /**  MXExportType  */  
   MXExportType:string,
      /**  MXGlobalInvoicePeriod  */  
   MXGlobalInvoicePeriod:string,
      /**  MXGlobalInvoiceMonth  */  
   MXGlobalInvoiceMonth:string,
      /**  ELIEInvServiceProviderStatus  */  
   ELIEInvServiceProviderStatus:number,
      /**  Incoterm Code  */  
   IncotermCode:string,
      /**  Incoterm Location  */  
   IncotermLocation:string,
      /**  CovenantDiscPercent  */  
   CovenantDiscPercent:number,
      /**  TotalCovenantDiscount  */  
   TotalCovenantDiscount:number,
      /**  DocCovenantDiscount  */  
   DocCovenantDiscount:number,
      /**  Rpt1CovenantDiscount  */  
   Rpt1CovenantDiscount:number,
      /**  Rpt2CovenantDiscount  */  
   Rpt2CovenantDiscount:number,
      /**  Rpt3CovenantDiscount  */  
   Rpt3CovenantDiscount:number,
      /**  TotalInCovenantDiscount  */  
   TotalInCovenantDiscount:number,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  Total advanced billing amount.  */  
   ABAmt:number,
      /**  Indicates if changes can occur after the document has been printed  */  
   AllowChgAfterPrint:boolean,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
      /**  ARPNHead's HeadNum  */  
   ARPNHeadNum:number,
      /**  when InvcHead.PIPayment = O then populate ARPaymentInstrumentID with a value of PI.  */  
   ARPromNoteID:string,
      /**  Auto generate payment instruments  */  
   AutoGenPN:boolean,
      /**  Delimited list of available bill to customers.  */  
   AvailBTCustList:string,
      /**  Used for Bill of Exchange.  Indicates the bank to use when a payment instrument for the invoice is created.  */  
   BankForPI:string,
   BankForPIName:string,
      /**  Customer ID for the bill to customer (InvcHead.CustNum).  */  
   BTCustID:string,
      /**  Bill to customer name.  */  
   BTCustomerName:string,
      /**  The date and time that the record was last changed  */  
   ChangeDateTime:string,
   CNGTIAction:string,
   CNGTIAddress:string,
   CNGTIBankAccount:string,
   CNGTIComment:string,
   CNGTICustomerName:string,
   CNGTIExportAddress:string,
      /**  CSF China, Gross Invoice Amount  */  
   CNGTIGrossInvcAmt:number,
      /**  CSF China, Total invoice amount = InvcHead.InvoiceAmt - InvcHead.WithholdAmt  */  
   CNGTIInvoiceAmt:number,
   CNGTINote:string,
   CNGTIShipToNum:string,
   CNGTIStatus1:string,
   CNGTIStatus2:boolean,
   CNGTITaxCode:string,
      /**  IFRS Calculation. If the checkbox is not checked then all the elements below are disabled. If the checkbox is checked, then some elements below become enabled showing default values so that the NPV can be calculated  */  
   COIFRSCalculation:boolean,
      /**  If true then Colombia IFRS Net Present Value calculation is enabled  */  
   COIFRSEnabled:boolean,
      /**  Financial Charge  */  
   COIFRSFinancialCharge:number,
   COIFRSInterestRate:number,
      /**  Number of Periods for payment  */  
   COIFRSNumberOfPeriods:number,
      /**  Present Value  */  
   COIFRSPresentValue:number,
      /**  Indicates if Invoice is in Collections (Peru localization)  */  
   CollectionsInv:boolean,
      /**  Contact email address.  */  
   ContactEmailAddr:string,
      /**  Contact fax number  */  
   ContactFaxNum:string,
      /**  Contact name  */  
   ContactName:string,
      /**  Contact phone number  */  
   ContactPhoneNum:string,
      /**  record converted from deposit  */  
   ConvertedFromDep:boolean,
   COOperTypeDesc:string,
      /**  True if the Country set for the current company contains an Intrastat code.  */  
   CountryIntrastat:boolean,
   CumulativeBalance:number,
      /**  Currncy switch used to determine what currency to display amounts in.  */  
   CurrencySwitch:boolean,
   CurrentInstanceNum:number,
   CustAllowOTS:boolean,
   CustOnCreditHold:boolean,
      /**  Deposit balance from CashHed  */  
   DepBal:number,
      /**  Deposit credit enabled flag.  */  
   DepositCreditEnabled:boolean,
   DirectDebiting:boolean,
      /**  The flag to indicate if Invoice Header Apply Date is supposed to be Read Only  */  
   DisableAplDate:boolean,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   DispBalDN:number,
      /**  Bill to address in list format.  */  
   DisplayBillAddr:string,
      /**  Display field for the masked credit card number  */  
   DisplayCreditCardNum:string,
   DisplayCurrencyID:string,
      /**  Currency display symbol  */  
   DisplaySymbol:string,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   DNPmtAmt:number,
      /**  Document Total advanced billing amount.  */  
   DocABAmt:number,
      /**  Financial Charge  */  
   DocCOIFRSFinancialCharge:number,
      /**  Present Value  */  
   DocCOIFRSPresentValue:number,
   DocCumulativeBalance:number,
      /**  Document deposit amount from cashhead.  */  
   DocDepBal:number,
      /**  The net of Invoice Balance and unposted Debit Note value(s) applied to the invoice during one particular Cash Receipt application.  */  
   DocDispBalDN:number,
      /**  Document display symbol  */  
   DocDisplaySymbol:string,
      /**  The unposted Debit Note value(s) applied to the invoice during the particular invoice payment transaction.  */  
   DocDNPmtAmt:number,
   DocDspPrepDeposit:number,
   DocDspTaxAmt:number,
      /**  CSF Peru - SUNAT Deposit Amount  */  
   DocPESUNATDepAmt:number,
   DocRemainTaxAmt:number,
   DocReverseTaxAmt:number,
   DocSATaxAmt:number,
   DocSourceRecurBalance:number,
      /**  Document sub total  */  
   DocSubTotal:number,
      /**  Document Total tax amount from InvcTax for Collection type 'Invoice'  */  
   DocTaxAmt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in document currency.  */  
   DocVr:number,
   DocWHTaxAmt:number,
      /**  Display advance billing amount  */  
   DspABAmt:number,
      /**  Display deposit balance.  */  
   DspDepBal:number,
      /**  Display deposit credit.  */  
   DspDepCr:number,
   DspDigitalSignature:string,
      /**  Display document advance billing amount  */  
   DspDocABAmt:number,
      /**  Display document deposit balance  */  
   DspDocDepBal:number,
      /**  Display document deposit credit.  */  
   DspDocDepCr:number,
      /**  Display document invoice amount  */  
   DspDocInvoiceAmt:number,
      /**  Display document invoice balance  */  
   DspDocInvoiceBal:number,
      /**  Display Invoice Doc Rounding  */  
   DspDocRounding:number,
      /**  display document sub total  */  
   DspDocSubTotal:number,
      /**  Display invoice amount  */  
   DspInvoiceAmt:number,
      /**  Display Invoice Balance.  */  
   DspInvoiceBal:number,
      /**  Display invoice reference  */  
   DspInvoiceRef:number,
   DspPayDiscDays:string,
   DspPrepDeposit:number,
      /**  Display Rounding in Base  */  
   DspRounding:number,
      /**  If SoldTo and Alt-Bill to are the same, this displays as null.  */  
   dspSoldToCustID:string,
      /**  Display sub total  */  
   DspSubTotal:number,
   DspTaxAmt:number,
      /**  Indicates if assign legal number option is available.  */  
   EnableAssignLegNum:boolean,
   EnableCentralCollection:boolean,
      /**  Flag to determine if UseSOCCDefaults should be enabled.  */  
   EnableSOCCDefaults:boolean,
      /**  Indicates if TranDocTypeID is available for input.  */  
   EnableTranDocType:boolean,
      /**  Indicates if the void legal number option is available  */  
   EnableVoidLegNum:boolean,
      /**  It will be displayed to identify invoices automatically generated due ERS shipments.  */  
   ERSInvoice:boolean,
      /**  Indicates which date to be used to calculate the exchange rate, I for Invoice Date, A for Apply Date.  */  
   ExchangeRateDate:string,
      /**  Flag for update of InvcHead to allow when group id is "RMACRREQ"  */  
   GenedFromRMA:boolean,
      /**  CustBank record exists for customer  */  
   HasBank:boolean,
      /**  Indicates if a legal number configuration exists for ar invoices/credit memos  */  
   HasLegNumCnfg:boolean,
      /**  In case if Invoice Header Tax Liability is not assigned this flag indicates if any of Invoice lines has Tax inclusive Tax Liability assinged  */  
   InPriceLn:boolean,
      /**  Integration invoice type.  Used for setting of InvoiceType.  */  
   IntInvoiceType:string,
      /**  InvoiceType description  */  
   InvoiceTypeDesc:string,
      /**  Denmark localization external field  */  
   IsDK:boolean,
      /**  Set to true if intrastat is enabled.  */  
   IsIntrastatSensitive:boolean,
   IsLatestRecurrence:boolean,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Indicates if the UR Invoice was created from an On Account PI instead of an on account cash receipt.  */  
   IsPIUnappliedReceipt:boolean,
   IsPMForGenPIType:boolean,
   LatestInvoice:number,
      /**  Stores the message when a legal number is generated.  */  
   LegalNumberMessage:string,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  MXCancellationID  */  
   MXCancellationID:string,
      /**  MXCancellationStatus  */  
   MXCancellationStatus:string,
      /**  It indicates that this Invoice has taxes, for which the confirmation is required.  */  
   NeedConfirmTaxes:boolean,
      /**  This field is to display in Cash Receipt Entry the Discount Date that the payment will take.  */  
   NextDiscDate:string,
      /**  NextInvoiceDate = InvcRecurringCycle.LastDate + RecurringCycle.Interval in RecurringCycle.Modifier units  */  
   NextInvoiceDate:string,
      /**  Pack slip number from the 1st line item.  */  
   PackSlipNum:number,
      /**  Pay schedule enabled flag  */  
   PaySchedEnabled:boolean,
      /**  Indicates what the user will change the status to  */  
   PEBOEChangeStatusTo:string,
   PEBOEStatusDesc:string,
      /**  Peru CSF: Collections date  */  
   PECollectionsDate:string,
      /**  PE Detraction good or service code description  */  
   PEDetrGoodServiceCodeDesc:string,
   PEDspCurrencySymbol:string,
      /**  Peru CSF: No if the invoice is moved out of collections, Yes if the invoice is moved into colletions.  */  
   PEInCollections:boolean,
      /**  PE Document Type Description  */  
   PERefDocumentTypeDesc:string,
      /**  PE Document Type Description 2  */  
   PERefDocumentTypeDesc2:string,
      /**  PE Document Type Description 3  */  
   PERefDocumentTypeDesc3:string,
      /**  PE Document Type Description 4  */  
   PERefDocumentTypeDesc4:string,
      /**  PE Document Type Description 5  */  
   PERefDocumentTypeDesc5:string,
      /**  PI - Bank account  */  
   PIBankAcctID:string,
      /**  PI Customer bank required  */  
   PICustBankDtl:boolean,
      /**  PI Initiation - generated or received  */  
   PIInitiation:string,
      /**  Prep Deposit enabled flag.  */  
   PrepDepositEnabled:boolean,
      /**  The description of the proposed Tax Region  */  
   ProposedTaxRgn:string,
      /**   This field indicates id all the amounts related to the invoice are supposed to be re-calculated on change of the Applate Date.
"R" - the user's answer is recalculate the amounts
"N" the user's answer is  do not recalculate the amount
Blank - user is not asked  */  
   RecalcAmts:string,
      /**  Recurring flag  */  
   Recurring:boolean,
   RemainTaxAmt:number,
   ReminderSeq:number,
      /**  Accumulate all reversal amounts of Credit Memos with the reference to the invoice  */  
   ReversalDocAmt:number,
   ReverseTaxAmt:number,
   Rpt1ABAmt:number,
      /**  Financial Charge  */  
   Rpt1COIFRSFinancialCharge:number,
      /**  Present Value  */  
   Rpt1COIFRSPresentValue:number,
   Rpt1CumulativeBalance:number,
   Rpt1DepBal:number,
   Rpt1DspABAmt:number,
   Rpt1DspDepBal:number,
   Rpt1DspDepCr:number,
   Rpt1DspInvoiceAmt:number,
   Rpt1DspInvoiceBal:number,
   Rpt1DspPrepDeposit:number,
   Rpt1DspRounding:number,
   Rpt1DspSubTotal:number,
   Rpt1DspTaxAmt:number,
   Rpt1RemainTaxAmt:number,
   Rpt1ReverseTaxAmt:number,
   Rpt1SATaxAmt:number,
   Rpt1SourceRecurBalance:number,
   Rpt1SubTotal:number,
   Rpt1TaxAmt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt1 currency.  */  
   Rpt1Vr:number,
   Rpt1WHTaxAmt:number,
   Rpt2ABAmt:number,
      /**  Financial Charge  */  
   Rpt2COIFRSFinancialCharge:number,
      /**  Present Value  */  
   Rpt2COIFRSPresentValue:number,
   Rpt2CumulativeBalance:number,
   Rpt2DepBal:number,
   Rpt2DspABAmt:number,
   Rpt2DspDepBal:number,
   Rpt2DspDepCr:number,
   Rpt2DspInvoiceAmt:number,
   Rpt2DspInvoiceBal:number,
   Rpt2DspPrepDeposit:number,
   Rpt2DspRounding:number,
   Rpt2DspSubTotal:number,
   Rpt2DspTaxAmt:number,
   Rpt2RemainTaxAmt:number,
   Rpt2ReverseTaxAmt:number,
   Rpt2SATaxAmt:number,
   Rpt2SourceRecurBalance:number,
   Rpt2SubTotal:number,
   Rpt2Taxamt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt2 currency.  */  
   Rpt2Vr:number,
   Rpt2WHTaxAmt:number,
   Rpt3ABAmt:number,
      /**  Financial Charge  */  
   Rpt3COIFRSFinancialCharge:number,
      /**  Present Value  */  
   Rpt3COIFRSPresentValue:number,
   Rpt3CumulativeBalance:number,
   Rpt3DepBal:number,
   Rpt3DspABAmt:number,
   Rpt3DspDepBal:number,
   Rpt3DspDepCr:number,
   Rpt3DspInvoiceAmt:number,
   Rpt3DspInvoiceBal:number,
   Rpt3DspPrepDeposit:number,
   Rpt3DspRounding:number,
   Rpt3DspSubTotal:number,
   Rpt3DspTaxAmt:number,
   Rpt3RemainTaxAmt:number,
   Rpt3ReverseTaxAmt:number,
   Rpt3SATaxAmt:number,
   Rpt3SourceRecurBalance:number,
   Rpt3SubTotal:number,
   Rpt3TaxAmt:number,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in Rpt3 currency.  */  
   Rpt3Vr:number,
   Rpt3WHTaxAmt:number,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  1st entry in SalesRepList  */  
   SalesRepCode1:string,
      /**  2nd entry in SalesRepList  */  
   SalesRepCode2:string,
      /**  3rd entry in SalesRepList.  */  
   SalesRepCode3:string,
      /**  4th entry in SalesRepList  */  
   SalesRepCode4:string,
      /**  5th entry in SalesRepList  */  
   SalesRepCode5:string,
      /**  1st sales rep name  */  
   SalesRepName1:string,
      /**  2nd sales rep name  */  
   SalesRepName2:string,
      /**  3rd sales rep name  */  
   SalesRepName3:string,
      /**  4th sales rep name  */  
   SalesRepName4:string,
      /**  5th sales rep name  */  
   SalesRepName5:string,
   SATaxAmt:number,
      /**  Boolean for selection of invoices in grid  */  
   Selected:boolean,
   SkipRecurring:boolean,
      /**  Sold to address list.  */  
   SoldToAddressList:string,
      /**  Sold to customer id  */  
   SoldToCustID:string,
      /**  Sold to customer name.  */  
   SoldToCustomerName:string,
   SourceInvoiceNum:number,
   SourceLastDate:string,
   SourceRecurBalance:number,
      /**  Sub total for invoice  */  
   SubTotal:number,
      /**  The system transaction type - ARInvoice or CreditMemo.  Used to filter combo list for TranDocTypeID.  */  
   SystemTranType:string,
      /**  Total tax amount from InvcTax  */  
   TaxAmt:number,
   TaxExchangeRate:number,
      /**  The flag to indicate if the user is supposed to be asked about Tax Liability change  */  
   TaxRgnLineChange:boolean,
   TotalInstanceNum:number,
      /**  This field is used when invoice is transferred to another Invoice Group and the user has a chance to change the Apply date of the invoice transferred.  */  
   TransApplyDate:string,
      /**  If true, the credit card info will come from the sales order.  */  
   UseSOCCDefaults:boolean,
   UseTaxRate:boolean,
   VNInvDescription:string,
   VNInvoiceType:string,
      /**  Difference between Deposit Amount from invoice header and Total Line Amount in base currency.  */  
   Vr:number,
   WHTaxAmt:number,
      /**  Currency label  */  
   XRateLabel:string,
   zEnableCreditHold:boolean,
      /**  The number of days the invoice is past due.  */  
   AgingDays:number,
      /**   The list of prohibited statuses.for the Invoice
For examle, if contains 2 (EINVOICE_STATUS_GENERATED) then Generate E-invoice is not allowed.
if contains 2 (EINVOICE_STATUS_SENT) then Sending Invoice via Service provider is not allowed  */  
   ELIEInvProhibitedStatuses:string,
      /**  Flag indicating whether to enable Incoterm Location  */  
   EnableIncotermLocation:boolean,
   BitFlag:number,
   AGInvoicingPointDescription:string,
   ARSystLNReqForInvc:boolean,
   CardTypeDescription:string,
   CurrencyCodeCurrencyID:string,
   CurrencyCodeCurrSymbol:string,
   CurrencyCodeCurrDesc:string,
   CurrRateGrpDescription:string,
   CustomerInactive:boolean,
   CustomerMXGeneralPublic:boolean,
   CustomerCustID:string,
   CustomerBTName:string,
   CustomerName:string,
   CustomerELISendingOption:number,
   FOBDescription:string,
   IncotermsDescription:string,
   JournalCodeJrnlDescription:string,
   MXPurchaseTypeCodeDesc:string,
   MXSubstInvoiceMXFiscalFolio:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   OurBankPayerRef:string,
   OurBankBankIdentifier:string,
   OurBankTypeCode:string,
   OurBankBankAcctID:string,
   OurBankCheckingAccount:string,
   OurBankBankName:string,
   OurBankIBANCode:string,
   OurBankLocalBIC:string,
   OurBankDescription:string,
   PayMethodName:string,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodType:number,
   PlantName:string,
   ProjectDescription:string,
   RecurringCycleMaximumValue:boolean,
   SoldToCustNumInactive:boolean,
   SoldToCustNumCustID:string,
   SoldToCustNumName:string,
   TaxRateGrpDescription:string,
   TaxRegionDescription:string,
   TermsCodeDescription:string,
   TranDocTypeDescription:string,
   XbSystOCRCalcType:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvcHeadTableset{
   InvcHead:Erp_Tablesets_InvcHeadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PEARInvSelBOTableset{
   PEARInvSel:Erp_Tablesets_PEARInvSelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PEARInvSelRow{
   Selected:boolean,
   InvoiceNum:number,
   LegalNumber:string,
   CustNum:number,
   Name:string,
   ApplyDate:string,
   DetractionTaxAmt:number,
   LastCashReceiptDate:string,
   ProductCode:string,
   CustID:string,
   CurrencyCode:string,
   DocDetractionTaxAmt:number,
   DueDate:string,
   InvoiceDate:string,
   CustBalance:number,
   CustAmount:number,
   Balance:number,
   InvoiceAmt:number,
   PECollectionsDate:string,
   InvInCollections:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UpdExtCreditManagerTableset{
   CMCustomer:Erp_Tablesets_CMCustomerRow[],
   CustomCrdPool:Erp_Tablesets_CustomCrdPoolRow[],
   GlbCustCred:Erp_Tablesets_GlbCustCredRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param inpFileName
      @param inpIncludeZero
      @param pNumberFormat
   */  
export interface ExportCustCreditFile_input{
      /**  Name that the exported file will have assigned to it  */  
   inpFileName:string,
      /**  A logical flag to indicate whether to include 0 Credit Limit Customers.  */  
   inpIncludeZero:boolean,
      /**  Number Format American/European.  */  
   pNumberFormat:string,
}

export interface ExportCustCreditFile_output{
   returnObj:Erp_Tablesets_ExportCustCredTableset[],
parameters : {
      /**  output parameters  */  
   msg:string,
}
}

   /** Required : 
      @param inpIncludeZero
      @param pNumberFormat
   */  
export interface ExportCustCredit_input{
      /**  A logical flag to indicate whether to include 0 Credit Limit Customers.  */  
   inpIncludeZero:boolean,
      /**  Number Format American/European.  */  
   pNumberFormat:string,
}

export interface ExportCustCredit_output{
   returnObj:Erp_Tablesets_ExportCustCredTableset[],
}

   /** Required : 
      @param ipCustID
   */  
export interface GetARLOC_input{
   ipCustID:string,
}

export interface GetARLOC_output{
   returnObj:Erp_Tablesets_ARLOCTableset[],
}

   /** Required : 
      @param custID
   */  
export interface GetByCustID_input{
      /**  The customer character ID  */  
   custID:string,
}

export interface GetByCustID_output{
   returnObj:Erp_Tablesets_CreditManagerTableset[],
}

   /** Required : 
      @param custNum
   */  
export interface GetByID_input{
   custNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CreditManagerTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CreditManagerTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CreditManagerTableset[],
}

   /** Required : 
      @param ipCustID
   */  
export interface GetCashDeposits_input{
   ipCustID:string,
}

export interface GetCashDeposits_output{
   returnObj:Erp_Tablesets_AllocDepositsTableset[],
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

   /** Required : 
      @param ipCustID
   */  
export interface GetContacts_input{
   ipCustID:string,
}

export interface GetContacts_output{
   returnObj:Erp_Tablesets_CustCntTableset[],
}

   /** Required : 
      @param custNum
   */  
export interface GetCustomerBalance_input{
   custNum:number,
}

export interface GetCustomerBalance_output{
parameters : {
      /**  output parameters  */  
   balance:number,
   rpt1Balance:number,
   rpt2Balance:number,
   rpt3Balance:number,
}
}

   /** Required : 
      @param CustNum
      @param GlobalLock
   */  
export interface GetCustomerGlobalFields_input{
   CustNum:number,
   GlobalLock:boolean,
}

export interface GetCustomerGlobalFields_output{
   returnObj:string,
}

   /** Required : 
      @param ipCustID
      @param ds
      @param ds1
   */  
export interface GetInvoicedDeposits_input{
   ipCustID:string,
   ds:Erp_Tablesets_AllocDepositsTableset[],
   ds1:Erp_Tablesets_InvcHeadTableset[],
}

export interface GetInvoicedDeposits_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AllocDepositsTableset,
   ds1:Erp_Tablesets_InvcHeadTableset,
}
}

   /** Required : 
      @param ipCustID
      @param mode
      @param fromDays
      @param inRange
      @param ds
   */  
export interface GetInvoicesEx_input{
   ipCustID:string,
   mode:string,
   fromDays:number,
   inRange:boolean,
   ds:Erp_Tablesets_AllocDepositsTableset[],
}

export interface GetInvoicesEx_output{
   returnObj:Erp_Tablesets_InvcHeadTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AllocDepositsTableset,
}
}

   /** Required : 
      @param ipCustID
      @param ds
   */  
export interface GetInvoices_input{
   ipCustID:string,
   ds:Erp_Tablesets_AllocDepositsTableset[],
}

export interface GetInvoices_output{
   returnObj:Erp_Tablesets_InvcHeadTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AllocDepositsTableset,
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
   returnObj:Erp_Tablesets_CMCustomerListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewCMCustomer_input{
   ds:Erp_Tablesets_CreditManagerTableset[],
}

export interface GetNewCMCustomer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditManagerTableset,
}
}

   /** Required : 
      @param ds
      @param custNum
   */  
export interface GetNewGlbCustCred_input{
   ds:Erp_Tablesets_CreditManagerTableset[],
   custNum:number,
}

export interface GetNewGlbCustCred_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditManagerTableset,
}
}

   /** Required : 
      @param ipCustID
   */  
export interface GetOrders_input{
   ipCustID:string,
}

export interface GetOrders_output{
   returnObj:Erp_Tablesets_CMOrderHedTableset[],
}

   /** Required : 
      @param ipCustID
   */  
export interface GetPayIns_input{
   ipCustID:string,
}

export interface GetPayIns_output{
   returnObj:Erp_Tablesets_ARPNHeadTableset[],
}

   /** Required : 
      @param groupID
      @param headNum
   */  
export interface GetPaymentsDetails_input{
      /**  Group ID of the transaction under which the Invoice was posted  */  
   groupID:string,
      /**  HeadNum, The foreign key that relates this detail record to a CashHead record.  */  
   headNum:number,
}

export interface GetPaymentsDetails_output{
   returnObj:Erp_Tablesets_CashDtlTableset[],
}

   /** Required : 
      @param ipCustID
   */  
export interface GetPaymentsHeaders_input{
      /**  The customer character ID  */  
   ipCustID:string,
}

export interface GetPaymentsHeaders_output{
   returnObj:Erp_Tablesets_CashHeadTableset[],
}

   /** Required : 
      @param ipCustID
      @param ds
   */  
export interface GetPayments_input{
   ipCustID:string,
   ds:Erp_Tablesets_AllocDepositsTableset[],
}

export interface GetPayments_output{
   returnObj:Erp_Tablesets_CashHeadTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_AllocDepositsTableset,
}
}

   /** Required : 
      @param whereClauseCMCustomer
      @param whereClauseCustomCrdPool
      @param whereClauseGlbCustCred
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCMCustomer:string,
   whereClauseCustomCrdPool:string,
   whereClauseGlbCustCred:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CreditManagerTableset[],
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
      @param inFile
      @param pNumberFormat
   */  
export interface ImportCustCreditCsv_input{
      /**  Name of the File imported. i.e. C:\EpicorData\Users\MANAGER\Import\import.csv  */  
   inFile:string,
      /**  Number Format American/European.  */  
   pNumberFormat:string,
}

export interface ImportCustCreditCsv_output{
}

   /** Required : 
      @param ds
      @param pNumberFormat
   */  
export interface ImportCustCredit_input{
   ds:Erp_Tablesets_ImportCustCredTableset[],
      /**  Number Format American/European.  */  
   pNumberFormat:string,
}

export interface ImportCustCredit_output{
   returnObj:Erp_Tablesets_CreditManagerTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ImportCustCredTableset,
}
}

   /** Required : 
      @param custNum
      @param collectionsDate
      @param dsPEARInvSel
   */  
export interface PESelectInvoices_input{
      /**  Customer No  */  
   custNum:number,
      /**  Collections Date  */  
   collectionsDate:string,
   dsPEARInvSel:Erp_Tablesets_PEARInvSelBOTableset[],
}

export interface PESelectInvoices_output{
parameters : {
      /**  output parameters  */  
   dsPEARInvSel:Erp_Tablesets_PEARInvSelBOTableset,
}
}

   /** Required : 
      @param custNum
      @param dsPEARInvSel
   */  
export interface PEUpdateInvcHeadRecords_input{
      /**  Customer No  */  
   custNum:number,
   dsPEARInvSel:Erp_Tablesets_PEARInvSelBOTableset[],
}

export interface PEUpdateInvcHeadRecords_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   dsPEARInvSel:Erp_Tablesets_PEARInvSelBOTableset,
}
}

   /** Required : 
      @param btcustNum
   */  
export interface SetOrdersCreditOverride_input{
   btcustNum:number,
}

export interface SetOrdersCreditOverride_output{
}

   /** Required : 
      @param ipCustNum
      @param ds
   */  
export interface UpdateCMOrderHed_input{
      /**  The customer Num  */  
   ipCustNum:number,
   ds:Erp_Tablesets_CMOrderHedTableset[],
}

export interface UpdateCMOrderHed_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CMOrderHedTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateCreditTotals_input{
   ds:Erp_Tablesets_CreditManagerTableset[],
}

export interface UpdateCreditTotals_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditManagerTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtCreditManagerTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCreditManagerTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateGlobalLimits_input{
   ds:Erp_Tablesets_CreditManagerTableset[],
}

export interface UpdateGlobalLimits_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditManagerTableset,
}
}

   /** Required : 
      @param status
      @param fieldName
      @param ds
   */  
export interface UpdateNACreditPrc_input{
      /**  Bool parameter to know if used/share (true) or unUsed/notShared (false)  */  
   status:boolean,
      /**  NACreditPrc field name to be reset  */  
   fieldName:string,
   ds:Erp_Tablesets_CreditManagerTableset[],
}

export interface UpdateNACreditPrc_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditManagerTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CreditManagerTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CreditManagerTableset,
}
}

   /** Required : 
      @param ipAgingCode
   */  
export interface ValidateAgingCode_input{
      /**  Aging Code  */  
   ipAgingCode:string,
}

export interface ValidateAgingCode_output{
   returnObj:boolean,
}

   /** Required : 
      @param creditSharedPrc
   */  
export interface ValidateGlbNACreditSharedPrc_input{
      /**  Value to be validated  */  
   creditSharedPrc:number,
}

export interface ValidateGlbNACreditSharedPrc_output{
   returnObj:boolean,
}

   /** Required : 
      @param parentCreditPrc
   */  
export interface ValidateGlbNAParentCreditPrc_input{
      /**  Value to be validated  */  
   parentCreditPrc:number,
}

export interface ValidateGlbNAParentCreditPrc_output{
   returnObj:boolean,
}

   /** Required : 
      @param creditSharedPrc
   */  
export interface ValidateNACreditSharedPrc_input{
      /**  Value to be validated  */  
   creditSharedPrc:number,
}

export interface ValidateNACreditSharedPrc_output{
   returnObj:boolean,
}

   /** Required : 
      @param parentCreditPrc
   */  
export interface ValidateNAParentCreditPrc_input{
      /**  Value to be validated  */  
   parentCreditPrc:number,
}

export interface ValidateNAParentCreditPrc_output{
   returnObj:boolean,
}

   /** Required : 
      @param ipCustNum
   */  
export interface isNAGlobalCustomer_input{
   ipCustNum:number,
}

export interface isNAGlobalCustomer_output{
   returnObj:boolean,
}

