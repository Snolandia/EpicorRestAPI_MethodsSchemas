import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.LangTranSvc
// Description: LangTran service.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get LangTrans items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LangTrans
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.LangTranRow
   */  
export function get_LangTrans(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LangTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/LangTrans", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LangTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LangTrans
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.LangTranRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.LangTranRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LangTrans(requestBody:Ice_Tablesets_LangTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/LangTrans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the LangTran item
   Description: Calls GetByID to retrieve the LangTran item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LangTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LangNameID Desc: LangNameID   Required: True   Allow empty value : True
      @param OrgTextID Desc: OrgTextID   Required: True
      @param ProgramID Desc: ProgramID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.LangTranRow
   */  
export function get_LangTrans_Company_LangNameID_OrgTextID_ProgramID(Company:string, LangNameID:string, OrgTextID:string, ProgramID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_LangTranRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/LangTrans(" + Company + "," + LangNameID + "," + OrgTextID + "," + ProgramID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Ice_Tablesets_LangTranRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LangTran for the service
   Description: Calls UpdateExt to update LangTran. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LangTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LangNameID Desc: LangNameID   Required: True   Allow empty value : True
      @param OrgTextID Desc: OrgTextID   Required: True
      @param ProgramID Desc: ProgramID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.LangTranRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LangTrans_Company_LangNameID_OrgTextID_ProgramID(Company:string, LangNameID:string, OrgTextID:string, ProgramID:string, requestBody:Ice_Tablesets_LangTranRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/LangTrans(" + Company + "," + LangNameID + "," + OrgTextID + "," + ProgramID + ")", {
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
   Summary: Call UpdateExt to delete LangTran item
   Description: Call UpdateExt to delete LangTran item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LangTran
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LangNameID Desc: LangNameID   Required: True   Allow empty value : True
      @param OrgTextID Desc: OrgTextID   Required: True
      @param ProgramID Desc: ProgramID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LangTrans_Company_LangNameID_OrgTextID_ProgramID(Company:string, LangNameID:string, OrgTextID:string, ProgramID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/LangTrans(" + Company + "," + LangNameID + "," + OrgTextID + "," + ProgramID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.LangTranListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LangTranListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LangTranListRow)
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
export function get_GetRows(whereClauseLangTran:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseLangTran!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLangTran=" + whereClauseLangTran
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(company:string, langNameID:string, orgTextID:string, programID:string, epicorHeaders?:Headers){
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
   if(typeof langNameID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "langNameID=" + langNameID
   }
   if(typeof orgTextID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "orgTextID=" + orgTextID
   }
   if(typeof programID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "programID=" + programID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method GetProgTrans
   Description: This method returns a list of program specific translations for a original text and language.
   OperationID: GetProgTrans
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetProgTrans_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetProgTrans_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetProgTrans(requestBody:GetProgTrans_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetProgTrans_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetProgTrans", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetProgTrans_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTransByProgramID
   Description: This method returns a list of translations from a start at program id
   OperationID: GetTransByProgramID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTransByProgramID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransByProgramID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransByProgramID(requestBody:GetTransByProgramID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTransByProgramID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetTransByProgramID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetTransByProgramID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTransByText
   Description: This method returns a list of translations from a start at text.
   OperationID: GetTransByText
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTransByText_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransByText_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransByText(requestBody:GetTransByText_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTransByText_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetTransByText", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetTransByText_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTransByTextID
   Description: This method returns a list of translations from a start at text id
   OperationID: GetTransByTextID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTransByTextID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransByTextID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransByTextID(requestBody:GetTransByTextID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTransByTextID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetTransByTextID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetTransByTextID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTransByTranslation
   Description: This method returns a list of translations from a start at translated text
   OperationID: GetTransByTranslation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTransByTranslation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransByTranslation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransByTranslation(requestBody:GetTransByTranslation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTransByTranslation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetTransByTranslation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetTransByTranslation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateAll
   Description: This method update LangTran table
Not used - obsoleted in 11.1.200.
   OperationID: UpdateAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateAll(requestBody:UpdateAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/UpdateAll", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateAll_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteTranRecords
   Description: Deletes Translation
   OperationID: DeleteTranRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteTranRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteTranRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteTranRecords(requestBody:DeleteTranRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteTranRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/DeleteTranRecords", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteTranRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportXml
   Description: Import translations passed from XML via TranTextTableset.
   OperationID: ImportXml
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportXml_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportXml_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportXml(requestBody:ImportXml_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportXml_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/ImportXml", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportXml_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Translate
   Description: Translate procedure
   OperationID: Translate
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Translate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Translate_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Translate(requestBody:Translate_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Translate_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/Translate", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Translate_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetTranslationForTool
   Description: Get Translations to show in Translation Tool
Works similar to Translate method, but divides Program specific and indenendent translations into 2 columns,
as expected by Translation Tool
   OperationID: GetTranslationForTool
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTranslationForTool_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranslationForTool_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTranslationForTool(requestBody:GetTranslationForTool_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTranslationForTool_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetTranslationForTool", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetTranslationForTool_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAppTranslations
   Description: This methods gets the MetaUI application translations.
   OperationID: Get_GetAppTranslations
      @param programID Desc: The program ID.   Required: True   Allow empty value : True
      @param languageID Desc: language ID.   Required: True   Allow empty value : True
      @param request Desc: MetaFX request (JSON serialized) to get the application strings   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAppTranslations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetAppTranslations(programID:string, languageID:string, request:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof programID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "programID=" + programID
   }
   if(typeof languageID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "languageID=" + languageID
   }
   if(typeof request!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "request=" + request
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAppTranslations_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetAppTranslations" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetAppTranslations_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateTranslations
   Description: This method update translations and also LangOrg, LangXref if necessary
   OperationID: UpdateTranslations
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateTranslations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateTranslations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateTranslations(requestBody:UpdateTranslations_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateTranslations_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/UpdateTranslations", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateTranslations_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteTranslation
   Description: Deletes Translation
   OperationID: DeleteTranslation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteTranslation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteTranslation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteTranslation(requestBody:DeleteTranslation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteTranslation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/DeleteTranslation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteTranslation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateSingleTranslation
   Description: Updates single translation.
   OperationID: UpdateSingleTranslation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateSingleTranslation_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateSingleTranslation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateSingleTranslation(requestBody:UpdateSingleTranslation_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateSingleTranslation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/UpdateSingleTranslation", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateSingleTranslation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteTranslations
   Description: Delete all translations for specified language.
   OperationID: DeleteTranslations
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteTranslations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteTranslations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteTranslations(requestBody:DeleteTranslations_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteTranslations_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/DeleteTranslations", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteTranslations_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteCustomizedTranslations
   Description: Delete all custom translations (ID less than 0) for a specified language.
   OperationID: DeleteCustomizedTranslations
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteCustomizedTranslations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteCustomizedTranslations_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteCustomizedTranslations(requestBody:DeleteCustomizedTranslations_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteCustomizedTranslations_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/DeleteCustomizedTranslations", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteCustomizedTranslations_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RemoveOrphans
   Description: Remove Orphan records
   OperationID: RemoveOrphans
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveOrphans_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RemoveOrphans(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RemoveOrphans_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/RemoveOrphans", {
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
         resolve(data as RemoveOrphans_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteRecordsNotInList
   Description: Delete Language records whose ID is not in the list passed.
   OperationID: DeleteRecordsNotInList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteRecordsNotInList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteRecordsNotInList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteRecordsNotInList(requestBody:DeleteRecordsNotInList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteRecordsNotInList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/DeleteRecordsNotInList", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as DeleteRecordsNotInList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportTranslationData
   Description: Import translation data
   OperationID: ImportTranslationData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportTranslationData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportTranslationData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportTranslationData(requestBody:ImportTranslationData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportTranslationData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/ImportTranslationData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ImportTranslationData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportTranslationData
   Description: Export translation data
   OperationID: ExportTranslationData
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportTranslationData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportTranslationData_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportTranslationData(requestBody:ExportTranslationData_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportTranslationData_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/ExportTranslationData", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExportTranslationData_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportToFile
   Description: Export translation data to file
   OperationID: ExportToFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportToFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportToFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportToFile(requestBody:ExportToFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportToFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/ExportToFile", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ExportToFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetLicensedModules
   Description: Gets the list of licensed (installed and enabled) modules.
   OperationID: GetLicensedModules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLicensedModules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetLicensedModules(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetLicensedModules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetLicensedModules", {
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
         resolve(data as GetLicensedModules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLangTran
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLangTran
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLangTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLangTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLangTran(requestBody:GetNewLangTran_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLangTran_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetNewLangTran", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewLangTran_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.LangTranSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LangTranListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_LangTranListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_LangTranRow{
   "odatametadata":string,
   "value":Ice_Tablesets_LangTranRow,
}

export interface Ice_Tablesets_LangTranListRow{
      /**  Language ID  */  
   "LangNameID":string,
      /**  Original Text ID  */  
   "OrgTextID":number,
      /**  Program ID  */  
   "ProgramID":string,
      /**  Translated text.  */  
   "TransText":string,
      /**  Custom Translation  */  
   "CustomTrans":boolean,
      /**  The first 50 characters from TransText  */  
   "SortTransText":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicating if an error occured during update  */  
   "HasError":boolean,
      /**  Error returned by update  */  
   "ErrMessage":string,
      /**  Language Name Description  */  
   "LangNameIDDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_LangTranRow{
      /**  Company  */  
   "Company":string,
      /**  Language ID  */  
   "LangNameID":string,
      /**  Original Text ID  */  
   "OrgTextID":number,
      /**  Program ID  */  
   "ProgramID":string,
      /**  Translated text.  */  
   "TransText":string,
      /**  Custom Translation  */  
   "CustomTrans":boolean,
      /**  The first 50 characters from TransText  */  
   "SortTransText":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  OrigOrgTextID  */  
   "OrigOrgTextID":number,
      /**  NomenclatureID  */  
   "NomenclatureID":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Error returned by update  */  
   "ErrMessage":string,
      /**  Indicating if an error occured during update  */  
   "HasError":boolean,
   "LangNameIDDescription":string,
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
      @param company
      @param langNameID
      @param orgTextID
      @param programID
   */  
export interface DeleteByID_input{
   company:string,
   langNameID:string,
   orgTextID:number,
   programID:string,
}

export interface DeleteByID_output{
}

   /** Required : 
      @param companyID
      @param languageID
   */  
export interface DeleteCustomizedTranslations_input{
      /**  Company ID  */  
   companyID:string,
      /**  Language ID  */  
   languageID:string,
}

export interface DeleteCustomizedTranslations_output{
}

   /** Required : 
      @param companyID
      @param listOrgTextID
   */  
export interface DeleteRecordsNotInList_input{
      /**  Company ID.  */  
   companyID:string,
      /**  List Of IDs.  */  
   listOrgTextID:number,
}

export interface DeleteRecordsNotInList_output{
}

   /** Required : 
      @param companyID
      @param pcLanguageID
      @param pcProgramID
      @param pcOrgTextID
   */  
export interface DeleteTranRecords_input{
      /**  The company ID  */  
   companyID:string,
      /**  The language ID  */  
   pcLanguageID:string,
      /**  The program ID  */  
   pcProgramID:string,
      /**  ID  */  
   pcOrgTextID:number,
}

export interface DeleteTranRecords_output{
parameters : {
      /**  output parameters  */  
   bSucceed:boolean,
}
}

   /** Required : 
      @param company
      @param pcLanguageID
      @param pcProgramID
      @param pcText
   */  
export interface DeleteTranslation_input{
      /**  The company ID.  */  
   company:string,
      /**  The language ID  */  
   pcLanguageID:string,
      /**  The program ID  */  
   pcProgramID:string,
      /**  Text  */  
   pcText:string,
}

export interface DeleteTranslation_output{
parameters : {
      /**  output parameters  */  
   bSucceed:boolean,
}
}

   /** Required : 
      @param companyID
      @param languageID
   */  
export interface DeleteTranslations_input{
      /**  Company ID  */  
   companyID:string,
      /**  Language ID  */  
   languageID:string,
}

export interface DeleteTranslations_output{
}

   /** Required : 
      @param ds
   */  
export interface ExportToFile_input{
   ds:Ice_Tablesets_TranslationDataTableset[],
}

export interface ExportToFile_output{
   returnObj:Ice_Tablesets_TranslationDataTableset[],
}

   /** Required : 
      @param companyID
      @param languageID
      @param withReferences
      @param onlyCustomization
      @param onlyTranslated
      @param onlyUntranslated
      @param fromOrgTextID
      @param toOrgTextID
   */  
export interface ExportTranslationData_input{
      /**  Company ID  */  
   companyID:string,
      /**  Language ID  */  
   languageID:string,
      /**  Export ProgramID references  */  
   withReferences:boolean,
      /**  Only customized  */  
   onlyCustomization:boolean,
      /**  Only translated  */  
   onlyTranslated:boolean,
      /**  Only untranslated  */  
   onlyUntranslated:boolean,
      /**  From ID  */  
   fromOrgTextID:number,
      /**  To ID  */  
   toOrgTextID:number,
}

export interface ExportTranslationData_output{
   returnObj:Ice_Tablesets_TranslationDataTableset[],
}

   /** Required : 
      @param programID
      @param languageID
      @param request
   */  
export interface GetAppTranslations_input{
      /**  The program ID.  */  
   programID:string,
      /**  language ID.  */  
   languageID:string,
      /**  MetaFX request (JSON serialized) to get the application strings  */  
   request:string,
}

export interface GetAppTranslations_output{
   returnObj:Ice_Tablesets_TranTextTableset[],
}

   /** Required : 
      @param company
      @param langNameID
      @param orgTextID
      @param programID
   */  
export interface GetByID_input{
   company:string,
   langNameID:string,
   orgTextID:number,
   programID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_LangTranTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_LangTranTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_LangTranTableset[],
}

export interface GetLicensedModules_output{
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
   returnObj:Ice_Tablesets_LangTranListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param company
      @param langNameID
      @param orgTextID
   */  
export interface GetNewLangTran_input{
   ds:Ice_Tablesets_LangTranTableset[],
   company:string,
   langNameID:string,
   orgTextID:number,
}

export interface GetNewLangTran_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_LangTranTableset,
}
}

   /** Required : 
      @param companyID
      @param pcLanguageID
      @param piOrigTextID
   */  
export interface GetProgTrans_input{
      /**  The company ID.  */  
   companyID:string,
      /**  The language ID.  */  
   pcLanguageID:string,
      /**  The original text ID.  */  
   piOrigTextID:number,
}

export interface GetProgTrans_output{
   returnObj:Ice_Tablesets_TranTextTableset[],
}

   /** Required : 
      @param whereClauseLangTran
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseLangTran:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_LangTranTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param pcLangID
      @param pcProgID
   */  
export interface GetTransByProgramID_input{
      /**  The language ID  */  
   pcLangID:string,
      /**  The start at program ID  */  
   pcProgID:string,
}

export interface GetTransByProgramID_output{
   returnObj:Ice_Tablesets_TranTextTableset[],
}

   /** Required : 
      @param pcLangID
      @param piTextID
   */  
export interface GetTransByTextID_input{
      /**  The language ID  */  
   pcLangID:string,
      /**  The start at text ID  */  
   piTextID:number,
}

export interface GetTransByTextID_output{
   returnObj:Ice_Tablesets_TranTextTableset[],
}

   /** Required : 
      @param companyID
      @param pcLangID
      @param pcText
   */  
export interface GetTransByText_input{
      /**  The company ID.  */  
   companyID:string,
      /**  The language ID.  */  
   pcLangID:string,
      /**  The start at text.  */  
   pcText:string,
}

export interface GetTransByText_output{
   returnObj:Ice_Tablesets_TranTextTableset[],
}

   /** Required : 
      @param pcLangID
      @param pcTranslation
   */  
export interface GetTransByTranslation_input{
      /**  The language ID  */  
   pcLangID:string,
      /**  The start at translated text  */  
   pcTranslation:string,
}

export interface GetTransByTranslation_output{
   returnObj:Ice_Tablesets_TranTextTableset[],
}

   /** Required : 
      @param ds
      @param bAddIfMissing
   */  
export interface GetTranslationForTool_input{
   ds:Ice_Tablesets_TranTextTableset[],
      /**  If True and record is missing in LangOrg, it will be added  */  
   bAddIfMissing:boolean,
}

export interface GetTranslationForTool_output{
   returnObj:Ice_Tablesets_TranTextTableset[],
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

export interface Ice_Tablesets_LangTranExportOptionsRow{
      /**  Range start.  */  
   Start:number,
      /**  Range end.  */  
   End:number,
      /**  If export should include ProgramID references.  */  
   IncludeReferences:boolean,
      /**  If the export should only included translated text entries.  */  
   OnlyTranslated:boolean,
      /**  If the export should include only untranslated text entries.  */  
   OnlyUntranslated:boolean,
      /**  If the export should only contain user-defined translation text entries.  */  
   OnlyCustomization:boolean,
      /**  Company.  */  
   Company:string,
      /**  Language Name ID.  */  
   LangNameID:string,
      /**  Export server filename.  */  
   ServerFileName:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_LangTranListRow{
      /**  Language ID  */  
   LangNameID:string,
      /**  Original Text ID  */  
   OrgTextID:number,
      /**  Program ID  */  
   ProgramID:string,
      /**  Translated text.  */  
   TransText:string,
      /**  Custom Translation  */  
   CustomTrans:boolean,
      /**  The first 50 characters from TransText  */  
   SortTransText:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicating if an error occured during update  */  
   HasError:boolean,
      /**  Error returned by update  */  
   ErrMessage:string,
      /**  Language Name Description  */  
   LangNameIDDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_LangTranListTableset{
   LangTranList:Ice_Tablesets_LangTranListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_LangTranRow{
      /**  Company  */  
   Company:string,
      /**  Language ID  */  
   LangNameID:string,
      /**  Original Text ID  */  
   OrgTextID:number,
      /**  Program ID  */  
   ProgramID:string,
      /**  Translated text.  */  
   TransText:string,
      /**  Custom Translation  */  
   CustomTrans:boolean,
      /**  The first 50 characters from TransText  */  
   SortTransText:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  OrigOrgTextID  */  
   OrigOrgTextID:number,
      /**  NomenclatureID  */  
   NomenclatureID:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Error returned by update  */  
   ErrMessage:string,
      /**  Indicating if an error occured during update  */  
   HasError:boolean,
   LangNameIDDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_LangTranTableset{
   LangTran:Ice_Tablesets_LangTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_TranDataHeaderRow{
   LanguageID:string,
   Description:string,
   FileVersion:string,
   TranDate:string,
   Company:string,
      /**  Company visibility. Either 0 if the record is database-wide or 10 if it is company-specific.  */  
   CompanyVisibility:number,
      /**  If the translation texts are system (Epicor) data.  */  
   SystemFlag:boolean,
      /**  UID of the license module that the translation data uses,  */  
   NomenclatureID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_TranDataRow{
   OrgTextID:number,
   OriginalText:string,
   TranslatedText:string,
   ProgramID:string,
   ErrorCode:number,
   ProgramSpecific:boolean,
   Company:string,
   SystemFlag:boolean,
      /**  Original OrgTextID.  */  
   OrigOrgTextID:number,
      /**  Nomenclature ID.  */  
   NomenclatureID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_TranTextLayerRow{
      /**  Company  */  
   Company:string,
   ErrorCode:number,
   LanguageID:string,
      /**  Nomenclature ID, i.e. the UID of the module used for this translation text.  */  
   NomenclatureID:string,
   OrgTextID:number,
   OriginalText:string,
      /**  If a customization is applied to the texts, this contains the OrgTextID of the original translation.  */  
   OrigOrgTextID:number,
   ProgramID:string,
   ProgTranText:string,
   SystemFlag:boolean,
   TranslatedText:string,
      /**  Layer, either Base or Customization.  */  
   Layer:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_TranTextRow{
   LanguageID:string,
   ProgramID:string,
   OriginalText:string,
   TranslatedText:string,
   ProgTranText:string,
   OrgTextID:number,
   ErrorCode:number,
   Company:string,
   SystemFlag:boolean,
      /**  Nomenclature ID, i.e. the UID of the module used for this translation text.  */  
   NomenclatureID:string,
      /**  If a customization is applied to the texts, this contains the OrgTextID of the original translation.  */  
   OrigOrgTextID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_TranTextTableset{
   TranText:Ice_Tablesets_TranTextRow[],
   TranTextLayer:Ice_Tablesets_TranTextLayerRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_TranslationDataTableset{
   TranData:Ice_Tablesets_TranDataRow[],
   LangTranExportOptions:Ice_Tablesets_LangTranExportOptionsRow[],
   TranDataHeader:Ice_Tablesets_TranDataHeaderRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_UpdExtLangTranTableset{
   LangTran:Ice_Tablesets_LangTranRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param overwriteTranslations
   */  
export interface ImportTranslationData_input{
   ds:Ice_Tablesets_TranslationDataTableset[],
      /**  Overwrite Translation  */  
   overwriteTranslations:boolean,
}

export interface ImportTranslationData_output{
   returnObj:Ice_Tablesets_TranslationDataTableset[],
}

   /** Required : 
      @param ds
      @param bCustomization
   */  
export interface ImportXml_input{
   ds:Ice_Tablesets_TranTextTableset[],
      /**  If true and record is missing in LangOrg, it will be added.  */  
   bCustomization:boolean,
}

export interface ImportXml_output{
   returnObj:Ice_Tablesets_TranTextTableset[],
}

export interface RemoveOrphans_output{
}

   /** Required : 
      @param ds
      @param bAddIfMissing
      @param bFindSimilar
   */  
export interface Translate_input{
   ds:Ice_Tablesets_TranTextTableset[],
      /**  If True and record is missing in LangOrg, it will be added  */  
   bAddIfMissing:boolean,
      /**  If True search for similar record when exact unmatched  */  
   bFindSimilar:boolean,
}

export interface Translate_output{
   returnObj:Ice_Tablesets_TranTextTableset[],
}

   /** Required : 
      @param ds
   */  
export interface UpdateAll_input{
   ds:Ice_Tablesets_LangTranTableset[],
}

export interface UpdateAll_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_LangTranTableset,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtLangTranTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtLangTranTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param company
      @param pcLanguage
      @param pcProgram
      @param pcText
      @param pcTranslation
      @param pcProgTranslation
      @param nomenclatureId
      @param system
   */  
export interface UpdateSingleTranslation_input{
      /**  Company  */  
   company:string,
      /**  Language  */  
   pcLanguage:string,
      /**  Program  */  
   pcProgram:string,
      /**  Text  */  
   pcText:string,
      /**  Translation  */  
   pcTranslation:string,
      /**  Program-specific translation  */  
   pcProgTranslation:string,
      /**  Nomenclature ID (null if not set).  */  
   nomenclatureId:string,
      /**  If system (if there is no Productization enabled, it will be set to false)  */  
   system:boolean,
}

export interface UpdateSingleTranslation_output{
parameters : {
      /**  output parameters  */  
   success:boolean,
}
}

   /** Required : 
      @param ds
      @param pbUpdateLangOrg
   */  
export interface UpdateTranslations_input{
   ds:Ice_Tablesets_TranTextTableset[],
      /**  Flag indicating if a LangOrg should be created if not exists  */  
   pbUpdateLangOrg:boolean,
}

export interface UpdateTranslations_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_TranTextTableset,
   bReturn:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_LangTranTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_LangTranTableset,
}
}

