import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.CurrExRateSearchSvc
// Description: Return unique records based on RateGrpCode and Effective date
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/$metadata", {
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
   Description: Get CurrExRateSearches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CurrExRateSearches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrExRateRow
   */  
export function get_CurrExRateSearches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrExRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/CurrExRateSearches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrExRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CurrExRateSearches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CurrExRateRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CurrExRateRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CurrExRateSearches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/CurrExRateSearches", {
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
   Summary: Calls GetByID to retrieve the CurrExRateSearch item
   Description: Calls GetByID to retrieve the CurrExRateSearch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CurrExRateSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param SourceCurrCode Desc: SourceCurrCode   Required: True   Allow empty value : True
      @param TargetCurrCode Desc: TargetCurrCode   Required: True   Allow empty value : True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CurrExRateRow
   */  
export function get_CurrExRateSearches_Company_RateGrpCode_SourceCurrCode_TargetCurrCode_EffectiveDate(Company:string, RateGrpCode:string, SourceCurrCode:string, TargetCurrCode:string, EffectiveDate:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_CurrExRateRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/CurrExRateSearches(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + "," + EffectiveDate + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_CurrExRateRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update CurrExRateSearch for the service
   Description: Calls UpdateExt to update CurrExRateSearch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CurrExRateSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param SourceCurrCode Desc: SourceCurrCode   Required: True   Allow empty value : True
      @param TargetCurrCode Desc: TargetCurrCode   Required: True   Allow empty value : True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CurrExRateRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_CurrExRateSearches_Company_RateGrpCode_SourceCurrCode_TargetCurrCode_EffectiveDate(Company:string, RateGrpCode:string, SourceCurrCode:string, TargetCurrCode:string, EffectiveDate:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/CurrExRateSearches(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + "," + EffectiveDate + ")", {
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
   Summary: Call UpdateExt to delete CurrExRateSearch item
   Description: Call UpdateExt to delete CurrExRateSearch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CurrExRateSearch
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param RateGrpCode Desc: RateGrpCode   Required: True   Allow empty value : True
      @param SourceCurrCode Desc: SourceCurrCode   Required: True   Allow empty value : True
      @param TargetCurrCode Desc: TargetCurrCode   Required: True   Allow empty value : True
      @param EffectiveDate Desc: EffectiveDate   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_CurrExRateSearches_Company_RateGrpCode_SourceCurrCode_TargetCurrCode_EffectiveDate(Company:string, RateGrpCode:string, SourceCurrCode:string, TargetCurrCode:string, EffectiveDate:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/CurrExRateSearches(" + Company + "," + RateGrpCode + "," + SourceCurrCode + "," + TargetCurrCode + "," + EffectiveDate + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CurrExRateListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrExRateListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrExRateListRow)
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
export function get_GetRows(whereClauseCurrExRate:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseCurrExRate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseCurrExRate=" + whereClauseCurrExRate
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(rateGrpCode:string, sourceCurrCode:string, targetCurrCode:string, effectiveDate:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof rateGrpCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "rateGrpCode=" + rateGrpCode
   }
   if(typeof sourceCurrCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sourceCurrCode=" + sourceCurrCode
   }
   if(typeof targetCurrCode!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "targetCurrCode=" + targetCurrCode
   }
   if(typeof effectiveDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "effectiveDate=" + effectiveDate
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/GetList" + params, {
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
   Summary: Invoke method GetNewCurrExRate
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCurrExRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCurrExRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCurrExRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewCurrExRate(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/GetNewCurrExRate", {
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
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteByID(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.CurrExRateSearchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrExRateListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CurrExRateListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CurrExRateRow{
   "odatametadata":string,
   "value":Erp_Tablesets_CurrExRateRow[],
}

export interface Erp_Tablesets_CurrExRateListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code that identifies the source currency.  */  
   "SourceCurrCode":string,
      /**  This rate is effective as of this date.  */  
   "EffectiveDate":string,
      /**   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "CurrentRate":number,
      /**  System date at time that record was modified.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was modified.  */  
   "SysTime":number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   "Reference":string,
      /**  A unique code that identifies the target currency.  */  
   "TargetCurrCode":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Value of the current rate modified by the scale of the Source and Target. DisplayRate = CurrentRate  * (Source Currency Scale / Target Currency Scale)  */  
   "DisplayRate":number,
      /**  Indicates if the exchange rate is fixed and cannot be updated  */  
   "FixedRate":boolean,
      /**  Display factor for exchange rates  */  
   "SourceScaleFactor":number,
      /**  Display factor for exchange rates  */  
   "TargetScaleFactor":number,
      /**  This field let us know if the combination RateGrpCode/SourceCurrCode/TargetCurrCode already exists. This field is filled in the currExRateAfterGetNew method.  */  
   "HasHistory":boolean,
      /**  Tell us is this record has the last effective date. Only records with the last effective date can be modified without user permissions.  */  
   "IsLastEffectiveDate":boolean,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   "GlbFlag":boolean,
   "HasSecurity":boolean,
      /**  Description  */  
   "RateGrpCodeDescription":string,
      /**  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  */  
   "RuleCodeRuleCode":number,
      /**  Indicates which exchange rate to display/update on the transaction  */  
   "RuleCodeDisplayMode":number,
      /**  Indiates if the exchange rate is fixed and cannot be updated  */  
   "RuleCodeFixedRate":boolean,
      /**  Description of the currency  */  
   "SourceCurrCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "SourceCurrCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "SourceCurrDocumentDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "SourceCurrCurrencyID":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "SourceCurrCurrName":string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   "TargetCurrCurrName":string,
      /**  Description of the currency  */  
   "TargetCurrCurrDesc":string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   "TargetCurrCurrSymbol":string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   "TargetCurrDocumentDesc":string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   "TargetCurrCurrencyID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_CurrExRateRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique code that identifies the source currency.  */  
   "SourceCurrCode":string,
      /**  This rate is effective as of this date.  */  
   "EffectiveDate":string,
      /**   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "CurrentRate":number,
      /**  System date at time that record was modified.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was modified.  */  
   "SysTime":number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   "Reference":string,
      /**  A unique code that identifies the target currency.  */  
   "TargetCurrCode":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Value of the current rate modified by the scale of the Source and Target. DisplayRate = CurrentRate  * (Source Currency Scale / Target Currency Scale)  */  
   "DisplayRate":number,
      /**  Indicates if the exchange rate is fixed and cannot be updated  */  
   "FixedRate":boolean,
      /**  Display factor for exchange rates  */  
   "SourceScaleFactor":number,
      /**  Display factor for exchange rates  */  
   "TargetScaleFactor":number,
      /**  This field let us know if the combination RateGrpCode/SourceCurrCode/TargetCurrCode already exists. This field is filled in the currExRateAfterGetNew method.  */  
   "HasHistory":boolean,
      /**  Tell us is this record has the last effective date. Only records with the last effective date can be modified without user permissions.  */  
   "IsLastEffectiveDate":boolean,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   "GlbFlag":boolean,
   "HasSecurity":boolean,
      /**  Source Currency ID with Scale Factor  */  
   "SouceCurrDspID":string,
      /**  Target Currency ID with Scale Factor  */  
   "TargetCurrDspID":string,
      /**  Describes Source/Target ratio  */  
   "ScaleDescr":string,
   "CurrRateActual":number,
      /**  RuleCode Description  */  
   "RuleCodeDesc":string,
   "BitFlag":number,
   "RateGrpCodeDescription":string,
   "RuleCodeRuleCode":number,
   "RuleCodeFixedRate":boolean,
   "RuleCodeDisplayMode":number,
   "SourceCurrCurrName":string,
   "SourceCurrCurrDesc":string,
   "SourceCurrCurrencyID":string,
   "SourceCurrDocumentDesc":string,
   "SourceCurrCurrSymbol":string,
   "SourceCurrMaintRate":boolean,
   "TargetCurrDocumentDesc":string,
   "TargetCurrCurrSymbol":string,
   "TargetCurrCurrencyID":string,
   "TargetCurrCurrDesc":string,
   "TargetCurrCurrName":string,
   "TargetCurrMaintRate":boolean,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param rateGrpCode
      @param sourceCurrCode
      @param targetCurrCode
      @param effectiveDate
   */  
export interface DeleteByID_input{
   rateGrpCode:string,
   sourceCurrCode:string,
   targetCurrCode:string,
   effectiveDate:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_CurrExRateListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the source currency.  */  
   SourceCurrCode:string,
      /**  This rate is effective as of this date.  */  
   EffectiveDate:string,
      /**   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   CurrentRate:number,
      /**  System date at time that record was modified.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was modified.  */  
   SysTime:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   Reference:string,
      /**  A unique code that identifies the target currency.  */  
   TargetCurrCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Value of the current rate modified by the scale of the Source and Target. DisplayRate = CurrentRate  * (Source Currency Scale / Target Currency Scale)  */  
   DisplayRate:number,
      /**  Indicates if the exchange rate is fixed and cannot be updated  */  
   FixedRate:boolean,
      /**  Display factor for exchange rates  */  
   SourceScaleFactor:number,
      /**  Display factor for exchange rates  */  
   TargetScaleFactor:number,
      /**  This field let us know if the combination RateGrpCode/SourceCurrCode/TargetCurrCode already exists. This field is filled in the currExRateAfterGetNew method.  */  
   HasHistory:boolean,
      /**  Tell us is this record has the last effective date. Only records with the last effective date can be modified without user permissions.  */  
   IsLastEffectiveDate:boolean,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   GlbFlag:boolean,
   HasSecurity:boolean,
      /**  Description  */  
   RateGrpCodeDescription:string,
      /**  Indicates the type of conversion rule. Direct, Inverse, Cross Rate, Reverse Cross Rate, Double Cross Rate or Reverse Double Cross Rate  */  
   RuleCodeRuleCode:number,
      /**  Indicates which exchange rate to display/update on the transaction  */  
   RuleCodeDisplayMode:number,
      /**  Indiates if the exchange rate is fixed and cannot be updated  */  
   RuleCodeFixedRate:boolean,
      /**  Description of the currency  */  
   SourceCurrCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   SourceCurrCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   SourceCurrDocumentDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   SourceCurrCurrencyID:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   SourceCurrCurrName:string,
      /**   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  */  
   TargetCurrCurrName:string,
      /**  Description of the currency  */  
   TargetCurrCurrDesc:string,
      /**  A symbol that identifies the currency. Used on Forms and displays  */  
   TargetCurrCurrSymbol:string,
      /**   An extended description that can be used on documents such as
POs and invoices.  */  
   TargetCurrDocumentDesc:string,
      /**  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  */  
   TargetCurrCurrencyID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CurrExRateListTableset{
   CurrExRateList:Erp_Tablesets_CurrExRateListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_CurrExRateRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique code that identifies the source currency.  */  
   SourceCurrCode:string,
      /**  This rate is effective as of this date.  */  
   EffectiveDate:string,
      /**   Current Rate will be the default used by the system.
Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   CurrentRate:number,
      /**  System date at time that record was modified.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was modified.  */  
   SysTime:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   Reference:string,
      /**  A unique code that identifies the target currency.  */  
   TargetCurrCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Value of the current rate modified by the scale of the Source and Target. DisplayRate = CurrentRate  * (Source Currency Scale / Target Currency Scale)  */  
   DisplayRate:number,
      /**  Indicates if the exchange rate is fixed and cannot be updated  */  
   FixedRate:boolean,
      /**  Display factor for exchange rates  */  
   SourceScaleFactor:number,
      /**  Display factor for exchange rates  */  
   TargetScaleFactor:number,
      /**  This field let us know if the combination RateGrpCode/SourceCurrCode/TargetCurrCode already exists. This field is filled in the currExRateAfterGetNew method.  */  
   HasHistory:boolean,
      /**  Tell us is this record has the last effective date. Only records with the last effective date can be modified without user permissions.  */  
   IsLastEffectiveDate:boolean,
      /**  Indicates if the Currency Rate Group is Global (master or linked)  */  
   GlbFlag:boolean,
   HasSecurity:boolean,
      /**  Source Currency ID with Scale Factor  */  
   SouceCurrDspID:string,
      /**  Target Currency ID with Scale Factor  */  
   TargetCurrDspID:string,
      /**  Describes Source/Target ratio  */  
   ScaleDescr:string,
   CurrRateActual:number,
      /**  RuleCode Description  */  
   RuleCodeDesc:string,
   BitFlag:number,
   RateGrpCodeDescription:string,
   RuleCodeRuleCode:number,
   RuleCodeFixedRate:boolean,
   RuleCodeDisplayMode:number,
   SourceCurrCurrName:string,
   SourceCurrCurrDesc:string,
   SourceCurrCurrencyID:string,
   SourceCurrDocumentDesc:string,
   SourceCurrCurrSymbol:string,
   SourceCurrMaintRate:boolean,
   TargetCurrDocumentDesc:string,
   TargetCurrCurrSymbol:string,
   TargetCurrCurrencyID:string,
   TargetCurrCurrDesc:string,
   TargetCurrCurrName:string,
   TargetCurrMaintRate:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_CurrExRateTableset{
   CurrExRate:Erp_Tablesets_CurrExRateRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtCurrExRateTableset{
   CurrExRate:Erp_Tablesets_CurrExRateRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param rateGrpCode
      @param sourceCurrCode
      @param targetCurrCode
      @param effectiveDate
   */  
export interface GetByID_input{
   rateGrpCode:string,
   sourceCurrCode:string,
   targetCurrCode:string,
   effectiveDate:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_CurrExRateTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_CurrExRateTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_CurrExRateTableset[],
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
   returnObj:Erp_Tablesets_CurrExRateListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param rateGrpCode
      @param sourceCurrCode
      @param targetCurrCode
   */  
export interface GetNewCurrExRate_input{
   ds:Erp_Tablesets_CurrExRateTableset[],
   rateGrpCode:string,
   sourceCurrCode:string,
   targetCurrCode:string,
}

export interface GetNewCurrExRate_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrExRateTableset[],
}
}

   /** Required : 
      @param whereClauseCurrExRate
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseCurrExRate:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_CurrExRateTableset[],
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
   ds:Erp_Tablesets_UpdExtCurrExRateTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtCurrExRateTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_CurrExRateTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_CurrExRateTableset[],
}
}

