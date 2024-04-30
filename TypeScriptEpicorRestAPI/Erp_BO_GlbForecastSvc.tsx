import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.GlbForecastSvc
// Description: Global Forecasts are the transport in the inter-company PO-SO mechanism.
In a nutshell, from the purchasing company's PO Suggestions the user can "Send Forecasts"
to the producing company;  this creates GlbForecast records in the producing company.  These
GlbForecast records can be reviewed, modified and deleted or "accepted" (turning the
GlbForecast records into Forecast records).
This BO supports these activities.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get GlbForecasts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GlbForecasts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbForecastRow
   */  
export function get_GlbForecasts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbForecastRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GlbForecasts", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbForecastRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GlbForecasts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GlbForecastRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GlbForecastRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GlbForecasts(requestBody:Erp_Tablesets_GlbForecastRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GlbForecasts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the GlbForecast item
   Description: Calls GetByID to retrieve the GlbForecast item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GlbForecast
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ForeDate Desc: ForeDate   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GlbForecastRow
   */  
export function get_GlbForecasts_Company_PartNum_Plant_ForeDate_CustNum(Company:string, PartNum:string, Plant:string, ForeDate:string, CustNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GlbForecastRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GlbForecasts(" + Company + "," + PartNum + "," + Plant + "," + ForeDate + "," + CustNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_GlbForecastRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GlbForecast for the service
   Description: Calls UpdateExt to update GlbForecast. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GlbForecast
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ForeDate Desc: ForeDate   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GlbForecastRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GlbForecasts_Company_PartNum_Plant_ForeDate_CustNum(Company:string, PartNum:string, Plant:string, ForeDate:string, CustNum:string, requestBody:Erp_Tablesets_GlbForecastRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GlbForecasts(" + Company + "," + PartNum + "," + Plant + "," + ForeDate + "," + CustNum + ")", {
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
   Summary: Call UpdateExt to delete GlbForecast item
   Description: Call UpdateExt to delete GlbForecast item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GlbForecast
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param ForeDate Desc: ForeDate   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GlbForecasts_Company_PartNum_Plant_ForeDate_CustNum(Company:string, PartNum:string, Plant:string, ForeDate:string, CustNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GlbForecasts(" + Company + "," + PartNum + "," + Plant + "," + ForeDate + "," + CustNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GlbForecastListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbForecastListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbForecastListRow)
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
export function get_GetRows(whereClauseGlbForecast:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGlbForecast!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGlbForecast=" + whereClauseGlbForecast
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Required: True   Allow empty value : True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(partNum:string, plant:string, foreDate:string, custNum:string, epicorHeaders?:Headers){
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
   if(typeof plant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plant=" + plant
   }
   if(typeof foreDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "foreDate=" + foreDate
   }
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method AcceptGlbForecasts
   Description: This method conditionally adds/overwrites Forecast records by copying the data out of
GlbForecast records.
Similar to the ImportForecasts routine, which takes in a dataset derived from a spreadsheet file.
   OperationID: AcceptGlbForecasts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AcceptGlbForecasts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AcceptGlbForecasts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AcceptGlbForecasts(requestBody:AcceptGlbForecasts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AcceptGlbForecasts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/AcceptGlbForecasts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as AcceptGlbForecasts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ClearGlbForecasts
   Description: This method deletes all GlbForecast records for the Current Plant, or all Plants, on or after the given date.
   OperationID: ClearGlbForecasts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ClearGlbForecasts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ClearGlbForecasts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ClearGlbForecasts(requestBody:ClearGlbForecasts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ClearGlbForecasts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/ClearGlbForecasts", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ClearGlbForecasts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsConfigurable
   Description: Returns `true` If any revision, or any revision of any child part in BOM, is/was configurable.
   OperationID: IsConfigurable
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsConfigurable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsConfigurable_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsConfigurable(requestBody:IsConfigurable_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsConfigurable_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/IsConfigurable", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as IsConfigurable_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGlbForecast
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGlbForecast
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGlbForecast_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGlbForecast_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGlbForecast(requestBody:GetNewGlbForecast_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGlbForecast_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GetNewGlbForecast", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewGlbForecast_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GlbForecastSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbForecastListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbForecastListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GlbForecastRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GlbForecastRow,
}

export interface Erp_Tablesets_GlbForecastListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   "CustNum":number,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Site id for this forecast  */  
   "Plant":string,
      /**  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  */  
   "ForeDate":string,
   "Inactive":boolean,
   "ForeQty":number,
      /**  The current accumulated quantity from all the order releases that fall within the forecast horizon.  */  
   "ConsumedQty":number,
      /**  Inbound Customer PO Number  */  
   "PONum":string,
      /**  The user ID that created this batch.  */  
   "CreatedBy":string,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Date the forecast was created  */  
   "CreatedDate":string,
   "TransDate":string,
   "AutoTransfer":boolean,
   "TransTime":number,
      /**  Date the forecast was transfered to the local forecast table  */  
   "UpdateDate":string,
   "DemandContract":string,
   "DemandReference":string,
   "DemandContractNum":number,
   "DemandHeadSeq":number,
   "ScheduleNumber":string,
   "EndDate":string,
   "ShipToNum":string,
   "ForeQtyUOM":string,
   "KitFlag":string,
   "ParentPartNum":string,
   "EDIUpdateDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "ReadyFlag":boolean,
   "InvalidData":boolean,
   "ErrorMsg":string,
      /**  A user defined external customer ID.  This must be unique within the file.  */  
   "CustId":string,
      /**  PartDescription from the Part table.  */  
   "PartPartDescription":string,
      /**  MinimumQty from the PartPlant table  */  
   "PartPlantMinimumQty":number,
      /**  MaximumQty from the PartPlant table.  */  
   "PartPlantMaximumQty":number,
      /**  SafetyQty from the PartPlant table.  */  
   "PartPlantSafetyQty":number,
      /**  MinOrderQty from the PartPlant table.  */  
   "PartPlantMinOrderQty":number,
      /**  OnHandQty from the PartPlant table.  */  
   "PartPlantOnHandQty":number,
      /**  LeadTime from the PartPlant table.  */  
   "PartPlantLeadTime":number,
      /**  Name field from the Customer table.  */  
   "CustomerName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GlbForecastRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   "CustNum":number,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   "PartNum":string,
      /**  Site id for this forecast  */  
   "Plant":string,
      /**  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  */  
   "ForeDate":string,
   "Inactive":boolean,
   "ForeQty":number,
      /**  The current accumulated quantity from all the order releases that fall within the forecast horizon.  */  
   "ConsumedQty":number,
      /**  Inbound Customer PO Number  */  
   "PONum":string,
      /**  The user ID that created this batch.  */  
   "CreatedBy":string,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Date the forecast was created  */  
   "CreatedDate":string,
   "TransDate":string,
   "AutoTransfer":boolean,
   "TransTime":number,
      /**  Date the forecast was transfered to the local forecast table  */  
   "UpdateDate":string,
   "DemandContract":string,
   "DemandReference":string,
   "DemandContractNum":number,
   "DemandHeadSeq":number,
   "ScheduleNumber":string,
   "EndDate":string,
   "ShipToNum":string,
   "ForeQtyUOM":string,
   "KitFlag":string,
   "ParentPartNum":string,
   "EDIUpdateDate":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  RevisionNum  */  
   "RevisionNum":string,
      /**  A user defined external customer ID.  This must be unique within the file.  */  
   "CustId":string,
      /**  Name field from the Customer table.  */  
   "CustomerName":string,
   "ErrorMsg":string,
   "InvalidData":boolean,
      /**  PartDescription from the Part table.  */  
   "PartPartDescription":string,
      /**  LeadTime from the PartPlant table.  */  
   "PartPlantLeadTime":number,
      /**  MaximumQty from the PartPlant table.  */  
   "PartPlantMaximumQty":number,
      /**  MinimumQty from the PartPlant table  */  
   "PartPlantMinimumQty":number,
      /**  MinOrderQty from the PartPlant table.  */  
   "PartPlantMinOrderQty":number,
      /**  OnHandQty from the PartPlant table.  */  
   "PartPlantOnHandQty":number,
      /**  SafetyQty from the PartPlant table.  */  
   "PartPlantSafetyQty":number,
   "ReadyFlag":boolean,
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
      @param pcImportOptions
      @param plAllPlants
      @param pdFromDate
   */  
export interface AcceptGlbForecasts_input{
   ds:Erp_Tablesets_GlbForecastTableset[],
      /**  Valid choices are "A"=Add+Replace, "C"=Clear+Reload, "N"=New.  */  
   pcImportOptions:string,
      /**  If TRUE, clear all plants; if FALSE, clear Current Plant.  */  
   plAllPlants:boolean,
      /**  Only records on or after the given date will be considered for import.  */  
   pdFromDate:string,
}

export interface AcceptGlbForecasts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbForecastTableset,
}
}

   /** Required : 
      @param plAllPlants
      @param pdFromDate
   */  
export interface ClearGlbForecasts_input{
      /**  If TRUE, clear all plants; if FALSE, clear Current Plant.  */  
   plAllPlants:boolean,
      /**  Only GlbForecast records on or after the given date will be deleted.  */  
   pdFromDate:string,
}

export interface ClearGlbForecasts_output{
}

   /** Required : 
      @param partNum
      @param plant
      @param foreDate
      @param custNum
   */  
export interface DeleteByID_input{
   partNum:string,
   plant:string,
   foreDate:string,
   custNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GlbForecastListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   CustNum:number,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Site id for this forecast  */  
   Plant:string,
      /**  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  */  
   ForeDate:string,
   Inactive:boolean,
   ForeQty:number,
      /**  The current accumulated quantity from all the order releases that fall within the forecast horizon.  */  
   ConsumedQty:number,
      /**  Inbound Customer PO Number  */  
   PONum:string,
      /**  The user ID that created this batch.  */  
   CreatedBy:string,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Date the forecast was created  */  
   CreatedDate:string,
   TransDate:string,
   AutoTransfer:boolean,
   TransTime:number,
      /**  Date the forecast was transfered to the local forecast table  */  
   UpdateDate:string,
   DemandContract:string,
   DemandReference:string,
   DemandContractNum:number,
   DemandHeadSeq:number,
   ScheduleNumber:string,
   EndDate:string,
   ShipToNum:string,
   ForeQtyUOM:string,
   KitFlag:string,
   ParentPartNum:string,
   EDIUpdateDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   ReadyFlag:boolean,
   InvalidData:boolean,
   ErrorMsg:string,
      /**  A user defined external customer ID.  This must be unique within the file.  */  
   CustId:string,
      /**  PartDescription from the Part table.  */  
   PartPartDescription:string,
      /**  MinimumQty from the PartPlant table  */  
   PartPlantMinimumQty:number,
      /**  MaximumQty from the PartPlant table.  */  
   PartPlantMaximumQty:number,
      /**  SafetyQty from the PartPlant table.  */  
   PartPlantSafetyQty:number,
      /**  MinOrderQty from the PartPlant table.  */  
   PartPlantMinOrderQty:number,
      /**  OnHandQty from the PartPlant table.  */  
   PartPlantOnHandQty:number,
      /**  LeadTime from the PartPlant table.  */  
   PartPlantLeadTime:number,
      /**  Name field from the Customer table.  */  
   CustomerName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbForecastListTableset{
   GlbForecastList:Erp_Tablesets_GlbForecastListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GlbForecastRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program. This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never need to know about the value of this field.  */  
   CustNum:number,
      /**  The PartNum field identifies the Part and is used as the primary key.  */  
   PartNum:string,
      /**  Site id for this forecast  */  
   Plant:string,
      /**  Date at which this forecast is considered effective.  This date is used to control the building of inventory based on this forecast.  */  
   ForeDate:string,
   Inactive:boolean,
   ForeQty:number,
      /**  The current accumulated quantity from all the order releases that fall within the forecast horizon.  */  
   ConsumedQty:number,
      /**  Inbound Customer PO Number  */  
   PONum:string,
      /**  The user ID that created this batch.  */  
   CreatedBy:string,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Date the forecast was created  */  
   CreatedDate:string,
   TransDate:string,
   AutoTransfer:boolean,
   TransTime:number,
      /**  Date the forecast was transfered to the local forecast table  */  
   UpdateDate:string,
   DemandContract:string,
   DemandReference:string,
   DemandContractNum:number,
   DemandHeadSeq:number,
   ScheduleNumber:string,
   EndDate:string,
   ShipToNum:string,
   ForeQtyUOM:string,
   KitFlag:string,
   ParentPartNum:string,
   EDIUpdateDate:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  RevisionNum  */  
   RevisionNum:string,
      /**  A user defined external customer ID.  This must be unique within the file.  */  
   CustId:string,
      /**  Name field from the Customer table.  */  
   CustomerName:string,
   ErrorMsg:string,
   InvalidData:boolean,
      /**  PartDescription from the Part table.  */  
   PartPartDescription:string,
      /**  LeadTime from the PartPlant table.  */  
   PartPlantLeadTime:number,
      /**  MaximumQty from the PartPlant table.  */  
   PartPlantMaximumQty:number,
      /**  MinimumQty from the PartPlant table  */  
   PartPlantMinimumQty:number,
      /**  MinOrderQty from the PartPlant table.  */  
   PartPlantMinOrderQty:number,
      /**  OnHandQty from the PartPlant table.  */  
   PartPlantOnHandQty:number,
      /**  SafetyQty from the PartPlant table.  */  
   PartPlantSafetyQty:number,
   ReadyFlag:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GlbForecastTableset{
   GlbForecast:Erp_Tablesets_GlbForecastRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGlbForecastTableset{
   GlbForecast:Erp_Tablesets_GlbForecastRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param partNum
      @param plant
      @param foreDate
      @param custNum
   */  
export interface GetByID_input{
   partNum:string,
   plant:string,
   foreDate:string,
   custNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GlbForecastTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GlbForecastTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GlbForecastTableset[],
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
   returnObj:Erp_Tablesets_GlbForecastListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param plant
      @param foreDate
   */  
export interface GetNewGlbForecast_input{
   ds:Erp_Tablesets_GlbForecastTableset[],
   partNum:string,
   plant:string,
   foreDate:string,
}

export interface GetNewGlbForecast_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbForecastTableset,
}
}

   /** Required : 
      @param whereClauseGlbForecast
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGlbForecast:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GlbForecastTableset[],
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
      @param pcPartNum
   */  
export interface IsConfigurable_input{
   pcPartNum:string,
}

export interface IsConfigurable_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtGlbForecastTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGlbForecastTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GlbForecastTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GlbForecastTableset,
}
}

