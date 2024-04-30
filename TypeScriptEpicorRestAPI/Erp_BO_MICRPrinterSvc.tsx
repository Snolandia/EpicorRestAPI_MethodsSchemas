import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.MICRPrinterSvc
// Description: Initializes a new class of "MICRPrinterSvc" />.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/$metadata", {
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
   Description: Get MICRPrinters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MICRPrinters
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MICRPrinterRow
   */  
export function get_MICRPrinters(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MICRPrinterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/MICRPrinters", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MICRPrinterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MICRPrinters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MICRPrinterRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Erp.Tablesets.MICRPrinterRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MICRPrinters(requestBody:Erp_Tablesets_MICRPrinterRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/MICRPrinters", {
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
   Summary: Calls GetByID to retrieve the MICRPrinter item
   Description: Calls GetByID to retrieve the MICRPrinter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MICRPrinter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MICRPrinterID Desc: MICRPrinterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Erp.Tablesets.MICRPrinterRow
   */  
export function get_MICRPrinters_Company_MICRPrinterID(Company:string, MICRPrinterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Erp_Tablesets_MICRPrinterRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/MICRPrinters(" + Company + "," + MICRPrinterID + ")", {
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
         resolve(data as Erp_Tablesets_MICRPrinterRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update MICRPrinter for the service
   Description: Calls UpdateExt to update MICRPrinter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MICRPrinter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MICRPrinterID Desc: MICRPrinterID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Erp.Tablesets.MICRPrinterRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_MICRPrinters_Company_MICRPrinterID(Company:string, MICRPrinterID:string, requestBody:Erp_Tablesets_MICRPrinterRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/MICRPrinters(" + Company + "," + MICRPrinterID + ")", {
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
   Summary: Call UpdateExt to delete MICRPrinter item
   Description: Call UpdateExt to delete MICRPrinter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MICRPrinter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param MICRPrinterID Desc: MICRPrinterID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_MICRPrinters_Company_MICRPrinterID(Company:string, MICRPrinterID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/MICRPrinters(" + Company + "," + MICRPrinterID + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MICRPrinterListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MICRPrinterListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MICRPrinterListRow)
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
export function get_GetRows(whereClauseMICRPrinter:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseMICRPrinter!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseMICRPrinter=" + whereClauseMICRPrinter
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/GetRows" + params, {
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
export function get_GetByID(miCRPrinterID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof miCRPrinterID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "miCRPrinterID=" + miCRPrinterID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/GetByID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/GetList" + params, {
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
   Summary: Invoke method ExistsDefaultCompanyMICRPrinter
   Description: Check if already exists a default MICR printer to print checks.
   OperationID: ExistsDefaultCompanyMICRPrinter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExistsDefaultCompanyMICRPrinter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsDefaultCompanyMICRPrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsDefaultCompanyMICRPrinter(requestBody:ExistsDefaultCompanyMICRPrinter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExistsDefaultCompanyMICRPrinter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/ExistsDefaultCompanyMICRPrinter", {
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
         resolve(data as ExistsDefaultCompanyMICRPrinter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method IsClientDefaultCompanyMICRPrinter
   Description: Check if the default MICR printer is Client or Server printer.
   OperationID: IsClientDefaultCompanyMICRPrinter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/IsClientDefaultCompanyMICRPrinter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/IsClientDefaultCompanyMICRPrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_IsClientDefaultCompanyMICRPrinter(requestBody:IsClientDefaultCompanyMICRPrinter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<IsClientDefaultCompanyMICRPrinter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/IsClientDefaultCompanyMICRPrinter", {
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
         resolve(data as IsClientDefaultCompanyMICRPrinter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistsPrinterID
   Description: Validates if Printer exists
   OperationID: ExistsPrinterID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExistsPrinterID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsPrinterID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsPrinterID(requestBody:ExistsPrinterID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExistsPrinterID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/ExistsPrinterID", {
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
         resolve(data as ExistsPrinterID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExistsOtherDefaultMICRPrinter
   Description: Validates other MICR Printer is set as default
   OperationID: ExistsOtherDefaultMICRPrinter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExistsOtherDefaultMICRPrinter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExistsOtherDefaultMICRPrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExistsOtherDefaultMICRPrinter(requestBody:ExistsOtherDefaultMICRPrinter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExistsOtherDefaultMICRPrinter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/ExistsOtherDefaultMICRPrinter", {
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
         resolve(data as ExistsOtherDefaultMICRPrinter_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSignatureImage
   Description: Get Signature image with line overlaid.
   OperationID: GetSignatureImage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSignatureImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSignatureImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSignatureImage(requestBody:GetSignatureImage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSignatureImage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/GetSignatureImage", {
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
         resolve(data as GetSignatureImage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMICRPrinter
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewMICRPrinter
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMICRPrinter_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMICRPrinter_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMICRPrinter(requestBody:GetNewMICRPrinter_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMICRPrinter_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/GetNewMICRPrinter", {
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
         resolve(data as GetNewMICRPrinter_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MICRPrinterSvc/UpdateExt", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MICRPrinterListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MICRPrinterListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MICRPrinterRow{
   "odatametadata":string,
   "value":Erp_Tablesets_MICRPrinterRow,
}

export interface Erp_Tablesets_MICRPrinterListRow{
      /**  Company  */  
   "Company":string,
      /**  ID for MICR Printer.  */  
   "MICRPrinterID":string,
      /**  Defines if the MICR Printer is the default or not.  */  
   "DefaultPrinter":boolean,
      /**  Tells the reader or sorter that next section of the MICR line represents the account number.  */  
   "OnUsSymbol":string,
      /**  Tells the reader/sorter that the numbers between these symbols identify the institution upon which the check is drawn  */  
   "TransitSymbol":string,
      /**  The dash symbol is sometimes used as a separator within the On Us field.  */  
   "DashSymbol":string,
      /**  Font used to print MICR checks.  */  
   "MICRFont":string,
      /**  ID for Printer used to print MICR cheks.  */  
   "PrinterID":string,
      /**  Signature type, stores I when is Image and T when is text.  */  
   "SignatureType":string,
      /**  ImageID for the image used as signature.  */  
   "SignatureImageID":string,
      /**  Font used when printing the signature.  */  
   "SignatureFont":string,
      /**  First line for signature's text.  */  
   "SignatureText01":string,
      /**  Second line for signature's text.  */  
   "SignatureText02":string,
      /**  Third line for signature's text.  */  
   "SignatureText03":string,
      /**  Fourth line for signature's text.  */  
   "SignatureText04":string,
      /**  Fifth line for signature's text.  */  
   "SignatureText05":string,
      /**  Sixth line for signature's text.  */  
   "SignatureText06":string,
      /**  Logo type, stores I when is Image and T when is text.  */  
   "LogoType":string,
      /**  ImageID for the image used as logo.  */  
   "LogoImageID":string,
      /**  Font used when printing the logo.  */  
   "LogoFont":string,
      /**  First line for logo's text.  */  
   "LogoText01":string,
      /**  Second line for logo's text.  */  
   "LogoText02":string,
      /**  Third line for logo's text.  */  
   "LogoText03":string,
      /**  Fourth line for logo's text.  */  
   "LogoText04":string,
      /**  Fifth line for logo's text.  */  
   "LogoText05":string,
      /**  Sixth line for logo's text.  */  
   "LogoText06":string,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Erp_Tablesets_MICRPrinterRow{
      /**  Company  */  
   "Company":string,
      /**  ID for MICR Printer.  */  
   "MICRPrinterID":string,
      /**  Defines if the MICR Printer is the default or not.  */  
   "DefaultPrinter":boolean,
      /**  Tells the reader or sorter that next section of the MICR line represents the account number.  */  
   "OnUsSymbol":string,
      /**  Tells the reader/sorter that the numbers between these symbols identify the institution upon which the check is drawn  */  
   "TransitSymbol":string,
      /**  The dash symbol is sometimes used as a separator within the On Us field.  */  
   "DashSymbol":string,
      /**  Font used to print MICR checks.  */  
   "MICRFont":string,
      /**  ID for Printer used to print MICR cheks.  */  
   "PrinterID":string,
      /**  Signature type, stores I when is Image and T when is text.  */  
   "SignatureType":string,
      /**  ImageID for the image used as signature.  */  
   "SignatureImageID":string,
      /**  Font used when printing the signature.  */  
   "SignatureFont":string,
      /**  First line for signature's text.  */  
   "SignatureText01":string,
      /**  Second line for signature's text.  */  
   "SignatureText02":string,
      /**  Third line for signature's text.  */  
   "SignatureText03":string,
      /**  Fourth line for signature's text.  */  
   "SignatureText04":string,
      /**  Fifth line for signature's text.  */  
   "SignatureText05":string,
      /**  Sixth line for signature's text.  */  
   "SignatureText06":string,
      /**  Logo type, stores I when is Image and T when is text.  */  
   "LogoType":string,
      /**  ImageID for the image used as logo.  */  
   "LogoImageID":string,
      /**  Font used when printing the logo.  */  
   "LogoFont":string,
      /**  First line for logo's text.  */  
   "LogoText01":string,
      /**  Second line for logo's text.  */  
   "LogoText02":string,
      /**  Third line for logo's text.  */  
   "LogoText03":string,
      /**  Fourth line for logo's text.  */  
   "LogoText04":string,
      /**  Fifth line for logo's text.  */  
   "LogoText05":string,
      /**  Sixth line for logo's text.  */  
   "LogoText06":string,
      /**  Defines whether is a client printer or server printer.  */  
   "IsClient":boolean,
      /**  CreatedBy  */  
   "CreatedBy":string,
      /**  CreatedOn  */  
   "CreatedOn":string,
      /**  ChangedBy  */  
   "ChangedBy":string,
      /**  ChangedOn  */  
   "ChangedOn":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
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
      @param miCRPrinterID
   */  
export interface DeleteByID_input{
   miCRPrinterID:string,
}

export interface DeleteByID_output{
}

export interface Erp_Tablesets_MICRPrinterListRow{
      /**  Company  */  
   Company:string,
      /**  ID for MICR Printer.  */  
   MICRPrinterID:string,
      /**  Defines if the MICR Printer is the default or not.  */  
   DefaultPrinter:boolean,
      /**  Tells the reader or sorter that next section of the MICR line represents the account number.  */  
   OnUsSymbol:string,
      /**  Tells the reader/sorter that the numbers between these symbols identify the institution upon which the check is drawn  */  
   TransitSymbol:string,
      /**  The dash symbol is sometimes used as a separator within the On Us field.  */  
   DashSymbol:string,
      /**  Font used to print MICR checks.  */  
   MICRFont:string,
      /**  ID for Printer used to print MICR cheks.  */  
   PrinterID:string,
      /**  Signature type, stores I when is Image and T when is text.  */  
   SignatureType:string,
      /**  ImageID for the image used as signature.  */  
   SignatureImageID:string,
      /**  Font used when printing the signature.  */  
   SignatureFont:string,
      /**  First line for signature's text.  */  
   SignatureText01:string,
      /**  Second line for signature's text.  */  
   SignatureText02:string,
      /**  Third line for signature's text.  */  
   SignatureText03:string,
      /**  Fourth line for signature's text.  */  
   SignatureText04:string,
      /**  Fifth line for signature's text.  */  
   SignatureText05:string,
      /**  Sixth line for signature's text.  */  
   SignatureText06:string,
      /**  Logo type, stores I when is Image and T when is text.  */  
   LogoType:string,
      /**  ImageID for the image used as logo.  */  
   LogoImageID:string,
      /**  Font used when printing the logo.  */  
   LogoFont:string,
      /**  First line for logo's text.  */  
   LogoText01:string,
      /**  Second line for logo's text.  */  
   LogoText02:string,
      /**  Third line for logo's text.  */  
   LogoText03:string,
      /**  Fourth line for logo's text.  */  
   LogoText04:string,
      /**  Fifth line for logo's text.  */  
   LogoText05:string,
      /**  Sixth line for logo's text.  */  
   LogoText06:string,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MICRPrinterListTableset{
   MICRPrinterList:Erp_Tablesets_MICRPrinterListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_MICRPrinterRow{
      /**  Company  */  
   Company:string,
      /**  ID for MICR Printer.  */  
   MICRPrinterID:string,
      /**  Defines if the MICR Printer is the default or not.  */  
   DefaultPrinter:boolean,
      /**  Tells the reader or sorter that next section of the MICR line represents the account number.  */  
   OnUsSymbol:string,
      /**  Tells the reader/sorter that the numbers between these symbols identify the institution upon which the check is drawn  */  
   TransitSymbol:string,
      /**  The dash symbol is sometimes used as a separator within the On Us field.  */  
   DashSymbol:string,
      /**  Font used to print MICR checks.  */  
   MICRFont:string,
      /**  ID for Printer used to print MICR cheks.  */  
   PrinterID:string,
      /**  Signature type, stores I when is Image and T when is text.  */  
   SignatureType:string,
      /**  ImageID for the image used as signature.  */  
   SignatureImageID:string,
      /**  Font used when printing the signature.  */  
   SignatureFont:string,
      /**  First line for signature's text.  */  
   SignatureText01:string,
      /**  Second line for signature's text.  */  
   SignatureText02:string,
      /**  Third line for signature's text.  */  
   SignatureText03:string,
      /**  Fourth line for signature's text.  */  
   SignatureText04:string,
      /**  Fifth line for signature's text.  */  
   SignatureText05:string,
      /**  Sixth line for signature's text.  */  
   SignatureText06:string,
      /**  Logo type, stores I when is Image and T when is text.  */  
   LogoType:string,
      /**  ImageID for the image used as logo.  */  
   LogoImageID:string,
      /**  Font used when printing the logo.  */  
   LogoFont:string,
      /**  First line for logo's text.  */  
   LogoText01:string,
      /**  Second line for logo's text.  */  
   LogoText02:string,
      /**  Third line for logo's text.  */  
   LogoText03:string,
      /**  Fourth line for logo's text.  */  
   LogoText04:string,
      /**  Fifth line for logo's text.  */  
   LogoText05:string,
      /**  Sixth line for logo's text.  */  
   LogoText06:string,
      /**  Defines whether is a client printer or server printer.  */  
   IsClient:boolean,
      /**  CreatedBy  */  
   CreatedBy:string,
      /**  CreatedOn  */  
   CreatedOn:string,
      /**  ChangedBy  */  
   ChangedBy:string,
      /**  ChangedOn  */  
   ChangedOn:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MICRPrinterTableset{
   MICRPrinter:Erp_Tablesets_MICRPrinterRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_UpdExtMICRPrinterTableset{
   MICRPrinter:Erp_Tablesets_MICRPrinterRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param currentCompany
   */  
export interface ExistsDefaultCompanyMICRPrinter_input{
      /**  Session Company.  */  
   currentCompany:string,
}

export interface ExistsDefaultCompanyMICRPrinter_output{
   returnObj:boolean,
}

   /** Required : 
      @param MICRPrinterID
   */  
export interface ExistsOtherDefaultMICRPrinter_input{
      /**  MICRPrinterID  */  
   MICRPrinterID:string,
}

export interface ExistsOtherDefaultMICRPrinter_output{
   returnObj:boolean,
}

   /** Required : 
      @param PrinterID
   */  
export interface ExistsPrinterID_input{
      /**  PrinterID  */  
   PrinterID:string,
}

export interface ExistsPrinterID_output{
   returnObj:boolean,
}

   /** Required : 
      @param miCRPrinterID
   */  
export interface GetByID_input{
   miCRPrinterID:string,
}

export interface GetByID_output{
   returnObj:Erp_Tablesets_MICRPrinterTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Erp_Tablesets_MICRPrinterTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Erp_Tablesets_MICRPrinterTableset[],
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
   returnObj:Erp_Tablesets_MICRPrinterListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewMICRPrinter_input{
   ds:Erp_Tablesets_MICRPrinterTableset[],
}

export interface GetNewMICRPrinter_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MICRPrinterTableset,
}
}

   /** Required : 
      @param whereClauseMICRPrinter
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseMICRPrinter:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_MICRPrinterTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param imageID
   */  
export interface GetSignatureImage_input{
   imageID:string,
}

export interface GetSignatureImage_output{
   returnObj:string,
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
      @param currentCompany
   */  
export interface IsClientDefaultCompanyMICRPrinter_input{
      /**  Session Company.  */  
   currentCompany:string,
}

export interface IsClientDefaultCompanyMICRPrinter_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Erp_Tablesets_UpdExtMICRPrinterTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UpdExtMICRPrinterTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_MICRPrinterTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MICRPrinterTableset,
}
}

