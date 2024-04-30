import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.GLJrnGrpSvc
// Description: Business Object for selected, updating, and posting a G/L Journal Group
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get GLJrnGrps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_GLJrnGrps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnGrpRow
   */  
export function get_GLJrnGrps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GLJrnGrps", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_GLJrnGrps
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.GLJrnGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.GLJrnGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GLJrnGrps(requestBody:Erp_Tablesets_GLJrnGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GLJrnGrps", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the GLJrnGrp item
   Description: Calls GetByID to retrieve the GLJrnGrp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_GLJrnGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.GLJrnGrpRow
   */  
export function get_GLJrnGrps_Company_GroupID(Company:string, GroupID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_GLJrnGrpRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GLJrnGrps(" + Company + "," + GroupID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_GLJrnGrpRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update GLJrnGrp for the service
   Description: Calls UpdateExt to update GLJrnGrp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_GLJrnGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.GLJrnGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_GLJrnGrps_Company_GroupID(Company:string, GroupID:string, requestBody:Erp_Tablesets_GLJrnGrpRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GLJrnGrps(" + Company + "," + GroupID + ")", {
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
   Summary: Call UpdateExt to delete GLJrnGrp item
   Description: Call UpdateExt to delete GLJrnGrp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_GLJrnGrp
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param GroupID Desc: GroupID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_GLJrnGrps_Company_GroupID(Company:string, GroupID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GLJrnGrps(" + Company + "," + GroupID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.GLJrnGrpListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnGrpListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnGrpListRow)
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
export function get_GetRows(whereClauseGLJrnGrp:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseGLJrnGrp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseGLJrnGrp=" + whereClauseGLJrnGrp
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(groupID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof groupID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "groupID=" + groupID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method ChangeBookID
   Description: Method to call when changing the Book.
   OperationID: ChangeBookID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeBookID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBookID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBookID(requestBody:ChangeBookID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeBookID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/ChangeBookID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeBookID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeEntryMode
   Description: Method to call when changing the Entry Mode.
   OperationID: ChangeEntryMode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeEntryMode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEntryMode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEntryMode(requestBody:ChangeEntryMode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeEntryMode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/ChangeEntryMode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeEntryMode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFiscalPeriod
   Description: Method to call when changing the Fiscal Period.
   OperationID: ChangeFiscalPeriod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFiscalPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFiscalPeriod(requestBody:ChangeFiscalPeriod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFiscalPeriod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/ChangeFiscalPeriod", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeFiscalPeriod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFiscalPeriodType
   Description: Method to call when changing the Fiscal Period Type.
   OperationID: ChangeFiscalPeriodType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFiscalPeriodType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalPeriodType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFiscalPeriodType(requestBody:ChangeFiscalPeriodType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFiscalPeriodType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/ChangeFiscalPeriodType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeFiscalPeriodType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFiscalYear
   Description: Method to call when changing the Fiscal Year.
   OperationID: ChangeFiscalYear
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFiscalYear(requestBody:ChangeFiscalYear_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFiscalYear_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/ChangeFiscalYear", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeFiscalYear_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFiscalYearSuffix
   Description: Method to call when changing the Fiscal Year Suffix.
   OperationID: ChangeFiscalYearSuffix
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFiscalYearSuffix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFiscalYearSuffix_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFiscalYearSuffix(requestBody:ChangeFiscalYearSuffix_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFiscalYearSuffix_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/ChangeFiscalYearSuffix", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeFiscalYearSuffix_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRateType
   Description: Method to call when changing the Rate Type.
   OperationID: ChangeRateType
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRateType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRateType_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRateType(requestBody:ChangeRateType_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRateType_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/ChangeRateType", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeRateType_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeJournalCode
   Description: Method to call when changing the Journal Code.
   OperationID: ChangeJournalCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeJournalCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJournalCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJournalCode(requestBody:ChangeJournalCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeJournalCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/ChangeJournalCode", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ChangeJournalCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckFiscalYear
   Description: Method to call before updating the journal group. This method will check the
date that the user entered to verify it is in the current fiscal year and period.
If it is not then opMessage will be assigned with message text.  If it is
then the Fiscal Period and Year will be updated.
   OperationID: CheckFiscalYear
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckFiscalYear_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckFiscalYear_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckFiscalYear(requestBody:CheckFiscalYear_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckFiscalYear_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/CheckFiscalYear", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckFiscalYear_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateActiveUserID
   Description: Check current ActiveUserID and update it, if it is empty.
   OperationID: UpdateActiveUserID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateActiveUserID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateActiveUserID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateActiveUserID(requestBody:UpdateActiveUserID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateActiveUserID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/UpdateActiveUserID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateActiveUserID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckDocumentIsLocked
   Description: Method to call when it is necessary to check if document is lock, before doing smth.
   OperationID: CheckDocumentIsLocked
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckDocumentIsLocked_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckDocumentIsLocked_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckDocumentIsLocked(requestBody:CheckDocumentIsLocked_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckDocumentIsLocked_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/CheckDocumentIsLocked", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckDocumentIsLocked_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckBeforePost
   OperationID: CheckBeforePost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckBeforePost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBeforePost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckBeforePost(requestBody:CheckBeforePost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckBeforePost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/CheckBeforePost", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as CheckBeforePost_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsNeedAsyncronousPosting
   Description: This method returns true if it is better to use asyncronous posting because of performance.
   OperationID: IsNeedAsyncronousPosting
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsNeedAsyncronousPosting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsNeedAsyncronousPosting_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsNeedAsyncronousPosting(requestBody:IsNeedAsyncronousPosting_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsNeedAsyncronousPosting_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/IsNeedAsyncronousPosting", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as IsNeedAsyncronousPosting_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PostGroupJournals
   Description: Method to call when posting journal for a specific group.  Posting of a group
causes the GlJrnGrp to be deleted from the database if all the records in the
group posted correctly.  It will also cause the GlJrnHed record to be deleted
after the specific journal is posted.
   OperationID: PostGroupJournals
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PostGroupJournals_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PostGroupJournals_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PostGroupJournals(requestBody:PostGroupJournals_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PostGroupJournals_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/PostGroupJournals", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as PostGroupJournals_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UnlockGroup
   Description: Method to call to unlock a group record.  This method should be called whenever
the group no longer needs to be locked.  The group no longer needs to be locked
when the journal object is closed, or when a different group is selected.
   OperationID: UnlockGroup
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UnlockGroup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlockGroup_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnlockGroup(requestBody:UnlockGroup_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UnlockGroup_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/UnlockGroup", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UnlockGroup_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsNoLock
   Description: GetRows method with disabled ActiveUser functionality.
   OperationID: GetRowsNoLock
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsNoLock(requestBody:GetRowsNoLock_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsNoLock_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GetRowsNoLock", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsNoLock_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLJrnGrpNoLock
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnGrpNoLock
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnGrpNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnGrpNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnGrpNoLock(requestBody:GetNewGLJrnGrpNoLock_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLJrnGrpNoLock_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GetNewGLJrnGrpNoLock", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewGLJrnGrpNoLock_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetRowsUseLockSetting
   Description: Returns the GLJrnGrp dataset using the automatic group lock configuration setting.
   OperationID: GetRowsUseLockSetting
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRowsUseLockSetting_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsUseLockSetting_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRowsUseLockSetting(requestBody:GetRowsUseLockSetting_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRowsUseLockSetting_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GetRowsUseLockSetting", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetRowsUseLockSetting_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateNoLock
   Description: Update group without locking by ActiveUser
   OperationID: UpdateNoLock
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateNoLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateNoLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateNoLock(requestBody:UpdateNoLock_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateNoLock_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/UpdateNoLock", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateNoLock_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GroupUnlock
   Description: Clears the lock of a group, only if the user of the current session is the same as the one locking the group.
This method update the database and refresh the group dataset with the information from the database.
Returns the dataset with the current lock status of GLJrnGrp.
   OperationID: GroupUnlock
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GroupUnlock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupUnlock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GroupUnlock(requestBody:GroupUnlock_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GroupUnlock_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GroupUnlock", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GroupUnlock_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GroupLock
   Description: Locks the groupID for the current user in session only if the group is not locked already
This method update the database and refresh the group dataset with the information from the database.
Returns the dataset with the current lock status of GLJrnGrp.
   OperationID: GroupLock
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GroupLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GroupLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GroupLock(requestBody:GroupLock_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GroupLock_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GroupLock", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GroupLock_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewGLJrnGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewGLJrnGrp
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewGLJrnGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewGLJrnGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewGLJrnGrp(requestBody:GetNewGLJrnGrp_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewGLJrnGrp_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GetNewGLJrnGrp", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewGLJrnGrp_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.GLJrnGrpSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnGrpListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnGrpListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_GLJrnGrpRow{
   "odatametadata":string,
   "value":Erp_Tablesets_GLJrnGrpRow,
}

export interface Erp_Tablesets_GLJrnGrpListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   "GroupID":string,
      /**  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  */  
   "BookMode":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  The user ID that created this batch.  */  
   "CreatedBy":string,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   "ActiveUserID":string,
      /**   Contains posting error messages. Possible messages are:
"Out of Balance transactions",
 "Invalid Account"  */  
   "PostErrorLog":string,
      /**  Default Journal Date for all entries made in this group. Must be valid in the Fiscal master.  Defaults as Today if Today is within the current G/L fiscal period, else it defaults to the current fiscal periods end date.  This date controls the assigned Fiscal Year/Period.  This can not be changed once GLJrnHed records exist for the group.  */  
   "JEDate":string,
      /**  Fiscal Year to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  */  
   "FiscalYear":number,
      /**  The Fiscal Period to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  */  
   "FiscalPeriod":number,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   "JournalCode":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods  */  
   "FiscalPeriodType":string,
      /**  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  */  
   "CloseFiscalPeriod":number,
      /**  It is true, if all records for this group were posted.  */  
   "Posted":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Display Fiscal Period  */  
   "DspFiscalPeriod":number,
      /**  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  */  
   "HasDetails":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  Indicates the base currency for the book  */  
   "BookIDCurrencyCode":string,
      /**  Descripiton of Book  */  
   "BookIDDescription":string,
      /**  Flag that indicates if correspondence accounting is set-up for the book.  */  
   "BookIDCorrAccounting":boolean,
      /**  Calendar description.  */  
   "FiscalCalDescription":string,
      /**  Journal  Description.  */  
   "JournalCodeJrnlDescription":string,
      /**  Description  */  
   "RateGrpCodeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_GLJrnGrpRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   "GroupID":string,
      /**  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  */  
   "BookMode":string,
      /**  Unique Book Identifier  */  
   "BookID":string,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Unique identifier  */  
   "RateGrpCode":string,
      /**  The user ID that created this batch.  */  
   "CreatedBy":string,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   "ActiveUserID":string,
      /**   Contains posting error messages. Possible messages are:
"Out of Balance transactions",
 "Invalid Account"  */  
   "PostErrorLog":string,
      /**  Default Journal Date for all entries made in this group. Must be valid in the Fiscal master.  Defaults as Today if Today is within the current G/L fiscal period, else it defaults to the current fiscal periods end date.  This date controls the assigned Fiscal Year/Period.  This can not be changed once GLJrnHed records exist for the group.  */  
   "JEDate":string,
      /**  Fiscal Year to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  */  
   "FiscalYear":number,
      /**  The Fiscal Period to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  */  
   "FiscalPeriod":number,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   "JournalCode":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  Chart of Account ID  */  
   "COACode":string,
      /**   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods  */  
   "FiscalPeriodType":string,
      /**  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  */  
   "CloseFiscalPeriod":number,
      /**  It is true, if all records for this group were posted.  */  
   "Posted":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Periods List. The value will be populated in the BO logic containing Ordinary or Closing periods.  */  
   "DspFiscalPeriod":string,
      /**  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  */  
   "HasDetails":boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   "LockStatus":string,
      /**  shows is this invoice is blocked in RvLock.  */  
   "IsLcked":boolean,
      /**  Review Journal UID  */  
   "RvnJrnUID":number,
      /**  Indicates that Book Mode cannot be changed by user  */  
   "BookModeDisabled":boolean,
      /**   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods
S - Opening
Calculated based on the Book Selected.  */  
   "DspFiscalPeriodType":string,
   "BitFlag":number,
   "BookIDCurrencyCode":string,
   "BookIDDescription":string,
   "BookIDCorrAccounting":boolean,
   "FiscalCalDescription":string,
   "JournalCodeAllowStatJournals":boolean,
   "JournalCodeJrnlDescription":string,
   "RateGrpCodeDescription":string,
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
      @param proposeBookID
      @param ds
   */  
export interface ChangeBookID_input{
      /**  The proposed Book ID  */  
   proposeBookID:string,
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface ChangeBookID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
}
}

   /** Required : 
      @param proposedBookMode
      @param ds
   */  
export interface ChangeEntryMode_input{
      /**  The proposed Entry Mode  */  
   proposedBookMode:string,
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface ChangeEntryMode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
}
}

   /** Required : 
      @param proposedPeriodType
      @param ds
   */  
export interface ChangeFiscalPeriodType_input{
      /**  The proposed Fiscal Period Type  */  
   proposedPeriodType:string,
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface ChangeFiscalPeriodType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
   opMessage:string,
}
}

   /** Required : 
      @param proposedFiscalPeriod
      @param ds
   */  
export interface ChangeFiscalPeriod_input{
      /**  The proposed Fiscal Period  */  
   proposedFiscalPeriod:number,
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface ChangeFiscalPeriod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
}
}

   /** Required : 
      @param proposedFiscalYearSuffix
      @param ds
   */  
export interface ChangeFiscalYearSuffix_input{
      /**  The proposed Fiscal Year Suffix  */  
   proposedFiscalYearSuffix:string,
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface ChangeFiscalYearSuffix_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
}
}

   /** Required : 
      @param proposedFiscalYear
      @param ds
   */  
export interface ChangeFiscalYear_input{
      /**  The proposed Fiscal Year  */  
   proposedFiscalYear:number,
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface ChangeFiscalYear_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
}
}

   /** Required : 
      @param proposedJournalCode
      @param ds
   */  
export interface ChangeJournalCode_input{
      /**  The proposed Journal Code  */  
   proposedJournalCode:string,
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface ChangeJournalCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
}
}

   /** Required : 
      @param proposedRateType
      @param ds
   */  
export interface ChangeRateType_input{
      /**  The proposed Rate Type  */  
   proposedRateType:string,
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface ChangeRateType_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
}
}

   /** Required : 
      @param groupID
   */  
export interface CheckBeforePost_input{
      /**  The group id of the group of journals to be posted  */  
   groupID:string,
}

export interface CheckBeforePost_output{
}

   /** Required : 
      @param keyValue
   */  
export interface CheckDocumentIsLocked_input{
      /**  keyValue  */  
   keyValue:string,
}

export interface CheckDocumentIsLocked_output{
}

   /** Required : 
      @param ds
      @param cGroupID
      @param cJEDate
   */  
export interface CheckFiscalYear_input{
   ds:Erp_Tablesets_GLJrnGrpTableset[],
      /**  Group Id field  */  
   cGroupID:string,
      /**  JEDate proposed value  */  
   cJEDate:string,
}

export interface CheckFiscalYear_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
   opMessage:string,
}
}

   /** Required : 
      @param groupID
   */  
export interface DeleteByID_input{
   groupID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_GLJrnGrpListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  */  
   BookMode:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  The user ID that created this batch.  */  
   CreatedBy:string,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   ActiveUserID:string,
      /**   Contains posting error messages. Possible messages are:
"Out of Balance transactions",
 "Invalid Account"  */  
   PostErrorLog:string,
      /**  Default Journal Date for all entries made in this group. Must be valid in the Fiscal master.  Defaults as Today if Today is within the current G/L fiscal period, else it defaults to the current fiscal periods end date.  This date controls the assigned Fiscal Year/Period.  This can not be changed once GLJrnHed records exist for the group.  */  
   JEDate:string,
      /**  Fiscal Year to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  */  
   FiscalYear:number,
      /**  The Fiscal Period to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  */  
   FiscalPeriod:number,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods  */  
   FiscalPeriodType:string,
      /**  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  */  
   CloseFiscalPeriod:number,
      /**  It is true, if all records for this group were posted.  */  
   Posted:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Display Fiscal Period  */  
   DspFiscalPeriod:number,
      /**  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  */  
   HasDetails:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  Indicates the base currency for the book  */  
   BookIDCurrencyCode:string,
      /**  Descripiton of Book  */  
   BookIDDescription:string,
      /**  Flag that indicates if correspondence accounting is set-up for the book.  */  
   BookIDCorrAccounting:boolean,
      /**  Calendar description.  */  
   FiscalCalDescription:string,
      /**  Journal  Description.  */  
   JournalCodeJrnlDescription:string,
      /**  Description  */  
   RateGrpCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnGrpListTableset{
   GLJrnGrpList:Erp_Tablesets_GLJrnGrpListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_GLJrnGrpRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Before allowing invoices to be entered the user establishes a Group ID. All invoices belong to a group until the group is posted. The GroupID is assigned by the user.  The GroupID is used to Selectively print and post the transactions and establishes the invoice date and fiscal period defaults for invoices assigned to the Group.  */  
   GroupID:string,
      /**  Indicates what mode the GL transactions will be entered. Valid values are (S) for Single Book and (M) for Multi-Book.  */  
   BookMode:string,
      /**  Unique Book Identifier  */  
   BookID:string,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**  The user ID that created this batch.  */  
   CreatedBy:string,
      /**  The user ID that is currently logged into this Group. This is displayed on the Group browser so that users may know which Groups are available.  */  
   ActiveUserID:string,
      /**   Contains posting error messages. Possible messages are:
"Out of Balance transactions",
 "Invalid Account"  */  
   PostErrorLog:string,
      /**  Default Journal Date for all entries made in this group. Must be valid in the Fiscal master.  Defaults as Today if Today is within the current G/L fiscal period, else it defaults to the current fiscal periods end date.  This date controls the assigned Fiscal Year/Period.  This can not be changed once GLJrnHed records exist for the group.  */  
   JEDate:string,
      /**  Fiscal Year to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  */  
   FiscalYear:number,
      /**  The Fiscal Period to which all entries in this group will be posted.  This is not directly maintainable.  It is set based on finding the Fiscal master for the GLJrnGrp.JEDate.  */  
   FiscalPeriod:number,
      /**  A code that defines a journal.  A  journal Identifies/groups entries together. See JrnlCode table.  */  
   JournalCode:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  Chart of Account ID  */  
   COACode:string,
      /**   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods  */  
   FiscalPeriodType:string,
      /**  The close fiscal period number in the fiscal year.  A value of 0 indicates a non-closing fiscal period; > 0 indicates a closing period.  */  
   CloseFiscalPeriod:number,
      /**  It is true, if all records for this group were posted.  */  
   Posted:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Periods List. The value will be populated in the BO logic containing Ordinary or Closing periods.  */  
   DspFiscalPeriod:string,
      /**  Indicates if detail records exist for the group.  Certain fields cannot be updated if detail records exist.  */  
   HasDetails:boolean,
      /**  locked means can not be posted: an invoice is already in review journal or in posting process.  */  
   LockStatus:string,
      /**  shows is this invoice is blocked in RvLock.  */  
   IsLcked:boolean,
      /**  Review Journal UID  */  
   RvnJrnUID:number,
      /**  Indicates that Book Mode cannot be changed by user  */  
   BookModeDisabled:boolean,
      /**   Indicates what type of fiscal periods can be selected for the group.  Values are:
O - Ordinary periods
C - Closing periods
S - Opening
Calculated based on the Book Selected.  */  
   DspFiscalPeriodType:string,
   BitFlag:number,
   BookIDCurrencyCode:string,
   BookIDDescription:string,
   BookIDCorrAccounting:boolean,
   FiscalCalDescription:string,
   JournalCodeAllowStatJournals:boolean,
   JournalCodeJrnlDescription:string,
   RateGrpCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_GLJrnGrpTableset{
   GLJrnGrp:Erp_Tablesets_GLJrnGrpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtGLJrnGrpTableset{
   GLJrnGrp:Erp_Tablesets_GLJrnGrpRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param groupID
   */  
export interface GetByID_input{
   groupID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_GLJrnGrpTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_GLJrnGrpTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_GLJrnGrpTableset[],
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
   returnObj:Erp_Tablesets_GLJrnGrpListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewGLJrnGrpNoLock_input{
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface GetNewGLJrnGrpNoLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewGLJrnGrp_input{
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface GetNewGLJrnGrp_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
}
}

   /** Required : 
      @param whereClauseGLJrnGrp
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsNoLock_input{
   whereClauseGLJrnGrp:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRowsNoLock_output{
   returnObj:Erp_Tablesets_GLJrnGrpTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseGLJrnGrp
      @param pageSize
      @param absolutePage
   */  
export interface GetRowsUseLockSetting_input{
      /**  GLJrnGrp where clause  */  
   whereClauseGLJrnGrp:string,
      /**  Page Size  */  
   pageSize:number,
      /**  Absolute Page  */  
   absolutePage:number,
}

export interface GetRowsUseLockSetting_output{
   returnObj:Erp_Tablesets_GLJrnGrpTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClauseGLJrnGrp
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseGLJrnGrp:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_GLJrnGrpTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param groupID
      @param ds
   */  
export interface GroupLock_input{
      /**  Group ID to lock  */  
   groupID:string,
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface GroupLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
}
}

   /** Required : 
      @param groupID
      @param ds
   */  
export interface GroupUnlock_input{
      /**  Group ID.  */  
   groupID:string,
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface GroupUnlock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
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
      @param groupID
      @param maxCountOfLines
   */  
export interface IsNeedAsyncronousPosting_input{
      /**  GroupID  */  
   groupID:string,
      /**  recommended maximum count of lines  */  
   maxCountOfLines:number,
}

export interface IsNeedAsyncronousPosting_output{
   returnObj:boolean,
}

   /** Required : 
      @param postGroupID
   */  
export interface PostGroupJournals_input{
      /**  The group id of the group of journals to be posted  */  
   postGroupID:string,
}

export interface PostGroupJournals_output{
parameters : {
      /**  output parameters  */  
   NotAllPostedMessage:string,
}
}

   /** Required : 
      @param inGroupID
   */  
export interface UnlockGroup_input{
      /**  The group id of the group record to unlock  */  
   inGroupID:string,
}

export interface UnlockGroup_output{
}

   /** Required : 
      @param groupID
   */  
export interface UpdateActiveUserID_input{
      /**  Group ID  */  
   groupID:string,
}

export interface UpdateActiveUserID_output{
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtGLJrnGrpTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtGLJrnGrpTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdateNoLock_input{
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface UpdateNoLock_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_GLJrnGrpTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_GLJrnGrpTableset,
}
}

