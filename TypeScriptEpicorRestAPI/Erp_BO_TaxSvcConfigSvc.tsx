import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.TaxSvcConfigSvc
// Version: v1



//////////////////////////////////////////////////////////////////////////
// OData methods:
//////////////////////////////////////////////////////////////////////////

   /**  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcConfigRow
   */  
export function get_TaxSvcConfigs(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcConfigRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/TaxSvcConfigs", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_TaxSvcConfigs(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/TaxSvcConfigs", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   */  
export function get_TaxSvcConfigs_Company(Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_TaxSvcConfigRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/TaxSvcConfigs(" + Company + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxSvcConfigRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_TaxSvcConfigs_Company(Company:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/TaxSvcConfigs(" + Company + ")", {
          method: 'patch',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/TaxSvcConfigs(" + Company + ")", {
          method: 'delete',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxSvcConfigListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcConfigListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcConfigListRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseTaxSvcConfig:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseTaxSvcConfig!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseTaxSvcConfig=" + whereClauseTaxSvcConfig
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/GetByID", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxSvcConfig_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxSvcConfig_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewTaxSvcConfig(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/GetNewTaxSvcConfig", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/DeleteByID", {
          method: 'post',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
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

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Update(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
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
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateExt(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.TaxSvcConfigSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as any)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}



//////////////////////////////////////////////////////////////////////////
// OData Schemas:
//////////////////////////////////////////////////////////////////////////
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcConfigListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxSvcConfigListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxSvcConfigRow{
   "odatametadata":string,
   "value":Erp_Tablesets_TaxSvcConfigRow[],
}

export interface Erp_Tablesets_TaxSvcConfigListRow{
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




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
export interface DeleteByID_output{
}

export interface Erp_Tablesets_TaxSvcConfigListRow{
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
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_TaxSvcConfigListTableset{
   TaxSvcConfigList:Erp_Tablesets_TaxSvcConfigListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
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

export interface Erp_Tablesets_TaxSvcConfigTableset{
   TaxSvcConfig:Erp_Tablesets_TaxSvcConfigRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtTaxSvcConfigTableset{
   TaxSvcConfig:Erp_Tablesets_TaxSvcConfigRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_TaxSvcConfigTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_TaxSvcConfigTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_TaxSvcConfigTableset[],
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
   returnObj:Erp_Tablesets_TaxSvcConfigListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewTaxSvcConfig_input{
   ds:Erp_Tablesets_TaxSvcConfigTableset[],
}

export interface GetNewTaxSvcConfig_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaxSvcConfigTableset[],
}
}

   /** Required : 
      @param whereClauseTaxSvcConfig
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseTaxSvcConfig:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_TaxSvcConfigTableset[],
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
   ds:Erp_Tablesets_UpdExtTaxSvcConfigTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtTaxSvcConfigTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_TaxSvcConfigTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_TaxSvcConfigTableset[],
}
}

