import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.DynamicQuerySvc
// Description: This is the DynamicQuery object. It has various methods for executing a query.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get DynamicQueries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DynamicQueries
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.DynamicQueryRow
   */  
export function get_DynamicQueries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DynamicQueryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DynamicQueryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the DynamicQuery item
   Description: Calls GetByID to retrieve the DynamicQuery item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DynamicQuery
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.DynamicQueryRow
   */  
export function get_DynamicQueries_Company_QueryID(Company:string, QueryID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_DynamicQueryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_DynamicQueryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryCtrls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryCtrls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryCtrls(Company:string, QueryID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryCtrls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryCtrl item
   Description: Calls GetByID to retrieve the QueryCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrl1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryCtrlRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryCtrls_Company_QueryID_ControlID(Company:string, QueryID:string, ControlID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryCtrls(" + Company + "," + QueryID + "," + ControlID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryCustomActions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryCustomActions1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCustomActionRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryCustomActions(Company:string, QueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCustomActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryCustomActions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCustomActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryCustomAction item
   Description: Calls GetByID to retrieve the QueryCustomAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCustomAction1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ActionID Desc: ActionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryCustomActionRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryCustomActions_Company_QueryID_ActionID(Company:string, QueryID:string, ActionID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryCustomActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryCustomActions(" + Company + "," + QueryID + "," + ActionID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryCustomActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryExecuteSettings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryExecuteSettings1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryExecuteSettingRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryExecuteSettings(Company:string, QueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryExecuteSettingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryExecuteSettings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryExecuteSettingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryExecuteSetting item
   Description: Calls GetByID to retrieve the QueryExecuteSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryExecuteSetting1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SettingID Desc: SettingID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryExecuteSettingRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryExecuteSettings_Company_QueryID_SettingID(Company:string, QueryID:string, SettingID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryExecuteSettingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryExecuteSettings(" + Company + "," + QueryID + "," + SettingID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryExecuteSettingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryParameters items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryParameters1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryParameters(Company:string, QueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryParameters", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryParameter item
   Description: Calls GetByID to retrieve the QueryParameter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameter1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryParameterRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryParameters_Company_QueryID_ParameterID(Company:string, QueryID:string, ParameterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryParameterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryParameters(" + Company + "," + QueryID + "," + ParameterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryParameterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryReferences items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryReferences1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryReferenceRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryReferences(Company:string, QueryID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryReferenceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryReferences", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryReferenceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryReference item
   Description: Calls GetByID to retrieve the QueryReference item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryReference1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryReferenceRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryReferences_Company_QueryID_ReferenceID(Company:string, QueryID:string, ReferenceID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryReferenceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryReferences(" + Company + "," + QueryID + "," + ReferenceID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryReferenceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuerySubQueries items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuerySubQueries1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySubQueryRow
   */  
export function get_DynamicQueries_Company_QueryID_QuerySubQueries(Company:string, QueryID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySubQueryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QuerySubQueries", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySubQueryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuerySubQuery item
   Description: Calls GetByID to retrieve the QuerySubQuery item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySubQuery1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QuerySubQueryRow
   */  
export function get_DynamicQueries_Company_QueryID_QuerySubQueries_Company_QueryID_SubQueryID(Company:string, QueryID:string, SubQueryID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QuerySubQueryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QuerySubQueryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryUpdateFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryUpdateFields1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateFieldRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryUpdateFields(Company:string, QueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryUpdateFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryUpdateField item
   Description: Calls GetByID to retrieve the QueryUpdateField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateField1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param MapTableName Desc: MapTableName   Required: True   Allow empty value : True
      @param MapFieldName Desc: MapFieldName   Required: True   Allow empty value : True
      @param Direction Desc: Direction   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryUpdateFieldRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryUpdateFields_Company_QueryID_MapTableName_MapFieldName_Direction(Company:string, QueryID:string, MapTableName:string, MapFieldName:string, Direction:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryUpdateFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryUpdateFields(" + Company + "," + QueryID + "," + MapTableName + "," + MapFieldName + "," + Direction + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryUpdateFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryUpdateSettings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryUpdateSettings1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateSettingsRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryUpdateSettings(Company:string, QueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateSettingsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryUpdateSettings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateSettingsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryUpdateSetting item
   Description: Calls GetByID to retrieve the QueryUpdateSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateSetting1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryUpdateSettingsRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryUpdateSettings_Company_QueryID(Company:string, QueryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryUpdateSettingsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryUpdateSettings(" + Company + "," + QueryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryUpdateSettingsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryValueSetItems items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryValueSetItems1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryValueSetItemsRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryValueSetItems(Company:string, QueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryValueSetItemsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryValueSetItems", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryValueSetItemsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryValueSetItem item
   Description: Calls GetByID to retrieve the QueryValueSetItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryValueSetItem1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ValueSetID Desc: ValueSetID   Required: True   Allow empty value : True
      @param ItemValue Desc: ItemValue   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryValueSetItemsRow
   */  
export function get_DynamicQueries_Company_QueryID_QueryValueSetItems_Company_QueryID_ValueSetID_ItemValue(Company:string, QueryID:string, ValueSetID:string, ItemValue:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryValueSetItemsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/DynamicQueries(" + Company + "," + QueryID + ")/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryValueSetItemsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryCtrls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryCtrls
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlRow
   */  
export function get_QueryCtrls(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCtrls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryCtrl item
   Description: Calls GetByID to retrieve the QueryCtrl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrl
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryCtrlRow
   */  
export function get_QueryCtrls_Company_QueryID_ControlID(Company:string, QueryID:string, ControlID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryCtrlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCtrls(" + Company + "," + QueryID + "," + ControlID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryCtrlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryCtrlValues items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryCtrlValues1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlValuesRow
   */  
export function get_QueryCtrls_Company_QueryID_ControlID_QueryCtrlValues(Company:string, QueryID:string, ControlID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCtrls(" + Company + "," + QueryID + "," + ControlID + ")/QueryCtrlValues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryCtrlValue item
   Description: Calls GetByID to retrieve the QueryCtrlValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrlValue1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      @param ID Desc: ID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryCtrlValuesRow
   */  
export function get_QueryCtrls_Company_QueryID_ControlID_QueryCtrlValues_Company_QueryID_ControlID_ID(Company:string, QueryID:string, ControlID:string, ID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryCtrlValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCtrls(" + Company + "," + QueryID + "," + ControlID + ")/QueryCtrlValues(" + Company + "," + QueryID + "," + ControlID + "," + ID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryCtrlValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryCtrlValues items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryCtrlValues
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCtrlValuesRow
   */  
export function get_QueryCtrlValues(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCtrlValues", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryCtrlValue item
   Description: Calls GetByID to retrieve the QueryCtrlValue item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCtrlValue
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ControlID Desc: ControlID   Required: True   Allow empty value : True
      @param ID Desc: ID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryCtrlValuesRow
   */  
export function get_QueryCtrlValues_Company_QueryID_ControlID_ID(Company:string, QueryID:string, ControlID:string, ID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryCtrlValuesRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCtrlValues(" + Company + "," + QueryID + "," + ControlID + "," + ID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryCtrlValuesRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryCustomActions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryCustomActions
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryCustomActionRow
   */  
export function get_QueryCustomActions(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCustomActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCustomActions", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCustomActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryCustomAction item
   Description: Calls GetByID to retrieve the QueryCustomAction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryCustomAction
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ActionID Desc: ActionID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryCustomActionRow
   */  
export function get_QueryCustomActions_Company_QueryID_ActionID(Company:string, QueryID:string, ActionID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryCustomActionRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryCustomActions(" + Company + "," + QueryID + "," + ActionID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryCustomActionRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryExecuteSettings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryExecuteSettings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryExecuteSettingRow
   */  
export function get_QueryExecuteSettings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryExecuteSettingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryExecuteSettings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryExecuteSettingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryExecuteSetting item
   Description: Calls GetByID to retrieve the QueryExecuteSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryExecuteSetting
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SettingID Desc: SettingID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryExecuteSettingRow
   */  
export function get_QueryExecuteSettings_Company_QueryID_SettingID(Company:string, QueryID:string, SettingID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryExecuteSettingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryExecuteSettings(" + Company + "," + QueryID + "," + SettingID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryExecuteSettingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryParameters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryParameters
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterRow
   */  
export function get_QueryParameters(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryParameters", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryParameter item
   Description: Calls GetByID to retrieve the QueryParameter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryParameterRow
   */  
export function get_QueryParameters_Company_QueryID_ParameterID(Company:string, QueryID:string, ParameterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryParameterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryParameters(" + Company + "," + QueryID + "," + ParameterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryParameterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryReferences items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryReferences
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryReferenceRow
   */  
export function get_QueryReferences(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryReferenceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryReferences", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryReferenceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryReference item
   Description: Calls GetByID to retrieve the QueryReference item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryReference
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryReferenceRow
   */  
export function get_QueryReferences_Company_QueryID_ReferenceID(Company:string, QueryID:string, ReferenceID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryReferenceRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryReferences(" + Company + "," + QueryID + "," + ReferenceID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryReferenceRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryParameterBindings items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryParameterBindings1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterBindingRow
   */  
export function get_QueryReferences_Company_QueryID_ReferenceID_QueryParameterBindings(Company:string, QueryID:string, ReferenceID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterBindingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryReferences(" + Company + "," + QueryID + "," + ReferenceID + ")/QueryParameterBindings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterBindingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryParameterBinding item
   Description: Calls GetByID to retrieve the QueryParameterBinding item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameterBinding1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryParameterBindingRow
   */  
export function get_QueryReferences_Company_QueryID_ReferenceID_QueryParameterBindings_Company_QueryID_ReferenceID_ParameterID(Company:string, QueryID:string, ReferenceID:string, ParameterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryParameterBindingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryReferences(" + Company + "," + QueryID + "," + ReferenceID + ")/QueryParameterBindings(" + Company + "," + QueryID + "," + ReferenceID + "," + ParameterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryParameterBindingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryParameterBindings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryParameterBindings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryParameterBindingRow
   */  
export function get_QueryParameterBindings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterBindingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryParameterBindings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterBindingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryParameterBinding item
   Description: Calls GetByID to retrieve the QueryParameterBinding item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryParameterBinding
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ReferenceID Desc: ReferenceID   Required: True   Allow empty value : True
      @param ParameterID Desc: ParameterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryParameterBindingRow
   */  
export function get_QueryParameterBindings_Company_QueryID_ReferenceID_ParameterID(Company:string, QueryID:string, ReferenceID:string, ParameterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryParameterBindingRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryParameterBindings(" + Company + "," + QueryID + "," + ReferenceID + "," + ParameterID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryParameterBindingRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuerySubQueries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuerySubQueries
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySubQueryRow
   */  
export function get_QuerySubQueries(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySubQueryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySubQueryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuerySubQuery item
   Description: Calls GetByID to retrieve the QuerySubQuery item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySubQuery
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QuerySubQueryRow
   */  
export function get_QuerySubQueries_Company_QueryID_SubQueryID(Company:string, QueryID:string, SubQueryID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QuerySubQueryRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QuerySubQueryRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryRelations items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryRelations1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationRow
   */  
export function get_QuerySubQueries_Company_QueryID_SubQueryID_QueryRelations(Company:string, QueryID:string, SubQueryID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryRelations", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryRelation item
   Description: Calls GetByID to retrieve the QueryRelation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelation1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryRelationRow
   */  
export function get_QuerySubQueries_Company_QueryID_SubQueryID_QueryRelations_Company_QueryID_SubQueryID_RelationID(Company:string, QueryID:string, SubQueryID:string, RelationID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryRelationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryRelations(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryRelationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QuerySortBies items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QuerySortBies1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySortByRow
   */  
export function get_QuerySubQueries_Company_QueryID_SubQueryID_QuerySortBies(Company:string, QueryID:string, SubQueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySortByRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QuerySortBies", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySortByRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuerySortBy item
   Description: Calls GetByID to retrieve the QuerySortBy item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySortBy1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QuerySortByRow
   */  
export function get_QuerySubQueries_Company_QueryID_SubQueryID_QuerySortBies_Company_QueryID_SubQueryID_TableID_FieldName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QuerySortByRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QuerySortBies(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QuerySortByRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryWhereItems items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryWhereItems1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryWhereItemRow
   */  
export function get_QuerySubQueries_Company_QueryID_SubQueryID_QueryWhereItems(Company:string, QueryID:string, SubQueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryWhereItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryWhereItems", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryWhereItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryWhereItem item
   Description: Calls GetByID to retrieve the QueryWhereItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryWhereItem1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryWhereItemRow
   */  
export function get_QuerySubQueries_Company_QueryID_SubQueryID_QueryWhereItems_SysRowID(Company:string, QueryID:string, SubQueryID:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryWhereItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryWhereItems(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryWhereItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryGroupBies items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryGroupBies1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryGroupByRow
   */  
export function get_QuerySubQueries_Company_QueryID_SubQueryID_QueryGroupBies(Company:string, QueryID:string, SubQueryID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryGroupByRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryGroupBies", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryGroupByRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryGroupBy item
   Description: Calls GetByID to retrieve the QueryGroupBy item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryGroupBy1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param GroupByID Desc: GroupByID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryGroupByRow
   */  
export function get_QuerySubQueries_Company_QueryID_SubQueryID_QueryGroupBies_Company_QueryID_SubQueryID_GroupByID(Company:string, QueryID:string, SubQueryID:string, GroupByID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryGroupByRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryGroupBies(" + Company + "," + QueryID + "," + SubQueryID + "," + GroupByID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryGroupByRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryTables items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryTables1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryTableRow
   */  
export function get_QuerySubQueries_Company_QueryID_SubQueryID_QueryTables(Company:string, QueryID:string, SubQueryID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryTables", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryTable item
   Description: Calls GetByID to retrieve the QueryTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryTable1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryTableRow
   */  
export function get_QuerySubQueries_Company_QueryID_SubQueryID_QueryTables_Company_QueryID_SubQueryID_TableID(Company:string, QueryID:string, SubQueryID:string, TableID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySubQueries(" + Company + "," + QueryID + "," + SubQueryID + ")/QueryTables(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryRelations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryRelations
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationRow
   */  
export function get_QueryRelations(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryRelations", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryRelation item
   Description: Calls GetByID to retrieve the QueryRelation item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelation
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryRelationRow
   */  
export function get_QueryRelations_Company_QueryID_SubQueryID_RelationID(Company:string, QueryID:string, SubQueryID:string, RelationID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryRelationRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryRelations(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryRelationRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryRelationFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryRelationFields1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationFieldRow
   */  
export function get_QueryRelations_Company_QueryID_SubQueryID_RelationID_QueryRelationFields(Company:string, QueryID:string, SubQueryID:string, RelationID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryRelations(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")/QueryRelationFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryRelationField item
   Description: Calls GetByID to retrieve the QueryRelationField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelationField1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryRelationFieldRow
   */  
export function get_QueryRelations_Company_QueryID_SubQueryID_RelationID_QueryRelationFields_Company_QueryID_SubQueryID_RelationID_Seq(Company:string, QueryID:string, SubQueryID:string, RelationID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryRelationFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryRelations(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + ")/QueryRelationFields(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryRelationFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryRelationFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryRelationFields
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryRelationFieldRow
   */  
export function get_QueryRelationFields(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryRelationFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryRelationField item
   Description: Calls GetByID to retrieve the QueryRelationField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryRelationField
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param RelationID Desc: RelationID   Required: True   Allow empty value : True
      @param Seq Desc: Seq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryRelationFieldRow
   */  
export function get_QueryRelationFields_Company_QueryID_SubQueryID_RelationID_Seq(Company:string, QueryID:string, SubQueryID:string, RelationID:string, Seq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryRelationFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryRelationFields(" + Company + "," + QueryID + "," + SubQueryID + "," + RelationID + "," + Seq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryRelationFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QuerySortBies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QuerySortBies
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QuerySortByRow
   */  
export function get_QuerySortBies(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySortByRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySortBies", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySortByRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QuerySortBy item
   Description: Calls GetByID to retrieve the QuerySortBy item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QuerySortBy
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QuerySortByRow
   */  
export function get_QuerySortBies_Company_QueryID_SubQueryID_TableID_FieldName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QuerySortByRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QuerySortBies(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QuerySortByRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryWhereItems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryWhereItems
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryWhereItemRow
   */  
export function get_QueryWhereItems(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryWhereItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryWhereItems", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryWhereItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryWhereItem item
   Description: Calls GetByID to retrieve the QueryWhereItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryWhereItem
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryWhereItemRow
   */  
export function get_QueryWhereItems_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryWhereItemRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryWhereItems(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryWhereItemRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryGroupBies items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryGroupBies
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryGroupByRow
   */  
export function get_QueryGroupBies(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryGroupByRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryGroupBies", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryGroupByRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryGroupBy item
   Description: Calls GetByID to retrieve the QueryGroupBy item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryGroupBy
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param GroupByID Desc: GroupByID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryGroupByRow
   */  
export function get_QueryGroupBies_Company_QueryID_SubQueryID_GroupByID(Company:string, QueryID:string, SubQueryID:string, GroupByID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryGroupByRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryGroupBies(" + Company + "," + QueryID + "," + SubQueryID + "," + GroupByID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryGroupByRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryTables items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryTables
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryTableRow
   */  
export function get_QueryTables(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryTables", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryTable item
   Description: Calls GetByID to retrieve the QueryTable item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryTable
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryTableRow
   */  
export function get_QueryTables_Company_QueryID_SubQueryID_TableID(Company:string, QueryID:string, SubQueryID:string, TableID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryTableRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryTables(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryTableRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryFields items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryFields1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldRow
   */  
export function get_QueryTables_Company_QueryID_SubQueryID_TableID_QueryFields(Company:string, QueryID:string, SubQueryID:string, TableID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryTables(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryField item
   Description: Calls GetByID to retrieve the QueryField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryField1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryFieldRow
   */  
export function get_QueryTables_Company_QueryID_SubQueryID_TableID_QueryFields_Company_QueryID_SubQueryID_TableID_FieldName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryTables(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFields(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryFunctionCalls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryFunctionCalls1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFunctionCallRow
   */  
export function get_QueryTables_Company_QueryID_SubQueryID_TableID_QueryFunctionCalls(Company:string, QueryID:string, SubQueryID:string, TableID:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFunctionCallRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryTables(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFunctionCalls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFunctionCallRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryFunctionCall item
   Description: Calls GetByID to retrieve the QueryFunctionCall item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFunctionCall1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FunctionID Desc: FunctionID   Required: True   Allow empty value : True
      @param ParameterName Desc: ParameterName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryFunctionCallRow
   */  
export function get_QueryTables_Company_QueryID_SubQueryID_TableID_QueryFunctionCalls_Company_QueryID_SubQueryID_FunctionID_ParameterName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FunctionID:string, ParameterName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryFunctionCallRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryTables(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + ")/QueryFunctionCalls(" + Company + "," + QueryID + "," + SubQueryID + "," + FunctionID + "," + ParameterName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryFunctionCallRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryFields
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldRow
   */  
export function get_QueryFields(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryField item
   Description: Calls GetByID to retrieve the QueryField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryField
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryFieldRow
   */  
export function get_QueryFields_Company_QueryID_SubQueryID_TableID_FieldName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFields(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get QueryFieldAttributes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_QueryFieldAttributes1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldAttributeRow
   */  
export function get_QueryFields_Company_QueryID_SubQueryID_TableID_FieldName_QueryFieldAttributes(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldAttributeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFields(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")/QueryFieldAttributes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldAttributeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryFieldAttribute item
   Description: Calls GetByID to retrieve the QueryFieldAttribute item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldAttribute1
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryFieldAttributeRow
   */  
export function get_QueryFields_Company_QueryID_SubQueryID_TableID_FieldName_QueryFieldAttributes_Company_QueryID_SubQueryID_TableID_FieldName_AttributeName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, AttributeName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryFieldAttributeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFields(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + ")/QueryFieldAttributes(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + "," + AttributeName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryFieldAttributeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryFieldAttributes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryFieldAttributes
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFieldAttributeRow
   */  
export function get_QueryFieldAttributes(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldAttributeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFieldAttributes", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldAttributeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryFieldAttribute item
   Description: Calls GetByID to retrieve the QueryFieldAttribute item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFieldAttribute
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param TableID Desc: TableID   Required: True   Allow empty value : True
      @param FieldName Desc: FieldName   Required: True   Allow empty value : True
      @param AttributeName Desc: AttributeName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryFieldAttributeRow
   */  
export function get_QueryFieldAttributes_Company_QueryID_SubQueryID_TableID_FieldName_AttributeName(Company:string, QueryID:string, SubQueryID:string, TableID:string, FieldName:string, AttributeName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryFieldAttributeRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFieldAttributes(" + Company + "," + QueryID + "," + SubQueryID + "," + TableID + "," + FieldName + "," + AttributeName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryFieldAttributeRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryFunctionCalls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryFunctionCalls
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryFunctionCallRow
   */  
export function get_QueryFunctionCalls(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFunctionCallRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFunctionCalls", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFunctionCallRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryFunctionCall item
   Description: Calls GetByID to retrieve the QueryFunctionCall item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryFunctionCall
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param SubQueryID Desc: SubQueryID   Required: True   Allow empty value : True
      @param FunctionID Desc: FunctionID   Required: True   Allow empty value : True
      @param ParameterName Desc: ParameterName   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryFunctionCallRow
   */  
export function get_QueryFunctionCalls_Company_QueryID_SubQueryID_FunctionID_ParameterName(Company:string, QueryID:string, SubQueryID:string, FunctionID:string, ParameterName:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryFunctionCallRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryFunctionCalls(" + Company + "," + QueryID + "," + SubQueryID + "," + FunctionID + "," + ParameterName + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryFunctionCallRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryUpdateFields items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryUpdateFields
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateFieldRow
   */  
export function get_QueryUpdateFields(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryUpdateFields", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryUpdateField item
   Description: Calls GetByID to retrieve the QueryUpdateField item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateField
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param MapTableName Desc: MapTableName   Required: True   Allow empty value : True
      @param MapFieldName Desc: MapFieldName   Required: True   Allow empty value : True
      @param Direction Desc: Direction   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryUpdateFieldRow
   */  
export function get_QueryUpdateFields_Company_QueryID_MapTableName_MapFieldName_Direction(Company:string, QueryID:string, MapTableName:string, MapFieldName:string, Direction:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryUpdateFieldRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryUpdateFields(" + Company + "," + QueryID + "," + MapTableName + "," + MapFieldName + "," + Direction + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryUpdateFieldRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryUpdateSettings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryUpdateSettings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryUpdateSettingsRow
   */  
export function get_QueryUpdateSettings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateSettingsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryUpdateSettings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateSettingsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryUpdateSetting item
   Description: Calls GetByID to retrieve the QueryUpdateSetting item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryUpdateSetting
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryUpdateSettingsRow
   */  
export function get_QueryUpdateSettings_Company_QueryID(Company:string, QueryID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryUpdateSettingsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryUpdateSettings(" + Company + "," + QueryID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryUpdateSettingsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get QueryValueSetItems items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_QueryValueSetItems
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.QueryValueSetItemsRow
   */  
export function get_QueryValueSetItems(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryValueSetItemsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryValueSetItemsRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the QueryValueSetItem item
   Description: Calls GetByID to retrieve the QueryValueSetItem item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_QueryValueSetItem
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param QueryID Desc: QueryID   Required: True   Allow empty value : True
      @param ValueSetID Desc: ValueSetID   Required: True   Allow empty value : True
      @param ItemValue Desc: ItemValue   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.QueryValueSetItemsRow
   */  
export function get_QueryValueSetItems_Company_QueryID_ValueSetID_ItemValue(Company:string, QueryID:string, ValueSetID:string, ItemValue:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_QueryValueSetItemsRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/QueryValueSetItems(" + Company + "," + QueryID + "," + ValueSetID + "," + ItemValue + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_QueryValueSetItemsRow)
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
   Description: This method returns a list of BAQs that have a specific like field
Used by: Server\bo\EpiSearch\EpiSearch.p
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
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseDynamicQuery:string, whereClauseQueryCtrl:string, whereClauseQueryCtrlValues:string, whereClauseQueryCustomAction:string, whereClauseQueryExecuteSetting:string, whereClauseQueryParameter:string, whereClauseQueryReference:string, whereClauseQueryParameterBinding:string, whereClauseQuerySubQuery:string, whereClauseQueryRelation:string, whereClauseQueryRelationField:string, whereClauseQuerySortBy:string, whereClauseQueryWhereItem:string, whereClauseQueryGroupBy:string, whereClauseQueryTable:string, whereClauseQueryField:string, whereClauseQueryFunctionCall:string, whereClauseQueryUpdateField:string, whereClauseQueryUpdateSettings:string, whereClauseQueryValueSetItems:string, whereClauseQueryFieldAttribute:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseDynamicQuery!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseDynamicQuery=" + whereClauseDynamicQuery
   }
   if(typeof whereClauseQueryCtrl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryCtrl=" + whereClauseQueryCtrl
   }
   if(typeof whereClauseQueryCtrlValues!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryCtrlValues=" + whereClauseQueryCtrlValues
   }
   if(typeof whereClauseQueryCustomAction!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryCustomAction=" + whereClauseQueryCustomAction
   }
   if(typeof whereClauseQueryExecuteSetting!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryExecuteSetting=" + whereClauseQueryExecuteSetting
   }
   if(typeof whereClauseQueryParameter!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryParameter=" + whereClauseQueryParameter
   }
   if(typeof whereClauseQueryReference!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryReference=" + whereClauseQueryReference
   }
   if(typeof whereClauseQueryParameterBinding!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryParameterBinding=" + whereClauseQueryParameterBinding
   }
   if(typeof whereClauseQuerySubQuery!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuerySubQuery=" + whereClauseQuerySubQuery
   }
   if(typeof whereClauseQueryRelation!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryRelation=" + whereClauseQueryRelation
   }
   if(typeof whereClauseQueryRelationField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryRelationField=" + whereClauseQueryRelationField
   }
   if(typeof whereClauseQuerySortBy!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQuerySortBy=" + whereClauseQuerySortBy
   }
   if(typeof whereClauseQueryWhereItem!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryWhereItem=" + whereClauseQueryWhereItem
   }
   if(typeof whereClauseQueryGroupBy!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryGroupBy=" + whereClauseQueryGroupBy
   }
   if(typeof whereClauseQueryTable!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryTable=" + whereClauseQueryTable
   }
   if(typeof whereClauseQueryField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryField=" + whereClauseQueryField
   }
   if(typeof whereClauseQueryFunctionCall!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryFunctionCall=" + whereClauseQueryFunctionCall
   }
   if(typeof whereClauseQueryUpdateField!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryUpdateField=" + whereClauseQueryUpdateField
   }
   if(typeof whereClauseQueryUpdateSettings!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryUpdateSettings=" + whereClauseQueryUpdateSettings
   }
   if(typeof whereClauseQueryValueSetItems!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryValueSetItems=" + whereClauseQueryValueSetItems
   }
   if(typeof whereClauseQueryFieldAttribute!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseQueryFieldAttribute=" + whereClauseQueryFieldAttribute
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: This method returns a dataset containing definition of the query.
   OperationID: GetByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByID(requestBody:GetByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Description: This method runs an updatable query and returns result dataset.
   OperationID: GetList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetList(requestBody:GetList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method GetByIDs
   Description: This method returns a dataset containing definition of queries with ids listed in parameter
   OperationID: GetByIDs
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDs(requestBody:GetByIDs_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByIDs_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetByIDs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByIDs_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDsTranslated
   Description: This method returns a dataset containing definition of queries with ids listed in parameter with translated labels.
   OperationID: GetByIDsTranslated
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByIDsTranslated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDsTranslated_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDsTranslated(requestBody:GetByIDsTranslated_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByIDsTranslated_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetByIDsTranslated", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByIDsTranslated_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExecuteByID
   Description: This method run an existing query and returns an untyped dataset
   OperationID: ExecuteByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExecuteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExecuteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExecuteByID(requestBody:ExecuteByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExecuteByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/ExecuteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExecuteByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Execute
   Description: This method runs a query based on default settings.
Used by: Server\Bpm\BpmQuery.i
   OperationID: Execute
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Execute_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Execute_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Execute(requestBody:Execute_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Execute_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/Execute", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Execute_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckTestQueryExecution
   Description: For MS SQL query checks if it is executed right now and cancel it if requested
   OperationID: CheckTestQueryExecution
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckTestQueryExecution_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckTestQueryExecution_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckTestQueryExecution(requestBody:CheckTestQueryExecution_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckTestQueryExecution_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/CheckTestQueryExecution", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckTestQueryExecution_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQueryExecutionPlan
   Description: For MS SQL query returns query execution plan
   OperationID: GetQueryExecutionPlan
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetQueryExecutionPlan_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryExecutionPlan_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQueryExecutionPlan(requestBody:GetQueryExecutionPlan_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetQueryExecutionPlan_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetQueryExecutionPlan", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetQueryExecutionPlan_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQueryListFromLike
   Description: This method returns a list of BAQs that have a specific like field
Used by: Server\bo\EpiSearch\EpiSearch.p
   OperationID: GetQueryListFromLike
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetQueryListFromLike_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryListFromLike_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQueryListFromLike(requestBody:GetQueryListFromLike_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetQueryListFromLike_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetQueryListFromLike", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetQueryListFromLike_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQueryExecutionParameters
   Description: This method returns a dataset representing an query's execution parameters information
   OperationID: GetQueryExecutionParameters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetQueryExecutionParameters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryExecutionParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQueryExecutionParameters(requestBody:GetQueryExecutionParameters_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetQueryExecutionParameters_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetQueryExecutionParameters", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetQueryExecutionParameters_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQueryExecutionParametersByID
   Description: This method returns a dataset representing an query's execution parameters information
   OperationID: GetQueryExecutionParametersByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetQueryExecutionParametersByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryExecutionParametersByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQueryExecutionParametersByID(requestBody:GetQueryExecutionParametersByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetQueryExecutionParametersByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetQueryExecutionParametersByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetQueryExecutionParametersByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQueryEmptyResultSet
   Description: This method returns an empty result dataset. It is useful if client need information about result set schema only
   OperationID: GetQueryEmptyResultSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetQueryEmptyResultSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryEmptyResultSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQueryEmptyResultSet(requestBody:GetQueryEmptyResultSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetQueryEmptyResultSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetQueryEmptyResultSet", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetQueryEmptyResultSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQueryEmptyResultSetByID
   Description: This method returns an empty result dataset. It is useful if client need information about result set schema only
   OperationID: GetQueryEmptyResultSetByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetQueryEmptyResultSetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryEmptyResultSetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQueryEmptyResultSetByID(requestBody:GetQueryEmptyResultSetByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetQueryEmptyResultSetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetQueryEmptyResultSetByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetQueryEmptyResultSetByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQueryEmptyResultSetByIDAndCompany
   Description: This method returns an empty result dataset. It is useful if client need information about result set schema only
   OperationID: GetQueryEmptyResultSetByIDAndCompany
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetQueryEmptyResultSetByIDAndCompany_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryEmptyResultSetByIDAndCompany_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQueryEmptyResultSetByIDAndCompany(requestBody:GetQueryEmptyResultSetByIDAndCompany_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetQueryEmptyResultSetByIDAndCompany_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetQueryEmptyResultSetByIDAndCompany", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetQueryEmptyResultSetByIDAndCompany_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQueryResultSetMetadataByID
   Description: This method returns a list of groups of attributes and values, each group per query's display field.
Attributes expose information about the field: Caption, Format, DataType, ReadOnly, etc.
   OperationID: GetQueryResultSetMetadataByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetQueryResultSetMetadataByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryResultSetMetadataByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetQueryResultSetMetadataByID(requestBody:GetQueryResultSetMetadataByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetQueryResultSetMetadataByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetQueryResultSetMetadataByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetQueryResultSetMetadataByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Analyze
   OperationID: Analyze
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Analyze_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Analyze_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Analyze(requestBody:Analyze_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Analyze_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/Analyze", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Analyze_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetQueryList
   Description: This method returns a list of BAQs that meet the criteria. The result can be paged.
   OperationID: Get_GetQueryList
      @param whereClause Desc: The criteria   Required: True   Allow empty value : True
      @param pageSize Desc: Size of the page   Required: True
      @param absolutePage Desc: The number of the page to return   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetQueryList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetQueryList(whereClause:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
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

   return (new Promise<GetQueryList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetQueryList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetQueryList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetListByID
   Description: This method runs an updatable query and returns result dataset.
   OperationID: GetListByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetListByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetListByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetListByID(requestBody:GetListByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetListByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetListByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetListByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Update
   Description: Call Update method of an updatable query and return result dataset
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Invoke method UpdateByID
   Description: Call Update method of an updatable query and return result dataset
   OperationID: UpdateByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateByID(requestBody:UpdateByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/UpdateByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNew
   Description: Calls GetNew method of an updatable query and return result set with added row.
   OperationID: GetNew
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNew_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNew(requestBody:GetNew_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNew_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetNew", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNew_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewByID
   Description: Calls GetNew method of an updatable query and return result set with added row.
   OperationID: GetNewByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewByID(requestBody:GetNewByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetNewByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FieldUpdate
   Description: Calls FieldUpdate method of an updatable query and return result set.
   OperationID: FieldUpdate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FieldUpdate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FieldUpdate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FieldUpdate(requestBody:FieldUpdate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FieldUpdate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/FieldUpdate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as FieldUpdate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FieldUpdateByID
   Description: Calls FieldUpdate method of an updatable query and return result set.
   OperationID: FieldUpdateByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FieldUpdateByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FieldUpdateByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FieldUpdateByID(requestBody:FieldUpdateByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FieldUpdateByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/FieldUpdateByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as FieldUpdateByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FieldValidate
   Description: Calls FieldUpdate method of an updatable query and return result set.
   OperationID: FieldValidate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FieldValidate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FieldValidate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FieldValidate(requestBody:FieldValidate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FieldValidate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/FieldValidate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as FieldValidate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FieldValidateByID
   Description: Calls FieldUpdate method of an updatable query and return result set.
   OperationID: FieldValidateByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FieldValidateByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FieldValidateByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FieldValidateByID(requestBody:FieldValidateByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FieldValidateByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/FieldValidateByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as FieldValidateByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RunCustomAction
   Description: This method does nothing per se, but is useful if there are BPM directives
attached to the query. Directives can examine actionId value and perform some actions.
   OperationID: RunCustomAction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RunCustomAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunCustomAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunCustomAction(requestBody:RunCustomAction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RunCustomAction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/RunCustomAction", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RunCustomAction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RunCustomActionByID
   Description: This method does nothing per se, but is useful if there are BPM directives
attached to the query. Directives can examine actionId value and perform some actions.
   OperationID: RunCustomActionByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RunCustomActionByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunCustomActionByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunCustomActionByID(requestBody:RunCustomActionByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RunCustomActionByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/RunCustomActionByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as RunCustomActionByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDistinctValues
   Description: This method runs a query based on default settings and passed execution parameters and return lists of distinct values of specified fields.
   OperationID: GetDistinctValues
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDistinctValues_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDistinctValues_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDistinctValues(requestBody:GetDistinctValues_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDistinctValues_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetDistinctValues", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetDistinctValues_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method InvalidateRuntimeQueryCache
   Description: Removes query definition from the runtime cache. It will be reloaded on the next execution.
   OperationID: InvalidateRuntimeQueryCache
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/InvalidateRuntimeQueryCache_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/InvalidateRuntimeQueryCache_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_InvalidateRuntimeQueryCache(requestBody:InvalidateRuntimeQueryCache_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<InvalidateRuntimeQueryCache_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/InvalidateRuntimeQueryCache", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as InvalidateRuntimeQueryCache_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDTranslated
   Description: This method returns a dataset containing definition of the query with translated labels.
   OperationID: GetByIDTranslated
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByIDTranslated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDTranslated_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDTranslated(requestBody:GetByIDTranslated_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByIDTranslated_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.DynamicQuerySvc/GetByIDTranslated", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetByIDTranslated_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_DynamicQueryRow{
   "odatametadata":string,
   "value":Ice_Tablesets_DynamicQueryRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryCtrlRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCtrlValuesRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryCtrlValuesRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryCustomActionRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryCustomActionRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryExecuteSettingRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryExecuteSettingRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldAttributeRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryFieldAttributeRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFieldRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryFieldRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryFunctionCallRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryFunctionCallRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryGroupByRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryGroupByRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterBindingRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryParameterBindingRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryParameterRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryParameterRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryReferenceRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryReferenceRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationFieldRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryRelationFieldRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryRelationRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryRelationRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySortByRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QuerySortByRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QuerySubQueryRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QuerySubQueryRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryTableRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryTableRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateFieldRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryUpdateFieldRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryUpdateSettingsRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryUpdateSettingsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryValueSetItemsRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryValueSetItemsRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_QueryWhereItemRow{
   "odatametadata":string,
   "value":Ice_Tablesets_QueryWhereItemRow,
}

export interface Ice_Tablesets_DynamicQueryRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  AuthorID  */  
   "AuthorID":string,
      /**  Description  */  
   "Description":string,
      /**  DisplayPhrase  */  
   "DisplayPhrase":string,
      /**  IsShared  */  
   "IsShared":boolean,
      /**  Version  */  
   "Version":string,
      /**  CGCCode  */  
   "CGCCode":string,
      /**  XCompany  */  
   "XCompany":boolean,
      /**  GlbCompany  */  
   "GlbCompany":string,
      /**  Updatable  */  
   "Updatable":boolean,
      /**  ExtQuery  */  
   "ExtQuery":boolean,
      /**  ExtDatasourceName  */  
   "ExtDatasourceName":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Extension  */  
   "Extension":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SecCode  */  
   "SecCode":string,
   "AllCompanies":boolean,
      /**  UseLiveDB  */  
   "UseLiveDB":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryCtrlRow{
      /**  Company Code  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  GUID for control  */  
   "ControlID":string,
      /**  Data Source  */  
   "DataSource":string,
      /**  Data Type  */  
   "DataType":string,
      /**  Field Format  */  
   "FieldFormat":string,
      /**  Mandatory flag  */  
   "IsMandatory":boolean,
      /**  Default Value  */  
   "DefaultValue":string,
      /**   One of predefined constants:
Standard ? free type editor/date picker, depend on DataType.
RadioSet ? radio button set. Items are specified in QueryCtrlValues table
DropDown ? dropdown list. Items are specified in QueryCtrlValues table
DropDownBAQ ? dropdown list. Information are stored in QueryCtrlValues table with tree rows with Ids:BAQID, BAQDisplayColumn, BAQValueColumn
DropDownUserCodes - dropdown list. Information are stored in QueryCtrlValues table with one row with Id = UserCodeTypeID  */  
   "ControlType":string,
      /**  Type of the datasource 0 - updatable field, 1 - parameter  */  
   "SourceType":number,
      /**  ListSource  */  
   "ListSource":string,
      /**  DisplayColumn  */  
   "DisplayColumn":string,
      /**  ValueColumn  */  
   "ValueColumn":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Seq  */  
   "Seq":number,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryCtrlValuesRow{
      /**  Company Code  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  GUID for control  */  
   "ControlID":string,
      /**  Id pof value record  */  
   "ID":string,
      /**  Value  */  
   "Val":string,
      /**  Sequence number  */  
   "Seq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryCustomActionRow{
      /**  Company Code  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  Action ID  */  
   "ActionID":string,
      /**  Displayble text for the action  */  
   "ActionLabel":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryExecuteSettingRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SettingID  */  
   "SettingID":string,
      /**  SettingValue  */  
   "SettingValue":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryFieldAttributeRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  TableID  */  
   "TableID":string,
      /**  FieldName  */  
   "FieldName":string,
      /**  AttributeName  */  
   "AttributeName":string,
      /**  Value  */  
   "Value":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Flags whether the attribute was changed by user.  */  
   "IsOverriden":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryFieldRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  TableID  */  
   "TableID":string,
      /**  Field Name  */  
   "FieldName":string,
      /**  Sequence  */  
   "Seq":number,
      /**  DBSchemaName  */  
   "DBSchemaName":string,
      /**  Database Table Name  */  
   "DBTableName":string,
      /**  Database Field Name  */  
   "DBFieldName":string,
      /**  Data Type  */  
   "DataType":string,
      /**  Description  */  
   "Description":string,
      /**  External  */  
   "External":boolean,
      /**  IsCalculated  */  
   "IsCalculated":boolean,
      /**  Formula  */  
   "Formula":string,
      /**  Field Format  */  
   "FieldFormat":string,
      /**  Field Label  */  
   "FieldLabel":string,
      /**  TableID to use with LikeField  */  
   "LikeDataFieldTableID":string,
      /**  Like Data Field Sequence  */  
   "LikeDataFieldSeq":number,
      /**  Aggregation  */  
   "Aggregation":string,
      /**  IsGroupBy  */  
   "IsGroupBy":boolean,
      /**  Use Like  */  
   "UseLike":boolean,
      /**  Like Data Field Name  */  
   "LikeDataFieldName":string,
      /**  Wheither field can be updated  */  
   "Updatable":boolean,
      /**  Raise event on update  */  
   "RaiseEvent":boolean,
      /**  ID of Quick Search assigned to this query field  */  
   "QuickSearchID":string,
      /**  This flag tells whether this display field is used as source of distinct values for drop down list in IW  */  
   "DropDown":boolean,
      /**  Initial expression for updatable field, filled on UBAQ.GetNew  */  
   "UpdInitExpression":string,
      /**  Alias  */  
   "Alias":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  obsolete, use Alias instead  */  
   "DisplayName":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryFunctionCallRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  FunctionID  */  
   "FunctionID":string,
      /**  ParameterName  */  
   "ParameterName":string,
      /**  Seq  */  
   "Seq":number,
      /**  Value  */  
   "Value":string,
      /**  DataType  */  
   "DataType":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryGroupByRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  GroupByID  */  
   "GroupByID":string,
      /**  Expression  */  
   "Expression":string,
      /**  Seq  */  
   "Seq":number,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryParameterBindingRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  ReferenceID  */  
   "ReferenceID":string,
      /**  ParameterID  */  
   "ParameterID":string,
      /**  MappingType  */  
   "MappingType":string,
      /**  MappingValue  */  
   "MappingValue":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryParameterRow{
      /**  Company Code  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  ParameterID  */  
   "ParameterID":string,
      /**  Data type of the parameter  */  
   "ParameterType":string,
      /**  ParameterLabel  */  
   "ParameterLabel":string,
      /**  Skip condition of parameter is not set  */  
   "SkipIfEmpty":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryReferenceRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  ReferenceID  */  
   "ReferenceID":string,
      /**  ReferenceName  */  
   "ReferenceName":string,
      /**  RefQueryID  */  
   "RefQueryID":string,
      /**  ExecType  */  
   "ExecType":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryRelationFieldRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  Query Relation ID  */  
   "RelationID":string,
      /**  Sequence Number  */  
   "Seq":number,
      /**  Parent Field Name  */  
   "ParentFieldName":string,
      /**  ParentFieldDataType  */  
   "ParentFieldDataType":string,
      /**  ParentFieldIsExpr  */  
   "ParentFieldIsExpr":boolean,
      /**  Child Field Name  */  
   "ChildFieldName":string,
      /**  ChildFieldDataType  */  
   "ChildFieldDataType":string,
      /**  ChildFieldIsExpr  */  
   "ChildFieldIsExpr":boolean,
      /**  AndOr  */  
   "AndOr":string,
      /**  Neg  */  
   "Neg":boolean,
      /**  LeftP  */  
   "LeftP":string,
      /**  RightP  */  
   "RightP":string,
      /**  CompOp  */  
   "CompOp":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryRelationRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  Query Relation ID  */  
   "RelationID":string,
      /**  IsFK  */  
   "IsFK":boolean,
      /**  ParentTableID  */  
   "ParentTableID":string,
      /**  ChildTableID  */  
   "ChildTableID":string,
      /**  "Outer" = outer-join, "" = inner-join  */  
   "JoinType":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "OuterJoin":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QuerySortByRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  TableID  */  
   "TableID":string,
      /**  Field Name  */  
   "FieldName":string,
      /**  Sequence Number  */  
   "Seq":number,
      /**  IsAsc  */  
   "IsAsc":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DisplayName":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QuerySubQueryRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  Name  */  
   "Name":string,
      /**  Type  */  
   "Type":string,
      /**  Seq  */  
   "Seq":number,
      /**  IsUnion  */  
   "IsUnion":boolean,
      /**  LeftP  */  
   "LeftP":string,
      /**  RightP  */  
   "RightP":string,
      /**  SelectListClause  */  
   "SelectListClause":string,
      /**  TopRowExpr  */  
   "TopRowExpr":number,
      /**  TopInPercent  */  
   "TopInPercent":boolean,
      /**  TopWithTies  */  
   "TopWithTies":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  OrderByOffSet  */  
   "OrderByOffSet":string,
      /**  OrderByFetch  */  
   "OrderByFetch":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryTableRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  TableID  */  
   "TableID":string,
      /**  Sequence Number  */  
   "Seq":number,
      /**  DBSchemaName  */  
   "DBSchemaName":string,
      /**  Database Table Name  */  
   "DBTableName":string,
      /**  TableType  */  
   "TableType":string,
      /**  Summary Table flag  */  
   "IsSummaryTable":boolean,
      /**  IsVisibleInDesigner  */  
   "IsVisibleInDesigner":boolean,
      /**  Modifiers  */  
   "Modifiers":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PivotFunction  */  
   "PivotFunction":string,
      /**  PivotDataType  */  
   "PivotDataType":string,
      /**  PivotFieldFormat  */  
   "PivotFieldFormat":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryUpdateFieldRow{
      /**  Company Code  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  MapTableName  */  
   "MapTableName":string,
      /**  MapFieldName  */  
   "MapFieldName":string,
      /**  Direction  */  
   "Direction":boolean,
      /**  Expression  */  
   "Expression":string,
      /**  IsKeyField  */  
   "IsKeyField":boolean,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  NetDataType  */  
   "NetDataType":string,
      /**  Shows field data type - taken from zDataField  */  
   "DataType":string,
      /**  DBTableName + "." + DBFieldName  */  
   "QualifiedName":string,
      /**  Shows if field is required - taken from zDataField  */  
   "Required":boolean,
      /**  Shows field description - taken from zDataField  */  
   "Description":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryUpdateSettingsRow{
      /**  Company  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  AllowAddNew  */  
   "AllowAddNew":boolean,
      /**  AddNewLabel  */  
   "AddNewLabel":string,
      /**  SupportMDR  */  
   "SupportMDR":boolean,
      /**  UpdatableType  */  
   "UpdatableType":string,
      /**  UpdatableBO  */  
   "UpdatableBO":string,
      /**  BOSystemCode  */  
   "BOSystemCode":string,
      /**  UpdateMethod  */  
   "UpdateMethod":string,
      /**  SCUrl  */  
   "SCUrl":string,
      /**  SCWorkflow  */  
   "SCWorkflow":string,
      /**  SCCtxUser  */  
   "SCCtxUser":string,
      /**  SCCtxPwd  */  
   "SCCtxPwd":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  SCUserID  */  
   "SCUserID":string,
      /**  SCPassword  */  
   "SCPassword":string,
      /**  SCCtxUrl  */  
   "SCCtxUrl":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryValueSetItemsRow{
      /**  Company Code  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  ID of set of values. Is referenced by QueryWhereItem record for example.  */  
   "ValueSetID":string,
      /**  Item Value  */  
   "ItemValue":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_QueryWhereItemRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  QueryID  */  
   "QueryID":string,
      /**  SubQueryID  */  
   "SubQueryID":string,
      /**  TableID  */  
   "TableID":string,
      /**  CriteriaID  */  
   "CriteriaID":string,
      /**  Sequence Number  */  
   "Seq":number,
   "FieldName":string,
      /**  DataType  */  
   "DataType":string,
      /**  Operator to use for relation between left value and right value.  */  
   "CompOp":string,
   "AndOr":string,
   "Neg":boolean,
      /**  LeftP  */  
   "LeftP":string,
      /**  RightP  */  
   "RightP":string,
      /**  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  */  
   "IsConst":boolean,
      /**  CriteriaType  */  
   "CriteriaType":number,
      /**  ToTableID  */  
   "ToTableID":string,
   "ToFieldName":string,
      /**  ToDataType  */  
   "ToDataType":string,
   "RValue":string,
      /**  ExtSecurity  */  
   "ExtSecurity":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
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
      @param queryDS
      @param executionParams
   */  
export interface Analyze_input{
   queryDS:Ice_Tablesets_DynamicQueryTableset[],
   executionParams:Ice_Tablesets_QueryExecutionTableset[],
}

export interface Analyze_output{
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   errorMessages:any[],
}
}

   /** Required : 
      @param executionToken
      @param extDsn
      @param cancelExecution
   */  
export interface CheckTestQueryExecution_input{
   executionToken:string,
      /**  dsn for external queries  */  
   extDsn:string,
   cancelExecution:boolean,
}

export interface CheckTestQueryExecution_output{
   returnObj:boolean,
}

   /** Required : 
      @param queryID
      @param executionParams
   */  
export interface ExecuteByID_input{
      /**  The current Query ID  */  
   queryID:string,
   executionParams:Ice_Tablesets_QueryExecutionTableset[],
}

export interface ExecuteByID_output{
      /**  Returns the result of the query  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryDS
      @param executionParams
   */  
export interface Execute_input{
   queryDS:Ice_Tablesets_DynamicQueryTableset[],
   executionParams:Ice_Tablesets_QueryExecutionTableset[],
}

export interface Execute_output{
      /**  Returns the result dataset  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryID
      @param fieldName
      @param queryResultDataset
   */  
export interface FieldUpdateByID_input{
      /**  Updatable query id  */  
   queryID:string,
      /**  Name of an updatable field  */  
   fieldName:string,
      /**  Query result dataset with a row where the field is going to be updated  */  
   queryResultDataset:any,      //schema had no properties on an object.
}

export interface FieldUpdateByID_output{
      /**  Query result dataset with a row where the field is going to be updated  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryDS
      @param fieldName
      @param queryResultDataset
   */  
export interface FieldUpdate_input{
   queryDS:Ice_Tablesets_DynamicQueryTableset[],
      /**  Name of an updatable field  */  
   fieldName:string,
      /**  Query result dataset with a row where the field is going to be updated  */  
   queryResultDataset:any,      //schema had no properties on an object.
}

export interface FieldUpdate_output{
      /**  Query result dataset with a row where the field is going to be updated  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryID
      @param fieldName
      @param queryResultDataset
   */  
export interface FieldValidateByID_input{
      /**  Updatable query id  */  
   queryID:string,
      /**  Name of an updatable field  */  
   fieldName:string,
      /**  Query result dataset with a changed row  */  
   queryResultDataset:any,      //schema had no properties on an object.
}

export interface FieldValidateByID_output{
      /**  Query result dataset with a row where the field is going to be updated  */  
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   isValid:boolean,
}
}

   /** Required : 
      @param queryDS
      @param fieldName
      @param queryResultDataset
   */  
export interface FieldValidate_input{
   queryDS:Ice_Tablesets_DynamicQueryTableset[],
      /**  Name of an updatable field  */  
   fieldName:string,
      /**  Query result dataset with a changed row  */  
   queryResultDataset:any,      //schema had no properties on an object.
}

export interface FieldValidate_output{
      /**  Query result dataset with a row where the field is going to be updated  */  
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   isValid:boolean,
}
}

   /** Required : 
      @param queryID
   */  
export interface GetByIDTranslated_input{
      /**  Query id to load definition  */  
   queryID:string,
}

export interface GetByIDTranslated_output{
   returnObj:Ice_Tablesets_DynamicQueryTableset[],
}

   /** Required : 
      @param queryID
   */  
export interface GetByID_input{
      /**  Query id to load definition.  */  
   queryID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_DynamicQueryTableset[],
}

   /** Required : 
      @param queryIDList
   */  
export interface GetByIDsTranslated_input{
      /**  List of query ids to load definition  */  
   queryIDList:string,
}

export interface GetByIDsTranslated_output{
   returnObj:Ice_Tablesets_DynamicQueryTableset[],
}

   /** Required : 
      @param queryIDList
   */  
export interface GetByIDs_input{
      /**  List of query ids to load definition  */  
   queryIDList:string,
}

export interface GetByIDs_output{
   returnObj:Ice_Tablesets_DynamicQueryTableset[],
}

   /** Required : 
      @param queryID
      @param executionParams
      @param distinctFields
   */  
export interface GetDistinctValues_input{
      /**  The Query ID  */  
   queryID:string,
   executionParams:Ice_Tablesets_QueryExecutionTableset[],
      /**  List of query display fields distinct values of which should be returned  */  
   distinctFields:string,
}

export interface GetDistinctValues_output{
      /**  Returns the result dataset  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryID
      @param executionParams
      @param pageSize
      @param absolutePage
   */  
export interface GetListByID_input{
      /**  Query's id to execute  */  
   queryID:string,
   executionParams:Ice_Tablesets_QueryExecutionTableset[],
      /**  Number of records in a page. 0 means you don't want paging  */  
   pageSize:number,
      /**  Number of page to return. 1 should be set by default  */  
   absolutePage:number,
}

export interface GetListByID_output{
      /**  Returns the result dataset  */  
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   hasMorePage:boolean,
}
}

   /** Required : 
      @param queryDS
      @param executionParams
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
   queryDS:Ice_Tablesets_DynamicQueryTableset[],
   executionParams:Ice_Tablesets_QueryExecutionTableset[],
      /**  Number of records in a page. 0 means you don't want paging  */  
   pageSize:number,
      /**  Number of page to return. 1 should be set by default  */  
   absolutePage:number,
}

export interface GetList_output{
      /**  Returns the result dataset  */  
   returnObj:any,      //schema had no properties on an object.
parameters : {
      /**  output parameters  */  
   hasMorePage:boolean,
}
}

   /** Required : 
      @param queryID
   */  
export interface GetNewByID_input{
      /**  Updatable query id  */  
   queryID:string,
}

export interface GetNewByID_output{
      /**  Result of method call. A new expected to be added to results table  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryDS
   */  
export interface GetNew_input{
   queryDS:Ice_Tablesets_DynamicQueryTableset[],
}

export interface GetNew_output{
      /**  Result of method call. A new expected to be added to results table  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryID
      @param companyID
   */  
export interface GetQueryEmptyResultSetByIDAndCompany_input{
      /**  The Query ID  */  
   queryID:string,
      /**  The query's Company ID  */  
   companyID:string,
}

export interface GetQueryEmptyResultSetByIDAndCompany_output{
      /**  Returns the empty dataset representing the query result  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryID
   */  
export interface GetQueryEmptyResultSetByID_input{
      /**  The Query ID  */  
   queryID:string,
}

export interface GetQueryEmptyResultSetByID_output{
      /**  Returns the empty dataset representing the query result  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryDS
   */  
export interface GetQueryEmptyResultSet_input{
   queryDS:Ice_Tablesets_DynamicQueryTableset[],
}

export interface GetQueryEmptyResultSet_output{
      /**  Returns the empty dataset representing the query result  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryID
   */  
export interface GetQueryExecutionParametersByID_input{
      /**  The Query ID  */  
   queryID:string,
}

export interface GetQueryExecutionParametersByID_output{
   returnObj:Ice_Tablesets_QueryExecutionTableset[],
}

   /** Required : 
      @param queryDS
   */  
export interface GetQueryExecutionParameters_input{
   queryDS:Ice_Tablesets_DynamicQueryTableset[],
}

export interface GetQueryExecutionParameters_output{
   returnObj:Ice_Tablesets_QueryExecutionTableset[],
}

   /** Required : 
      @param executionToken
      @param extDsn
   */  
export interface GetQueryExecutionPlan_input{
   executionToken:string,
      /**  dsn for external queries  */  
   extDsn:string,
}

export interface GetQueryExecutionPlan_output{
   returnObj:string,
}

   /** Required : 
      @param likeTableName
      @param likeFieldName
   */  
export interface GetQueryListFromLike_input{
      /**  The table name of the like field  */  
   likeTableName:string,
      /**  The field name of the like field  */  
   likeFieldName:string,
}

export interface GetQueryListFromLike_output{
   returnObj:Ice_Tablesets_DynamicQueryListTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetQueryList_input{
      /**  The criteria  */  
   whereClause:string,
      /**  Size of the page  */  
   pageSize:number,
      /**  The number of the page to return  */  
   absolutePage:number,
}

export interface GetQueryList_output{
   returnObj:Ice_Tablesets_DynamicQueryListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param queryID
   */  
export interface GetQueryResultSetMetadataByID_input{
      /**  The Query ID  */  
   queryID:string,
}

export interface GetQueryResultSetMetadataByID_output{
      /**  Returns the attributes and values grouped by query's display fields  */  
   returnObj:Ice_BO_DynamicQuery_ResultFieldMetadata[],
}

   /** Required : 
      @param whereClauseDynamicQuery
      @param whereClauseQueryCtrl
      @param whereClauseQueryCtrlValues
      @param whereClauseQueryCustomAction
      @param whereClauseQueryExecuteSetting
      @param whereClauseQueryParameter
      @param whereClauseQueryReference
      @param whereClauseQueryParameterBinding
      @param whereClauseQuerySubQuery
      @param whereClauseQueryRelation
      @param whereClauseQueryRelationField
      @param whereClauseQuerySortBy
      @param whereClauseQueryWhereItem
      @param whereClauseQueryGroupBy
      @param whereClauseQueryTable
      @param whereClauseQueryField
      @param whereClauseQueryFunctionCall
      @param whereClauseQueryUpdateField
      @param whereClauseQueryUpdateSettings
      @param whereClauseQueryValueSetItems
      @param whereClauseQueryFieldAttribute
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseDynamicQuery:string,
   whereClauseQueryCtrl:string,
   whereClauseQueryCtrlValues:string,
   whereClauseQueryCustomAction:string,
   whereClauseQueryExecuteSetting:string,
   whereClauseQueryParameter:string,
   whereClauseQueryReference:string,
   whereClauseQueryParameterBinding:string,
   whereClauseQuerySubQuery:string,
   whereClauseQueryRelation:string,
   whereClauseQueryRelationField:string,
   whereClauseQuerySortBy:string,
   whereClauseQueryWhereItem:string,
   whereClauseQueryGroupBy:string,
   whereClauseQueryTable:string,
   whereClauseQueryField:string,
   whereClauseQueryFunctionCall:string,
   whereClauseQueryUpdateField:string,
   whereClauseQueryUpdateSettings:string,
   whereClauseQueryValueSetItems:string,
   whereClauseQueryFieldAttribute:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_DynamicQueryTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

export interface Ice_BO_DynamicQuery_ResultFieldMetadata{
   alias:string,
   typeName:string,
   seq:number,
   caption:string,
   format:string,
   like:string,
   readOnly:boolean,
   required:boolean,
   attributes:any,      //schema had no properties on an object.
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

export interface Ice_Tablesets_DynamicQueryListRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  AuthorID  */  
   AuthorID:string,
      /**  Description  */  
   Description:string,
      /**  IsShared  */  
   IsShared:boolean,
      /**  CGCCode  */  
   CGCCode:string,
      /**  XCompany  */  
   XCompany:boolean,
      /**  Updatable  */  
   Updatable:boolean,
      /**  ExtQuery  */  
   ExtQuery:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRowID  */  
   SysRowID:string,
   AllCompanies:boolean,
      /**  SecCode  */  
   SecCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DynamicQueryListTableset{
   DynamicQueryList:Ice_Tablesets_DynamicQueryListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_DynamicQueryRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  AuthorID  */  
   AuthorID:string,
      /**  Description  */  
   Description:string,
      /**  DisplayPhrase  */  
   DisplayPhrase:string,
      /**  IsShared  */  
   IsShared:boolean,
      /**  Version  */  
   Version:string,
      /**  CGCCode  */  
   CGCCode:string,
      /**  XCompany  */  
   XCompany:boolean,
      /**  GlbCompany  */  
   GlbCompany:string,
      /**  Updatable  */  
   Updatable:boolean,
      /**  ExtQuery  */  
   ExtQuery:boolean,
      /**  ExtDatasourceName  */  
   ExtDatasourceName:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Extension  */  
   Extension:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SecCode  */  
   SecCode:string,
   AllCompanies:boolean,
      /**  UseLiveDB  */  
   UseLiveDB:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_DynamicQueryTableset{
   DynamicQuery:Ice_Tablesets_DynamicQueryRow[],
   QueryCtrl:Ice_Tablesets_QueryCtrlRow[],
   QueryCtrlValues:Ice_Tablesets_QueryCtrlValuesRow[],
   QueryCustomAction:Ice_Tablesets_QueryCustomActionRow[],
   QueryExecuteSetting:Ice_Tablesets_QueryExecuteSettingRow[],
   QueryParameter:Ice_Tablesets_QueryParameterRow[],
   QueryReference:Ice_Tablesets_QueryReferenceRow[],
   QueryParameterBinding:Ice_Tablesets_QueryParameterBindingRow[],
   QuerySubQuery:Ice_Tablesets_QuerySubQueryRow[],
   QueryRelation:Ice_Tablesets_QueryRelationRow[],
   QueryRelationField:Ice_Tablesets_QueryRelationFieldRow[],
   QuerySortBy:Ice_Tablesets_QuerySortByRow[],
   QueryWhereItem:Ice_Tablesets_QueryWhereItemRow[],
   QueryGroupBy:Ice_Tablesets_QueryGroupByRow[],
   QueryTable:Ice_Tablesets_QueryTableRow[],
   QueryField:Ice_Tablesets_QueryFieldRow[],
   QueryFieldAttribute:Ice_Tablesets_QueryFieldAttributeRow[],
   QueryFunctionCall:Ice_Tablesets_QueryFunctionCallRow[],
   QueryUpdateField:Ice_Tablesets_QueryUpdateFieldRow[],
   QueryUpdateSettings:Ice_Tablesets_QueryUpdateSettingsRow[],
   QueryValueSetItems:Ice_Tablesets_QueryValueSetItemsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ExecutionFilterRow{
   DataTableID:string,
   FieldName:string,
   Neg:boolean,
   CompOp:string,
   RValue:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExecutionParameterRow{
   ParameterID:string,
   ParameterValue:string,
   ValueType:string,
   IsEmpty:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExecutionSettingRow{
      /**  name of setting  */  
   Name:string,
   Value:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ExecutionValueSetItemsRow{
   ValueSetID:string,
   ItemValue:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryCtrlRow{
      /**  Company Code  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  GUID for control  */  
   ControlID:string,
      /**  Data Source  */  
   DataSource:string,
      /**  Data Type  */  
   DataType:string,
      /**  Field Format  */  
   FieldFormat:string,
      /**  Mandatory flag  */  
   IsMandatory:boolean,
      /**  Default Value  */  
   DefaultValue:string,
      /**   One of predefined constants:
Standard ? free type editor/date picker, depend on DataType.
RadioSet ? radio button set. Items are specified in QueryCtrlValues table
DropDown ? dropdown list. Items are specified in QueryCtrlValues table
DropDownBAQ ? dropdown list. Information are stored in QueryCtrlValues table with tree rows with Ids:BAQID, BAQDisplayColumn, BAQValueColumn
DropDownUserCodes - dropdown list. Information are stored in QueryCtrlValues table with one row with Id = UserCodeTypeID  */  
   ControlType:string,
      /**  Type of the datasource 0 - updatable field, 1 - parameter  */  
   SourceType:number,
      /**  ListSource  */  
   ListSource:string,
      /**  DisplayColumn  */  
   DisplayColumn:string,
      /**  ValueColumn  */  
   ValueColumn:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Seq  */  
   Seq:number,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryCtrlValuesRow{
      /**  Company Code  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  GUID for control  */  
   ControlID:string,
      /**  Id pof value record  */  
   ID:string,
      /**  Value  */  
   Val:string,
      /**  Sequence number  */  
   Seq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryCustomActionRow{
      /**  Company Code  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  Action ID  */  
   ActionID:string,
      /**  Displayble text for the action  */  
   ActionLabel:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryExecuteSettingRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SettingID  */  
   SettingID:string,
      /**  SettingValue  */  
   SettingValue:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryExecutionTableset{
   ExecutionFilter:Ice_Tablesets_ExecutionFilterRow[],
   ExecutionParameter:Ice_Tablesets_ExecutionParameterRow[],
   ExecutionSetting:Ice_Tablesets_ExecutionSettingRow[],
   ExecutionValueSetItems:Ice_Tablesets_ExecutionValueSetItemsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_QueryFieldAttributeRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  TableID  */  
   TableID:string,
      /**  FieldName  */  
   FieldName:string,
      /**  AttributeName  */  
   AttributeName:string,
      /**  Value  */  
   Value:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Flags whether the attribute was changed by user.  */  
   IsOverriden:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryFieldRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  TableID  */  
   TableID:string,
      /**  Field Name  */  
   FieldName:string,
      /**  Sequence  */  
   Seq:number,
      /**  DBSchemaName  */  
   DBSchemaName:string,
      /**  Database Table Name  */  
   DBTableName:string,
      /**  Database Field Name  */  
   DBFieldName:string,
      /**  Data Type  */  
   DataType:string,
      /**  Description  */  
   Description:string,
      /**  External  */  
   External:boolean,
      /**  IsCalculated  */  
   IsCalculated:boolean,
      /**  Formula  */  
   Formula:string,
      /**  Field Format  */  
   FieldFormat:string,
      /**  Field Label  */  
   FieldLabel:string,
      /**  TableID to use with LikeField  */  
   LikeDataFieldTableID:string,
      /**  Like Data Field Sequence  */  
   LikeDataFieldSeq:number,
      /**  Aggregation  */  
   Aggregation:string,
      /**  IsGroupBy  */  
   IsGroupBy:boolean,
      /**  Use Like  */  
   UseLike:boolean,
      /**  Like Data Field Name  */  
   LikeDataFieldName:string,
      /**  Wheither field can be updated  */  
   Updatable:boolean,
      /**  Raise event on update  */  
   RaiseEvent:boolean,
      /**  ID of Quick Search assigned to this query field  */  
   QuickSearchID:string,
      /**  This flag tells whether this display field is used as source of distinct values for drop down list in IW  */  
   DropDown:boolean,
      /**  Initial expression for updatable field, filled on UBAQ.GetNew  */  
   UpdInitExpression:string,
      /**  Alias  */  
   Alias:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  obsolete, use Alias instead  */  
   DisplayName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryFunctionCallRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  FunctionID  */  
   FunctionID:string,
      /**  ParameterName  */  
   ParameterName:string,
      /**  Seq  */  
   Seq:number,
      /**  Value  */  
   Value:string,
      /**  DataType  */  
   DataType:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryGroupByRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  GroupByID  */  
   GroupByID:string,
      /**  Expression  */  
   Expression:string,
      /**  Seq  */  
   Seq:number,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryParameterBindingRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  ReferenceID  */  
   ReferenceID:string,
      /**  ParameterID  */  
   ParameterID:string,
      /**  MappingType  */  
   MappingType:string,
      /**  MappingValue  */  
   MappingValue:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryParameterRow{
      /**  Company Code  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  ParameterID  */  
   ParameterID:string,
      /**  Data type of the parameter  */  
   ParameterType:string,
      /**  ParameterLabel  */  
   ParameterLabel:string,
      /**  Skip condition of parameter is not set  */  
   SkipIfEmpty:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryReferenceRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  ReferenceID  */  
   ReferenceID:string,
      /**  ReferenceName  */  
   ReferenceName:string,
      /**  RefQueryID  */  
   RefQueryID:string,
      /**  ExecType  */  
   ExecType:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryRelationFieldRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  Query Relation ID  */  
   RelationID:string,
      /**  Sequence Number  */  
   Seq:number,
      /**  Parent Field Name  */  
   ParentFieldName:string,
      /**  ParentFieldDataType  */  
   ParentFieldDataType:string,
      /**  ParentFieldIsExpr  */  
   ParentFieldIsExpr:boolean,
      /**  Child Field Name  */  
   ChildFieldName:string,
      /**  ChildFieldDataType  */  
   ChildFieldDataType:string,
      /**  ChildFieldIsExpr  */  
   ChildFieldIsExpr:boolean,
      /**  AndOr  */  
   AndOr:string,
      /**  Neg  */  
   Neg:boolean,
      /**  LeftP  */  
   LeftP:string,
      /**  RightP  */  
   RightP:string,
      /**  CompOp  */  
   CompOp:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryRelationRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  Query Relation ID  */  
   RelationID:string,
      /**  IsFK  */  
   IsFK:boolean,
      /**  ParentTableID  */  
   ParentTableID:string,
      /**  ChildTableID  */  
   ChildTableID:string,
      /**  "Outer" = outer-join, "" = inner-join  */  
   JoinType:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   OuterJoin:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QuerySortByRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  TableID  */  
   TableID:string,
      /**  Field Name  */  
   FieldName:string,
      /**  Sequence Number  */  
   Seq:number,
      /**  IsAsc  */  
   IsAsc:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DisplayName:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QuerySubQueryRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  Name  */  
   Name:string,
      /**  Type  */  
   Type:string,
      /**  Seq  */  
   Seq:number,
      /**  IsUnion  */  
   IsUnion:boolean,
      /**  LeftP  */  
   LeftP:string,
      /**  RightP  */  
   RightP:string,
      /**  SelectListClause  */  
   SelectListClause:string,
      /**  TopRowExpr  */  
   TopRowExpr:number,
      /**  TopInPercent  */  
   TopInPercent:boolean,
      /**  TopWithTies  */  
   TopWithTies:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  OrderByOffSet  */  
   OrderByOffSet:string,
      /**  OrderByFetch  */  
   OrderByFetch:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryTableRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  TableID  */  
   TableID:string,
      /**  Sequence Number  */  
   Seq:number,
      /**  DBSchemaName  */  
   DBSchemaName:string,
      /**  Database Table Name  */  
   DBTableName:string,
      /**  TableType  */  
   TableType:string,
      /**  Summary Table flag  */  
   IsSummaryTable:boolean,
      /**  IsVisibleInDesigner  */  
   IsVisibleInDesigner:boolean,
      /**  Modifiers  */  
   Modifiers:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PivotFunction  */  
   PivotFunction:string,
      /**  PivotDataType  */  
   PivotDataType:string,
      /**  PivotFieldFormat  */  
   PivotFieldFormat:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryUpdateFieldRow{
      /**  Company Code  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  MapTableName  */  
   MapTableName:string,
      /**  MapFieldName  */  
   MapFieldName:string,
      /**  Direction  */  
   Direction:boolean,
      /**  Expression  */  
   Expression:string,
      /**  IsKeyField  */  
   IsKeyField:boolean,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  NetDataType  */  
   NetDataType:string,
      /**  Shows field data type - taken from zDataField  */  
   DataType:string,
      /**  DBTableName + "." + DBFieldName  */  
   QualifiedName:string,
      /**  Shows if field is required - taken from zDataField  */  
   Required:boolean,
      /**  Shows field description - taken from zDataField  */  
   Description:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryUpdateSettingsRow{
      /**  Company  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  AllowAddNew  */  
   AllowAddNew:boolean,
      /**  AddNewLabel  */  
   AddNewLabel:string,
      /**  SupportMDR  */  
   SupportMDR:boolean,
      /**  UpdatableType  */  
   UpdatableType:string,
      /**  UpdatableBO  */  
   UpdatableBO:string,
      /**  BOSystemCode  */  
   BOSystemCode:string,
      /**  UpdateMethod  */  
   UpdateMethod:string,
      /**  SCUrl  */  
   SCUrl:string,
      /**  SCWorkflow  */  
   SCWorkflow:string,
      /**  SCCtxUser  */  
   SCCtxUser:string,
      /**  SCCtxPwd  */  
   SCCtxPwd:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  SCUserID  */  
   SCUserID:string,
      /**  SCPassword  */  
   SCPassword:string,
      /**  SCCtxUrl  */  
   SCCtxUrl:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryValueSetItemsRow{
      /**  Company Code  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  ID of set of values. Is referenced by QueryWhereItem record for example.  */  
   ValueSetID:string,
      /**  Item Value  */  
   ItemValue:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_QueryWhereItemRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  QueryID  */  
   QueryID:string,
      /**  SubQueryID  */  
   SubQueryID:string,
      /**  TableID  */  
   TableID:string,
      /**  CriteriaID  */  
   CriteriaID:string,
      /**  Sequence Number  */  
   Seq:number,
   FieldName:string,
      /**  DataType  */  
   DataType:string,
      /**  Operator to use for relation between left value and right value.  */  
   CompOp:string,
   AndOr:string,
   Neg:boolean,
      /**  LeftP  */  
   LeftP:string,
      /**  RightP  */  
   RightP:string,
      /**  Indicates that the ChildField is a contant rather than a database field.  Example: Relationships to Reason requires a reasontype which would be entered as a constant.  */  
   IsConst:boolean,
      /**  CriteriaType  */  
   CriteriaType:number,
      /**  ToTableID  */  
   ToTableID:string,
   ToFieldName:string,
      /**  ToDataType  */  
   ToDataType:string,
   RValue:string,
      /**  ExtSecurity  */  
   ExtSecurity:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param queryID
      @param companyID
   */  
export interface InvalidateRuntimeQueryCache_input{
      /**  Query id to remove from cache. Leave empty to clear cache completely.  */  
   queryID:string,
      /**  Company Id from query definition.  */  
   companyID:string,
}

export interface InvalidateRuntimeQueryCache_output{
}

   /** Required : 
      @param queryID
      @param actionID
      @param queryResultDataset
   */  
export interface RunCustomActionByID_input{
      /**  Updatable query id  */  
   queryID:string,
      /**  An action id  */  
   actionID:string,
      /**  Query result dataset with a changed row  */  
   queryResultDataset:any,      //schema had no properties on an object.
}

export interface RunCustomActionByID_output{
      /**  Query result dataset with a changed row  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryDS
      @param actionID
      @param queryResultDataset
   */  
export interface RunCustomAction_input{
   queryDS:Ice_Tablesets_DynamicQueryTableset[],
      /**  An action id  */  
   actionID:string,
      /**  Query result dataset with a changed row  */  
   queryResultDataset:any,      //schema had no properties on an object.
}

export interface RunCustomAction_output{
      /**  Query result dataset with a changed row  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryID
      @param queryResultDataset
   */  
export interface UpdateByID_input{
      /**  Updatable query id  */  
   queryID:string,
      /**  Query result dataset  */  
   queryResultDataset:any,      //schema had no properties on an object.
}

export interface UpdateByID_output{
      /**  Result of Update method call. Usually this is incoming query result dataset with some changes  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param queryDS
      @param queryResultDataset
   */  
export interface Update_input{
   queryDS:Ice_Tablesets_DynamicQueryTableset[],
      /**  Query result dataset  */  
   queryResultDataset:any,      //schema had no properties on an object.
}

export interface Update_output{
      /**  Result of Update method call. Usually this is incoming query result dataset with some changes  */  
   returnObj:any,      //schema had no properties on an object.
}

