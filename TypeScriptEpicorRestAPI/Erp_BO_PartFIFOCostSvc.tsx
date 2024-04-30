import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PartFIFOCostSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/$metadata", {
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
   Description: Get PartFIFOCosts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartFIFOCosts
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartFIFOCostRow
   */  
export function get_PartFIFOCosts(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartFIFOCostRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/PartFIFOCosts", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartFIFOCostRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartFIFOCosts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartFIFOCostRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PartFIFOCostRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartFIFOCosts(requestBody:Erp_Tablesets_PartFIFOCostRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/PartFIFOCosts", {
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
   Summary: Calls GetByID to retrieve the PartFIFOCost item
   Description: Calls GetByID to retrieve the PartFIFOCost item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartFIFOCost
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param CostID Desc: CostID   Required: True   Allow empty value : True
      @param FIFODate Desc: FIFODate   Required: True   Allow empty value : True
      @param FIFOSeq Desc: FIFOSeq   Required: True
      @param FIFOSubSeq Desc: FIFOSubSeq   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PartFIFOCostRow
   */  
export function get_PartFIFOCosts_Company_PartNum_LotNum_CostID_FIFODate_FIFOSeq_FIFOSubSeq(Company:string, PartNum:string, LotNum:string, CostID:string, FIFODate:string, FIFOSeq:string, FIFOSubSeq:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartFIFOCostRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/PartFIFOCosts(" + Company + "," + PartNum + "," + LotNum + "," + CostID + "," + FIFODate + "," + FIFOSeq + "," + FIFOSubSeq + ")", {
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
         resolve(data as Erp_Tablesets_PartFIFOCostRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartFIFOCost for the service
   Description: Calls UpdateExt to update PartFIFOCost. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartFIFOCost
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param CostID Desc: CostID   Required: True   Allow empty value : True
      @param FIFODate Desc: FIFODate   Required: True   Allow empty value : True
      @param FIFOSeq Desc: FIFOSeq   Required: True
      @param FIFOSubSeq Desc: FIFOSubSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartFIFOCostRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartFIFOCosts_Company_PartNum_LotNum_CostID_FIFODate_FIFOSeq_FIFOSubSeq(Company:string, PartNum:string, LotNum:string, CostID:string, FIFODate:string, FIFOSeq:string, FIFOSubSeq:string, requestBody:Erp_Tablesets_PartFIFOCostRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/PartFIFOCosts(" + Company + "," + PartNum + "," + LotNum + "," + CostID + "," + FIFODate + "," + FIFOSeq + "," + FIFOSubSeq + ")", {
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
   Summary: Call UpdateExt to delete PartFIFOCost item
   Description: Call UpdateExt to delete PartFIFOCost item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartFIFOCost
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PartNum Desc: PartNum   Required: True   Allow empty value : True
      @param LotNum Desc: LotNum   Required: True   Allow empty value : True
      @param CostID Desc: CostID   Required: True   Allow empty value : True
      @param FIFODate Desc: FIFODate   Required: True   Allow empty value : True
      @param FIFOSeq Desc: FIFOSeq   Required: True
      @param FIFOSubSeq Desc: FIFOSubSeq   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartFIFOCosts_Company_PartNum_LotNum_CostID_FIFODate_FIFOSeq_FIFOSubSeq(Company:string, PartNum:string, LotNum:string, CostID:string, FIFODate:string, FIFOSeq:string, FIFOSubSeq:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/PartFIFOCosts(" + Company + "," + PartNum + "," + LotNum + "," + CostID + "," + FIFODate + "," + FIFOSeq + "," + FIFOSubSeq + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartFIFOCostListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartFIFOCostListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartFIFOCostListRow)
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
export function get_GetRows(whereClausePartFIFOCost:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartFIFOCost!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartFIFOCost=" + whereClausePartFIFOCost
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/GetRows" + params, {
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(partNum:string, lotNum:string, costID:string, fiFODate:string, fiFOSeq:string, fiFOSubSeq:string, epicorHeaders?:Headers){
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
   if(typeof lotNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "lotNum=" + lotNum
   }
   if(typeof costID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "costID=" + costID
   }
   if(typeof fiFODate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fiFODate=" + fiFODate
   }
   if(typeof fiFOSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fiFOSeq=" + fiFOSeq
   }
   if(typeof fiFOSubSeq!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "fiFOSubSeq=" + fiFOSubSeq
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/GetList" + params, {
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
   Summary: Invoke method GetNewPartFIFOCost
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartFIFOCost
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPartFIFOCost_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartFIFOCost_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartFIFOCost(requestBody:GetNewPartFIFOCost_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPartFIFOCost_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/GetNewPartFIFOCost", {
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
         resolve(data as GetNewPartFIFOCost_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartFIFOCostSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartFIFOCostListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartFIFOCostListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartFIFOCostRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartFIFOCostRow,
}

export interface Erp_Tablesets_PartFIFOCostListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Unique lot number for the part.  */  
   "LotNum":string,
      /**  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  */  
   "CostID":string,
      /**  This could be the transaction date or the system date at the time this FIFO cost record was created.  Depending on the setting at Company Configuration (XbSyst.UseTranDate).  */  
   "FIFODate":string,
      /**  A number which is used to allow create a unique key for the file.  */  
   "FIFOSeq":number,
      /**  A subsequence number which is used to create a unique FIFO Sequence within the same FIFO Date.  */  
   "FIFOSubSeq":number,
      /**   Flag which indicates if the Part FIFO cost queue is considered as "Inactive".  This flag will be used to exclude FIFO from the queue of valid FIFO costs.
This flag will be used to exclude parts from certain searches and reports.  */  
   "InActive":boolean,
      /**  Holds the Quantity On Hand for this Part FIFO cost queue.  Whenever this quantity becomes zero the record should be deactivated.  This quantity is updated by Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse transfers, Shipping and Adjustments.  */  
   "OnHandQty":number,
      /**   FIFO Unit Labor Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   "FIFOLaborCost":number,
      /**   FIFO Unit Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   "FIFOBurdenCost":number,
      /**   FIFO Unit Material Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   "FIFOMaterialCost":number,
      /**   FIFO Unit Subcontract Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   "FIFOSubContCost":number,
      /**   FIFO Unit Material Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   "FIFOMtlBurCost":number,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  An internal code to identify the source transaction that created this FIFO cost queue.  To make it match with the source PartTran that created it, SourceType will have the same value as the source transaction type if part's cost method is FIFO or LOT FIFO.  But if the source is a non-FIFO part and FIFO Layer is enabled then Source Type is "NON-FIFO":U.  */  
   "SourceType":string,
      /**  System date of the source PartTran that created this FIFO cost queue record.  */  
   "SourceSysDate":string,
      /**  System Time (hr-min-sec) of the source PartTran that created this FIFO cost queue record.  */  
   "SourceSysTime":number,
      /**  The Transaction number of the source PartTran that created this FIFO cost queue record.  */  
   "SourceTranNum":number,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   "VendorNum":number,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   "PurPoint":string,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   "PackSlip":string,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   "PackLine":number,
      /**  Holds the original Quantity On Hand of the Part FIFO cost when first created.  */  
   "OrigOnHandQty":number,
      /**  Holds the quantity consumed from this Part FIFO cost queue.  This quantity plus the OnHand quantity will equal the OrigOnHandQty in most cases.  But in the event where the FIFO cost queue is deactivated due to backing out of the transaction then the OrigOnHandQty and OnHandQty are set to zero but ConsumedQty retains its value.  */  
   "ConsumedQty":number,
      /**  Latest date that the FIFO cost record was referenced.  */  
   "LastRefDate":string,
      /**  Identifies the transaction file that created this FIFO cost.  */  
   "SourceTable":string,
      /**  First component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   "SourceKey1":string,
      /**  2nd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   "SourceKey2":string,
      /**  3rd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   "SourceKey3":string,
      /**  4th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   "SourceKey4":string,
      /**  5th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   "SourceKey5":string,
      /**  6th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   "SourceKey6":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartFIFOCostRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  A unique part number that identifies this part.  */  
   "PartNum":string,
      /**  Unique lot number for the part.  */  
   "LotNum":string,
      /**  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  */  
   "CostID":string,
      /**  This could be the transaction date or the system date at the time this FIFO cost record was created.  Depending on the setting at Company Configuration (XbSyst.UseTranDate).  */  
   "FIFODate":string,
      /**  A number which is used to allow create a unique key for the file.  */  
   "FIFOSeq":number,
      /**  A subsequence number which is used to create a unique FIFO Sequence within the same FIFO Date.  */  
   "FIFOSubSeq":number,
      /**   Flag which indicates if the Part FIFO cost queue is considered as "Inactive".  This flag will be used to exclude FIFO from the queue of valid FIFO costs.
This flag will be used to exclude parts from certain searches and reports.  */  
   "InActive":boolean,
      /**  Holds the Quantity On Hand for this Part FIFO cost queue.  Whenever this quantity becomes zero the record should be deactivated.  This quantity is updated by Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse transfers, Shipping and Adjustments.  */  
   "OnHandQty":number,
      /**   FIFO Unit Labor Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   "FIFOLaborCost":number,
      /**   FIFO Unit Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   "FIFOBurdenCost":number,
      /**   FIFO Unit Material Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   "FIFOMaterialCost":number,
      /**   FIFO Unit Subcontract Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   "FIFOSubContCost":number,
      /**   FIFO Unit Material Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   "FIFOMtlBurCost":number,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  An internal code to identify the source transaction that created this FIFO cost queue.  To make it match with the source PartTran that created it, SourceType will have the same value as the source transaction type if part's cost method is FIFO or LOT FIFO.  But if the source is a non-FIFO part and FIFO Layer is enabled then Source Type is "NON-FIFO":U.  */  
   "SourceType":string,
      /**  System date of the source PartTran that created this FIFO cost queue record.  */  
   "SourceSysDate":string,
      /**  System Time (hr-min-sec) of the source PartTran that created this FIFO cost queue record.  */  
   "SourceSysTime":number,
      /**  The Transaction number of the source PartTran that created this FIFO cost queue record.  */  
   "SourceTranNum":number,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   "VendorNum":number,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   "PurPoint":string,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   "PackSlip":string,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   "PackLine":number,
      /**  Holds the original Quantity On Hand of the Part FIFO cost when first created.  */  
   "OrigOnHandQty":number,
      /**  Holds the quantity consumed from this Part FIFO cost queue.  This quantity plus the OnHand quantity will equal the OrigOnHandQty in most cases.  But in the event where the FIFO cost queue is deactivated due to backing out of the transaction then the OrigOnHandQty and OnHandQty are set to zero but ConsumedQty retains its value.  */  
   "ConsumedQty":number,
      /**  Latest date that the FIFO cost record was referenced.  */  
   "LastRefDate":string,
      /**  Identifies the transaction file that created this FIFO cost.  */  
   "SourceTable":string,
      /**  First component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   "SourceKey1":string,
      /**  2nd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   "SourceKey2":string,
      /**  3rd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   "SourceKey3":string,
      /**  4th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   "SourceKey4":string,
      /**  5th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   "SourceKey5":string,
      /**  6th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   "SourceKey6":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "PartTranExtNonRecoverableCost":number,
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
      @param partNum
      @param lotNum
      @param costID
      @param fiFODate
      @param fiFOSeq
      @param fiFOSubSeq
   */  
export interface DeleteByID_input{
   partNum:string,
   lotNum:string,
   costID:string,
   fiFODate:string,
   fiFOSeq:number,
   fiFOSubSeq:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PartFIFOCostListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  */  
   CostID:string,
      /**  This could be the transaction date or the system date at the time this FIFO cost record was created.  Depending on the setting at Company Configuration (XbSyst.UseTranDate).  */  
   FIFODate:string,
      /**  A number which is used to allow create a unique key for the file.  */  
   FIFOSeq:number,
      /**  A subsequence number which is used to create a unique FIFO Sequence within the same FIFO Date.  */  
   FIFOSubSeq:number,
      /**   Flag which indicates if the Part FIFO cost queue is considered as "Inactive".  This flag will be used to exclude FIFO from the queue of valid FIFO costs.
This flag will be used to exclude parts from certain searches and reports.  */  
   InActive:boolean,
      /**  Holds the Quantity On Hand for this Part FIFO cost queue.  Whenever this quantity becomes zero the record should be deactivated.  This quantity is updated by Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse transfers, Shipping and Adjustments.  */  
   OnHandQty:number,
      /**   FIFO Unit Labor Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   FIFOLaborCost:number,
      /**   FIFO Unit Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   FIFOBurdenCost:number,
      /**   FIFO Unit Material Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   FIFOMaterialCost:number,
      /**   FIFO Unit Subcontract Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   FIFOSubContCost:number,
      /**   FIFO Unit Material Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   FIFOMtlBurCost:number,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  An internal code to identify the source transaction that created this FIFO cost queue.  To make it match with the source PartTran that created it, SourceType will have the same value as the source transaction type if part's cost method is FIFO or LOT FIFO.  But if the source is a non-FIFO part and FIFO Layer is enabled then Source Type is "NON-FIFO":U.  */  
   SourceType:string,
      /**  System date of the source PartTran that created this FIFO cost queue record.  */  
   SourceSysDate:string,
      /**  System Time (hr-min-sec) of the source PartTran that created this FIFO cost queue record.  */  
   SourceSysTime:number,
      /**  The Transaction number of the source PartTran that created this FIFO cost queue record.  */  
   SourceTranNum:number,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   VendorNum:number,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   PurPoint:string,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   PackSlip:string,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   PackLine:number,
      /**  Holds the original Quantity On Hand of the Part FIFO cost when first created.  */  
   OrigOnHandQty:number,
      /**  Holds the quantity consumed from this Part FIFO cost queue.  This quantity plus the OnHand quantity will equal the OrigOnHandQty in most cases.  But in the event where the FIFO cost queue is deactivated due to backing out of the transaction then the OrigOnHandQty and OnHandQty are set to zero but ConsumedQty retains its value.  */  
   ConsumedQty:number,
      /**  Latest date that the FIFO cost record was referenced.  */  
   LastRefDate:string,
      /**  Identifies the transaction file that created this FIFO cost.  */  
   SourceTable:string,
      /**  First component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   SourceKey1:string,
      /**  2nd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   SourceKey2:string,
      /**  3rd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   SourceKey3:string,
      /**  4th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   SourceKey4:string,
      /**  5th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   SourceKey5:string,
      /**  6th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   SourceKey6:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartFIFOCostListTableset{
   PartFIFOCostList:Erp_Tablesets_PartFIFOCostListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartFIFOCostRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  A unique part number that identifies this part.  */  
   PartNum:string,
      /**  Unique lot number for the part.  */  
   LotNum:string,
      /**  Included in the unique index this value allows the Part to have different costs in different Sites.  Default value for CostID = 1.  */  
   CostID:string,
      /**  This could be the transaction date or the system date at the time this FIFO cost record was created.  Depending on the setting at Company Configuration (XbSyst.UseTranDate).  */  
   FIFODate:string,
      /**  A number which is used to allow create a unique key for the file.  */  
   FIFOSeq:number,
      /**  A subsequence number which is used to create a unique FIFO Sequence within the same FIFO Date.  */  
   FIFOSubSeq:number,
      /**   Flag which indicates if the Part FIFO cost queue is considered as "Inactive".  This flag will be used to exclude FIFO from the queue of valid FIFO costs.
This flag will be used to exclude parts from certain searches and reports.  */  
   InActive:boolean,
      /**  Holds the Quantity On Hand for this Part FIFO cost queue.  Whenever this quantity becomes zero the record should be deactivated.  This quantity is updated by Manufactured receipts, Purchased receipts, Physical inventories, Inventory issues, Warehouse transfers, Shipping and Adjustments.  */  
   OnHandQty:number,
      /**   FIFO Unit Labor Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   FIFOLaborCost:number,
      /**   FIFO Unit Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   FIFOBurdenCost:number,
      /**   FIFO Unit Material Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   FIFOMaterialCost:number,
      /**   FIFO Unit Subcontract Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   FIFOSubContCost:number,
      /**   FIFO Unit Material Burden Cost of the Part. This is updated by Cost Adjustment, Manufacture receipts and Purchased Part receipts. GENERAL NOTES ABOUT UNIT COSTS:
The system is configurable to use either Average, Standard, Last or FIFO unit cost.  This configuration option can be set per individual Part. 
Also both the Average and Last Unit costs are updated during inventory receipts regardless of the Costing method specified.  */  
   FIFOMtlBurCost:number,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  An internal code to identify the source transaction that created this FIFO cost queue.  To make it match with the source PartTran that created it, SourceType will have the same value as the source transaction type if part's cost method is FIFO or LOT FIFO.  But if the source is a non-FIFO part and FIFO Layer is enabled then Source Type is "NON-FIFO":U.  */  
   SourceType:string,
      /**  System date of the source PartTran that created this FIFO cost queue record.  */  
   SourceSysDate:string,
      /**  System Time (hr-min-sec) of the source PartTran that created this FIFO cost queue record.  */  
   SourceSysTime:number,
      /**  The Transaction number of the source PartTran that created this FIFO cost queue record.  */  
   SourceTranNum:number,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   VendorNum:number,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   PurPoint:string,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   PackSlip:string,
      /**  One of the internal keys that is used to tie back to the RcvDtl.  */  
   PackLine:number,
      /**  Holds the original Quantity On Hand of the Part FIFO cost when first created.  */  
   OrigOnHandQty:number,
      /**  Holds the quantity consumed from this Part FIFO cost queue.  This quantity plus the OnHand quantity will equal the OrigOnHandQty in most cases.  But in the event where the FIFO cost queue is deactivated due to backing out of the transaction then the OrigOnHandQty and OnHandQty are set to zero but ConsumedQty retains its value.  */  
   ConsumedQty:number,
      /**  Latest date that the FIFO cost record was referenced.  */  
   LastRefDate:string,
      /**  Identifies the transaction file that created this FIFO cost.  */  
   SourceTable:string,
      /**  First component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   SourceKey1:string,
      /**  2nd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   SourceKey2:string,
      /**  3rd component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   SourceKey3:string,
      /**  4th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   SourceKey4:string,
      /**  5th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   SourceKey5:string,
      /**  6th component of the foreign key used to related back to the source transaction that created this FIFO cost record.  */  
   SourceKey6:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PartTranExtNonRecoverableCost:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartFIFOCostTableset{
   PartFIFOCost:Erp_Tablesets_PartFIFOCostRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPartFIFOCostTableset{
   PartFIFOCost:Erp_Tablesets_PartFIFOCostRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param partNum
      @param lotNum
      @param costID
      @param fiFODate
      @param fiFOSeq
      @param fiFOSubSeq
   */  
export interface GetByID_input{
   partNum:string,
   lotNum:string,
   costID:string,
   fiFODate:string,
   fiFOSeq:number,
   fiFOSubSeq:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PartFIFOCostTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PartFIFOCostTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PartFIFOCostTableset[],
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
   returnObj:Erp_Tablesets_PartFIFOCostListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param lotNum
      @param costID
      @param fiFODate
      @param fiFOSeq
   */  
export interface GetNewPartFIFOCost_input{
   ds:Erp_Tablesets_PartFIFOCostTableset[],
   partNum:string,
   lotNum:string,
   costID:string,
   fiFODate:string,
   fiFOSeq:number,
}

export interface GetNewPartFIFOCost_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartFIFOCostTableset,
}
}

   /** Required : 
      @param whereClausePartFIFOCost
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartFIFOCost:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartFIFOCostTableset[],
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
   ds:Erp_Tablesets_UpdExtPartFIFOCostTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPartFIFOCostTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PartFIFOCostTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartFIFOCostTableset,
}
}

