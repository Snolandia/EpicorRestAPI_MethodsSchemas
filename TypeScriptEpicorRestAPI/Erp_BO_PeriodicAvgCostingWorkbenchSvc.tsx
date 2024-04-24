import * as configEpicorSchemas from "./configEpicorSchemas"


// Title: Erp.BO.PeriodicAvgCostingWorkbenchSvc
// Description: Periodic Average CostingWorkbenchSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/$metadata", {
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
   Description: Get PeriodicAvgCostingWorkbenches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PeriodicAvgCostingWorkbenches
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PeriodicAverageCostHeadRow
   */  
export function get_PeriodicAvgCostingWorkbenches(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicAverageCostHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/PeriodicAvgCostingWorkbenches", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicAverageCostHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PeriodicAvgCostingWorkbenches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PeriodicAverageCostHeadRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PeriodicAverageCostHeadRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PeriodicAvgCostingWorkbenches(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/PeriodicAvgCostingWorkbenches", {
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
   Summary: Calls GetByID to retrieve the PeriodicAvgCostingWorkbench item
   Description: Calls GetByID to retrieve the PeriodicAvgCostingWorkbench item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PeriodicAvgCostingWorkbench
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PeriodicAverageCostID Desc: PeriodicAverageCostID   Required: True   Allow empty value : True
      @param CalculationNum Desc: CalculationNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PeriodicAverageCostHeadRow
   */  
export function get_PeriodicAvgCostingWorkbenches_Company_Plant_PeriodicAverageCostID_CalculationNum(Company:string, Plant:string, PeriodicAverageCostID:string, CalculationNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PeriodicAverageCostHeadRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/PeriodicAvgCostingWorkbenches(" + Company + "," + Plant + "," + PeriodicAverageCostID + "," + CalculationNum + ")", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Erp_Tablesets_PeriodicAverageCostHeadRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update PeriodicAvgCostingWorkbench for the service
   Description: Calls UpdateExt to update PeriodicAvgCostingWorkbench. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PeriodicAvgCostingWorkbench
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PeriodicAverageCostID Desc: PeriodicAverageCostID   Required: True   Allow empty value : True
      @param CalculationNum Desc: CalculationNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PeriodicAverageCostHeadRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_PeriodicAvgCostingWorkbenches_Company_Plant_PeriodicAverageCostID_CalculationNum(Company:string, Plant:string, PeriodicAverageCostID:string, CalculationNum:string, requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/PeriodicAvgCostingWorkbenches(" + Company + "," + Plant + "," + PeriodicAverageCostID + "," + CalculationNum + ")", {
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
   Summary: Call UpdateExt to delete PeriodicAvgCostingWorkbench item
   Description: Call UpdateExt to delete PeriodicAvgCostingWorkbench item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PeriodicAvgCostingWorkbench
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param PeriodicAverageCostID Desc: PeriodicAverageCostID   Required: True   Allow empty value : True
      @param CalculationNum Desc: CalculationNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_PeriodicAvgCostingWorkbenches_Company_Plant_PeriodicAverageCostID_CalculationNum(Company:string, Plant:string, PeriodicAverageCostID:string, CalculationNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/PeriodicAvgCostingWorkbenches(" + Company + "," + Plant + "," + PeriodicAverageCostID + "," + CalculationNum + ")", {
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PeriodicAverageCostHeadListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicAverageCostHeadListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/List", {
          method: 'get',
          headers: headers,
      })
      fetch(request)
      .then((res) => res.json())
      .then((data) => {
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicAverageCostHeadListRow)
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
export function get_GetRows(whereClausePeriodicAverageCostHead:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePeriodicAverageCostHead!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePeriodicAverageCostHead=" + whereClausePeriodicAverageCostHead
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/GetRows" + params, {
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
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(plant:string, periodicAverageCostID:string, calculationNum:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof plant!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "plant=" + plant
   }
   if(typeof periodicAverageCostID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "periodicAverageCostID=" + periodicAverageCostID
   }
   if(typeof calculationNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "calculationNum=" + calculationNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/GetList" + params, {
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
   Summary: Invoke method OnChangedFiscalYrPeriod
   Description: Sets FromDate and ToDate
   OperationID: OnChangedFiscalYrPeriod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangedFiscalYrPeriod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangedFiscalYrPeriod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangedFiscalYrPeriod(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/OnChangedFiscalYrPeriod", {
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
   Summary: Invoke method GetPeriodicAverageCostLineRows
   Description: Returns PeriodicAverageCostLine
   OperationID: GetPeriodicAverageCostLineRows
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPeriodicAverageCostLineRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPeriodicAverageCostLineRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPeriodicAverageCostLineRows(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/GetPeriodicAverageCostLineRows", {
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
   Summary: Invoke method GetNewPeriodicAverageCostHead
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPeriodicAverageCostHead
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPeriodicAverageCostHead_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPeriodicAverageCostHead_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPeriodicAverageCostHead(requestBody:any, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/GetNewPeriodicAverageCostHead", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicAvgCostingWorkbenchSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicAverageCostHeadListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PeriodicAverageCostHeadListRow[],
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicAverageCostHeadRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PeriodicAverageCostHeadRow[],
}

export interface Erp_Tablesets_PeriodicAverageCostHeadListRow{
      /**  Company  */  
   "Company":string,
      /**  Plant  */  
   "Plant":string,
      /**  Periodic Average Cost ID  */  
   "PeriodicAverageCostID":string,
      /**  Calculation Num  */  
   "CalculationNum":number,
      /**  Fiscal Year  */  
   "FiscalYear":number,
      /**  Fiscal Year Suffix  */  
   "FiscalYearSuffix":string,
      /**  From Period  */  
   "FromPeriod":number,
      /**  To Period  */  
   "ToPeriod":number,
      /**  From Date  */  
   "FromDate":string,
      /**  To Date  */  
   "ToDate":string,
      /**  Posted  */  
   "Posted":boolean,
      /**  Posted Date  */  
   "PostedDate":string,
      /**  Comment  */  
   "Comment":string,
      /**  Apply Date  */  
   "ApplyDate":string,
      /**  Include Parts with Zero Quantities  */  
   "IncludePartZeroQty":boolean,
      /**  Include Parts with any Costing Method  */  
   "IncludePartAnyCostMethod":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PeriodicAverageCostHeadRow{
      /**  Company  */  
   "Company":string,
      /**  Plant  */  
   "Plant":string,
      /**  Periodic Average Cost ID  */  
   "PeriodicAverageCostID":string,
      /**  Calculation Num  */  
   "CalculationNum":number,
      /**  Fiscal Year  */  
   "FiscalYear":number,
      /**  Fiscal Year Suffix  */  
   "FiscalYearSuffix":string,
      /**  From Period  */  
   "FromPeriod":number,
      /**  To Period  */  
   "ToPeriod":number,
      /**  From Date  */  
   "FromDate":string,
      /**  To Date  */  
   "ToDate":string,
      /**  Posted  */  
   "Posted":boolean,
      /**  Posted Date  */  
   "PostedDate":string,
      /**  Comment  */  
   "Comment":string,
      /**  Apply Date  */  
   "ApplyDate":string,
      /**  Include Parts with Zero Quantities  */  
   "IncludePartZeroQty":boolean,
      /**  Include Parts with any Costing Method  */  
   "IncludePartAnyCostMethod":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "Generated":boolean,
   "IsTheFirstCalculation":boolean,
   "FiscalCalendarID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}




//////////////////////////////////////////////////////////////////////////
// Custom Schemas:
//////////////////////////////////////////////////////////////////////////
   /** Required : 
      @param plant
      @param periodicAverageCostID
      @param calculationNum
   */  
export interface DeleteByID_input{
   plant:string,
   periodicAverageCostID:string,
   calculationNum:number,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PeriodicAverageCostHeadListRow{
      /**  Company  */  
   Company:string,
      /**  Plant  */  
   Plant:string,
      /**  Periodic Average Cost ID  */  
   PeriodicAverageCostID:string,
      /**  Calculation Num  */  
   CalculationNum:number,
      /**  Fiscal Year  */  
   FiscalYear:number,
      /**  Fiscal Year Suffix  */  
   FiscalYearSuffix:string,
      /**  From Period  */  
   FromPeriod:number,
      /**  To Period  */  
   ToPeriod:number,
      /**  From Date  */  
   FromDate:string,
      /**  To Date  */  
   ToDate:string,
      /**  Posted  */  
   Posted:boolean,
      /**  Posted Date  */  
   PostedDate:string,
      /**  Comment  */  
   Comment:string,
      /**  Apply Date  */  
   ApplyDate:string,
      /**  Include Parts with Zero Quantities  */  
   IncludePartZeroQty:boolean,
      /**  Include Parts with any Costing Method  */  
   IncludePartAnyCostMethod:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PeriodicAverageCostHeadRow{
      /**  Company  */  
   Company:string,
      /**  Plant  */  
   Plant:string,
      /**  Periodic Average Cost ID  */  
   PeriodicAverageCostID:string,
      /**  Calculation Num  */  
   CalculationNum:number,
      /**  Fiscal Year  */  
   FiscalYear:number,
      /**  Fiscal Year Suffix  */  
   FiscalYearSuffix:string,
      /**  From Period  */  
   FromPeriod:number,
      /**  To Period  */  
   ToPeriod:number,
      /**  From Date  */  
   FromDate:string,
      /**  To Date  */  
   ToDate:string,
      /**  Posted  */  
   Posted:boolean,
      /**  Posted Date  */  
   PostedDate:string,
      /**  Comment  */  
   Comment:string,
      /**  Apply Date  */  
   ApplyDate:string,
      /**  Include Parts with Zero Quantities  */  
   IncludePartZeroQty:boolean,
      /**  Include Parts with any Costing Method  */  
   IncludePartAnyCostMethod:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   Generated:boolean,
   IsTheFirstCalculation:boolean,
   FiscalCalendarID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PeriodicAverageCostLineListRow{
      /**  Company  */  
   Company:string,
      /**  Plant  */  
   Plant:string,
      /**  Periodic Average Cost ID  */  
   PeriodicAverageCostID:string,
      /**  Calculation Num  */  
   CalculationNum:number,
      /**  Part Num  */  
   PartNum:string,
      /**  UOM  */  
   UOM:string,
      /**  Received Qunatity  */  
   ReceivedQty:number,
      /**  Sold Qunatity  */  
   SoldQty:number,
      /**  On-hand Qunatity Start  */  
   OnHandQtyStart:number,
      /**  On-hand Qunatity End  */  
   OnHandQtyEnd:number,
      /**  Cost Method  */  
   CostMethod:string,
      /**  Original Material Cost  */  
   CurrentMaterialCost:number,
      /**  Original Material Burden Cost  */  
   CurrentMtlBurCost:number,
      /**  Original Labor Cost  */  
   CurrentLaborCost:number,
      /**  Original Burden Cost  */  
   CurrentBurdenCost:number,
      /**  Original Subcontract Cost  */  
   CurrentSubContCost:number,
      /**  Original Extended Cost  */  
   CurrentExtendedCost:number,
      /**  Start Material Cost  */  
   StartMaterialCost:number,
      /**  Start Material Burden Cost  */  
   StartMtlBurCost:number,
      /**  Start Labor Cost  */  
   StartLaborCost:number,
      /**  Start Burden Cost  */  
   StartBurdenCost:number,
      /**  Start Subcontract Cost  */  
   StartSubContCost:number,
      /**  Start Extended Cost  */  
   StartExtendedCost:number,
      /**  PAC Material Cost  */  
   PACMaterialCost:number,
      /**  PAC Materilal Burden Cost  */  
   PACMtlBurCost:number,
      /**  PAC Labor Cost  */  
   PACLaborCost:number,
      /**  PAC Burden Cost  */  
   PACBurdenCost:number,
      /**  PAC Subcontract Cost  */  
   PACSubContCost:number,
      /**  PAC Extended Cost  */  
   PACExtendedCost:number,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   CostMethodDesc:string,
   FromDate:string,
   ToDate:string,
   PostedDate:string,
   Posted:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PeriodicAverageCostLineTableset{
   PeriodicAverageCostLineList:Erp_Tablesets_PeriodicAverageCostLineListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PeriodicAvgCostWorkbenchListTableset{
   PeriodicAverageCostHeadList:Erp_Tablesets_PeriodicAverageCostHeadListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset{
   PeriodicAverageCostHead:Erp_Tablesets_PeriodicAverageCostHeadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPeriodicAvgCostingWorkbenchTableset{
   PeriodicAverageCostHead:Erp_Tablesets_PeriodicAverageCostHeadRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param plant
      @param periodicAverageCostID
      @param calculationNum
   */  
export interface GetByID_input{
   plant:string,
   periodicAverageCostID:string,
   calculationNum:number,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset[],
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
   returnObj:Erp_Tablesets_PeriodicAvgCostWorkbenchListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
      @param periodicAverageCostID
   */  
export interface GetNewPeriodicAverageCostHead_input{
   ds:Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset[],
   plant:string,
   periodicAverageCostID:string,
}

export interface GetNewPeriodicAverageCostHead_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset[],
}
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetPeriodicAverageCostLineRows_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetPeriodicAverageCostLineRows_output{
   returnObj:Erp_Tablesets_PeriodicAverageCostLineTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param whereClausePeriodicAverageCostHead
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePeriodicAverageCostHead:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset[],
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
   */  
export interface OnChangedFiscalYrPeriod_input{
   ds:Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset[],
}

export interface OnChangedFiscalYrPeriod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset[],
}
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtPeriodicAvgCostingWorkbenchTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPeriodicAvgCostingWorkbenchTableset[],
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PeriodicAvgCostingWorkbenchTableset[],
}
}

