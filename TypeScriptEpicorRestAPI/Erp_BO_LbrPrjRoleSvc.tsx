import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.LbrPrjRoleSvc
// Description: LrbPrjRole BO used by Labor Transaction Project Role Code Maint
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/$metadata", {
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
   Description: Get LbrPrjRoles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LbrPrjRoles
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlRow
   */  
export function get_LbrPrjRoles(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/LbrPrjRoles", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LbrPrjRoles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LbrPrjRoles(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/LbrPrjRoles", {
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
   Summary: Calls GetByID to retrieve the LbrPrjRole item
   Description: Calls GetByID to retrieve the LbrPrjRole item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LbrPrjRole
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   */  
export function get_LbrPrjRoles_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_LaborDtlRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/LbrPrjRoles(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_LaborDtlRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update LbrPrjRole for the service
   Description: Calls UpdateExt to update LbrPrjRole. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LbrPrjRole
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_LbrPrjRoles_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/LbrPrjRoles(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
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
   Summary: Call UpdateExt to delete LbrPrjRole item
   Description: Call UpdateExt to delete LbrPrjRole item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LbrPrjRole
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param LaborHedSeq Desc: LaborHedSeq   Required: True
      @param LaborDtlSeq Desc: LaborDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_LbrPrjRoles_Company_LaborHedSeq_LaborDtlSeq(Company:string, LaborHedSeq:string, LaborDtlSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/LbrPrjRoles(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlListRow)
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
export function get_GetRows(whereClauseLaborDtl:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseLaborDtl!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseLaborDtl=" + whereClauseLaborDtl
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/GetRows" + params, {
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(laborHedSeq:string, laborDtlSeq:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof laborHedSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "laborHedSeq=" + laborHedSeq
   }
   if(typeof laborDtlSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "laborDtlSeq=" + laborDtlSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/GetList" + params, {
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
   Summary: Invoke method OnChangeNewPrjRoleCd
   Description: This method validates the NewPrjRoleCd.
   OperationID: OnChangeNewPrjRoleCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeNewPrjRoleCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeNewPrjRoleCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeNewPrjRoleCd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/OnChangeNewPrjRoleCd", {
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
   Summary: Invoke method UpdatePrjRoleCd
   Description: .
   OperationID: UpdatePrjRoleCd
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdatePrjRoleCd_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdatePrjRoleCd_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdatePrjRoleCd(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/UpdatePrjRoleCd", {
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
   Summary: Invoke method GetNewLaborDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborDtl(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/GetNewLaborDtl", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.LbrPrjRoleSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborDtlListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow{
   "odatametadata":string,
   "value":Erp_Tablesets_LaborDtlRow[],
}

export interface Erp_Tablesets_LaborDtlListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   "EmployeeNum":string,
      /**  Used as the foreign key to the LaborHed record.  */  
   "LaborHedSeq":number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   "LaborDtlSeq":number,
      /**   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   "LaborType":string,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   "LaborTypePseudo":string,
      /**  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  */  
   "ReWork":boolean,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  */  
   "ReworkReasonCode":string,
      /**  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  */  
   "JobNum":string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  */  
   "AssemblySeq":number,
      /**   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  */  
   "OprSeq":number,
      /**  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  */  
   "JCDept":string,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  */  
   "ResourceGrpID":string,
      /**  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  */  
   "OpCode":string,
      /**  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  */  
   "LaborHrs":number,
      /**  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  */  
   "BurdenHrs":number,
      /**  The Total production quantity reported.  */  
   "LaborQty":number,
      /**  The reported scrap quantity.  */  
   "ScrapQty":number,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  */  
   "ScrapReasonCode":string,
      /**  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  */  
   "SetupPctComplete":number,
      /**  Indicates if this transaction "completes" either the setup or production for this operation.  */  
   "Complete":boolean,
      /**  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  */  
   "IndirectCode":string,
      /**  A short note that the user can make about the labor transaction.  */  
   "LaborNote":string,
      /**  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  */  
   "ExpenseCode":string,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   "LaborCollection":boolean,
      /**  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  */  
   "AppliedToSchedule":boolean,
      /**  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  */  
   "ClockInMInute":number,
      /**  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  */  
   "ClockOutMinute":number,
      /**  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  */  
   "ClockInDate":string,
      /**   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  */  
   "ClockinTime":number,
      /**   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  */  
   "ClockOutTime":number,
      /**   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  */  
   "ActiveTrans":boolean,
      /**  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  */  
   "OverRidePayRate":number,
      /**  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  */  
   "LaborRate":number,
      /**  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  */  
   "BurdenRate":number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   "DspClockInTime":string,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   "DspClockOutTime":string,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   "ResourceID":string,
      /**  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  */  
   "OpComplete":boolean,
      /**  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  */  
   "EarnedHrs":number,
      /**  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  */  
   "AddedOper":boolean,
      /**  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  */  
   "PayrollDate":string,
      /**   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  */  
   "PostedToGL":boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  */  
   "GLTrans":boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Indicates if the labordtl record inspection has completed.  */  
   "InspectionPending":boolean,
      /**  The service call that this service record belongs to.  */  
   "CallNum":number,
      /**  The line number of the service call this labor detail is for.  */  
   "CallLine":number,
      /**  the service that is being performed on this line.  */  
   "ServNum":number,
      /**  A unique code that identifies the Service  */  
   "ServCode":string,
      /**  Problem reason code from the reason master table. type Service call.  */  
   "ResReasonCode":string,
      /**  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  */  
   "WipPosted":boolean,
      /**  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  */  
   "DiscrepQty":number,
      /**   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  */  
   "DiscrpRsnCode":string,
      /**  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  */  
   "ParentLaborDtlSeq":number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  */  
   "LaborEntryMethod":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  */  
   "BFLaborReq":boolean,
      /**  Reference to the ABT, it is GUID,used in PostingEngine  */  
   "ABTUID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Project Role Code  */  
   "RoleCd":string,
      /**  Time Type Code  */  
   "TimeTypCd":string,
      /**  The Project Billing Invoice Number where these charges were processed.  */  
   "PBInvNum":number,
      /**  The payment method of the time.  */  
   "PMUID":number,
      /**  Link to Task set  */  
   "TaskSetID":string,
      /**  The date the time received final approval.  */  
   "ApprovedDate":string,
      /**  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   "ClaimRef":string,
      /**  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  */  
   "QuickEntryCode":string,
      /**   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   "TimeStatus":string,
      /**  Userid of the user who created the record.  */  
   "CreatedBy":string,
      /**  The date the record was created.  */  
   "CreateDate":string,
      /**  The time the record was created (in seconds since midnight)  */  
   "CreateTime":number,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date the record was last changed.  */  
   "ChangeDate":string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   "ChangeTime":number,
      /**  The Currently active Stage changing task  */  
   "ActiveTaskID":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
      /**  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  */  
   "CreatedViaTEWeekView":boolean,
      /**  The identifier of the workflow stage.  */  
   "CurrentWFStageID":string,
      /**  The identifier of the workflow group  */  
   "WFGroupID":string,
      /**  This indicates if the workflow for this group is complete.  */  
   "WFComplete":boolean,
      /**  Indicates if approval is required for this transaction.  */  
   "ApprovalRequired":boolean,
      /**  The User ID of the submitter.  */  
   "SubmittedBy":string,
      /**  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  */  
   "PBRateFrom":string,
      /**  Project Billing calculation in COSandWIP: Currency code is got from Project  */  
   "PBCurrencyCode":string,
      /**  Project Billing calculation in COSandWIP: Hours used for charge  */  
   "PBHours":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  */  
   "PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  */  
   "PBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  */  
   "DocPBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   "Rpt1PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   "Rpt2PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   "Rpt3PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  */  
   "DocPBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   "Rpt1PBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   "Rpt2PBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   "Rpt3PBChargeAmt":number,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   "Shift":number,
      /**  Links to PActDtl.ActID  */  
   "ActID":number,
      /**  System assigned unique id number for the detail. Links to PActDtl.DetailID  */  
   "DtailID":number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   "ProjProcessed":boolean,
      /**  Used By Project Analysis Process.  */  
   "AsOfDate":string,
      /**  Used By Project Analysis Process.  */  
   "AsOfSeq":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "JobType":string,
   "CompleteFlag":boolean,
   "ProdDesc":string,
   "DisplayJob":string,
   "FSComplete":boolean,
   "DspTotHours":string,
      /**  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  */  
   "OkToChangeResourceGrpID":boolean,
   "EndActivity":boolean,
   "NextAssemblySeq":number,
   "NextOprSeq":number,
   "RequestMove":boolean,
   "NextResourceDesc":string,
   "NextOperDesc":string,
   "EnableResourceGrpID":boolean,
   "JCSystScrapReasons":boolean,
   "JobOperComplete":boolean,
   "EnableRequestMove":boolean,
   "UnapprovedFirstArt":boolean,
   "EnableLaborQty":boolean,
   "EnableComplete":boolean,
   "EnableScrapQty":boolean,
   "EnableDiscrepQty":boolean,
   "PrintNCTag":boolean,
      /**  calculated field: LaborHrs * LaborRate  */  
   "LaborCost":number,
      /**  calculated field: BurdenHrs * BurdenRate  */  
   "BurdenCost":number,
   "DtClockIn":string,
   "DtClockOut":string,
   "CapabilityID":string,
   "CapabilityDescription":string,
   "MultipleEmployeesText":string,
   "StartActivity":boolean,
      /**  GL Journal Source Transaction Date  */  
   "GLTranDate":string,
      /**  GL Journal Source Transaction Amount  */  
   "GLTranAmt":number,
      /**  Labor Detail Employee Name  */  
   "EmployeeName":string,
      /**  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  */  
   "EfficiencyPercentage":number,
   "JCSystReworkReasons":boolean,
   "ResourceDesc":string,
      /**  Unit of Measure used for DiscrepQty  */  
   "DiscrepUOM":string,
      /**  Unit of Measure used for LaborQty  */  
   "LaborUOM":string,
      /**  Unit of Measure used for ScrapQty.  */  
   "ScrapUOM":string,
      /**  Enable the SN Button?  */  
   "EnableSN":boolean,
      /**  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  */  
   "PhaseOprSeq":number,
      /**  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  */  
   "PhaseJobNum":string,
      /**  Field that indicates if field PrjRoleCd should be disabled.  */  
   "DisPrjRoleCd":boolean,
      /**  Field that indicates if field TimeTypCd should be disabled.  */  
   "DisTimeTypCd":boolean,
      /**  Field that indicates if field DisLaborTypeshould be disabled.  */  
   "DisLaborType":boolean,
      /**  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  */  
   "NewPrjRoleCd":string,
      /**  Holds the description for NewPrjRoleCd  */  
   "NewRoleCdDesc":string,
      /**  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  */  
   "JobTypeCode":string,
   "PrjUsedTran":string,
   "PBAllowModify":boolean,
   "ApprovedBy":string,
   "PendingApprovalBy":string,
   "TreeNodeImageName":string,
   "EnableInspection":boolean,
      /**  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  */  
   "LbrDay":string,
      /**  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  */  
   "LbrMonth":string,
      /**  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  */  
   "LbrWeek":string,
      /**  Company Base currency code description for display in LaborDtl grid.  */  
   "BaseCurrCodeDesc":string,
      /**  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  */  
   "ChgRateCurrDesc":string,
      /**  Charge rate calculated for Time and Expense approval  */  
   "ChargeRate":number,
      /**  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  */  
   "ChargeRateSRC":string,
      /**  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalProjectID":string,
      /**  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalProjectDesc":string,
   "DspCreateTime":string,
   "DspChangeTime":string,
      /**  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalPhaseID":string,
      /**  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalPhaseDesc":string,
   "WeekDisplayText":string,
   "NotSubmitted":boolean,
   "TimeDisableUpdate":boolean,
   "TimeDisableDelete":boolean,
   "RoleCdDisplayAll":boolean,
      /**  Indicates if the user has access to the row  */  
   "HasAccessToRow":boolean,
      /**  Indicates if the submit button is enabled  */  
   "EnableSubmit":boolean,
      /**  Indicates if the recall button is enabled  */  
   "EnableRecall":boolean,
      /**  Indicates if the copy button is enabled  */  
   "EnableCopy":boolean,
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   "AllowDirLbr":boolean,
   "MES":boolean,
      /**  Indicates if recall is available for an approver  */  
   "EnableRecallAprv":boolean,
      /**  Used in approval entry.  Indicates if the approver has an open task or not.  */  
   "ApprvrHasOpenTask":boolean,
      /**  To know if the LaborDtl was created on the current plant  */  
   "EnteredOnCurPlant":boolean,
      /**  Full description of Reason... used on displays/reports.  */  
   "DiscrpRsnDescription":string,
      /**  First name of employee.  */  
   "EmpBasicFirstName":string,
      /**  Last name of employee  */  
   "EmpBasicLastName":string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   "EmpBasicName":string,
      /**  Full description of the Labor Expense Code master.  */  
   "ExpenseCodeDescription":string,
      /**  Full description of the Indirect Labor.  */  
   "IndirectDescription":string,
      /**  Job Costing department description.  */  
   "JCDeptDescription":string,
      /**  Full description of Resource.  */  
   "MachineDescription":string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   "OpCodeOpDesc":string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   "PayMethodSummarizePerCustomer":boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   "PayMethodType":number,
      /**  Name of the payment method  */  
   "PayMethodName":string,
      /**  Description  */  
   "PhaseIDDescription":string,
      /**  Full description of Project Management Code.  */  
   "ProjectDescription":string,
      /**  Long description of the Resource Group.  */  
   "ResourceGrpDescription":string,
      /**  Full description of Reason... used on displays/reports.  */  
   "ResReasonDescription":string,
      /**  Full description of Reason... used on displays/reports.  */  
   "ReWorkReasonDescription":string,
      /**  A description of the role.  */  
   "RoleCdRoleDescription":string,
      /**  Full description of Reason... used on displays/reports.  */  
   "ScrapReasonDescription":string,
      /**  A concatenation of Start + End time.  */  
   "ShiftDescription":string,
      /**  The description of the Time Type Code  */  
   "TimeTypCdDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_LaborDtlRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   "EmployeeNum":string,
      /**  Used as the foreign key to the LaborHed record.  */  
   "LaborHedSeq":number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   "LaborDtlSeq":number,
      /**   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   "LaborType":string,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   "LaborTypePseudo":string,
      /**  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  */  
   "ReWork":boolean,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  */  
   "ReworkReasonCode":string,
      /**  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  */  
   "JobNum":string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  */  
   "AssemblySeq":number,
      /**   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  */  
   "OprSeq":number,
      /**  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  */  
   "JCDept":string,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  */  
   "ResourceGrpID":string,
      /**  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  */  
   "OpCode":string,
      /**  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  */  
   "LaborHrs":number,
      /**  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  */  
   "BurdenHrs":number,
      /**  The Total production quantity reported.  */  
   "LaborQty":number,
      /**  The reported scrap quantity.  */  
   "ScrapQty":number,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  */  
   "ScrapReasonCode":string,
      /**  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  */  
   "SetupPctComplete":number,
      /**  Indicates if this transaction "completes" either the setup or production for this operation.  */  
   "Complete":boolean,
      /**  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  */  
   "IndirectCode":string,
      /**  A short note that the user can make about the labor transaction.  */  
   "LaborNote":string,
      /**  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  */  
   "ExpenseCode":string,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   "LaborCollection":boolean,
      /**  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  */  
   "AppliedToSchedule":boolean,
      /**  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  */  
   "ClockInMInute":number,
      /**  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  */  
   "ClockOutMinute":number,
      /**  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  */  
   "ClockInDate":string,
      /**   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  */  
   "ClockinTime":number,
      /**   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  */  
   "ClockOutTime":number,
      /**   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  */  
   "ActiveTrans":boolean,
      /**  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  */  
   "OverRidePayRate":number,
      /**  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  */  
   "LaborRate":number,
      /**  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  */  
   "BurdenRate":number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   "DspClockInTime":string,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   "DspClockOutTime":string,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   "ResourceID":string,
      /**  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  */  
   "OpComplete":boolean,
      /**  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  */  
   "EarnedHrs":number,
      /**  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  */  
   "AddedOper":boolean,
      /**  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  */  
   "PayrollDate":string,
      /**   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  */  
   "PostedToGL":boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   "FiscalYear":number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "FiscalPeriod":number,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   "JournalNum":number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  */  
   "GLTrans":boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   "JournalCode":string,
      /**  Indicates if the labordtl record inspection has completed.  */  
   "InspectionPending":boolean,
      /**  The service call that this service record belongs to.  */  
   "CallNum":number,
      /**  The line number of the service call this labor detail is for.  */  
   "CallLine":number,
      /**  the service that is being performed on this line.  */  
   "ServNum":number,
      /**  A unique code that identifies the Service  */  
   "ServCode":string,
      /**  Problem reason code from the reason master table. type Service call.  */  
   "ResReasonCode":string,
      /**  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  */  
   "WipPosted":boolean,
      /**  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  */  
   "DiscrepQty":number,
      /**   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  */  
   "DiscrpRsnCode":string,
      /**  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  */  
   "ParentLaborDtlSeq":number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  */  
   "LaborEntryMethod":string,
      /**  Fiscal year suffix.  */  
   "FiscalYearSuffix":string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   "FiscalCalendarID":string,
      /**  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  */  
   "BFLaborReq":boolean,
      /**  Reference to the ABT, it is GUID,used in PostingEngine  */  
   "ABTUID":string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   "ProjectID":string,
      /**  Project Phase ID  */  
   "PhaseID":string,
      /**  Project Role Code  */  
   "RoleCd":string,
      /**  Time Type Code  */  
   "TimeTypCd":string,
      /**  The Project Billing Invoice Number where these charges were processed.  */  
   "PBInvNum":number,
      /**  The payment method of the time.  */  
   "PMUID":number,
      /**  Link to Task set  */  
   "TaskSetID":string,
      /**  The date the time received final approval.  */  
   "ApprovedDate":string,
      /**  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   "ClaimRef":string,
      /**  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  */  
   "QuickEntryCode":string,
      /**   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   "TimeStatus":string,
      /**  Userid of the user who created the record.  */  
   "CreatedBy":string,
      /**  The date the record was created.  */  
   "CreateDate":string,
      /**  The time the record was created (in seconds since midnight)  */  
   "CreateTime":number,
      /**  Userid of the user who made the last change to this record.  */  
   "ChangedBy":string,
      /**  The date the record was last changed.  */  
   "ChangeDate":string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   "ChangeTime":number,
      /**  The Currently active Stage changing task  */  
   "ActiveTaskID":string,
      /**  The Last Complete Milestone task  */  
   "LastTaskID":string,
      /**  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  */  
   "CreatedViaTEWeekView":boolean,
      /**  The identifier of the workflow stage.  */  
   "CurrentWFStageID":string,
      /**  The identifier of the workflow group  */  
   "WFGroupID":string,
      /**  This indicates if the workflow for this group is complete.  */  
   "WFComplete":boolean,
      /**  Indicates if approval is required for this transaction.  */  
   "ApprovalRequired":boolean,
      /**  The User ID of the submitter.  */  
   "SubmittedBy":string,
      /**  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  */  
   "PBRateFrom":string,
      /**  Project Billing calculation in COSandWIP: Currency code is got from Project  */  
   "PBCurrencyCode":string,
      /**  Project Billing calculation in COSandWIP: Hours used for charge  */  
   "PBHours":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  */  
   "PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  */  
   "PBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  */  
   "DocPBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   "Rpt1PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   "Rpt2PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   "Rpt3PBChargeRate":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  */  
   "DocPBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   "Rpt1PBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   "Rpt2PBChargeAmt":number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   "Rpt3PBChargeAmt":number,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   "Shift":number,
      /**  Links to PActDtl.ActID  */  
   "ActID":number,
      /**  System assigned unique id number for the detail. Links to PActDtl.DetailID  */  
   "DtailID":number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   "ProjProcessed":boolean,
      /**  Used By Project Analysis Process.  */  
   "AsOfDate":string,
      /**  Used By Project Analysis Process.  */  
   "AsOfSeq":number,
      /**  JDFInputFiles  */  
   "JDFInputFiles":string,
      /**  JDFNumberOfPages  */  
   "JDFNumberOfPages":string,
      /**  BatchWasSaved  */  
   "BatchWasSaved":string,
      /**  AssignToBatch  */  
   "AssignToBatch":boolean,
      /**  BatchComplete  */  
   "BatchComplete":boolean,
      /**  BatchRequestMove  */  
   "BatchRequestMove":boolean,
      /**  BatchPrint  */  
   "BatchPrint":boolean,
      /**  BatchLaborHrs  */  
   "BatchLaborHrs":number,
      /**  BatchPctOfTotHrs  */  
   "BatchPctOfTotHrs":number,
      /**  BatchQty  */  
   "BatchQty":number,
      /**  BatchTotalExpectedHrs  */  
   "BatchTotalExpectedHrs":number,
      /**  JDFOpCompleted  */  
   "JDFOpCompleted":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Downtime  */  
   "Downtime":boolean,
      /**  RefJobNum  */  
   "RefJobNum":string,
      /**  RefAssemblySeq  */  
   "RefAssemblySeq":number,
      /**  RefOprSeq  */  
   "RefOprSeq":number,
      /**  Imported  */  
   "Imported":boolean,
      /**  ImportDate  */  
   "ImportDate":string,
      /**   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  */  
   "TimeAutoSubmit":boolean,
      /**  BatchMode  */  
   "BatchMode":boolean,
      /**  BillServiceRate  */  
   "BillServiceRate":number,
      /**  Pay Hours used for HCM  */  
   "HCMPayHours":number,
      /**  True if transaction is related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  */  
   "DiscrepAttributeSetID":number,
      /**  The unique identifier of the related Dynamic Attribute Set for the Labor Qty  */  
   "LaborAttributeSetID":number,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  */  
   "ScrapAttributeSetID":number,
      /**  PCID  */  
   "PCID":string,
      /**  NonConfPCID  */  
   "NonConfPCID":string,
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   "AllowDirLbr":boolean,
      /**  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalPhaseDesc":string,
      /**  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalPhaseID":string,
      /**  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalProjectDesc":string,
      /**  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   "ApprovalProjectID":string,
   "ApprovedBy":string,
      /**  Used in approval entry.  Indicates if the approver has an open task or not.  */  
   "ApprvrHasOpenTask":boolean,
      /**  Company Base currency code description for display in LaborDtl grid.  */  
   "BaseCurrCodeDesc":string,
      /**  calculated field: BurdenHrs * BurdenRate  */  
   "BurdenCost":number,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   "CallCode":string,
   "CapabilityDescription":string,
   "CapabilityID":string,
      /**  Charge rate calculated for Time and Expense approval  */  
   "ChargeRate":number,
      /**  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  */  
   "ChargeRateSRC":string,
      /**  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  */  
   "ChgRateCurrDesc":string,
   "CompleteFlag":boolean,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   "ContractCode":string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   "ContractNum":number,
      /**  Unit of Measure used for DiscrepQty  */  
   "DiscrepUOM":string,
      /**  Field that indicates if field DisLaborTypeshould be disabled.  */  
   "DisLaborType":boolean,
   "DisplayJob":string,
      /**  Field that indicates if field PrjRoleCd should be disabled.  */  
   "DisPrjRoleCd":boolean,
      /**  Field that indicates if field TimeTypCd should be disabled.  */  
   "DisTimeTypCd":boolean,
   "DowntimeTotal":number,
   "DspChangeTime":string,
   "DspCreateTime":string,
   "DspTotHours":string,
   "DtClockIn":string,
   "DtClockOut":string,
      /**  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  */  
   "EfficiencyPercentage":number,
      /**  Labor Detail Employee Name  */  
   "EmployeeName":string,
   "EnableComplete":boolean,
      /**  Indicates if the copy button is enabled  */  
   "EnableCopy":boolean,
   "EnableDiscrepQty":boolean,
   "EnableInspection":boolean,
   "EnableLaborQty":boolean,
   "EnableNextOprSeq":boolean,
   "EnablePrintTagsList":boolean,
      /**  Indicates if the recall button is enabled  */  
   "EnableRecall":boolean,
      /**  Indicates if recall is available for an approver  */  
   "EnableRecallAprv":boolean,
   "EnableRequestMove":boolean,
   "EnableResourceGrpID":boolean,
   "EnableScrapQty":boolean,
      /**  Enable the SN Button?  */  
   "EnableSN":boolean,
      /**  Indicates if the submit button is enabled  */  
   "EnableSubmit":boolean,
   "EndActivity":boolean,
      /**  To know if the LaborDtl was created on the current plant  */  
   "EnteredOnCurPlant":boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   "FSAAction":string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   "FSACallCode":string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   "FSAContractCode":string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   "FSAContractNum":number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   "FSAEmpID":string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   "FSAEquipmentInstallID":number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   "FSAEquipmentPartNum":string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderNum":number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderResourceNum":number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   "FSAWarrantyCode":string,
   "FSComplete":boolean,
      /**  GL Journal Source Transaction Amount  */  
   "GLTranAmt":number,
      /**  GL Journal Source Transaction Date  */  
   "GLTranDate":string,
      /**  Indicates if the user has access to the row  */  
   "HasAccessToRow":boolean,
      /**  Indicates if the labor detail has comments  */  
   "HasComments":boolean,
      /**  To tell the bo that this transaction was being modified from HH.  */  
   "HH":boolean,
      /**  Unique identifier of related integration record.  */  
   "IntExternalKey":string,
      /**  Indicates if the job operation is marked as fixed hours and quantity only.  */  
   "ISFixHourAndQtyOnly":boolean,
   "JCSystReworkReasons":boolean,
   "JCSystScrapReasons":boolean,
   "JobOperComplete":boolean,
   "JobType":string,
      /**  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  */  
   "JobTypeCode":string,
      /**  calculated field: LaborHrs * LaborRate  */  
   "LaborCost":number,
      /**  Unit of Measure used for LaborQty  */  
   "LaborUOM":string,
      /**  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  */  
   "LbrDay":string,
      /**  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  */  
   "LbrMonth":string,
      /**  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  */  
   "LbrWeek":string,
   "MES":boolean,
   "MultipleEmployeesText":string,
   "NewDifDateFlag":number,
      /**  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  */  
   "NewPrjRoleCd":string,
      /**  Holds the description for NewPrjRoleCd  */  
   "NewRoleCdDesc":string,
   "NextAssemblySeq":number,
   "NextOperDesc":string,
   "NextOprSeq":number,
   "NextResourceDesc":string,
      /**  To evaluate if the NonComformance has been already processed in inspection and no changes can be applied on LaborDtl then.  */  
   "NonConfProcessed":boolean,
   "NotSubmitted":boolean,
      /**  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  */  
   "OkToChangeResourceGrpID":boolean,
   "PartDescription":string,
   "PartNum":string,
   "PBAllowModify":boolean,
   "PendingApprovalBy":string,
      /**  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  */  
   "PhaseJobNum":string,
      /**  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  */  
   "PhaseOprSeq":number,
   "PrintNCTag":boolean,
   "PrjUsedTran":string,
   "ProdDesc":string,
   "ProjPhaseID":string,
   "RequestMove":boolean,
   "ResourceDesc":string,
   "RoleCdDisplayAll":boolean,
      /**  Unit of Measure used for ScrapQty.  */  
   "ScrapUOM":string,
      /**  Flag field to identify if the row is being sent from MES  */  
   "SentFromMES":boolean,
   "StartActivity":boolean,
   "TimeDisableDelete":boolean,
   "TimeDisableUpdate":boolean,
   "TreeNodeImageName":string,
   "UnapprovedFirstArt":boolean,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   "WarrantyCode":string,
   "WeekDisplayText":string,
      /**  EnablePCID  */  
   "EnablePCID":boolean,
      /**  The output bin from the resource  */  
   "OutputBin":string,
      /**  The output warehouse from the resource  */  
   "OutputWarehouse":string,
      /**  Internal flag used for the row rules to control whether the Lot columns should be enabled.  */  
   "EnableLot":boolean,
      /**  Lot number that is to be added to the PCID  */  
   "LotNum":string,
      /**  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  */  
   "PrintPCIDContents":boolean,
      /**  Indicates if the labor detail has attachments  */  
   "HasAttachments":boolean,
   "AttrClassID":string,
      /**  The Full Description of the Attribute Set for DiscrepQty  */  
   "DiscrepAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set for DiscrepQty  */  
   "DiscrepAttributeSetShortDescription":string,
      /**  The Full Description of the Attribute Set for ScrapQty  */  
   "ScrapAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set for ScrapQty  */  
   "ScrapAttributeSetShortDescription":string,
      /**  The Full Description of the Attribute Set for LaborQty  */  
   "LaborAttributeSetDescription":string,
      /**  The Short Description of the Attribute Set for LaborQty  */  
   "LaborAttributeSetShortDescription":string,
      /**  Indicates if recall and delete should be disabled  */  
   "DisableRecallAndDelete":boolean,
      /**  List of available role codes  */  
   "RoleCdList":string,
      /**  Indicates if the row is selected for submit, recall, or copy  */  
   "RowSelected":boolean,
      /**  Start date/time for calendar appoinment  */  
   "AppointmentStart":string,
      /**  End date/time for calendar appoinment  */  
   "AppointmentEnd":string,
      /**  Title to display for the calendar appointment  */  
   "AppointmentTitle":string,
      /**  PDF Form Template linked to the Job Operation  */  
   "TemplateID":string,
      /**  Flag to validate if the transaction includes WIP  */  
   "WIPTransaction":boolean,
      /**  Revision for DiscrepQty  */  
   "DiscrepRevision":string,
      /**  Revision for LaborQty  */  
   "LaborRevision":string,
      /**  Revision for ScrapQty  */  
   "ScrapRevision":string,
   "TrackInventoryByRevision":boolean,
      /**  Indicates whether co-parts can be entered  */  
   "ReportPartQtyAllowed":boolean,
   "BitFlag":number,
   "DiscrpRsnDescription":string,
   "EmpBasicLastName":string,
   "EmpBasicFirstName":string,
   "EmpBasicName":string,
   "ExpenseCodeDescription":string,
   "HCMIntregationHCMEnabled":boolean,
   "HCMStatusStatus":string,
   "IndirectDescription":string,
   "JCDeptDescription":string,
   "JobAsmblPartNum":string,
   "JobAsmblDescription":string,
   "MachineDescription":string,
   "OpCodeOpDesc":string,
   "OpDescOpDesc":string,
   "PayMethodType":number,
   "PayMethodSummarizePerCustomer":boolean,
   "PayMethodName":string,
   "PhaseIDDescription":string,
   "ProjectDescription":string,
   "ResourceGrpDescription":string,
   "ResReasonDescription":string,
   "ReWorkReasonDescription":string,
   "RoleCdRoleDescription":string,
   "ScrapReasonDescription":string,
   "ShiftDescription":string,
   "TimeTypCdDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface DeleteByID_input{
   laborHedSeq:number,
   laborDtlSeq:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_LaborDtlListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   EmployeeNum:string,
      /**  Used as the foreign key to the LaborHed record.  */  
   LaborHedSeq:number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   LaborDtlSeq:number,
      /**   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   LaborType:string,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   LaborTypePseudo:string,
      /**  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  */  
   ReWork:boolean,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  */  
   ReworkReasonCode:string,
      /**  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  */  
   JobNum:string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  */  
   AssemblySeq:number,
      /**   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  */  
   OprSeq:number,
      /**  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  */  
   JCDept:string,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  */  
   ResourceGrpID:string,
      /**  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  */  
   OpCode:string,
      /**  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  */  
   LaborHrs:number,
      /**  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  */  
   BurdenHrs:number,
      /**  The Total production quantity reported.  */  
   LaborQty:number,
      /**  The reported scrap quantity.  */  
   ScrapQty:number,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  */  
   ScrapReasonCode:string,
      /**  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  */  
   SetupPctComplete:number,
      /**  Indicates if this transaction "completes" either the setup or production for this operation.  */  
   Complete:boolean,
      /**  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  */  
   IndirectCode:string,
      /**  A short note that the user can make about the labor transaction.  */  
   LaborNote:string,
      /**  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  */  
   ExpenseCode:string,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   LaborCollection:boolean,
      /**  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  */  
   AppliedToSchedule:boolean,
      /**  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  */  
   ClockInMInute:number,
      /**  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  */  
   ClockOutMinute:number,
      /**  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  */  
   ClockInDate:string,
      /**   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  */  
   ClockinTime:number,
      /**   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  */  
   ClockOutTime:number,
      /**   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  */  
   ActiveTrans:boolean,
      /**  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  */  
   OverRidePayRate:number,
      /**  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  */  
   LaborRate:number,
      /**  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  */  
   BurdenRate:number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockInTime:string,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockOutTime:string,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   ResourceID:string,
      /**  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  */  
   OpComplete:boolean,
      /**  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  */  
   EarnedHrs:number,
      /**  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  */  
   AddedOper:boolean,
      /**  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  */  
   PayrollDate:string,
      /**   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  */  
   PostedToGL:boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  */  
   GLTrans:boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Indicates if the labordtl record inspection has completed.  */  
   InspectionPending:boolean,
      /**  The service call that this service record belongs to.  */  
   CallNum:number,
      /**  The line number of the service call this labor detail is for.  */  
   CallLine:number,
      /**  the service that is being performed on this line.  */  
   ServNum:number,
      /**  A unique code that identifies the Service  */  
   ServCode:string,
      /**  Problem reason code from the reason master table. type Service call.  */  
   ResReasonCode:string,
      /**  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  */  
   WipPosted:boolean,
      /**  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  */  
   DiscrepQty:number,
      /**   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  */  
   DiscrpRsnCode:string,
      /**  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  */  
   ParentLaborDtlSeq:number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  */  
   LaborEntryMethod:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  */  
   BFLaborReq:boolean,
      /**  Reference to the ABT, it is GUID,used in PostingEngine  */  
   ABTUID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Project Role Code  */  
   RoleCd:string,
      /**  Time Type Code  */  
   TimeTypCd:string,
      /**  The Project Billing Invoice Number where these charges were processed.  */  
   PBInvNum:number,
      /**  The payment method of the time.  */  
   PMUID:number,
      /**  Link to Task set  */  
   TaskSetID:string,
      /**  The date the time received final approval.  */  
   ApprovedDate:string,
      /**  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   ClaimRef:string,
      /**  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  */  
   QuickEntryCode:string,
      /**   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   TimeStatus:string,
      /**  Userid of the user who created the record.  */  
   CreatedBy:string,
      /**  The date the record was created.  */  
   CreateDate:string,
      /**  The time the record was created (in seconds since midnight)  */  
   CreateTime:number,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date the record was last changed.  */  
   ChangeDate:string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   ChangeTime:number,
      /**  The Currently active Stage changing task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  */  
   CreatedViaTEWeekView:boolean,
      /**  The identifier of the workflow stage.  */  
   CurrentWFStageID:string,
      /**  The identifier of the workflow group  */  
   WFGroupID:string,
      /**  This indicates if the workflow for this group is complete.  */  
   WFComplete:boolean,
      /**  Indicates if approval is required for this transaction.  */  
   ApprovalRequired:boolean,
      /**  The User ID of the submitter.  */  
   SubmittedBy:string,
      /**  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  */  
   PBRateFrom:string,
      /**  Project Billing calculation in COSandWIP: Currency code is got from Project  */  
   PBCurrencyCode:string,
      /**  Project Billing calculation in COSandWIP: Hours used for charge  */  
   PBHours:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  */  
   PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  */  
   PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  */  
   DocPBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt1PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt2PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt3PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  */  
   DocPBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt1PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt2PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt3PBChargeAmt:number,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   Shift:number,
      /**  Links to PActDtl.ActID  */  
   ActID:number,
      /**  System assigned unique id number for the detail. Links to PActDtl.DetailID  */  
   DtailID:number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   ProjProcessed:boolean,
      /**  Used By Project Analysis Process.  */  
   AsOfDate:string,
      /**  Used By Project Analysis Process.  */  
   AsOfSeq:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   JobType:string,
   CompleteFlag:boolean,
   ProdDesc:string,
   DisplayJob:string,
   FSComplete:boolean,
   DspTotHours:string,
      /**  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  */  
   OkToChangeResourceGrpID:boolean,
   EndActivity:boolean,
   NextAssemblySeq:number,
   NextOprSeq:number,
   RequestMove:boolean,
   NextResourceDesc:string,
   NextOperDesc:string,
   EnableResourceGrpID:boolean,
   JCSystScrapReasons:boolean,
   JobOperComplete:boolean,
   EnableRequestMove:boolean,
   UnapprovedFirstArt:boolean,
   EnableLaborQty:boolean,
   EnableComplete:boolean,
   EnableScrapQty:boolean,
   EnableDiscrepQty:boolean,
   PrintNCTag:boolean,
      /**  calculated field: LaborHrs * LaborRate  */  
   LaborCost:number,
      /**  calculated field: BurdenHrs * BurdenRate  */  
   BurdenCost:number,
   DtClockIn:string,
   DtClockOut:string,
   CapabilityID:string,
   CapabilityDescription:string,
   MultipleEmployeesText:string,
   StartActivity:boolean,
      /**  GL Journal Source Transaction Date  */  
   GLTranDate:string,
      /**  GL Journal Source Transaction Amount  */  
   GLTranAmt:number,
      /**  Labor Detail Employee Name  */  
   EmployeeName:string,
      /**  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  */  
   EfficiencyPercentage:number,
   JCSystReworkReasons:boolean,
   ResourceDesc:string,
      /**  Unit of Measure used for DiscrepQty  */  
   DiscrepUOM:string,
      /**  Unit of Measure used for LaborQty  */  
   LaborUOM:string,
      /**  Unit of Measure used for ScrapQty.  */  
   ScrapUOM:string,
      /**  Enable the SN Button?  */  
   EnableSN:boolean,
      /**  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  */  
   PhaseOprSeq:number,
      /**  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  */  
   PhaseJobNum:string,
      /**  Field that indicates if field PrjRoleCd should be disabled.  */  
   DisPrjRoleCd:boolean,
      /**  Field that indicates if field TimeTypCd should be disabled.  */  
   DisTimeTypCd:boolean,
      /**  Field that indicates if field DisLaborTypeshould be disabled.  */  
   DisLaborType:boolean,
      /**  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  */  
   NewPrjRoleCd:string,
      /**  Holds the description for NewPrjRoleCd  */  
   NewRoleCdDesc:string,
      /**  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  */  
   JobTypeCode:string,
   PrjUsedTran:string,
   PBAllowModify:boolean,
   ApprovedBy:string,
   PendingApprovalBy:string,
   TreeNodeImageName:string,
   EnableInspection:boolean,
      /**  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  */  
   LbrDay:string,
      /**  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  */  
   LbrMonth:string,
      /**  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  */  
   LbrWeek:string,
      /**  Company Base currency code description for display in LaborDtl grid.  */  
   BaseCurrCodeDesc:string,
      /**  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  */  
   ChgRateCurrDesc:string,
      /**  Charge rate calculated for Time and Expense approval  */  
   ChargeRate:number,
      /**  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  */  
   ChargeRateSRC:string,
      /**  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalProjectID:string,
      /**  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalProjectDesc:string,
   DspCreateTime:string,
   DspChangeTime:string,
      /**  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalPhaseID:string,
      /**  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalPhaseDesc:string,
   WeekDisplayText:string,
   NotSubmitted:boolean,
   TimeDisableUpdate:boolean,
   TimeDisableDelete:boolean,
   RoleCdDisplayAll:boolean,
      /**  Indicates if the user has access to the row  */  
   HasAccessToRow:boolean,
      /**  Indicates if the submit button is enabled  */  
   EnableSubmit:boolean,
      /**  Indicates if the recall button is enabled  */  
   EnableRecall:boolean,
      /**  Indicates if the copy button is enabled  */  
   EnableCopy:boolean,
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   AllowDirLbr:boolean,
   MES:boolean,
      /**  Indicates if recall is available for an approver  */  
   EnableRecallAprv:boolean,
      /**  Used in approval entry.  Indicates if the approver has an open task or not.  */  
   ApprvrHasOpenTask:boolean,
      /**  To know if the LaborDtl was created on the current plant  */  
   EnteredOnCurPlant:boolean,
      /**  Full description of Reason... used on displays/reports.  */  
   DiscrpRsnDescription:string,
      /**  First name of employee.  */  
   EmpBasicFirstName:string,
      /**  Last name of employee  */  
   EmpBasicLastName:string,
      /**  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  */  
   EmpBasicName:string,
      /**  Full description of the Labor Expense Code master.  */  
   ExpenseCodeDescription:string,
      /**  Full description of the Indirect Labor.  */  
   IndirectDescription:string,
      /**  Job Costing department description.  */  
   JCDeptDescription:string,
      /**  Full description of Resource.  */  
   MachineDescription:string,
      /**  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  */  
   OpCodeOpDesc:string,
      /**   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  */  
   PayMethodSummarizePerCustomer:boolean,
      /**  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  */  
   PayMethodType:number,
      /**  Name of the payment method  */  
   PayMethodName:string,
      /**  Description  */  
   PhaseIDDescription:string,
      /**  Full description of Project Management Code.  */  
   ProjectDescription:string,
      /**  Long description of the Resource Group.  */  
   ResourceGrpDescription:string,
      /**  Full description of Reason... used on displays/reports.  */  
   ResReasonDescription:string,
      /**  Full description of Reason... used on displays/reports.  */  
   ReWorkReasonDescription:string,
      /**  A description of the role.  */  
   RoleCdRoleDescription:string,
      /**  Full description of Reason... used on displays/reports.  */  
   ScrapReasonDescription:string,
      /**  A concatenation of Start + End time.  */  
   ShiftDescription:string,
      /**  The description of the Time Type Code  */  
   TimeTypCdDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LaborDtlListTableset{
   LaborDtlList:Erp_Tablesets_LaborDtlListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LaborDtlRow{
      /**  Company Identifier.  */  
   Company:string,
      /**   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  */  
   EmployeeNum:string,
      /**  Used as the foreign key to the LaborHed record.  */  
   LaborHedSeq:number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   LaborDtlSeq:number,
      /**   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   LaborType:string,
      /**   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  */  
   LaborTypePseudo:string,
      /**  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  */  
   ReWork:boolean,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  */  
   ReworkReasonCode:string,
      /**  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  */  
   JobNum:string,
      /**  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  */  
   AssemblySeq:number,
      /**   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  */  
   OprSeq:number,
      /**  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  */  
   JCDept:string,
      /**   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  */  
   ResourceGrpID:string,
      /**  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  */  
   OpCode:string,
      /**  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  */  
   LaborHrs:number,
      /**  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  */  
   BurdenHrs:number,
      /**  The Total production quantity reported.  */  
   LaborQty:number,
      /**  The reported scrap quantity.  */  
   ScrapQty:number,
      /**   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  */  
   ScrapReasonCode:string,
      /**  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  */  
   SetupPctComplete:number,
      /**  Indicates if this transaction "completes" either the setup or production for this operation.  */  
   Complete:boolean,
      /**  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  */  
   IndirectCode:string,
      /**  A short note that the user can make about the labor transaction.  */  
   LaborNote:string,
      /**  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  */  
   ExpenseCode:string,
      /**  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  */  
   LaborCollection:boolean,
      /**  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  */  
   AppliedToSchedule:boolean,
      /**  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  */  
   ClockInMInute:number,
      /**  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  */  
   ClockOutMinute:number,
      /**  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  */  
   ClockInDate:string,
      /**   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  */  
   ClockinTime:number,
      /**   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  */  
   ClockOutTime:number,
      /**   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  */  
   ActiveTrans:boolean,
      /**  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  */  
   OverRidePayRate:number,
      /**  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  */  
   LaborRate:number,
      /**  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  */  
   BurdenRate:number,
      /**  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockInTime:string,
      /**  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  */  
   DspClockOutTime:string,
      /**  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  */  
   ResourceID:string,
      /**  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  */  
   OpComplete:boolean,
      /**  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  */  
   EarnedHrs:number,
      /**  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  */  
   AddedOper:boolean,
      /**  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  */  
   PayrollDate:string,
      /**   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  */  
   PostedToGL:boolean,
      /**   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  */  
   FiscalYear:number,
      /**   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  */  
   FiscalPeriod:number,
      /**   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  */  
   JournalNum:number,
      /**  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  */  
   GLTrans:boolean,
      /**  Journal Code of the related GLJrnDtl.  */  
   JournalCode:string,
      /**  Indicates if the labordtl record inspection has completed.  */  
   InspectionPending:boolean,
      /**  The service call that this service record belongs to.  */  
   CallNum:number,
      /**  The line number of the service call this labor detail is for.  */  
   CallLine:number,
      /**  the service that is being performed on this line.  */  
   ServNum:number,
      /**  A unique code that identifies the Service  */  
   ServCode:string,
      /**  Problem reason code from the reason master table. type Service call.  */  
   ResReasonCode:string,
      /**  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  */  
   WipPosted:boolean,
      /**  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  */  
   DiscrepQty:number,
      /**   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  */  
   DiscrpRsnCode:string,
      /**  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  */  
   ParentLaborDtlSeq:number,
      /**  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  */  
   LaborEntryMethod:string,
      /**  Fiscal year suffix.  */  
   FiscalYearSuffix:string,
      /**  The fiscal calendar year/suffix/period were derived from.  */  
   FiscalCalendarID:string,
      /**  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  */  
   BFLaborReq:boolean,
      /**  Reference to the ABT, it is GUID,used in PostingEngine  */  
   ABTUID:string,
      /**  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  */  
   ProjectID:string,
      /**  Project Phase ID  */  
   PhaseID:string,
      /**  Project Role Code  */  
   RoleCd:string,
      /**  Time Type Code  */  
   TimeTypCd:string,
      /**  The Project Billing Invoice Number where these charges were processed.  */  
   PBInvNum:number,
      /**  The payment method of the time.  */  
   PMUID:number,
      /**  Link to Task set  */  
   TaskSetID:string,
      /**  The date the time received final approval.  */  
   ApprovedDate:string,
      /**  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  */  
   ClaimRef:string,
      /**  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  */  
   QuickEntryCode:string,
      /**   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  */  
   TimeStatus:string,
      /**  Userid of the user who created the record.  */  
   CreatedBy:string,
      /**  The date the record was created.  */  
   CreateDate:string,
      /**  The time the record was created (in seconds since midnight)  */  
   CreateTime:number,
      /**  Userid of the user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date the record was last changed.  */  
   ChangeDate:string,
      /**  The time the record was last changed (in seconds since midnight)  */  
   ChangeTime:number,
      /**  The Currently active Stage changing task  */  
   ActiveTaskID:string,
      /**  The Last Complete Milestone task  */  
   LastTaskID:string,
      /**  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  */  
   CreatedViaTEWeekView:boolean,
      /**  The identifier of the workflow stage.  */  
   CurrentWFStageID:string,
      /**  The identifier of the workflow group  */  
   WFGroupID:string,
      /**  This indicates if the workflow for this group is complete.  */  
   WFComplete:boolean,
      /**  Indicates if approval is required for this transaction.  */  
   ApprovalRequired:boolean,
      /**  The User ID of the submitter.  */  
   SubmittedBy:string,
      /**  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  */  
   PBRateFrom:string,
      /**  Project Billing calculation in COSandWIP: Currency code is got from Project  */  
   PBCurrencyCode:string,
      /**  Project Billing calculation in COSandWIP: Hours used for charge  */  
   PBHours:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  */  
   PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  */  
   PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  */  
   DocPBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt1PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt2PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  */  
   Rpt3PBChargeRate:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  */  
   DocPBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt1PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt2PBChargeAmt:number,
      /**  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  */  
   Rpt3PBChargeAmt:number,
      /**  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  */  
   Shift:number,
      /**  Links to PActDtl.ActID  */  
   ActID:number,
      /**  System assigned unique id number for the detail. Links to PActDtl.DetailID  */  
   DtailID:number,
      /**  Logical field to indicate if this record has been read by project analysis process.  */  
   ProjProcessed:boolean,
      /**  Used By Project Analysis Process.  */  
   AsOfDate:string,
      /**  Used By Project Analysis Process.  */  
   AsOfSeq:number,
      /**  JDFInputFiles  */  
   JDFInputFiles:string,
      /**  JDFNumberOfPages  */  
   JDFNumberOfPages:string,
      /**  BatchWasSaved  */  
   BatchWasSaved:string,
      /**  AssignToBatch  */  
   AssignToBatch:boolean,
      /**  BatchComplete  */  
   BatchComplete:boolean,
      /**  BatchRequestMove  */  
   BatchRequestMove:boolean,
      /**  BatchPrint  */  
   BatchPrint:boolean,
      /**  BatchLaborHrs  */  
   BatchLaborHrs:number,
      /**  BatchPctOfTotHrs  */  
   BatchPctOfTotHrs:number,
      /**  BatchQty  */  
   BatchQty:number,
      /**  BatchTotalExpectedHrs  */  
   BatchTotalExpectedHrs:number,
      /**  JDFOpCompleted  */  
   JDFOpCompleted:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Downtime  */  
   Downtime:boolean,
      /**  RefJobNum  */  
   RefJobNum:string,
      /**  RefAssemblySeq  */  
   RefAssemblySeq:number,
      /**  RefOprSeq  */  
   RefOprSeq:number,
      /**  Imported  */  
   Imported:boolean,
      /**  ImportDate  */  
   ImportDate:string,
      /**   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  */  
   TimeAutoSubmit:boolean,
      /**  BatchMode  */  
   BatchMode:boolean,
      /**  BillServiceRate  */  
   BillServiceRate:number,
      /**  Pay Hours used for HCM  */  
   HCMPayHours:number,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  */  
   DiscrepAttributeSetID:number,
      /**  The unique identifier of the related Dynamic Attribute Set for the Labor Qty  */  
   LaborAttributeSetID:number,
      /**  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  */  
   ScrapAttributeSetID:number,
      /**  PCID  */  
   PCID:string,
      /**  NonConfPCID  */  
   NonConfPCID:string,
      /**  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  */  
   AllowDirLbr:boolean,
      /**  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalPhaseDesc:string,
      /**  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalPhaseID:string,
      /**  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalProjectDesc:string,
      /**  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  */  
   ApprovalProjectID:string,
   ApprovedBy:string,
      /**  Used in approval entry.  Indicates if the approver has an open task or not.  */  
   ApprvrHasOpenTask:boolean,
      /**  Company Base currency code description for display in LaborDtl grid.  */  
   BaseCurrCodeDesc:string,
      /**  calculated field: BurdenHrs * BurdenRate  */  
   BurdenCost:number,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   CallCode:string,
   CapabilityDescription:string,
   CapabilityID:string,
      /**  Charge rate calculated for Time and Expense approval  */  
   ChargeRate:number,
      /**  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  */  
   ChargeRateSRC:string,
      /**  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  */  
   ChgRateCurrDesc:string,
   CompleteFlag:boolean,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   ContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   ContractNum:number,
      /**  Unit of Measure used for DiscrepQty  */  
   DiscrepUOM:string,
      /**  Field that indicates if field DisLaborTypeshould be disabled.  */  
   DisLaborType:boolean,
   DisplayJob:string,
      /**  Field that indicates if field PrjRoleCd should be disabled.  */  
   DisPrjRoleCd:boolean,
      /**  Field that indicates if field TimeTypCd should be disabled.  */  
   DisTimeTypCd:boolean,
   DowntimeTotal:number,
   DspChangeTime:string,
   DspCreateTime:string,
   DspTotHours:string,
   DtClockIn:string,
   DtClockOut:string,
      /**  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  */  
   EfficiencyPercentage:number,
      /**  Labor Detail Employee Name  */  
   EmployeeName:string,
   EnableComplete:boolean,
      /**  Indicates if the copy button is enabled  */  
   EnableCopy:boolean,
   EnableDiscrepQty:boolean,
   EnableInspection:boolean,
   EnableLaborQty:boolean,
   EnableNextOprSeq:boolean,
   EnablePrintTagsList:boolean,
      /**  Indicates if the recall button is enabled  */  
   EnableRecall:boolean,
      /**  Indicates if recall is available for an approver  */  
   EnableRecallAprv:boolean,
   EnableRequestMove:boolean,
   EnableResourceGrpID:boolean,
   EnableScrapQty:boolean,
      /**  Enable the SN Button?  */  
   EnableSN:boolean,
      /**  Indicates if the submit button is enabled  */  
   EnableSubmit:boolean,
   EndActivity:boolean,
      /**  To know if the LaborDtl was created on the current plant  */  
   EnteredOnCurPlant:boolean,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   FSACallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   FSAContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   FSAContractNum:number,
      /**  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  */  
   FSAEmpID:string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  */  
   FSAWarrantyCode:string,
   FSComplete:boolean,
      /**  GL Journal Source Transaction Amount  */  
   GLTranAmt:number,
      /**  GL Journal Source Transaction Date  */  
   GLTranDate:string,
      /**  Indicates if the user has access to the row  */  
   HasAccessToRow:boolean,
      /**  Indicates if the labor detail has comments  */  
   HasComments:boolean,
      /**  To tell the bo that this transaction was being modified from HH.  */  
   HH:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  Indicates if the job operation is marked as fixed hours and quantity only.  */  
   ISFixHourAndQtyOnly:boolean,
   JCSystReworkReasons:boolean,
   JCSystScrapReasons:boolean,
   JobOperComplete:boolean,
   JobType:string,
      /**  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  */  
   JobTypeCode:string,
      /**  calculated field: LaborHrs * LaborRate  */  
   LaborCost:number,
      /**  Unit of Measure used for LaborQty  */  
   LaborUOM:string,
      /**  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  */  
   LbrDay:string,
      /**  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  */  
   LbrMonth:string,
      /**  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  */  
   LbrWeek:string,
   MES:boolean,
   MultipleEmployeesText:string,
   NewDifDateFlag:number,
      /**  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  */  
   NewPrjRoleCd:string,
      /**  Holds the description for NewPrjRoleCd  */  
   NewRoleCdDesc:string,
   NextAssemblySeq:number,
   NextOperDesc:string,
   NextOprSeq:number,
   NextResourceDesc:string,
      /**  To evaluate if the NonComformance has been already processed in inspection and no changes can be applied on LaborDtl then.  */  
   NonConfProcessed:boolean,
   NotSubmitted:boolean,
      /**  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  */  
   OkToChangeResourceGrpID:boolean,
   PartDescription:string,
   PartNum:string,
   PBAllowModify:boolean,
   PendingApprovalBy:string,
      /**  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  */  
   PhaseJobNum:string,
      /**  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  */  
   PhaseOprSeq:number,
   PrintNCTag:boolean,
   PrjUsedTran:string,
   ProdDesc:string,
   ProjPhaseID:string,
   RequestMove:boolean,
   ResourceDesc:string,
   RoleCdDisplayAll:boolean,
      /**  Unit of Measure used for ScrapQty.  */  
   ScrapUOM:string,
      /**  Flag field to identify if the row is being sent from MES  */  
   SentFromMES:boolean,
   StartActivity:boolean,
   TimeDisableDelete:boolean,
   TimeDisableUpdate:boolean,
   TreeNodeImageName:string,
   UnapprovedFirstArt:boolean,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   WarrantyCode:string,
   WeekDisplayText:string,
      /**  EnablePCID  */  
   EnablePCID:boolean,
      /**  The output bin from the resource  */  
   OutputBin:string,
      /**  The output warehouse from the resource  */  
   OutputWarehouse:string,
      /**  Internal flag used for the row rules to control whether the Lot columns should be enabled.  */  
   EnableLot:boolean,
      /**  Lot number that is to be added to the PCID  */  
   LotNum:string,
      /**  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  */  
   PrintPCIDContents:boolean,
      /**  Indicates if the labor detail has attachments  */  
   HasAttachments:boolean,
   AttrClassID:string,
      /**  The Full Description of the Attribute Set for DiscrepQty  */  
   DiscrepAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set for DiscrepQty  */  
   DiscrepAttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set for ScrapQty  */  
   ScrapAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set for ScrapQty  */  
   ScrapAttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set for LaborQty  */  
   LaborAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set for LaborQty  */  
   LaborAttributeSetShortDescription:string,
      /**  Indicates if recall and delete should be disabled  */  
   DisableRecallAndDelete:boolean,
      /**  List of available role codes  */  
   RoleCdList:string,
      /**  Indicates if the row is selected for submit, recall, or copy  */  
   RowSelected:boolean,
      /**  Start date/time for calendar appoinment  */  
   AppointmentStart:string,
      /**  End date/time for calendar appoinment  */  
   AppointmentEnd:string,
      /**  Title to display for the calendar appointment  */  
   AppointmentTitle:string,
      /**  PDF Form Template linked to the Job Operation  */  
   TemplateID:string,
      /**  Flag to validate if the transaction includes WIP  */  
   WIPTransaction:boolean,
      /**  Revision for DiscrepQty  */  
   DiscrepRevision:string,
      /**  Revision for LaborQty  */  
   LaborRevision:string,
      /**  Revision for ScrapQty  */  
   ScrapRevision:string,
   TrackInventoryByRevision:boolean,
      /**  Indicates whether co-parts can be entered  */  
   ReportPartQtyAllowed:boolean,
   BitFlag:number,
   DiscrpRsnDescription:string,
   EmpBasicLastName:string,
   EmpBasicFirstName:string,
   EmpBasicName:string,
   ExpenseCodeDescription:string,
   HCMIntregationHCMEnabled:boolean,
   HCMStatusStatus:string,
   IndirectDescription:string,
   JCDeptDescription:string,
   JobAsmblPartNum:string,
   JobAsmblDescription:string,
   MachineDescription:string,
   OpCodeOpDesc:string,
   OpDescOpDesc:string,
   PayMethodType:number,
   PayMethodSummarizePerCustomer:boolean,
   PayMethodName:string,
   PhaseIDDescription:string,
   ProjectDescription:string,
   ResourceGrpDescription:string,
   ResReasonDescription:string,
   ReWorkReasonDescription:string,
   RoleCdRoleDescription:string,
   ScrapReasonDescription:string,
   ShiftDescription:string,
   TimeTypCdDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LbrPrjRoleTableset{
   LaborDtl:Erp_Tablesets_LaborDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtLbrPrjRoleTableset{
   LaborDtl:Erp_Tablesets_LaborDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param laborHedSeq
      @param laborDtlSeq
   */  
export interface GetByID_input{
   laborHedSeq:number,
   laborDtlSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_LbrPrjRoleTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_LbrPrjRoleTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_LbrPrjRoleTableset[],
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
   returnObj:Erp_Tablesets_LaborDtlListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param laborHedSeq
   */  
export interface GetNewLaborDtl_input{
   ds:Erp_Tablesets_LbrPrjRoleTableset[],
   laborHedSeq:number,
}

export interface GetNewLaborDtl_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LbrPrjRoleTableset[],
}
}

   /** Required : 
      @param whereClauseLaborDtl
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseLaborDtl:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_LbrPrjRoleTableset[],
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
      @param ipNewPrjRoleCd
      @param ds
   */  
export interface OnChangeNewPrjRoleCd_input{
      /**  The NewPrjRoleCd value.  */  
   ipNewPrjRoleCd:string,
   ds:Erp_Tablesets_LbrPrjRoleTableset[],
}

export interface OnChangeNewPrjRoleCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LbrPrjRoleTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtLbrPrjRoleTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtLbrPrjRoleTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface UpdatePrjRoleCd_input{
   ds:Erp_Tablesets_LbrPrjRoleTableset[],
}

export interface UpdatePrjRoleCd_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LbrPrjRoleTableset[],
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_LbrPrjRoleTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_LbrPrjRoleTableset[],
}
}

