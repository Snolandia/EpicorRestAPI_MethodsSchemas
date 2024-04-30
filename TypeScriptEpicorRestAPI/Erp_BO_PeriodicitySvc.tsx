import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.PeriodicitySvc
// Description: Periodicity Code Maintenance - for maintaining Periodicity information for
Purchase Scheduling and Sales Scheduling
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/$metadata", {
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
   Description: Get Periodicities items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Periodicities
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PeriodicityRow
   */  
export function get_Periodicities(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/Periodicities", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Periodicities
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PeriodicityRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.PeriodicityRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Periodicities(requestBody:Erp_Tablesets_PeriodicityRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/Periodicities", {
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
   Summary: Calls GetByID to retrieve the Periodicity item
   Description: Calls GetByID to retrieve the Periodicity item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Periodicity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.PeriodicityRow
   */  
export function get_Periodicities_Company_Plant_VendorNum_PurPoint_CustNum_ShipToNum(Company:string, Plant:string, VendorNum:string, PurPoint:string, CustNum:string, ShipToNum:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_PeriodicityRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/Periodicities(" + Company + "," + Plant + "," + VendorNum + "," + PurPoint + "," + CustNum + "," + ShipToNum + ")", {
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
         resolve(data as Erp_Tablesets_PeriodicityRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Periodicity for the service
   Description: Calls UpdateExt to update Periodicity. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Periodicity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.PeriodicityRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Periodicities_Company_Plant_VendorNum_PurPoint_CustNum_ShipToNum(Company:string, Plant:string, VendorNum:string, PurPoint:string, CustNum:string, ShipToNum:string, requestBody:Erp_Tablesets_PeriodicityRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/Periodicities(" + Company + "," + Plant + "," + VendorNum + "," + PurPoint + "," + CustNum + "," + ShipToNum + ")", {
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
   Summary: Call UpdateExt to delete Periodicity item
   Description: Call UpdateExt to delete Periodicity item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Periodicity
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param Plant Desc: Plant   Required: True   Allow empty value : True
      @param VendorNum Desc: VendorNum   Required: True
      @param PurPoint Desc: PurPoint   Required: True   Allow empty value : True
      @param CustNum Desc: CustNum   Required: True
      @param ShipToNum Desc: ShipToNum   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Periodicities_Company_Plant_VendorNum_PurPoint_CustNum_ShipToNum(Company:string, Plant:string, VendorNum:string, PurPoint:string, CustNum:string, ShipToNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/Periodicities(" + Company + "," + Plant + "," + VendorNum + "," + PurPoint + "," + CustNum + "," + ShipToNum + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PeriodicityListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicityListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicityListRow)
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
export function get_GetRows(whereClausePeriodicity:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClausePeriodicity!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClausePeriodicity=" + whereClausePeriodicity
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/GetRows" + params, {
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
   Required: True
   Required: True   Allow empty value : True
   Required: True
   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetByID(plant:string, vendorNum:string, purPoint:string, custNum:string, shipToNum:string, epicorHeaders?:Headers){
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
   if(typeof vendorNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "vendorNum=" + vendorNum
   }
   if(typeof purPoint!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "purPoint=" + purPoint
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
   if(typeof shipToNum!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "shipToNum=" + shipToNum
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/GetList" + params, {
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
   Summary: Invoke method Existplant
   OperationID: Existplant
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Existplant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Existplant_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Existplant(requestBody:Existplant_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Existplant_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/Existplant", {
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
         resolve(data as Existplant_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCodeDescList
   OperationID: GetCodeDescList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCodeDescList(requestBody:GetCodeDescList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCodeDescList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/GetCodeDescList", {
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
         resolve(data as GetCodeDescList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindCustNum
   Description: Returns the CustNum and Customer Name.
   OperationID: FindCustNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FindCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindCustNum(requestBody:FindCustNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FindCustNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/FindCustNum", {
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
         resolve(data as FindCustNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindVendorNum
   OperationID: FindVendorNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FindVendorNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindVendorNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindVendorNum(requestBody:FindVendorNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FindVendorNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/FindVendorNum", {
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
         resolve(data as FindVendorNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewPeriodicity
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPeriodicity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewPeriodicity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPeriodicity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewPeriodicity(requestBody:GetNewPeriodicity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewPeriodicity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/GetNewPeriodicity", {
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
         resolve(data as GetNewPeriodicity_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.PeriodicitySvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicityListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PeriodicityListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PeriodicityRow{
   "odatametadata":string,
   "value":Erp_Tablesets_PeriodicityRow,
}

export interface Erp_Tablesets_PeriodicityListRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  A unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "VendorNum":number,
      /**  Vendor Purchase Point  */  
   "PurPoint":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   "CustNum":number,
      /**  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  */  
   "ShipToNum":string,
      /**  Code 1 = Semi-Weekly  */  
   "Code1Rules":boolean,
      /**  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   "Code1DeliveryDay1":number,
      /**  The day of the week for the second delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   "Code1DeliveryDay2":number,
      /**  Code 2 = Daily  */  
   "Code2Rules":boolean,
      /**  Are deliveries required on Saturday and Sunday?  */  
   "Code2IncludeSatSun":boolean,
      /**  Code 3 = Monthly Forward  */  
   "Code3Rules":boolean,
      /**  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   "Code3DeliveryDay1":number,
      /**  The week number in the month that the delivery is required.  Valid values are 1-5.  */  
   "Code3WeekNumberInMonth":number,
      /**  Code 4 = Weekly Forward  */  
   "Code4Rules":boolean,
      /**  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   "Code4DeliveryDayInWeek":number,
      /**  Code 5 = Weekly Not Last Week of the Month  */  
   "Code5Rules":boolean,
      /**  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   "Code5DeliveryDayInWeek":number,
      /**  Code 6 = Nth Day of the Month  */  
   "Code6Rules":boolean,
      /**  The day of the month for the delivery.  Valid values are 1-31.  */  
   "Code6DeliveryDayInMonth":number,
      /**  Code 7 = Shipment Day of Week.  */  
   "Code7Rules":boolean,
      /**  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   "Code7ShipmentDayInWeek":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  The full name of the customer.  */  
   "CustomerName":string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   "CustomerBTName":string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   "CustomerCustID":string,
      /**  The Plant name. Used on shipping reports.  */  
   "PlantNameName":string,
      /**  Third address line of the Supplier  */  
   "VendorNumAddress3":string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   "VendorNumVendorID":string,
      /**  A unique code that identifies the currency.  */  
   "VendorNumCurrencyCode":string,
      /**  Can be blank.  */  
   "VendorNumState":string,
      /**  First address line of the Supplier  */  
   "VendorNumAddress1":string,
      /**  City portion of the address of the Supplier  */  
   "VendorNumCity":string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   "VendorNumZIP":string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   "VendorNumDefaultFOB":string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   "VendorNumTermsCode":string,
      /**  Second address line of the Supplier  */  
   "VendorNumAddress2":string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   "VendorNumCountry":string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   "VendorNumName":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_PeriodicityRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Unique identifier of this Site assigned by the user.  */  
   "Plant":string,
      /**  A unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   "VendorNum":number,
      /**  Vendor Purchase Point  */  
   "PurPoint":string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   "CustNum":number,
      /**  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  */  
   "ShipToNum":string,
      /**  Code 1 = Semi-Weekly  */  
   "Code1Rules":boolean,
      /**  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   "Code1DeliveryDay1":number,
      /**  The day of the week for the second delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   "Code1DeliveryDay2":number,
      /**  Code 2 = Daily  */  
   "Code2Rules":boolean,
      /**  Are deliveries required on Saturday and Sunday?  */  
   "Code2IncludeSatSun":boolean,
      /**  Code 3 = Monthly Forward  */  
   "Code3Rules":boolean,
      /**  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   "Code3DeliveryDay1":number,
      /**  The week number in the month that the delivery is required.  Valid values are 1-5.  */  
   "Code3WeekNumberInMonth":number,
      /**  Code 4 = Weekly Forward  */  
   "Code4Rules":boolean,
      /**  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   "Code4DeliveryDayInWeek":number,
      /**  Code 5 = Weekly Not Last Week of the Month  */  
   "Code5Rules":boolean,
      /**  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   "Code5DeliveryDayInWeek":number,
      /**  Code 6 = Nth Day of the Month  */  
   "Code6Rules":boolean,
      /**  The day of the month for the delivery.  Valid values are 1-31.  */  
   "Code6DeliveryDayInMonth":number,
      /**  Code 7 = Shipment Day of Week.  */  
   "Code7Rules":boolean,
      /**  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   "Code7ShipmentDayInWeek":number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "BitFlag":number,
   "CustomerBTName":string,
   "CustomerName":string,
   "CustomerCustID":string,
   "PlantNameName":string,
   "VendorNumCountry":string,
   "VendorNumTermsCode":string,
   "VendorNumDefaultFOB":string,
   "VendorNumVendorID":string,
   "VendorNumName":string,
   "VendorNumState":string,
   "VendorNumAddress1":string,
   "VendorNumCurrencyCode":string,
   "VendorNumCity":string,
   "VendorNumZIP":string,
   "VendorNumAddress3":string,
   "VendorNumAddress2":string,
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
      @param plant
      @param vendorNum
      @param purPoint
      @param custNum
      @param shipToNum
   */  
export interface DeleteByID_input{
   plant:string,
   vendorNum:number,
   purPoint:string,
   custNum:number,
   shipToNum:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_PeriodicityListRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  A unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
      /**  Vendor Purchase Point  */  
   PurPoint:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  */  
   ShipToNum:string,
      /**  Code 1 = Semi-Weekly  */  
   Code1Rules:boolean,
      /**  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   Code1DeliveryDay1:number,
      /**  The day of the week for the second delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   Code1DeliveryDay2:number,
      /**  Code 2 = Daily  */  
   Code2Rules:boolean,
      /**  Are deliveries required on Saturday and Sunday?  */  
   Code2IncludeSatSun:boolean,
      /**  Code 3 = Monthly Forward  */  
   Code3Rules:boolean,
      /**  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   Code3DeliveryDay1:number,
      /**  The week number in the month that the delivery is required.  Valid values are 1-5.  */  
   Code3WeekNumberInMonth:number,
      /**  Code 4 = Weekly Forward  */  
   Code4Rules:boolean,
      /**  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   Code4DeliveryDayInWeek:number,
      /**  Code 5 = Weekly Not Last Week of the Month  */  
   Code5Rules:boolean,
      /**  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   Code5DeliveryDayInWeek:number,
      /**  Code 6 = Nth Day of the Month  */  
   Code6Rules:boolean,
      /**  The day of the month for the delivery.  Valid values are 1-31.  */  
   Code6DeliveryDayInMonth:number,
      /**  Code 7 = Shipment Day of Week.  */  
   Code7Rules:boolean,
      /**  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   Code7ShipmentDayInWeek:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  The full name of the customer.  */  
   CustomerName:string,
      /**  The Bill To name of this customer. Will be used by the AR module for Invoices. This defaults to the Customer.Name but can be overrode by the user.  */  
   CustomerBTName:string,
      /**  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to th  */  
   CustomerCustID:string,
      /**  The Plant name. Used on shipping reports.  */  
   PlantNameName:string,
      /**  Third address line of the Supplier  */  
   VendorNumAddress3:string,
      /**  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the sy  */  
   VendorNumVendorID:string,
      /**  A unique code that identifies the currency.  */  
   VendorNumCurrencyCode:string,
      /**  Can be blank.  */  
   VendorNumState:string,
      /**  First address line of the Supplier  */  
   VendorNumAddress1:string,
      /**  City portion of the address of the Supplier  */  
   VendorNumCity:string,
      /**  Postal Code or Zip code portion of the address of the Supplier  */  
   VendorNumZIP:string,
      /**  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  */  
   VendorNumDefaultFOB:string,
      /**  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  */  
   VendorNumTermsCode:string,
      /**  Second address line of the Supplier  */  
   VendorNumAddress2:string,
      /**  Country Name. Printed as last line of mailing address. Can be blank.  */  
   VendorNumCountry:string,
      /**  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  */  
   VendorNumName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PeriodicityListTableset{
   PeriodicityList:Erp_Tablesets_PeriodicityListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_PeriodicityRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Unique identifier of this Site assigned by the user.  */  
   Plant:string,
      /**  A unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  */  
   VendorNum:number,
      /**  Vendor Purchase Point  */  
   PurPoint:string,
      /**  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  */  
   CustNum:number,
      /**  The ID assigned by the user which makes this record unique for the customer.  When a customer is created a ShipTo record is automatically created by the system for that customer with a ShipToNum equal to NULL.  */  
   ShipToNum:string,
      /**  Code 1 = Semi-Weekly  */  
   Code1Rules:boolean,
      /**  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   Code1DeliveryDay1:number,
      /**  The day of the week for the second delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   Code1DeliveryDay2:number,
      /**  Code 2 = Daily  */  
   Code2Rules:boolean,
      /**  Are deliveries required on Saturday and Sunday?  */  
   Code2IncludeSatSun:boolean,
      /**  Code 3 = Monthly Forward  */  
   Code3Rules:boolean,
      /**  The day of the week for the first delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   Code3DeliveryDay1:number,
      /**  The week number in the month that the delivery is required.  Valid values are 1-5.  */  
   Code3WeekNumberInMonth:number,
      /**  Code 4 = Weekly Forward  */  
   Code4Rules:boolean,
      /**  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   Code4DeliveryDayInWeek:number,
      /**  Code 5 = Weekly Not Last Week of the Month  */  
   Code5Rules:boolean,
      /**  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   Code5DeliveryDayInWeek:number,
      /**  Code 6 = Nth Day of the Month  */  
   Code6Rules:boolean,
      /**  The day of the month for the delivery.  Valid values are 1-31.  */  
   Code6DeliveryDayInMonth:number,
      /**  Code 7 = Shipment Day of Week.  */  
   Code7Rules:boolean,
      /**  The day of the week for the delivery.  Valid values:  1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday.  */  
   Code7ShipmentDayInWeek:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   CustomerBTName:string,
   CustomerName:string,
   CustomerCustID:string,
   PlantNameName:string,
   VendorNumCountry:string,
   VendorNumTermsCode:string,
   VendorNumDefaultFOB:string,
   VendorNumVendorID:string,
   VendorNumName:string,
   VendorNumState:string,
   VendorNumAddress1:string,
   VendorNumCurrencyCode:string,
   VendorNumCity:string,
   VendorNumZIP:string,
   VendorNumAddress3:string,
   VendorNumAddress2:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PeriodicityTableset{
   Periodicity:Erp_Tablesets_PeriodicityRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtPeriodicityTableset{
   Periodicity:Erp_Tablesets_PeriodicityRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param plant
   */  
export interface Existplant_input{
   plant:string,
}

export interface Existplant_output{
parameters : {
      /**  output parameters  */  
   exist:boolean,
}
}

   /** Required : 
      @param inCustID
   */  
export interface FindCustNum_input{
      /**  The CustID to get the CustNum for  */  
   inCustID:string,
}

export interface FindCustNum_output{
parameters : {
      /**  output parameters  */  
   outCustNum:number,
   outCustName:string,
}
}

   /** Required : 
      @param VendorID
   */  
export interface FindVendorNum_input{
   VendorID:string,
}

export interface FindVendorNum_output{
parameters : {
      /**  output parameters  */  
   VendorNum:number,
   Vendorname:string,
}
}

   /** Required : 
      @param plant
      @param vendorNum
      @param purPoint
      @param custNum
      @param shipToNum
   */  
export interface GetByID_input{
   plant:string,
   vendorNum:number,
   purPoint:string,
   custNum:number,
   shipToNum:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_PeriodicityTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_PeriodicityTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_PeriodicityTableset[],
}

   /** Required : 
      @param tableName
      @param fieldName
   */  
export interface GetCodeDescList_input{
   tableName:string,
   fieldName:string,
}

export interface GetCodeDescList_output{
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
   returnObj:Erp_Tablesets_PeriodicityListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param plant
      @param vendorNum
      @param purPoint
      @param custNum
   */  
export interface GetNewPeriodicity_input{
   ds:Erp_Tablesets_PeriodicityTableset[],
   plant:string,
   vendorNum:number,
   purPoint:string,
   custNum:number,
}

export interface GetNewPeriodicity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PeriodicityTableset,
}
}

   /** Required : 
      @param whereClausePeriodicity
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClausePeriodicity:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_PeriodicityTableset[],
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
   ds:Erp_Tablesets_UpdExtPeriodicityTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtPeriodicityTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_PeriodicityTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_PeriodicityTableset,
}
}

