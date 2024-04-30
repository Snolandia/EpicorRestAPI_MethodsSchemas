import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.SerialNumMaskingSvc
// Description: Add your summary for this object here
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/$metadata", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Description: Get SerialNumMaskings items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_SerialNumMaskings
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialMaskRow
   */  
export function get_SerialNumMaskings(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialMaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/SerialNumMaskings", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialMaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_SerialNumMaskings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.SerialMaskRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.SerialMaskRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SerialNumMaskings(requestBody:Erp_Tablesets_SerialMaskRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/SerialNumMaskings", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
   Summary: Calls GetByID to retrieve the SerialNumMasking item
   Description: Calls GetByID to retrieve the SerialNumMasking item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_SerialNumMasking
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SerialMaskID Desc: SerialMaskID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.SerialMaskRow
   */  
export function get_SerialNumMaskings_Company_SerialMaskID(Company:string, SerialMaskID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_SerialMaskRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/SerialNumMaskings(" + Company + "," + SerialMaskID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Erp_Tablesets_SerialMaskRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update SerialNumMasking for the service
   Description: Calls UpdateExt to update SerialNumMasking. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_SerialNumMasking
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SerialMaskID Desc: SerialMaskID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.SerialMaskRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_SerialNumMaskings_Company_SerialMaskID(Company:string, SerialMaskID:string, requestBody:Erp_Tablesets_SerialMaskRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/SerialNumMaskings(" + Company + "," + SerialMaskID + ")", {
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
   Summary: Call UpdateExt to delete SerialNumMasking item
   Description: Call UpdateExt to delete SerialNumMasking item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_SerialNumMasking
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SerialMaskID Desc: SerialMaskID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_SerialNumMaskings_Company_SerialMaskID(Company:string, SerialMaskID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/SerialNumMaskings(" + Company + "," + SerialMaskID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.SerialMaskListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialMaskListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialMaskListRow)
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
export function get_GetRows(whereClauseSerialMask:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseSerialMask!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseSerialMask=" + whereClauseSerialMask
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/GetRows" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
export function get_GetByID(serialMaskID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof serialMaskID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "serialMaskID=" + serialMaskID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/GetByID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/GetList" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
   Summary: Invoke method UpdateCharactersUsed
   Description: Returns number of characters used in serial number.
   OperationID: UpdateCharactersUsed
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateCharactersUsed_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCharactersUsed_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateCharactersUsed(requestBody:UpdateCharactersUsed_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateCharactersUsed_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/UpdateCharactersUsed", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as UpdateCharactersUsed_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOfMask
   Description: TO BE CALLED ON CHANGE OF ttSerialMask.Mask
   OperationID: OnChangeOfMask
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOfMask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfMask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOfMask(requestBody:OnChangeOfMask_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOfMask_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/OnChangeOfMask", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeOfMask_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConstructExampleString
   Description: TO BE CALLED ON CHANGE OF ttSerialMask.Mask
   OperationID: ConstructExampleString
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ConstructExampleString_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConstructExampleString_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConstructExampleString(requestBody:ConstructExampleString_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ConstructExampleString_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/ConstructExampleString", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as ConstructExampleString_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeSNLastUsedSeq
   Description: NEEDS TO BE CALLED FOR GENERATE MASK TYPES
   OperationID: OnChangeSNLastUsedSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSNLastUsedSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSNLastUsedSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSNLastUsedSeq(requestBody:OnChangeSNLastUsedSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSNLastUsedSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/OnChangeSNLastUsedSeq", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as OnChangeSNLastUsedSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewSerialMask
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewSerialMask
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewSerialMask_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewSerialMask_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewSerialMask(requestBody:GetNewSerialMask_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewSerialMask_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/GetNewSerialMask", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
      .then((res) => {
         if(res.ok){
             return res.json()
         }
         else{
             return res.json().then(text => {throw new Error(text["ErrorMessage"]) })
         }
      })
      .then((data) => {
         resolve(data as GetNewSerialMask_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/DeleteByID", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/GetBySysRowID" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/GetBySysRowIDs" + params, {
          method: 'get',
          headers: headers,
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/Update", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SerialNumMaskingSvc/UpdateExt", {
          method: 'post',
          headers: headers,
          body: JSON.stringify(requestBody)
      })
      fetch(request)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialMaskListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SerialMaskListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_SerialMaskRow{
   "odatametadata":string,
   "value":Erp_Tablesets_SerialMaskRow,
}

export interface Erp_Tablesets_SerialMaskListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  This is the ID by which the user will reference a particular serial number format mask.  */  
   "SerialMaskID":string,
      /**  User defined Mask description. This field is mandatory. It should be flagged for Include in Links = true.  */  
   "Description":string,
      /**   Determines if the serial mask can be used in part maintenance.
Default value is yes  */  
   "Active":boolean,
      /**   Determines how the mask is being used. It can either be a validation type or generation type.
If set to validation, then this mask cannot be used for generation of serial numbers ans vice versa.
It should be flagged for Include in Links = true.
Default = 0.
This will require code/desc definition:
0 = Validation
1 = Generation  */  
   "MaskType":number,
      /**  Free form text validated against the defined valid characters for a Mask. This is a mandatory field.  */  
   "Mask":string,
      /**  BL-generated example of the serial number mask that has been defined.  */  
   "Example":string,
      /**  The number of characters that serial numbers will use based on the mask entered.  */  
   "CharactersUsed":number,
      /**  Numeric value up to 10 that defines the maximum number of characters that can be specified for a prefix by a part/Site using this mask.  */  
   "PrefixLength":number,
      /**  Numeric value up to 10 that defines the maximum number of characters that can be specified for a suffix by a part/Site using this mask.  */  
   "SuffixLength":number,
      /**  The portion of the Mask field to be used for generation of the next logical serial number or the default starting serial sequence. It will be the mask minus any special elements (those surrounded by < and >).  */  
   "GenerateSeqString":string,
      /**  This is the global last used serial sequence default. It is used only for the Mask Generate type to determine the next logical serial number to generate when the part/Site is flagged to use the global sequence counter.  */  
   "SNLastUsedSeq":string,
      /**  Marks this SerialMask as global, available to be sent out to other companies.  */  
   "GlobalSerialMask":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates whether this mask is used in Part or SerialNo  */  
   "IsUsed":boolean,
   "WarnMsg":string,
      /**  Mask Type Description  */  
   "MaskTypeDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_SerialMaskRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  This is the ID by which the user will reference a particular serial number format mask.  */  
   "SerialMaskID":string,
      /**  User defined Mask description. This field is mandatory. It should be flagged for Include in Links = true.  */  
   "Description":string,
      /**   Determines if the serial mask can be used in part maintenance.
Default value is yes  */  
   "Active":boolean,
      /**   Determines how the mask is being used. It can either be a validation type or generation type.
If set to validation, then this mask cannot be used for generation of serial numbers ans vice versa.
It should be flagged for Include in Links = true.
Default = 0.
This will require code/desc definition:
0 = Validation
1 = Generation  */  
   "MaskType":number,
      /**  Free form text validated against the defined valid characters for a Mask. This is a mandatory field.  */  
   "Mask":string,
      /**  BL-generated example of the serial number mask that has been defined.  */  
   "Example":string,
      /**  The number of characters that serial numbers will use based on the mask entered.  */  
   "CharactersUsed":number,
      /**  Numeric value up to 10 that defines the maximum number of characters that can be specified for a prefix by a part/Site using this mask.  */  
   "PrefixLength":number,
      /**  Numeric value up to 10 that defines the maximum number of characters that can be specified for a suffix by a part/Site using this mask.  */  
   "SuffixLength":number,
      /**  The portion of the Mask field to be used for generation of the next logical serial number or the default starting serial sequence. It will be the mask minus any special elements (those surrounded by < and >).  */  
   "GenerateSeqString":string,
      /**  This is the global last used serial sequence default. It is used only for the Mask Generate type to determine the next logical serial number to generate when the part/Site is flagged to use the global sequence counter.  */  
   "SNLastUsedSeq":string,
      /**  Marks this SerialMask as global, available to be sent out to other companies.  */  
   "GlobalSerialMask":boolean,
      /**  Disables this record from receiving global updates.  */  
   "GlobalLock":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates whether this mask is used in Part or SerialNo  */  
   "IsUsed":boolean,
   "WarnMsg":string,
      /**  Mask Type Description  */  
   "MaskTypeDesc":string,
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
      @param ipMask
      @param ipPart
   */  
export interface ConstructExampleString_input{
      /**  SerialMask.Mask  */  
   ipMask:string,
      /**  Part.PartNum  */  
   ipPart:string,
}

export interface ConstructExampleString_output{
parameters : {
      /**  output parameters  */  
   opExampleStr:string,
}
}

   /** Required : 
      @param serialMaskID
   */  
export interface DeleteByID_input{
   serialMaskID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_SerialMaskListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  This is the ID by which the user will reference a particular serial number format mask.  */  
   SerialMaskID:string,
      /**  User defined Mask description. This field is mandatory. It should be flagged for Include in Links = true.  */  
   Description:string,
      /**   Determines if the serial mask can be used in part maintenance.
Default value is yes  */  
   Active:boolean,
      /**   Determines how the mask is being used. It can either be a validation type or generation type.
If set to validation, then this mask cannot be used for generation of serial numbers ans vice versa.
It should be flagged for Include in Links = true.
Default = 0.
This will require code/desc definition:
0 = Validation
1 = Generation  */  
   MaskType:number,
      /**  Free form text validated against the defined valid characters for a Mask. This is a mandatory field.  */  
   Mask:string,
      /**  BL-generated example of the serial number mask that has been defined.  */  
   Example:string,
      /**  The number of characters that serial numbers will use based on the mask entered.  */  
   CharactersUsed:number,
      /**  Numeric value up to 10 that defines the maximum number of characters that can be specified for a prefix by a part/Site using this mask.  */  
   PrefixLength:number,
      /**  Numeric value up to 10 that defines the maximum number of characters that can be specified for a suffix by a part/Site using this mask.  */  
   SuffixLength:number,
      /**  The portion of the Mask field to be used for generation of the next logical serial number or the default starting serial sequence. It will be the mask minus any special elements (those surrounded by < and >).  */  
   GenerateSeqString:string,
      /**  This is the global last used serial sequence default. It is used only for the Mask Generate type to determine the next logical serial number to generate when the part/Site is flagged to use the global sequence counter.  */  
   SNLastUsedSeq:string,
      /**  Marks this SerialMask as global, available to be sent out to other companies.  */  
   GlobalSerialMask:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates whether this mask is used in Part or SerialNo  */  
   IsUsed:boolean,
   WarnMsg:string,
      /**  Mask Type Description  */  
   MaskTypeDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SerialMaskListTableset{
   SerialMaskList:Erp_Tablesets_SerialMaskListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SerialMaskRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  This is the ID by which the user will reference a particular serial number format mask.  */  
   SerialMaskID:string,
      /**  User defined Mask description. This field is mandatory. It should be flagged for Include in Links = true.  */  
   Description:string,
      /**   Determines if the serial mask can be used in part maintenance.
Default value is yes  */  
   Active:boolean,
      /**   Determines how the mask is being used. It can either be a validation type or generation type.
If set to validation, then this mask cannot be used for generation of serial numbers ans vice versa.
It should be flagged for Include in Links = true.
Default = 0.
This will require code/desc definition:
0 = Validation
1 = Generation  */  
   MaskType:number,
      /**  Free form text validated against the defined valid characters for a Mask. This is a mandatory field.  */  
   Mask:string,
      /**  BL-generated example of the serial number mask that has been defined.  */  
   Example:string,
      /**  The number of characters that serial numbers will use based on the mask entered.  */  
   CharactersUsed:number,
      /**  Numeric value up to 10 that defines the maximum number of characters that can be specified for a prefix by a part/Site using this mask.  */  
   PrefixLength:number,
      /**  Numeric value up to 10 that defines the maximum number of characters that can be specified for a suffix by a part/Site using this mask.  */  
   SuffixLength:number,
      /**  The portion of the Mask field to be used for generation of the next logical serial number or the default starting serial sequence. It will be the mask minus any special elements (those surrounded by < and >).  */  
   GenerateSeqString:string,
      /**  This is the global last used serial sequence default. It is used only for the Mask Generate type to determine the next logical serial number to generate when the part/Site is flagged to use the global sequence counter.  */  
   SNLastUsedSeq:string,
      /**  Marks this SerialMask as global, available to be sent out to other companies.  */  
   GlobalSerialMask:boolean,
      /**  Disables this record from receiving global updates.  */  
   GlobalLock:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates whether this mask is used in Part or SerialNo  */  
   IsUsed:boolean,
   WarnMsg:string,
      /**  Mask Type Description  */  
   MaskTypeDesc:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SerialNumMaskingTableset{
   SerialMask:Erp_Tablesets_SerialMaskRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtSerialNumMaskingTableset{
   SerialMask:Erp_Tablesets_SerialMaskRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param serialMaskID
   */  
export interface GetByID_input{
   serialMaskID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_SerialNumMaskingTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_SerialNumMaskingTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_SerialNumMaskingTableset[],
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
   returnObj:Erp_Tablesets_SerialMaskListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewSerialMask_input{
   ds:Erp_Tablesets_SerialNumMaskingTableset[],
}

export interface GetNewSerialMask_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNumMaskingTableset,
}
}

   /** Required : 
      @param whereClauseSerialMask
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseSerialMask:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_SerialNumMaskingTableset[],
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
      @param ipNewMask
      @param ipMaskType
      @param ds
   */  
export interface OnChangeOfMask_input{
      /**  SerialMask.Mask  */  
   ipNewMask:string,
      /**  SerialMask.MaskType  */  
   ipMaskType:number,
   ds:Erp_Tablesets_SerialNumMaskingTableset[],
}

export interface OnChangeOfMask_output{
parameters : {
      /**  output parameters  */  
   opWarnMsg:string,
   ds:Erp_Tablesets_SerialNumMaskingTableset,
}
}

   /** Required : 
      @param ipGenSeqStr
      @param ipLastUsedSeq
   */  
export interface OnChangeSNLastUsedSeq_input{
      /**  SerialMask.GenerateSeqString  */  
   ipGenSeqStr:string,
      /**  SerialMask.SNLastUsedSeq  */  
   ipLastUsedSeq:string,
}

export interface OnChangeSNLastUsedSeq_output{
}

   /** Required : 
      @param iPrefixLength
      @param iSuffixLength
      @param example
   */  
export interface UpdateCharactersUsed_input{
      /**  Length of the Prefix  */  
   iPrefixLength:number,
      /**  Length of the Suffix  */  
   iSuffixLength:number,
      /**  serial mask example  */  
   example:string,
}

export interface UpdateCharactersUsed_output{
parameters : {
      /**  output parameters  */  
   charactersUsed:number,
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtSerialNumMaskingTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtSerialNumMaskingTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_SerialNumMaskingTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNumMaskingTableset,
}
}

