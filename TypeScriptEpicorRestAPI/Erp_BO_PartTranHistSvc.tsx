import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PartTranHistSvc
// Description: Part Tracker Transaction History Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/$metadata", {
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
   Description: Get PartTranHists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartTranHists
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranHistRow
   */  
export function get_PartTranHists(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranHistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranHists", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranHistRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartTranHists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartTranHistRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartTranHistRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartTranHists(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranHists", {
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
   Summary: Calls GetByID to retrieve the PartTranHist item
   Description: Calls GetByID to retrieve the PartTranHist item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartTranHist
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SysDate Desc: SysDate   Required: True   Allow empty value : True
      @param SysTime Desc: SysTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartTranHistRow
   */  
export function get_PartTranHists_Company_SysDate_SysTime_TranNum(Company:string, SysDate:string, SysTime:string, TranNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartTranHistRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranHists(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartTranHistRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartTranHist for the service
   Description: Calls UpdateExt to update PartTranHist. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartTranHist
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SysDate Desc: SysDate   Required: True   Allow empty value : True
      @param SysTime Desc: SysTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartTranHistRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartTranHists_Company_SysDate_SysTime_TranNum(Company:string, SysDate:string, SysTime:string, TranNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranHists(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")", {
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
   Summary: Call UpdateExt to delete PartTranHist item
   Description: Call UpdateExt to delete PartTranHist item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartTranHist
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param SysDate Desc: SysDate   Required: True   Allow empty value : True
      @param SysTime Desc: SysTime   Required: True
      @param TranNum Desc: TranNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartTranHists_Company_SysDate_SysTime_TranNum(Company:string, SysDate:string, SysTime:string, TranNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranHists(" + Company + "," + SysDate + "," + SysTime + "," + TranNum + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get PartTranAttrValueSets items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartTranAttrValueSets
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranAttrValueSetRow
   */  
export function get_PartTranAttrValueSets(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranAttrValueSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranAttrValueSets", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranAttrValueSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartTranAttrValueSets
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartTranAttrValueSetRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartTranAttrValueSetRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PartTranAttrValueSets(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranAttrValueSets", {
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
   Summary: Calls GetByID to retrieve the PartTranAttrValueSet item
   Description: Calls GetByID to retrieve the PartTranAttrValueSet item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartTranAttrValueSet
      @param SysRowID Desc: SysRowID   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartTranAttrValueSetRow
   */  
export function get_PartTranAttrValueSets_SysRowID(SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PartTranAttrValueSetRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranAttrValueSets(" + SysRowID + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PartTranAttrValueSetRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PartTranAttrValueSet for the service
   Description: Calls UpdateExt to update PartTranAttrValueSet. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartTranAttrValueSet
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartTranAttrValueSetRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PartTranAttrValueSets_SysRowID(SysRowID:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranAttrValueSets(" + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete PartTranAttrValueSet item
   Description: Call UpdateExt to delete PartTranAttrValueSet item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartTranAttrValueSet
      @param SysRowID Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PartTranAttrValueSets_SysRowID(SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/PartTranAttrValueSets(" + SysRowID + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartTranHistListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranHistListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranHistListRow)
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
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClausePartTranHist:string, whereClausePartTranAttrValueSet:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePartTranHist!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartTranHist=" + whereClausePartTranHist
   }
   if(typeof whereClausePartTranAttrValueSet!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePartTranAttrValueSet=" + whereClausePartTranAttrValueSet
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/GetRows" + params, {
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
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(sysDate:string, sysTime:string, tranNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof sysDate!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sysDate=" + sysDate
   }
   if(typeof sysTime!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "sysTime=" + sysTime
   }
   if(typeof tranNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "tranNum=" + tranNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/GetList" + params, {
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
   Summary: Invoke method GetSortByList
   Description: This method returns the Sort By selection list.
   OperationID: GetSortByList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetSortByList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSortByList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSortByList(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/GetSortByList", {
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
   Summary: Invoke method RunPartTranHistory
   Description: This method returns the transaction history of a given part.
   OperationID: RunPartTranHistory
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RunPartTranHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RunPartTranHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RunPartTranHistory(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/RunPartTranHistory", {
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
   Summary: Invoke method GetNewPartTranHist
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartTranHist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartTranHist_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartTranHist_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartTranHist(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/GetNewPartTranHist", {
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
   Summary: Invoke method GetNewPartTranAttrValueSet
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartTranAttrValueSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartTranAttrValueSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartTranAttrValueSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPartTranAttrValueSet(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/GetNewPartTranAttrValueSet", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PartTranHistSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranAttrValueSetRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartTranAttrValueSetRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranHistListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartTranHistListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartTranHistRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PartTranHistRow[],
}

export interface Erp_Tablesets_PartTranAttrValueSetRow{
      /**  Company  */  
   "Company":string,
      /**  System date of the related PartTran.  */  
   "SysDate":string,
      /**  System time of the related PartTran.  */  
   "SysTime":number,
      /**  Transaction Number of the related PartTran.  */  
   "TranNum":number,
      /**  A system-generated number which uniquely identifies this row.  */  
   "TranSeq":number,
      /**  The internal key that is used to tie back to the Supplier (Vendor) master file.  */  
   "VendorNum":number,
      /**  The Supplier’s Purchase Point ID.  */  
   "PurPoint":string,
      /**  The Supplier’s Packing Slip Number.  */  
   "PackSlip":string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   "PackLine":number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  Unique identifier for this Attribute Value for this receipt detail.  */  
   "AttributeValueSeq":number,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   "UM":string,
      /**  Transaction Quantity.  */  
   "TranQty":number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   "ActTransUOM":string,
      /**  Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.  */  
   "ActTranQty":number,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  Unit of measure for the NumberOfPieces.  */  
   "NumberOfPiecesUOM":string,
      /**  ID of related Attribute Class.  */  
   "AttrClassID":string,
      /**   Inventory = "PUR-STK"         
JobMaterial = "PUR-MTL"
JobSubcontract = "PUR-SUB"
Other = "PUR-UKN"
Inspection = "PUR-INS"
CustomerManaged = "PUR-CMI"
SupplierManaged = "PUR-SMI"  */  
   "TranType":string,
   "BitFlag":number,
   "DynAttrValueSetDescription":string,
   "DynAttrValueSetShortDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartTranHistListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  A number which is used to allow create a unique key for the file.  */  
   "TranNum":number,
      /**  Part Number that this transaction is for.  */  
   "PartNum":string,
      /**  Warehouse that transaction is applied to  */  
   "WareHouseCode":string,
      /**  Identifies the Bin location that this transaction affected.  */  
   "BinNum":string,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   "TranType":string,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   "InventoryTrans":boolean,
      /**  date of transaction.  */  
   "TranDate":string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   "TranQty":number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   "UM":string,
      /**  Material Unit Cost  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost  */  
   "MtlBurUnitCost":number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   "ExtCost":number,
      /**  Job Number that transaction is associated with.  */  
   "JobNum":string,
      /**  Packing slip number.  */  
   "PackNum":number,
      /**  Created by Purchase Order Receipt Process.  */  
   "PONum":number,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   "OrderNum":number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   "TranReference":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Lot Number  */  
   "LotNum":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  RMA Number  */  
   "RMANum":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Reference to the service call that the material is being issued for.  */  
   "CallNum":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlMtlUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlLabUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlSubUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlBurdenUnitCost":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  */  
   "ActTranQty":number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   "ActTransUOM":string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   "BinType":string,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PCID  */  
   "PCID":string,
      /**  PCIDCollapseCounter  */  
   "PCIDCollapseCounter":number,
      /**  PCID2  */  
   "PCID2":string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   "LCFlag":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Calculated Running Total  */  
   "RunningTotal":number,
   "Packer":string,
      /**  Dim Code Description  */  
   "DimCodeDesc":string,
      /**  Dimension Quantity  */  
   "DimQty":number,
      /**  PackID from Transfer Order Packing type  */  
   "TOPackID":number,
      /**  Miscelaneous Shipment Entry Packing ID  */  
   "MiscShipPackID":number,
      /**  Subcontractor Shipment Packing ID  */  
   "SubConShipPackID":number,
      /**  RunningTotal UOM  */  
   "RunningTotalUOM":string,
      /**  Description of the Bin.  */  
   "BinDescription":string,
      /**  The name of the plant.  */  
   "PlantName":string,
      /**  Description of the warehouse  */  
   "WarehouseDesc":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PartTranHistRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  System date at time that record was created.  */  
   "SysDate":string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   "SysTime":number,
      /**  A number which is used to allow create a unique key for the file.  */  
   "TranNum":number,
      /**  Part Number that this transaction is for.  */  
   "PartNum":string,
      /**  Warehouse that transaction is applied to  */  
   "WareHouseCode":string,
      /**  Identifies the Bin location that this transaction affected.  */  
   "BinNum":string,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   "TranType":string,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   "InventoryTrans":boolean,
      /**  date of transaction.  */  
   "TranDate":string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   "TranQty":number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   "UM":string,
      /**  Material Unit Cost  */  
   "MtlUnitCost":number,
      /**  Labor Unit Cost  */  
   "LbrUnitCost":number,
      /**  Burden Unit Cost  */  
   "BurUnitCost":number,
      /**  Subcontract Unit Cost  */  
   "SubUnitCost":number,
      /**  Material Burden Unit Cost  */  
   "MtlBurUnitCost":number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   "ExtCost":number,
      /**  Job Number that transaction is associated with.  */  
   "JobNum":string,
      /**  Packing slip number.  */  
   "PackNum":number,
      /**  Created by Purchase Order Receipt Process.  */  
   "PONum":number,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   "OrderNum":number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   "EntryPerson":string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   "TranReference":string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  */  
   "RevisionNum":string,
      /**  Vendors Packing Slip #.  */  
   "PackSlip":string,
      /**  Lot Number  */  
   "LotNum":string,
      /**  Unique dimension code for the part.  */  
   "DimCode":string,
      /**  Dimension unit of measure.  */  
   "DUM":string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   "DimConvFactor":number,
      /**  RMA Number  */  
   "RMANum":number,
      /**  Site Identifier.  */  
   "Plant":string,
      /**  Reference to the service call that the material is being issued for.  */  
   "CallNum":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlMtlUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlLabUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   "MtlSubUnitCost":number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   "MtlBurdenUnitCost":number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   "LegalNumber":string,
      /**   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  */  
   "ActTranQty":number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   "ActTransUOM":string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   "BinType":string,
      /**  Drop shipment Packing Slip.  */  
   "DropShipPackSlip":string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  PCID  */  
   "PCID":string,
      /**  PCIDCollapseCounter  */  
   "PCIDCollapseCounter":number,
      /**  PCID2  */  
   "PCID2":string,
      /**  ContractID  */  
   "ContractID":string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   "LCFlag":boolean,
      /**  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  */  
   "ExtNonRecoverableCost":number,
      /**  True if transaction is related to Epicor FSA  */  
   "EpicorFSA":boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   "AttributeSetID":number,
      /**  The Full Description of the Attribute Set.  */  
   "AttributeSetDescription":string,
      /**  The Short Description of the Attribute Set.  */  
   "AttributeSetShortDescription":string,
      /**  Number of pieces for this attribute set.  */  
   "NumberOfPieces":number,
      /**  Bin Description  */  
   "BinDescription":string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   "CallCode":string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   "ContractCode":string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   "ContractNum":number,
      /**  Dim Code Description  */  
   "DimCodeDesc":string,
      /**  Dimension Quantity  */  
   "DimQty":number,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   "FSAAction":string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   "FSAEquipmentInstallID":number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   "FSAEquipmentPartNum":string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderNum":number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   "FSAServiceOrderResourceNum":number,
      /**  Miscelaneous Shipment Entry Packing ID  */  
   "MiscShipPackID":number,
   "Packer":string,
      /**  Plant Name.  */  
   "PlantName":string,
      /**  Full description of Reason... used on displays/reports.  */  
   "ReasonDesc":string,
      /**  Calculated Running Total  */  
   "RunningTotal":number,
      /**  RunningTotal UOM  */  
   "RunningTotalUOM":string,
      /**  Subcontractor Shipment Packing ID  */  
   "SubConShipPackID":number,
      /**  PackID from Transfer Order Packing type  */  
   "TOPackID":number,
      /**  Warehouse description.  */  
   "WarehouseDesc":string,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   "WarrantyCode":string,
   "BitFlag":number,
   "PartNumAttrClassID":string,
   "PartNumTrackLots":boolean,
   "PartNumIUM":string,
   "PartNumSalesUM":string,
   "PartNumTrackDimension":boolean,
   "PartNumPartDescription":string,
   "PartNumTrackInventoryAttributes":boolean,
   "PartNumSellingFactor":number,
   "PartNumTrackSerialNum":boolean,
   "PartNumPricePerCode":string,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param sysDate
      @param sysTime
      @param tranNum
   */  
export interface DeleteByID_input{
   sysDate:string,
   sysTime:number,
   tranNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PartTranAttrValueSetRow{
      /**  Company  */  
   Company:string,
      /**  System date of the related PartTran.  */  
   SysDate:string,
      /**  System time of the related PartTran.  */  
   SysTime:number,
      /**  Transaction Number of the related PartTran.  */  
   TranNum:number,
      /**  A system-generated number which uniquely identifies this row.  */  
   TranSeq:number,
      /**  The internal key that is used to tie back to the Supplier (Vendor) master file.  */  
   VendorNum:number,
      /**  The Supplier’s Purchase Point ID.  */  
   PurPoint:string,
      /**  The Supplier’s Packing Slip Number.  */  
   PackSlip:string,
      /**  An integer that uniquely identifies a detail record within a Packing slip. This is assigned by the system by finding the last RcvDtl record for the vendor's packing slip and add 1.  */  
   PackLine:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Unique identifier for this Attribute Value for this receipt detail.  */  
   AttributeValueSeq:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   UM:string,
      /**  Transaction Quantity.  */  
   TranQty:number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   ActTransUOM:string,
      /**  Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.  */  
   ActTranQty:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  Unit of measure for the NumberOfPieces.  */  
   NumberOfPiecesUOM:string,
      /**  ID of related Attribute Class.  */  
   AttrClassID:string,
      /**   Inventory = "PUR-STK"         
JobMaterial = "PUR-MTL"
JobSubcontract = "PUR-SUB"
Other = "PUR-UKN"
Inspection = "PUR-INS"
CustomerManaged = "PUR-CMI"
SupplierManaged = "PUR-SMI"  */  
   TranType:string,
   BitFlag:number,
   DynAttrValueSetDescription:string,
   DynAttrValueSetShortDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartTranHistListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  A number which is used to allow create a unique key for the file.  */  
   TranNum:number,
      /**  Part Number that this transaction is for.  */  
   PartNum:string,
      /**  Warehouse that transaction is applied to  */  
   WareHouseCode:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   TranType:string,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   InventoryTrans:boolean,
      /**  date of transaction.  */  
   TranDate:string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   TranQty:number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   UM:string,
      /**  Material Unit Cost  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   ExtCost:number,
      /**  Job Number that transaction is associated with.  */  
   JobNum:string,
      /**  Packing slip number.  */  
   PackNum:number,
      /**  Created by Purchase Order Receipt Process.  */  
   PONum:number,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   TranReference:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Lot Number  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  RMA Number  */  
   RMANum:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Reference to the service call that the material is being issued for.  */  
   CallNum:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlLabUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlSubUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlBurdenUnitCost:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  */  
   ActTranQty:number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   ActTransUOM:string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   BinType:string,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  PCIDCollapseCounter  */  
   PCIDCollapseCounter:number,
      /**  PCID2  */  
   PCID2:string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   LCFlag:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Calculated Running Total  */  
   RunningTotal:number,
   Packer:string,
      /**  Dim Code Description  */  
   DimCodeDesc:string,
      /**  Dimension Quantity  */  
   DimQty:number,
      /**  PackID from Transfer Order Packing type  */  
   TOPackID:number,
      /**  Miscelaneous Shipment Entry Packing ID  */  
   MiscShipPackID:number,
      /**  Subcontractor Shipment Packing ID  */  
   SubConShipPackID:number,
      /**  RunningTotal UOM  */  
   RunningTotalUOM:string,
      /**  Description of the Bin.  */  
   BinDescription:string,
      /**  The name of the plant.  */  
   PlantName:string,
      /**  Description of the warehouse  */  
   WarehouseDesc:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartTranHistListTableset{
   PartTranHistList:Erp_Tablesets_PartTranHistListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PartTranHistRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  System date at time that record was created.  */  
   SysDate:string,
      /**  System Time (hr-min-sec) when transaction was created.  */  
   SysTime:number,
      /**  A number which is used to allow create a unique key for the file.  */  
   TranNum:number,
      /**  Part Number that this transaction is for.  */  
   PartNum:string,
      /**  Warehouse that transaction is applied to  */  
   WareHouseCode:string,
      /**  Identifies the Bin location that this transaction affected.  */  
   BinNum:string,
      /**   Field that indicates the type of transaction:
ADJ-CST -  Adjustment to Stock Cost.
ADJ-DEM - Adjustment to Demand Quantity.
ADJ-MTL - Adjustment to Job Cost Material.
ADJ-PUR - Purchase Price variance (created by A/P invoice)
ADJ-QTY - Adjustment to  */  
   TranType:string,
      /**  Indicates if this is an inventory transaction, which is any part transaction that affects inventory quantity or cost.  Specifically,  the following transaction types: (1) begin or end with "STK", (2) "ADJ-CST" and "ADJ-QTY", (3) "INS-DMR" and "DMR-REJ" for non-part-master parts.  */  
   InventoryTrans:boolean,
      /**  date of transaction.  */  
   TranDate:string,
      /**   Transaction Quantity.
Always represented in the Parts Primary Inventory Unit of Measure which will be stored in Parttran.UM This is the UOM that the unit costs are based on. 
The actual Transaction quatity is found in ActTranQty  */  
   TranQty:number,
      /**  Unit of Measure.  (part primary inventory uom)  */  
   UM:string,
      /**  Material Unit Cost  */  
   MtlUnitCost:number,
      /**  Labor Unit Cost  */  
   LbrUnitCost:number,
      /**  Burden Unit Cost  */  
   BurUnitCost:number,
      /**  Subcontract Unit Cost  */  
   SubUnitCost:number,
      /**  Material Burden Unit Cost  */  
   MtlBurUnitCost:number,
      /**   Extended Cost is calculated as
(TranQty * (MtlUnitCost + LbrUnitCost + BurUnitCost) ). This is updated via the PartTran write trigger. 
NOTE: An exception is where PartTran.TranType = "Adj-Pur" in which case the TranQty and UnitCost fields are zero and the ExtCost is calculated outside of the write trigger.  */  
   ExtCost:number,
      /**  Job Number that transaction is associated with.  */  
   JobNum:string,
      /**  Packing slip number.  */  
   PackNum:number,
      /**  Created by Purchase Order Receipt Process.  */  
   PONum:number,
      /**   The sales order number that this detail shipment line is linked to.
This is not directly maintainable; It is carried forward through from the ShipHead.OrderNum field.  */  
   OrderNum:number,
      /**   This is used as a selection parameter for reporting and browsing. The intent is for users to be able to select transactions that they have entered for hard copy edit.
This field is set equal to the Login ID variable. It can not be overridden.  */  
   EntryPerson:string,
      /**  Can be used to hold a short comment.  In some cases the Manufacturing System uses this field to make a comment about the source of the transaction, as in the case of "backflush" process.  */  
   TranReference:string,
      /**  Part Revision number. Not directly entered. Instead it is duplicated at the time of transaction creation from an associated Parent record. The Parent file could be the Part, JobOPer, JobMtl, ShipDtl,  SubShipD ....  */  
   RevisionNum:string,
      /**  Vendors Packing Slip #.  */  
   PackSlip:string,
      /**  Lot Number  */  
   LotNum:string,
      /**  Unique dimension code for the part.  */  
   DimCode:string,
      /**  Dimension unit of measure.  */  
   DUM:string,
      /**   Dimension conversion factor.  This conversion factor is used to convert the qty to the base part unit of measure.
Example: A half sheet to full sheet conversion factor would be 2 and a double sheet to full sheet conversion factor would be 0.5.  */  
   DimConvFactor:number,
      /**  RMA Number  */  
   RMANum:number,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Reference to the service call that the material is being issued for.  */  
   CallNum:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlMtlUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlLabUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost.  */  
   MtlSubUnitCost:number,
      /**  Breakdown of MtlUnit cost into individual components. MtlUnitCost = MtlMtlUnitCost + MtlLabUnitCost + MtlBurdenUnitCost + MtlSubUnitCost + MtlMtlBurUnitCost  */  
   MtlBurdenUnitCost:number,
      /**  The Legal Number for the record.  This number is created based on setup parameters in table LegalNumber.  */  
   LegalNumber:string,
      /**   Actual Transaction Quantity is the quatity that was phsically entered for the transaction and is relative to the ActTranUOM.
Related to PartTran.TranQty which is the ActTranQty converted into the Parts Primary Inventory UOM.  */  
   ActTranQty:number,
      /**  Actual Unit of Measure of the ActTransQty.  */  
   ActTransUOM:string,
      /**  The BinType of the bin identified in BinNum field.  Valid values are "Std', 'Cust', and 'Supp'.  */  
   BinType:string,
      /**  Drop shipment Packing Slip.  */  
   DropShipPackSlip:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  PCID  */  
   PCID:string,
      /**  PCIDCollapseCounter  */  
   PCIDCollapseCounter:number,
      /**  PCID2  */  
   PCID2:string,
      /**  ContractID  */  
   ContractID:string,
      /**  Indicates if the MtlBurUnitcost is Landed costs of standard burden.  */  
   LCFlag:boolean,
      /**  The Non Recoverable Tax that has been included on the Extended Cost.  This will be calculated from the Receipt Header and Receipt Line tax records by subtracting the total deductable tax from the total tax.  */  
   ExtNonRecoverableCost:number,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Bin Description  */  
   BinDescription:string,
      /**  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  */  
   CallCode:string,
      /**  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  */  
   ContractCode:string,
      /**  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  */  
   ContractNum:number,
      /**  Dim Code Description  */  
   DimCodeDesc:string,
      /**  Dimension Quantity  */  
   DimQty:number,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Miscelaneous Shipment Entry Packing ID  */  
   MiscShipPackID:number,
   Packer:string,
      /**  Plant Name.  */  
   PlantName:string,
      /**  Full description of Reason... used on displays/reports.  */  
   ReasonDesc:string,
      /**  Calculated Running Total  */  
   RunningTotal:number,
      /**  RunningTotal UOM  */  
   RunningTotalUOM:string,
      /**  Subcontractor Shipment Packing ID  */  
   SubConShipPackID:number,
      /**  PackID from Transfer Order Packing type  */  
   TOPackID:number,
      /**  Warehouse description.  */  
   WarehouseDesc:string,
      /**  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  */  
   WarrantyCode:string,
   BitFlag:number,
   PartNumAttrClassID:string,
   PartNumTrackLots:boolean,
   PartNumIUM:string,
   PartNumSalesUM:string,
   PartNumTrackDimension:boolean,
   PartNumPartDescription:string,
   PartNumTrackInventoryAttributes:boolean,
   PartNumSellingFactor:number,
   PartNumTrackSerialNum:boolean,
   PartNumPricePerCode:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartTranHistTableset{
   PartTranHist:Erp_Tablesets_PartTranHistRow[],
   PartTranAttrValueSet:Erp_Tablesets_PartTranAttrValueSetRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPartTranHistTableset{
   PartTranHist:Erp_Tablesets_PartTranHistRow[],
   PartTranAttrValueSet:Erp_Tablesets_PartTranAttrValueSetRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param sysDate
      @param sysTime
      @param tranNum
   */  
export interface GetByID_input{
   sysDate:string,
   sysTime:number,
   tranNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PartTranHistTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PartTranHistTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PartTranHistTableset[],
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
   returnObj:Erp_Tablesets_PartTranHistListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewPartTranAttrValueSet_input{
   ds:Erp_Tablesets_PartTranHistTableset[],
}

export interface GetNewPartTranAttrValueSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartTranHistTableset[],
}
}

   /** Required : 
      @param ds
      @param sysDate
      @param sysTime
   */  
export interface GetNewPartTranHist_input{
   ds:Erp_Tablesets_PartTranHistTableset[],
   sysDate:string,
   sysTime:number,
}

export interface GetNewPartTranHist_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartTranHistTableset[],
}
}

   /** Required : 
      @param whereClausePartTranHist
      @param whereClausePartTranAttrValueSet
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePartTranHist:string,
   whereClausePartTranAttrValueSet:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PartTranHistTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ipPartNum
   */  
export interface GetSortByList_input{
      /**  The Part Number to be processed  */  
   ipPartNum:string,
}

export interface GetSortByList_output{
parameters : {
      /**  output parameters  */  
   SortByList:string,
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
      @param ipPartNum
      @param ipPlant
      @param ipTranDate
      @param ipStartingDate
      @param ipLotNum
      @param ipDimCode
      @param ipSortBy
   */  
export interface RunPartTranHistory_input{
      /**  The Part Number to process  */  
   ipPartNum:string,
      /**  The valid Plant ID to process.  */  
   ipPlant:string,
      /**  The Cut Off Transaction Date to process. If not supplied then the default is today.  */  
   ipTranDate:string,
      /**  The Starting Transaction Date to process. If not supplied then it will start with the first transaction saved.  */  
   ipStartingDate:string,
      /**  The starting Lot Number to process  */  
   ipLotNum:string,
      /**  The starting Dimension Code to process  */  
   ipDimCode:string,
      /**  The sort by selected by the user.  Valid options are:
            THIST-BRW (Tran Date Browse); THISTLOT-BRW (Lot Number/Tran Date browse)
            and THISTDIM-BRW (Dim Code/Tran Date browse)  */  
   ipSortBy:string,
}

export interface RunPartTranHistory_output{
   returnObj:Erp_Tablesets_PartTranHistTableset[],
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPartTranHistTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPartTranHistTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PartTranHistTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PartTranHistTableset[],
}
}

