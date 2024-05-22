import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Ice.BO.ReportSvc
// Description: Business Logic for the Report Object.
Report Object establishes the existence of a report.
The following tables comprise a report object
Report, ReportStyle, ReportDefaultStyle.
ReportDefaultStyle is not exposed to the UI. Instead a logical table ReportComp is created.
ReportComp represents if a style is valid for a company and if it's the default for the company.
There is no GetNew methods for ReportComp, all companies are set in the dataset.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/$metadata", {
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
   Description: Get Reports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Reports
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportRow
   */  
export function get_Reports(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Reports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ReportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ReportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Reports(requestBody:Ice_Tablesets_ReportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports", {
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
   Summary: Calls GetByID to retrieve the Report item
   Description: Calls GetByID to retrieve the Report item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Report
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ReportRow
   */  
export function get_Reports_ReportID(ReportID:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ReportRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports(" + ReportID + ")", {
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
         resolve(data as Ice_Tablesets_ReportRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update Report for the service
   Description: Calls UpdateExt to update Report. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Report
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ReportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_Reports_ReportID(ReportID:string, requestBody:Ice_Tablesets_ReportRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports(" + ReportID + ")", {
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
   Summary: Call UpdateExt to delete Report item
   Description: Call UpdateExt to delete Report item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Report
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_Reports_ReportID(ReportID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports(" + ReportID + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get ReportStyles items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReportStyles1
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportStyleRow
   */  
export function get_Reports_ReportID_ReportStyles(ReportID:string, select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports(" + ReportID + ")/ReportStyles", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ReportStyle item
   Description: Calls GetByID to retrieve the ReportStyle item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportStyle1
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ReportStyleRow
   */  
export function get_Reports_ReportID_ReportStyles_ReportID_StyleNum(ReportID:string, StyleNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ReportStyleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Reports(" + ReportID + ")/ReportStyles(" + ReportID + "," + StyleNum + ")", {
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
         resolve(data as Ice_Tablesets_ReportStyleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get ReportStyles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReportStyles
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportStyleRow
   */  
export function get_ReportStyles(select?:string, expand?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReportStyles
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ReportStyleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ReportStyleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReportStyles(requestBody:Ice_Tablesets_ReportStyleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles", {
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
   Summary: Calls GetByID to retrieve the ReportStyle item
   Description: Calls GetByID to retrieve the ReportStyle item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportStyle
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param expand Desc: Odata expand to child
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ReportStyleRow
   */  
export function get_ReportStyles_ReportID_StyleNum(ReportID:string, StyleNum:string, select?:string, expand?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ReportStyleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")", {
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
         resolve(data as Ice_Tablesets_ReportStyleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ReportStyle for the service
   Description: Calls UpdateExt to update ReportStyle. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReportStyle
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ReportStyleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ReportStyles_ReportID_StyleNum(ReportID:string, StyleNum:string, requestBody:Ice_Tablesets_ReportStyleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")", {
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
   Summary: Call UpdateExt to delete ReportStyle item
   Description: Call UpdateExt to delete ReportStyle item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReportStyle
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ReportStyles_ReportID_StyleNum(ReportID:string, StyleNum:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")", {
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
   Summary: Calls GetByID for the service
   Description: Get RptStylePrinters items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RptStylePrinters1
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStylePrintersRow
   */  
export function get_ReportStyles_ReportID_StyleNum_RptStylePrinters(ReportID:string, StyleNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStylePrintersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")/RptStylePrinters", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStylePrintersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the RptStylePrinter item
   Description: Calls GetByID to retrieve the RptStylePrinter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStylePrinter1
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param PrinterID Desc: PrinterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptStylePrintersRow
   */  
export function get_ReportStyles_ReportID_StyleNum_RptStylePrinters_Company_ReportID_StyleNum_PrinterID(ReportID:string, StyleNum:string, Company:string, PrinterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptStylePrintersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")/RptStylePrinters(" + Company + "," + ReportID + "," + StyleNum + "," + PrinterID + ")", {
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
         resolve(data as Ice_Tablesets_RptStylePrintersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ReportStyleImages items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReportStyleImages1
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportStyleImageRow
   */  
export function get_ReportStyles_ReportID_StyleNum_ReportStyleImages(ReportID:string, StyleNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleImageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")/ReportStyleImages", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleImageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ReportStyleImage item
   Description: Calls GetByID to retrieve the ReportStyleImage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportStyleImage1
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param ReportStyleImageName Desc: ReportStyleImageName   Required: True   Allow empty value : True
      @param ImageCompany Desc: ImageCompany   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ReportStyleImageRow
   */  
export function get_ReportStyles_ReportID_StyleNum_ReportStyleImages_ReportID_StyleNum_ReportStyleImageName_ImageCompany(ReportID:string, StyleNum:string, ReportStyleImageName:string, ImageCompany:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ReportStyleImageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")/ReportStyleImages(" + ReportID + "," + StyleNum + "," + ReportStyleImageName + "," + ImageCompany + ")", {
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
         resolve(data as Ice_Tablesets_ReportStyleImageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID for the service
   Description: Get ReportStyleRules items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_ReportStyleRules1
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportStyleRuleRow
   */  
export function get_ReportStyles_ReportID_StyleNum_ReportStyleRules(ReportID:string, StyleNum:string, select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")/ReportStyleRules", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetByID to retrieve the ReportStyleRule item
   Description: Calls GetByID to retrieve the ReportStyleRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportStyleRule1
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ReportStyleRuleRow
   */  
export function get_ReportStyles_ReportID_StyleNum_ReportStyleRules_ReportID_StyleNum_SysRowID(ReportID:string, StyleNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ReportStyleRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyles(" + ReportID + "," + StyleNum + ")/ReportStyleRules(" + ReportID + "," + StyleNum + "," + SysRowID + ")", {
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
         resolve(data as Ice_Tablesets_ReportStyleRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls GetRows for the service
   Description: Get RptStylePrinters items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RptStylePrinters
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.RptStylePrintersRow
   */  
export function get_RptStylePrinters(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStylePrintersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/RptStylePrinters", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStylePrintersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RptStylePrinters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.RptStylePrintersRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.RptStylePrintersRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RptStylePrinters(requestBody:Ice_Tablesets_RptStylePrintersRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/RptStylePrinters", {
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
   Summary: Calls GetByID to retrieve the RptStylePrinter item
   Description: Calls GetByID to retrieve the RptStylePrinter item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RptStylePrinter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param PrinterID Desc: PrinterID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.RptStylePrintersRow
   */  
export function get_RptStylePrinters_Company_ReportID_StyleNum_PrinterID(Company:string, ReportID:string, StyleNum:string, PrinterID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_RptStylePrintersRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/RptStylePrinters(" + Company + "," + ReportID + "," + StyleNum + "," + PrinterID + ")", {
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
         resolve(data as Ice_Tablesets_RptStylePrintersRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update RptStylePrinter for the service
   Description: Calls UpdateExt to update RptStylePrinter. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RptStylePrinter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param PrinterID Desc: PrinterID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.RptStylePrintersRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_RptStylePrinters_Company_ReportID_StyleNum_PrinterID(Company:string, ReportID:string, StyleNum:string, PrinterID:string, requestBody:Ice_Tablesets_RptStylePrintersRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/RptStylePrinters(" + Company + "," + ReportID + "," + StyleNum + "," + PrinterID + ")", {
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
   Summary: Call UpdateExt to delete RptStylePrinter item
   Description: Call UpdateExt to delete RptStylePrinter item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RptStylePrinter
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param PrinterID Desc: PrinterID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_RptStylePrinters_Company_ReportID_StyleNum_PrinterID(Company:string, ReportID:string, StyleNum:string, PrinterID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/RptStylePrinters(" + Company + "," + ReportID + "," + StyleNum + "," + PrinterID + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get ReportStyleImages items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReportStyleImages
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportStyleImageRow
   */  
export function get_ReportStyleImages(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleImageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleImages", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleImageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReportStyleImages
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ReportStyleImageRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ReportStyleImageRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReportStyleImages(requestBody:Ice_Tablesets_ReportStyleImageRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleImages", {
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
   Summary: Calls GetByID to retrieve the ReportStyleImage item
   Description: Calls GetByID to retrieve the ReportStyleImage item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportStyleImage
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param ReportStyleImageName Desc: ReportStyleImageName   Required: True   Allow empty value : True
      @param ImageCompany Desc: ImageCompany   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ReportStyleImageRow
   */  
export function get_ReportStyleImages_ReportID_StyleNum_ReportStyleImageName_ImageCompany(ReportID:string, StyleNum:string, ReportStyleImageName:string, ImageCompany:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ReportStyleImageRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleImages(" + ReportID + "," + StyleNum + "," + ReportStyleImageName + "," + ImageCompany + ")", {
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
         resolve(data as Ice_Tablesets_ReportStyleImageRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ReportStyleImage for the service
   Description: Calls UpdateExt to update ReportStyleImage. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReportStyleImage
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param ReportStyleImageName Desc: ReportStyleImageName   Required: True   Allow empty value : True
      @param ImageCompany Desc: ImageCompany   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ReportStyleImageRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ReportStyleImages_ReportID_StyleNum_ReportStyleImageName_ImageCompany(ReportID:string, StyleNum:string, ReportStyleImageName:string, ImageCompany:string, requestBody:Ice_Tablesets_ReportStyleImageRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleImages(" + ReportID + "," + StyleNum + "," + ReportStyleImageName + "," + ImageCompany + ")", {
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
   Summary: Call UpdateExt to delete ReportStyleImage item
   Description: Call UpdateExt to delete ReportStyleImage item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReportStyleImage
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param ReportStyleImageName Desc: ReportStyleImageName   Required: True   Allow empty value : True
      @param ImageCompany Desc: ImageCompany   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ReportStyleImages_ReportID_StyleNum_ReportStyleImageName_ImageCompany(ReportID:string, StyleNum:string, ReportStyleImageName:string, ImageCompany:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleImages(" + ReportID + "," + StyleNum + "," + ReportStyleImageName + "," + ImageCompany + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get ReportStyleRules items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReportStyleRules
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportStyleRuleRow
   */  
export function get_ReportStyleRules(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleRules", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReportStyleRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ReportStyleRuleRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ReportStyleRuleRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReportStyleRules(requestBody:Ice_Tablesets_ReportStyleRuleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleRules", {
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
   Summary: Calls GetByID to retrieve the ReportStyleRule item
   Description: Calls GetByID to retrieve the ReportStyleRule item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportStyleRule
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ReportStyleRuleRow
   */  
export function get_ReportStyleRules_ReportID_StyleNum_SysRowID(ReportID:string, StyleNum:string, SysRowID:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ReportStyleRuleRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleRules(" + ReportID + "," + StyleNum + "," + SysRowID + ")", {
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
         resolve(data as Ice_Tablesets_ReportStyleRuleRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ReportStyleRule for the service
   Description: Calls UpdateExt to update ReportStyleRule. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReportStyleRule
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ReportStyleRuleRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ReportStyleRules_ReportID_StyleNum_SysRowID(ReportID:string, StyleNum:string, SysRowID:string, requestBody:Ice_Tablesets_ReportStyleRuleRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleRules(" + ReportID + "," + StyleNum + "," + SysRowID + ")", {
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
   Summary: Call UpdateExt to delete ReportStyleRule item
   Description: Call UpdateExt to delete ReportStyleRule item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReportStyleRule
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param SysRowID Desc: SysRowID   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ReportStyleRules_ReportID_StyleNum_SysRowID(ReportID:string, StyleNum:string, SysRowID:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportStyleRules(" + ReportID + "," + StyleNum + "," + SysRowID + ")", {
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
   Summary: Calls GetRows for the service
   Description: Get ReportComps items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_ReportComps
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param orderby Desc: Odata sort results
      @param top Desc: Odata top results
      @param skip Desc: Odata skip results
      @param inlinecount Desc: Odata.count value
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportCompRow
   */  
export function get_ReportComps(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportComps", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportCompRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_ReportComps
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: Input parameters  => reference#/components/schemas/Ice.Tablesets.ReportCompRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference #/components/schemas/Ice.Tablesets.ReportCompRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReportComps(requestBody:Ice_Tablesets_ReportCompRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportComps", {
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
   Summary: Calls GetByID to retrieve the ReportComp item
   Description: Calls GetByID to retrieve the ReportComp item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_ReportComp
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param select Desc: Odata select comma delimited list of fields
      @param filter Desc: Odata filter results
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      200 Desc: OK => reference #/components/schemas/Ice.Tablesets.ReportCompRow
   */  
export function get_ReportComps_ReportID_StyleNum_Company(ReportID:string, StyleNum:string, Company:string, select?:string, filter?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Ice_Tablesets_ReportCompRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportComps(" + ReportID + "," + StyleNum + "," + Company + ")", {
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
         resolve(data as Ice_Tablesets_ReportCompRow)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Calls UpdateExt to update ReportComp for the service
   Description: Calls UpdateExt to update ReportComp. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_ReportComp
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
      @param requestBody  Desc: input params  => reference#/components/schemas/Ice.Tablesets.ReportCompRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function patch_ReportComps_ReportID_StyleNum_Company(ReportID:string, StyleNum:string, Company:string, requestBody:Ice_Tablesets_ReportCompRow, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportComps(" + ReportID + "," + StyleNum + "," + Company + ")", {
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
   Summary: Call UpdateExt to delete ReportComp item
   Description: Call UpdateExt to delete ReportComp item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_ReportComp
      @param ReportID Desc: ReportID   Required: True   Allow empty value : True
      @param StyleNum Desc: StyleNum   Required: True
      @param Company Desc: Company   Required: True   Allow empty value : True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas headers
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function delete_ReportComps_ReportID_StyleNum_Company(ReportID:string, StyleNum:string, Company:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<any>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ReportComps(" + ReportID + "," + StyleNum + "," + Company + ")", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Ice.Tablesets.ReportListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportListRow)
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function get_GetRows(whereClauseReport:string, whereClauseReportStyle:string, whereClauseRptStylePrinters:string, whereClauseReportStyleImage:string, whereClauseReportStyleRule:string, whereClauseReportComp:string, pageSize:string, absolutePage:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof whereClauseReport!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseReport=" + whereClauseReport
   }
   if(typeof whereClauseReportStyle!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseReportStyle=" + whereClauseReportStyle
   }
   if(typeof whereClauseRptStylePrinters!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseRptStylePrinters=" + whereClauseRptStylePrinters
   }
   if(typeof whereClauseReportStyleImage!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseReportStyleImage=" + whereClauseReportStyleImage
   }
   if(typeof whereClauseReportStyleRule!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseReportStyleRule=" + whereClauseReportStyleRule
   }
   if(typeof whereClauseReportComp!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "whereClauseReportComp=" + whereClauseReportComp
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetRows" + params, {
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
export function get_GetByID(reportID:string, epicorHeaders?:Headers){
   var firstParam = true
   var params = ""
   if(typeof reportID!== 'undefined'){
      if(firstParam){
         params += "?"
         firstParam = false
      }else{
         params += "&"
      }
      params += "reportID=" + reportID
   }

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetByID" + params, {
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
   Summary: Invoke method VerifyCertCanBeUsedForReportSigning
   Description: Verifies that the specified cert can be used to digitally sign a report PDF.
Cert must have both public and private keys and be flagged as exportable.
   OperationID: VerifyCertCanBeUsedForReportSigning
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VerifyCertCanBeUsedForReportSigning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyCertCanBeUsedForReportSigning_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifyCertCanBeUsedForReportSigning(requestBody:VerifyCertCanBeUsedForReportSigning_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VerifyCertCanBeUsedForReportSigning_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/VerifyCertCanBeUsedForReportSigning", {
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
         resolve(data as VerifyCertCanBeUsedForReportSigning_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOutputEDI
   Description: Set Default OutputEDI after change RptTypeID
   OperationID: OnChangeOutputEDI
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOutputEDI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOutputEDI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOutputEDI(requestBody:OnChangeOutputEDI_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOutputEDI_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/OnChangeOutputEDI", {
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
         resolve(data as OnChangeOutputEDI_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultOutputEDI
   Description: Get default value for OutputEDI
   OperationID: GetDefaultOutputEDI
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDefaultOutputEDI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultOutputEDI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultOutputEDI(requestBody:GetDefaultOutputEDI_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultOutputEDI_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetDefaultOutputEDI", {
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
         resolve(data as GetDefaultOutputEDI_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VerifyRptDataDefHasBQAOrEI
   Description: Verifies the report data definition has a data source with BAQ or EI.
   OperationID: VerifyRptDataDefHasBQAOrEI
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VerifyRptDataDefHasBQAOrEI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyRptDataDefHasBQAOrEI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifyRptDataDefHasBQAOrEI(requestBody:VerifyRptDataDefHasBQAOrEI_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VerifyRptDataDefHasBQAOrEI_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/VerifyRptDataDefHasBQAOrEI", {
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
         resolve(data as VerifyRptDataDefHasBQAOrEI_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AnalyzeRptDataDefForBAQandEI
   Description: Checks the report data definition has data source with BAQ or EI and that it's only BAQ report definition
   OperationID: AnalyzeRptDataDefForBAQandEI
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AnalyzeRptDataDefForBAQandEI_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AnalyzeRptDataDefForBAQandEI_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AnalyzeRptDataDefForBAQandEI(requestBody:AnalyzeRptDataDefForBAQandEI_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AnalyzeRptDataDefForBAQandEI_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/AnalyzeRptDataDefForBAQandEI", {
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
         resolve(data as AnalyzeRptDataDefForBAQandEI_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReportTypeList
   Description: Use to get a sub delimited list of ReportType.RptTypeID and ReportType.RptTypeDescription.
The Code/Description pairs are delimited by the ~ character.
The Code/Description element is sub delimited by the ` character.
   OperationID: GetReportTypeList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportTypeList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReportTypeList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetReportTypeList", {
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
         resolve(data as GetReportTypeList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportReportStyle
   Description: Exports the report style for use by Solution Workbench.
   OperationID: ExportReportStyle
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportReportStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReportStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportReportStyle(requestBody:ExportReportStyle_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportReportStyle_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ExportReportStyle", {
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
         resolve(data as ExportReportStyle_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HasReportStyleImages
   Description: Checks whether report images exist.
   OperationID: HasReportStyleImages
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HasReportStyleImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasReportStyleImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HasReportStyleImages(requestBody:HasReportStyleImages_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HasReportStyleImages_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/HasReportStyleImages", {
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
         resolve(data as HasReportStyleImages_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportReportStyleBySysRowId
   Description: Exports the report style by report style SysRowID for use by Solution Workbench.
   OperationID: ExportReportStyleBySysRowId
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportReportStyleBySysRowId_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReportStyleBySysRowId_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportReportStyleBySysRowId(requestBody:ExportReportStyleBySysRowId_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportReportStyleBySysRowId_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ExportReportStyleBySysRowId", {
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
         resolve(data as ExportReportStyleBySysRowId_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReportStylesBySysRowIds
   Description: Get report styles by report style SysRowIDs for use by Solution Workbench.
   OperationID: GetReportStylesBySysRowIds
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetReportStylesBySysRowIds_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportStylesBySysRowIds_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportStylesBySysRowIds(requestBody:GetReportStylesBySysRowIds_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReportStylesBySysRowIds_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetReportStylesBySysRowIds", {
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
         resolve(data as GetReportStylesBySysRowIds_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportReportStyle
   Description: Imports the report style.
   OperationID: ImportReportStyle
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportReportStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReportStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportReportStyle(requestBody:ImportReportStyle_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportReportStyle_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ImportReportStyle", {
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
         resolve(data as ImportReportStyle_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateReportParamsScreen
   Description: Generate report parameters screen
   OperationID: GenerateReportParamsScreen
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateReportParamsScreen_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateReportParamsScreen_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateReportParamsScreen(requestBody:GenerateReportParamsScreen_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateReportParamsScreen_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GenerateReportParamsScreen", {
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
         resolve(data as GenerateReportParamsScreen_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportReportStyleImages
   Description: Exports the report style images. This is used by Solution Workbench to export images for a report.
   OperationID: ExportReportStyleImages
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportReportStyleImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportReportStyleImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportReportStyleImages(requestBody:ExportReportStyleImages_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportReportStyleImages_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ExportReportStyleImages", {
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
         resolve(data as ExportReportStyleImages_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportReportStyleImages
   Description: Imports the specified previously exported data set.
   OperationID: ImportReportStyleImages
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportReportStyleImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportReportStyleImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportReportStyleImages(requestBody:ImportReportStyleImages_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportReportStyleImages_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ImportReportStyleImages", {
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
         resolve(data as ImportReportStyleImages_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailableDocumentTypes
   Description: Gets the available document types for each kind of action.
   OperationID: GetAvailableDocumentTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableDocumentTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailableDocumentTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailableDocumentTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetAvailableDocumentTypes", {
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
         resolve(data as GetAvailableDocumentTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSsrsReportPageSettings
   Description: Gets the page settings defined in the SSRS report.
   OperationID: GetSsrsReportPageSettings
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSsrsReportPageSettings_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSsrsReportPageSettings_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSsrsReportPageSettings(requestBody:GetSsrsReportPageSettings_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSsrsReportPageSettings_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetSsrsReportPageSettings", {
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
         resolve(data as GetSsrsReportPageSettings_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReportsThatDefaultToEmfRenderFormat
   Description: Gets the reports that default to EMF render format.
   OperationID: GetReportsThatDefaultToEmfRenderFormat
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportsThatDefaultToEmfRenderFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportsThatDefaultToEmfRenderFormat(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReportsThatDefaultToEmfRenderFormat_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetReportsThatDefaultToEmfRenderFormat", {
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
         resolve(data as GetReportsThatDefaultToEmfRenderFormat_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportSsrsRdl
   Description: Imports the SSRS RDL.
   OperationID: ImportSsrsRdl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportSsrsRdl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportSsrsRdl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportSsrsRdl(requestBody:ImportSsrsRdl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportSsrsRdl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ImportSsrsRdl", {
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
         resolve(data as ImportSsrsRdl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportSsrsReports
   Description: Imports the SSRS reports.
   OperationID: ImportSsrsReports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportSsrsReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportSsrsReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportSsrsReports(requestBody:ImportSsrsReports_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportSsrsReports_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ImportSsrsReports", {
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
         resolve(data as ImportSsrsReports_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportSsrsRdl
   Description: Exports the SSRS RDL.
   OperationID: ExportSsrsRdl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportSsrsRdl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportSsrsRdl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportSsrsRdl(requestBody:ExportSsrsRdl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportSsrsRdl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ExportSsrsRdl", {
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
         resolve(data as ExportSsrsRdl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method LoadSsrsRdl
   Description: Exports the SSRS RDL.
   OperationID: LoadSsrsRdl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/LoadSsrsRdl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LoadSsrsRdl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_LoadSsrsRdl(requestBody:LoadSsrsRdl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<LoadSsrsRdl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/LoadSsrsRdl", {
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
         resolve(data as LoadSsrsRdl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExportSsrsReports
   Description: Exports the SSRS reports.
   OperationID: ExportSsrsReports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExportSsrsReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExportSsrsReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExportSsrsReports(requestBody:ExportSsrsReports_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExportSsrsReports_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ExportSsrsReports", {
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
         resolve(data as ExportSsrsReports_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PrepareZipWithSsrsReports
   Description: Collect SSRS reports, prepare ZIP file with it and returns server path (in user directory) to zip file
   OperationID: PrepareZipWithSsrsReports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PrepareZipWithSsrsReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PrepareZipWithSsrsReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PrepareZipWithSsrsReports(requestBody:PrepareZipWithSsrsReports_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PrepareZipWithSsrsReports_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/PrepareZipWithSsrsReports", {
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
         resolve(data as PrepareZipWithSsrsReports_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteZip
   Description: Deletes temporary zip file and folder after downloading
   OperationID: DeleteZip
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteZip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteZip(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteZip_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/DeleteZip", {
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
         resolve(data as DeleteZip_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ExtractAndUploadReportsZip
   Description: Extracts report from uploaded zip file and uploads it to SSRS
   OperationID: ExtractAndUploadReportsZip
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ExtractAndUploadReportsZip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ExtractAndUploadReportsZip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ExtractAndUploadReportsZip(requestBody:ExtractAndUploadReportsZip_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ExtractAndUploadReportsZip_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ExtractAndUploadReportsZip", {
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
         resolve(data as ExtractAndUploadReportsZip_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReportStyleRules
   Description: Returns a list of style numbers that have routing rules for the report
   OperationID: GetReportStyleRules
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetReportStyleRules_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportStyleRules_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportStyleRules(requestBody:GetReportStyleRules_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReportStyleRules_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetReportStyleRules", {
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
         resolve(data as GetReportStyleRules_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopySsrsStyle
   Description: Copies the SSRS report style.
   OperationID: CopySsrsStyle
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopySsrsStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopySsrsStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopySsrsStyle(requestBody:CopySsrsStyle_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopySsrsStyle_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/CopySsrsStyle", {
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
         resolve(data as CopySsrsStyle_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CopyBartenderStyle
   Description: Copies the Bartender report style record.
   OperationID: CopyBartenderStyle
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CopyBartenderStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyBartenderStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CopyBartenderStyle(requestBody:CopyBartenderStyle_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CopyBartenderStyle_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/CopyBartenderStyle", {
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
         resolve(data as CopyBartenderStyle_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CollectReportsForCopyAndCheckForDuplicates
   Description: Retrieves the reports that the user wants to copy from SSRS. Also, retrieves any reports that already
exist in the custom folder. If the reports already exist and have been modified, returns the report with the IsDuplicate flag set.
   OperationID: CollectReportsForCopyAndCheckForDuplicates
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CollectReportsForCopyAndCheckForDuplicates_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CollectReportsForCopyAndCheckForDuplicates_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CollectReportsForCopyAndCheckForDuplicates(requestBody:CollectReportsForCopyAndCheckForDuplicates_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CollectReportsForCopyAndCheckForDuplicates_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/CollectReportsForCopyAndCheckForDuplicates", {
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
         resolve(data as CollectReportsForCopyAndCheckForDuplicates_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CollectReportsForCopyAndCheckForDuplicates2
   Description: Retrieves the reports that the user wants to copy from SSRS. Also, retrieves any reports that already
exist in the custom folder. If the reports already exist and have been modified, returns the report with the IsDuplicate flag set.
   OperationID: CollectReportsForCopyAndCheckForDuplicates2
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CollectReportsForCopyAndCheckForDuplicates2_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CollectReportsForCopyAndCheckForDuplicates2_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CollectReportsForCopyAndCheckForDuplicates2(requestBody:CollectReportsForCopyAndCheckForDuplicates2_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CollectReportsForCopyAndCheckForDuplicates2_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/CollectReportsForCopyAndCheckForDuplicates2", {
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
         resolve(data as CollectReportsForCopyAndCheckForDuplicates2_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateSsrsReport
   Description: Creates the SSRS report and adds it to the SSRS reports.
   OperationID: CreateSsrsReport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateSsrsReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSsrsReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateSsrsReport(requestBody:CreateSsrsReport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateSsrsReport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/CreateSsrsReport", {
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
         resolve(data as CreateSsrsReport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SynchronizeDataset
   Description: Synchronize fields and tables between report definition and SSRS *.rdl file
   OperationID: SynchronizeDataset
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SynchronizeDataset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SynchronizeDataset_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SynchronizeDataset(requestBody:SynchronizeDataset_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SynchronizeDataset_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/SynchronizeDataset", {
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
         resolve(data as SynchronizeDataset_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPrinterPageInformation
   Description: Gets the printer page information for PaperSource and PaperKind. The lists are built
from the .NET enums `System.Drawing.Printing.PaperKind` and
`System.Drawing.Printing.PaperSourceKind`.
   OperationID: GetPrinterPageInformation
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrinterPageInformation_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPrinterPageInformation(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPrinterPageInformation_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetPrinterPageInformation", {
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
         resolve(data as GetPrinterPageInformation_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AnalyzeReportStyle
   Description: Analyze Report Style and Include Missing Report Data Definition Elements
   OperationID: AnalyzeReportStyle
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AnalyzeReportStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AnalyzeReportStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AnalyzeReportStyle(requestBody:AnalyzeReportStyle_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AnalyzeReportStyle_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/AnalyzeReportStyle", {
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
         resolve(data as AnalyzeReportStyle_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VerifyReportStyleRdls
   Description: Gets a list of the RDLs missing from all report styles in all the companies in the database.
   OperationID: VerifyReportStyleRdls
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyReportStyleRdls_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifyReportStyleRdls(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VerifyReportStyleRdls_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/VerifyReportStyleRdls", {
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
         resolve(data as VerifyReportStyleRdls_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetReportStyleHealthCheckStatus
   Description: Gets the report health check status.
   OperationID: GetReportStyleHealthCheckStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetReportStyleHealthCheckStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetReportStyleHealthCheckStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetReportStyleHealthCheckStatus(requestBody:GetReportStyleHealthCheckStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetReportStyleHealthCheckStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetReportStyleHealthCheckStatus", {
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
         resolve(data as GetReportStyleHealthCheckStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetCopiedReportFolders
   Description: Returns the display path for the copied reports. Display path might be different from the actual path
in case of multi-tenancy because the actual path has the tenant identifier in it, while the display path doesn't.
   OperationID: GetCopiedReportFolders
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetCopiedReportFolders_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCopiedReportFolders_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetCopiedReportFolders(requestBody:GetCopiedReportFolders_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetCopiedReportFolders_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetCopiedReportFolders", {
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
         resolve(data as GetCopiedReportFolders_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDisplayPathWithUpdatedFolderName
   Description: Updates folder name in report paths
   OperationID: GetDisplayPathWithUpdatedFolderName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDisplayPathWithUpdatedFolderName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDisplayPathWithUpdatedFolderName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDisplayPathWithUpdatedFolderName(requestBody:GetDisplayPathWithUpdatedFolderName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDisplayPathWithUpdatedFolderName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetDisplayPathWithUpdatedFolderName", {
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
         resolve(data as GetDisplayPathWithUpdatedFolderName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateFolderName
   Description: Validates the custom target folder name that the user entered on the UI. Empty string
and special characters are not allowed.
   OperationID: ValidateFolderName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateFolderName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateFolderName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateFolderName(requestBody:ValidateFolderName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateFolderName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ValidateFolderName", {
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
         resolve(data as ValidateFolderName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAutoProgramList
   Description: Get list of auto programs installed on the server
   OperationID: GetAutoProgramList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAutoProgramList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAutoProgramList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAutoProgramList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetAutoProgramList", {
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
         resolve(data as GetAutoProgramList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetDefaultEDIDefinitionFileName
   Description: Generate default name for EDI definition file
   OperationID: GetDefaultEDIDefinitionFileName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetDefaultEDIDefinitionFileName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultEDIDefinitionFileName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetDefaultEDIDefinitionFileName(requestBody:GetDefaultEDIDefinitionFileName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetDefaultEDIDefinitionFileName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetDefaultEDIDefinitionFileName", {
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
         resolve(data as GetDefaultEDIDefinitionFileName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GenerateEDIDefinitionFile
   Description: Generate EDI Definition file
   OperationID: GenerateEDIDefinitionFile
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GenerateEDIDefinitionFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateEDIDefinitionFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GenerateEDIDefinitionFile(requestBody:GenerateEDIDefinitionFile_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GenerateEDIDefinitionFile_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GenerateEDIDefinitionFile", {
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
         resolve(data as GenerateEDIDefinitionFile_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HasMarkupInDirectoryName
   Description: Checks if the sequence markup is present within the folder names
of the file path.
   OperationID: HasMarkupInDirectoryName
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HasMarkupInDirectoryName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HasMarkupInDirectoryName_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HasMarkupInDirectoryName(requestBody:HasMarkupInDirectoryName_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HasMarkupInDirectoryName_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/HasMarkupInDirectoryName", {
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
         resolve(data as HasMarkupInDirectoryName_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAsymmetricCryptoAlgorithmList
   Description: Get the Asymmetric Encryption algorithm list separated by Ice.Constants.ListSeparator.
   OperationID: GetAsymmetricCryptoAlgorithmList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAsymmetricCryptoAlgorithmList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAsymmetricCryptoAlgorithmList(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAsymmetricCryptoAlgorithmList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetAsymmetricCryptoAlgorithmList", {
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
         resolve(data as GetAsymmetricCryptoAlgorithmList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ImportZippedReports
   Description: Imports the zipped reports to the SSRS server.
   OperationID: ImportZippedReports
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ImportZippedReports_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportZippedReports_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ImportZippedReports(requestBody:ImportZippedReports_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ImportZippedReports_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/ImportZippedReports", {
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
         resolve(data as ImportZippedReports_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReport
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReport_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReport(requestBody:GetNewReport_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReport_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetNewReport", {
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
         resolve(data as GetNewReport_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReportStyle
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReportStyle
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReportStyle_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReportStyle_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReportStyle(requestBody:GetNewReportStyle_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReportStyle_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetNewReportStyle", {
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
         resolve(data as GetNewReportStyle_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewRptStylePrinters
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRptStylePrinters
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewRptStylePrinters_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRptStylePrinters_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewRptStylePrinters(requestBody:GetNewRptStylePrinters_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewRptStylePrinters_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetNewRptStylePrinters", {
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
         resolve(data as GetNewRptStylePrinters_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReportStyleImage
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReportStyleImage
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReportStyleImage_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReportStyleImage_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReportStyleImage(requestBody:GetNewReportStyleImage_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReportStyleImage_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetNewReportStyleImage", {
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
         resolve(data as GetNewReportStyleImage_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReportStyleRule
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewReportStyleRule
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReportStyleRule_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReportStyleRule_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReportStyleRule(requestBody:GetNewReportStyleRule_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReportStyleRule_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetNewReportStyleRule", {
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
         resolve(data as GetNewReportStyleRule_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/DeleteByID", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetList" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetBySysRowID" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/GetBySysRowIDs" + params, {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/Update", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/UpdateExt", {
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

   /**  
   Summary: Invoke method RetrieveReportStyleImages
   Description: Retrieves the Ice.Services.BO.ReportSvc.ReportStyleImage rows for the specified report style and synchronizes with the
SSRS *.rdl files to make sure each named image has a row and no extra rows exist.
   OperationID: RetrieveReportStyleImages
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RetrieveReportStyleImages_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveReportStyleImages_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RetrieveReportStyleImages(requestBody:RetrieveReportStyleImages_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RetrieveReportStyleImages_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Ice.BO.ReportSvc/RetrieveReportStyleImages", {
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
         resolve(data as RetrieveReportStyleImages_output)
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportCompRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ReportCompRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportListRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ReportListRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ReportRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleImageRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ReportStyleImageRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ReportStyleRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_ReportStyleRuleRow{
   "odatametadata":string,
   "value":Ice_Tablesets_ReportStyleRuleRow,
}

export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Ice_Tablesets_RptStylePrintersRow{
   "odatametadata":string,
   "value":Ice_Tablesets_RptStylePrintersRow,
}

export interface Ice_Tablesets_ReportCompRow{
   "ReportID":string,
   "StyleNum":number,
   "Company":string,
   "ValidStyle":boolean,
   "IsDefault":boolean,
   "CompanyName":string,
   "SysRowID":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ReportListRow{
      /**  Report ID  */  
   "ReportID":string,
      /**  Report Description  */  
   "RptDescription":string,
      /**  Name of the BL program file used as a broker when auto-printing Crystal Reports or Bartender Labels from a BAM.  */  
   "AutoProgram":string,
      /**  Indicates if this is a base system report  These are records delived as part of the system and should not be modified by the end user  */  
   "SystemRpt":boolean,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Indicates if the current report can be auto-printed  */  
   "CanAutoPrint":boolean,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ReportRow{
      /**  Report ID  */  
   "ReportID":string,
      /**  Report Description  */  
   "RptDescription":string,
      /**  Name of the BL program file used as a broker when auto-printing Crystal Reports or Bartender Labels from a BAM.  */  
   "AutoProgram":string,
      /**  Indicates if this is a base system report  These are records delived as part of the system and should not be modified by the end user  */  
   "SystemRpt":boolean,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  Company  */  
   "Company":string,
      /**  CompanyVisibility  */  
   "CompanyVisibility":number,
      /**  Indicates if the current report can be auto-printed  */  
   "CanAutoPrint":boolean,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ReportStyleImageRow{
      /**  Company  */  
   "Company":string,
      /**  ReportID  */  
   "ReportID":string,
      /**  StyleNum  */  
   "StyleNum":number,
      /**  ReportStyleImageName  */  
   "ReportStyleImageName":string,
      /**  ImageCompany  */  
   "ImageCompany":string,
      /**  ImageID  */  
   "ImageID":string,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "ImageContent":string,
   "ImageType":string,
   "CategoryID":string,
   "SubcategoryID":string,
   "BitFlag":number,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ReportStyleRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Report ID  */  
   "ReportID":string,
      /**  Report Style Number  */  
   "StyleNum":number,
      /**  Report Style Description  */  
   "StyleDescription":string,
      /**  Foreign key to the ReportType table which defines the type of report (Crystal, EpiForms, etc)  */  
   "RptTypeID":string,
      /**  Program which performs the actual printing  */  
   "PrintProgram":string,
      /**  additonal options/settings required by specfic PrintProgram  */  
   "PrintProgramOptions":string,
      /**  Foreign Key to RptDef table.  */  
   "RptDefID":string,
      /**   Delimited list of company id's that can use this ReportStyle.
Blank = All Companies. This field will not be overlaid during release upgrades.
This field is not intended to be directly updatable. Instead it is exposed to the UI in a separate table (ReportCompany) which is not a physical db table. All Companies are created in ReportCompany. If in the CompanyList, then ReportCompany.ValidStyle = Yes
Delimeter character is global LIST-DELIM value  (~)  */  
   "CompanyList":string,
      /**  This is a Crystal Server Num that is defined in CrystalServer table.  */  
   "ServerNum":number,
      /**   Specifies an output location for Bartender and Outbound EDI Reports to override the default locations:
mfgsysdata\Bartender
mfgsysdata\EDI  */  
   "OutputLocation":string,
      /**  Field to save if file is going to be exported in txt o xml format  */  
   "OutputEDI":string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   "SystemFlag":boolean,
      /**  Country Group Code / Country Code for CSF  */  
   "CGCCode":string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   "SysRevID":number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
      /**  RptCriteriaSetID  */  
   "RptCriteriaSetID":string,
      /**  RptStructuredOutputDefID  */  
   "RptStructuredOutputDefID":string,
      /**  StructuredOutputEnabled  */  
   "StructuredOutputEnabled":boolean,
      /**  RequireSubmissionID  */  
   "RequireSubmissionID":boolean,
      /**  AllowResetAfterSubmit  */  
   "AllowResetAfterSubmit":boolean,
      /**  CertificateID  */  
   "CertificateID":string,
      /**  Language  */  
   "LangNameID":string,
      /**  Culture Format  */  
   "FormatCulture":string,
      /**  StructuredOutputCertificateID  */  
   "StructuredOutputCertificateID":string,
      /**  StructuredOutputAlgorithm  */  
   "StructuredOutputAlgorithm":string,
      /**  True if any data source for this report data definition is related to a BAQ or EI. False in other case.  */  
   "HasBAQOrEI":boolean,
      /**  Flag to indicate if this report style record has an enabled routing rule.  */  
   "RoutingRuleEnabled":boolean,
      /**  Digital cert for signing is an All Company cert.  */  
   "CertificateIsAllComp":boolean,
      /**  Indicates the certificate is a system cert.  */  
   "CertificateIsSystem":boolean,
      /**  Certificate expiration date.  */  
   "CertExpiration":string,
      /**  Report Style status (from HealthCheck).It indicates if there are issues in the report style: 0 - OK, 1 - Missing RDL, etc.  */  
   "Status":number,
      /**  Report Style status message (from HealthCheck).It is a more detailed message with  issues found, ie. the names of the missing RDL files.  */  
   "StatusMessage":string,
   "RptDefSystemFlag":boolean,
   "LangNameIDDescription":string,
   "IsBAQReport":boolean,
   "StructuredOutputCertificateIsAllComp":boolean,
   "StructuredOutputCertificateIsSystem":boolean,
   "StructuredOutputCertificateExpirationDate":string,
   "AllowGenerateEDI":boolean,
   "BitFlag":number,
   "ReportRptDescription":string,
   "RptDefRptDescription":string,
   "RptTypeRptTypeDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_ReportStyleRuleRow{
      /**  Company  */  
   "Company":string,
      /**  ReportID  */  
   "ReportID":string,
      /**  StyleNum  */  
   "StyleNum":number,
      /**  RptDefID  */  
   "RptDefID":string,
      /**  RptTableID  */  
   "RptTableID":string,
      /**  SystemCode  */  
   "SystemCode":string,
      /**  ZDataTableID  */  
   "ZDataTableID":string,
      /**  RuleBody  */  
   "RuleBody":string,
      /**  Thumbnail  */  
   "Thumbnail":string,
      /**  IsEnabled  */  
   "IsEnabled":boolean,
      /**  SysRevID  */  
   "SysRevID":number,
      /**  SysRowID  */  
   "SysRowID":string,
   "BitFlag":number,
   "ReportDataDefinitionRptDescription":string,
   "ReportStyleStyleDescription":string,
      /**  RowMod  */  
   "RowMod":string,
}

export interface Ice_Tablesets_RptStylePrintersRow{
      /**  Company Identifier.  */  
   "Company":string,
      /**  Report  ID  */  
   "ReportID":string,
      /**  Report Style Number  */  
   "StyleNum":number,
      /**  Printer Identifier. (PK)  */  
   "PrinterID":string,
      /**  SystemFlag  */  
   "SystemFlag":boolean,
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
      @param reportID
      @param styleNum
   */  
export interface AnalyzeReportStyle_input{
      /**  The report identifier.  */  
   reportID:string,
      /**  The style number.  */  
   styleNum:number,
}

export interface AnalyzeReportStyle_output{
      /**  The list of changes that were made.  */  
   returnObj:string,
}

   /** Required : 
      @param rptDefId
   */  
export interface AnalyzeRptDataDefForBAQandEI_input{
      /**  Report Data Definition Id  */  
   rptDefId:string,
}

export interface AnalyzeRptDataDefForBAQandEI_output{
parameters : {
      /**  output parameters  */  
   hasBAQorEI:boolean,
   isBAQReport:boolean,
}
}

   /** Required : 
      @param reportID
      @param styleNum
      @param printProgram
      @param ds
   */  
export interface CollectReportsForCopyAndCheckForDuplicates2_input{
      /**  Report identifier  */  
   reportID:string,
      /**  Report Style  */  
   styleNum:number,
      /**  ReportStyle.PrintProgram  */  
   printProgram:string,
   ds:Ice_Tablesets_CopiedReportFoldersTableset[],
}

export interface CollectReportsForCopyAndCheckForDuplicates2_output{
      /**  DataSet with the reports that will be copied. A flag indicates if a report already exists in the target folder  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param reportID
      @param styleNum
      @param userEnteredReportLocation
   */  
export interface CollectReportsForCopyAndCheckForDuplicates_input{
      /**  Report identifier  */  
   reportID:string,
      /**  Report Style  */  
   styleNum:number,
      /**  Custom folder path that the user selected on the UI  */  
   userEnteredReportLocation:any,      //schema had no properties on an object.
}

export interface CollectReportsForCopyAndCheckForDuplicates_output{
      /**  DataSet with the reports that will be copied. A flag indicates if a report already exists in the target folder  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param reportID
      @param styleNum
   */  
export interface CopyBartenderStyle_input{
      /**  The report identifier.  */  
   reportID:string,
      /**  the style number.  */  
   styleNum:number,
}

export interface CopyBartenderStyle_output{
}

   /** Required : 
      @param reportID
      @param styleNum
      @param ds
   */  
export interface CopySsrsStyle_input{
      /**  The report identifier.  */  
   reportID:string,
      /**  The style number.  */  
   styleNum:number,
      /**  The location of the custom reports entered by the user  */  
   ds:any,      //schema had no properties on an object.
}

export interface CopySsrsStyle_output{
}

   /** Required : 
      @param company
      @param reportId
      @param styleNum
      @param forceOverwrite
   */  
export interface CreateSsrsReport_input{
      /**  The company.  */  
   company:string,
      /**  The report identifier.  */  
   reportId:string,
      /**  The style number.  */  
   styleNum:number,
      /**  `true` to force overwrite.  */  
   forceOverwrite:boolean,
}

export interface CreateSsrsReport_output{
      /**  `true` if a new report was created or if report already existed.  */  
   returnObj:boolean,
}

   /** Required : 
      @param reportID
   */  
export interface DeleteByID_input{
   reportID:string,
}

export interface DeleteByID_output{
}

export interface DeleteZip_output{
}

   /** Required : 
      @param sysRowID
   */  
export interface ExportReportStyleBySysRowId_input{
      /**  The report style SysRowID.  */  
   sysRowID:string,
}

export interface ExportReportStyleBySysRowId_output{
   returnObj:Ice_Tablesets_ReportTableset[],
}

   /** Required : 
      @param reportId
      @param styleNumber
   */  
export interface ExportReportStyleImages_input{
      /**  The report identifier.  */  
   reportId:string,
      /**  The style number.  */  
   styleNumber:number,
}

export interface ExportReportStyleImages_output{
      /**  The image information for the specified report style.  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param reportId
      @param styleNumber
   */  
export interface ExportReportStyle_input{
      /**  The report identifier.  */  
   reportId:string,
      /**  The style number.  */  
   styleNumber:number,
}

export interface ExportReportStyle_output{
   returnObj:Ice_Tablesets_ReportTableset[],
}

   /** Required : 
      @param reportPath
   */  
export interface ExportSsrsRdl_input{
      /**  The report path.  */  
   reportPath:string,
}

export interface ExportSsrsRdl_output{
      /**  The SSRS RDL bytes.  */  
   returnObj:string,
}

   /** Required : 
      @param locations
   */  
export interface ExportSsrsReports_input{
      /**  The report locations.  */  
   locations:string,
}

export interface ExportSsrsReports_output{
      /**  The reports and any sub-reports associated with them.  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param printProgram
   */  
export interface ExtractAndUploadReportsZip_input{
   printProgram:string,
}

export interface ExtractAndUploadReportsZip_output{
      /**  List of uploaded reports (for display message)  */  
   returnObj:string,
}

   /** Required : 
      @param reportDefinitionId
      @param ediDefinitionName
   */  
export interface GenerateEDIDefinitionFile_input{
      /**  Report definition Id  */  
   reportDefinitionId:string,
      /**  File name  */  
   ediDefinitionName:string,
}

export interface GenerateEDIDefinitionFile_output{
}

   /** Required : 
      @param reportID
      @param cgcCode
      @param company
   */  
export interface GenerateReportParamsScreen_input{
   reportID:string,
   cgcCode:string,
   company:string,
}

export interface GenerateReportParamsScreen_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   warningText:string,
}
}

export interface GetAsymmetricCryptoAlgorithmList_output{
      /**  List of  Asymmetric Encryption algorithms separated by Ice.Constants.ListSeparator.  */  
   returnObj:string,
}

export interface GetAutoProgramList_output{
      /**  list of auto programs  */  
   returnObj:string,
}

export interface GetAvailableDocumentTypes_output{
parameters : {
      /**  output parameters  */  
   previewTypes:any[],
   printTypes:any[],
   saveTypes:any[],
   emailTypes:any[],
   electronicComplianceTypes:any[],
}
}

   /** Required : 
      @param reportID
   */  
export interface GetByID_input{
   reportID:string,
}

export interface GetByID_output{
   returnObj:Ice_Tablesets_ReportTableset[],
}

   /** Required : 
      @param id
   */  
export interface GetBySysRowID_input{
   id:string,
}

export interface GetBySysRowID_output{
   returnObj:Ice_Tablesets_ReportTableset[],
}

   /** Required : 
      @param ids
   */  
export interface GetBySysRowIDs_input{
   ids:string,
}

export interface GetBySysRowIDs_output{
   returnObj:Ice_Tablesets_ReportTableset[],
}

   /** Required : 
      @param printProgram
   */  
export interface GetCopiedReportFolders_input{
      /**  The reports that are listed on the Report Location field for the report style that is being copied  */  
   printProgram:string,
}

export interface GetCopiedReportFolders_output{
   returnObj:Ice_Tablesets_CopiedReportFoldersTableset[],
}

   /** Required : 
      @param reportDefinitionId
      @param styleNum
      @param printProgramOptions
   */  
export interface GetDefaultEDIDefinitionFileName_input{
      /**  Report Definition Id  */  
   reportDefinitionId:string,
      /**  Style number  */  
   styleNum:number,
      /**  Print program options  */  
   printProgramOptions:string,
}

export interface GetDefaultEDIDefinitionFileName_output{
      /**  Generated file name  */  
   returnObj:string,
}

   /** Required : 
      @param rptTypeID
   */  
export interface GetDefaultOutputEDI_input{
      /**  Report Type ID  */  
   rptTypeID:string,
}

export interface GetDefaultOutputEDI_output{
      /**  Default value for OutputEDI  */  
   returnObj:string,
}

   /** Required : 
      @param originalPath
      @param folderName
   */  
export interface GetDisplayPathWithUpdatedFolderName_input{
   originalPath:string,
   folderName:string,
}

export interface GetDisplayPathWithUpdatedFolderName_output{
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
   returnObj:Ice_Tablesets_ReportListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param ds
      @param reportID
      @param styleNum
      @param reportStyleImageName
   */  
export interface GetNewReportStyleImage_input{
   ds:Ice_Tablesets_ReportTableset[],
   reportID:string,
   styleNum:number,
   reportStyleImageName:string,
}

export interface GetNewReportStyleImage_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ReportTableset,
}
}

   /** Required : 
      @param ds
      @param reportID
      @param styleNum
   */  
export interface GetNewReportStyleRule_input{
   ds:Ice_Tablesets_ReportTableset[],
   reportID:string,
   styleNum:number,
}

export interface GetNewReportStyleRule_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ReportTableset,
}
}

   /** Required : 
      @param ds
      @param reportID
   */  
export interface GetNewReportStyle_input{
   ds:Ice_Tablesets_ReportTableset[],
   reportID:string,
}

export interface GetNewReportStyle_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ReportTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetNewReport_input{
   ds:Ice_Tablesets_ReportTableset[],
}

export interface GetNewReport_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ReportTableset,
}
}

   /** Required : 
      @param ds
      @param company
      @param reportID
      @param styleNum
   */  
export interface GetNewRptStylePrinters_input{
   ds:Ice_Tablesets_ReportTableset[],
   company:string,
   reportID:string,
   styleNum:number,
}

export interface GetNewRptStylePrinters_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ReportTableset,
}
}

export interface GetPrinterPageInformation_output{
   returnObj:Ice_BO_Report_PrinterPageInfo[],
}

   /** Required : 
      @param reportId
      @param styleNum
   */  
export interface GetReportStyleHealthCheckStatus_input{
   reportId:string,
   styleNum:number,
}

export interface GetReportStyleHealthCheckStatus_output{
parameters : {
      /**  output parameters  */  
   status:number,
   message:string,
}
}

   /** Required : 
      @param reportid
   */  
export interface GetReportStyleRules_input{
      /**  Report ID  */  
   reportid:string,
}

export interface GetReportStyleRules_output{
      /**  String array of styles with routing rules  */  
   returnObj:string,
}

   /** Required : 
      @param sysRowIDs
   */  
export interface GetReportStylesBySysRowIds_input{
      /**  The report style SysRowIDs.  */  
   sysRowIDs:string,
}

export interface GetReportStylesBySysRowIds_output{
   returnObj:Ice_Tablesets_ReportTableset[],
}

export interface GetReportTypeList_output{
   returnObj:string,
}

export interface GetReportsThatDefaultToEmfRenderFormat_output{
      /**  The reports that default to EMF render format.  */  
   returnObj:string,
}

   /** Required : 
      @param whereClauseReport
      @param whereClauseReportStyle
      @param whereClauseRptStylePrinters
      @param whereClauseReportStyleImage
      @param whereClauseReportStyleRule
      @param whereClauseReportComp
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseReport:string,
   whereClauseReportStyle:string,
   whereClauseRptStylePrinters:string,
   whereClauseReportStyleImage:string,
   whereClauseReportStyleRule:string,
   whereClauseReportComp:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Ice_Tablesets_ReportTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param reportLocation
   */  
export interface GetSsrsReportPageSettings_input{
      /**  The report location. This comes from the ReportStyle.PrintProgram column value.  */  
   reportLocation:string,
}

export interface GetSsrsReportPageSettings_output{
parameters : {
      /**  output parameters  */  
   height:number,
   width:number,
   top:number,
   bottom:number,
   left:number,
   right:number,
}
}

   /** Required : 
      @param outputLocation
   */  
export interface HasMarkupInDirectoryName_input{
      /**  Output location.  */  
   outputLocation:string,
}

export interface HasMarkupInDirectoryName_output{
      /**  `True` if mark up was found within any directory name.  */  
   returnObj:boolean,
}

   /** Required : 
      @param reportID
      @param styleNumber
   */  
export interface HasReportStyleImages_input{
      /**  Report identifier.  */  
   reportID:string,
      /**  Style number.  */  
   styleNumber:number,
}

export interface HasReportStyleImages_output{
   returnObj:boolean,
}

export interface Ice_BO_Report_ErpPaperSourceKind{
   SourceName:string,
   RawKind:number,
}

export interface Ice_BO_Report_PrinterPageInfo{
   PaperSizes:string,
   PaperSources:Ice_BO_Report_ErpPaperSourceKind[],
   DuplexSetting:string,
}

export interface Ice_BO_Report_ReportHealthCheckMissingCatalogItems{
   Company:string,
   ReportID:string,
   ReportStyleNum:number,
   CatalogItems:string,
}

export interface Ice_BO_Report_SsrsReportImportInfo{
   ReportFullName:string,
   Error:string,
   Warnings:string,
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

export interface Ice_Tablesets_CopiedReportFoldersRow{
      /**  Report folder name  */  
   Folder:string,
      /**  Paths of the copied reports  */  
   CopiedPaths:string,
      /**  Paths of the original reports  */  
   OriginalPaths:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_CopiedReportFoldersTableset{
   CopiedReportFolders:Ice_Tablesets_CopiedReportFoldersRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ReportCompRow{
   ReportID:string,
   StyleNum:number,
   Company:string,
   ValidStyle:boolean,
   IsDefault:boolean,
   CompanyName:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ReportListRow{
      /**  Report ID  */  
   ReportID:string,
      /**  Report Description  */  
   RptDescription:string,
      /**  Name of the BL program file used as a broker when auto-printing Crystal Reports or Bartender Labels from a BAM.  */  
   AutoProgram:string,
      /**  Indicates if this is a base system report  These are records delived as part of the system and should not be modified by the end user  */  
   SystemRpt:boolean,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Indicates if the current report can be auto-printed  */  
   CanAutoPrint:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ReportListTableset{
   ReportList:Ice_Tablesets_ReportListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_ReportRow{
      /**  Report ID  */  
   ReportID:string,
      /**  Report Description  */  
   RptDescription:string,
      /**  Name of the BL program file used as a broker when auto-printing Crystal Reports or Bartender Labels from a BAM.  */  
   AutoProgram:string,
      /**  Indicates if this is a base system report  These are records delived as part of the system and should not be modified by the end user  */  
   SystemRpt:boolean,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  Company  */  
   Company:string,
      /**  CompanyVisibility  */  
   CompanyVisibility:number,
      /**  Indicates if the current report can be auto-printed  */  
   CanAutoPrint:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ReportStyleImageRow{
      /**  Company  */  
   Company:string,
      /**  ReportID  */  
   ReportID:string,
      /**  StyleNum  */  
   StyleNum:number,
      /**  ReportStyleImageName  */  
   ReportStyleImageName:string,
      /**  ImageCompany  */  
   ImageCompany:string,
      /**  ImageID  */  
   ImageID:string,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   ImageContent:string,
   ImageType:string,
   CategoryID:string,
   SubcategoryID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ReportStyleRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Report ID  */  
   ReportID:string,
      /**  Report Style Number  */  
   StyleNum:number,
      /**  Report Style Description  */  
   StyleDescription:string,
      /**  Foreign key to the ReportType table which defines the type of report (Crystal, EpiForms, etc)  */  
   RptTypeID:string,
      /**  Program which performs the actual printing  */  
   PrintProgram:string,
      /**  additonal options/settings required by specfic PrintProgram  */  
   PrintProgramOptions:string,
      /**  Foreign Key to RptDef table.  */  
   RptDefID:string,
      /**   Delimited list of company id's that can use this ReportStyle.
Blank = All Companies. This field will not be overlaid during release upgrades.
This field is not intended to be directly updatable. Instead it is exposed to the UI in a separate table (ReportCompany) which is not a physical db table. All Companies are created in ReportCompany. If in the CompanyList, then ReportCompany.ValidStyle = Yes
Delimeter character is global LIST-DELIM value  (~)  */  
   CompanyList:string,
      /**  This is a Crystal Server Num that is defined in CrystalServer table.  */  
   ServerNum:number,
      /**   Specifies an output location for Bartender and Outbound EDI Reports to override the default locations:
mfgsysdata\Bartender
mfgsysdata\EDI  */  
   OutputLocation:string,
      /**  Field to save if file is going to be exported in txt o xml format  */  
   OutputEDI:string,
      /**  Indicates a base System record (delivered by Epicor). System records may be overlaid during patch/release updates.  */  
   SystemFlag:boolean,
      /**  Country Group Code / Country Code for CSF  */  
   CGCCode:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  RptCriteriaSetID  */  
   RptCriteriaSetID:string,
      /**  RptStructuredOutputDefID  */  
   RptStructuredOutputDefID:string,
      /**  StructuredOutputEnabled  */  
   StructuredOutputEnabled:boolean,
      /**  RequireSubmissionID  */  
   RequireSubmissionID:boolean,
      /**  AllowResetAfterSubmit  */  
   AllowResetAfterSubmit:boolean,
      /**  CertificateID  */  
   CertificateID:string,
      /**  Language  */  
   LangNameID:string,
      /**  Culture Format  */  
   FormatCulture:string,
      /**  StructuredOutputCertificateID  */  
   StructuredOutputCertificateID:string,
      /**  StructuredOutputAlgorithm  */  
   StructuredOutputAlgorithm:string,
      /**  True if any data source for this report data definition is related to a BAQ or EI. False in other case.  */  
   HasBAQOrEI:boolean,
      /**  Flag to indicate if this report style record has an enabled routing rule.  */  
   RoutingRuleEnabled:boolean,
      /**  Digital cert for signing is an All Company cert.  */  
   CertificateIsAllComp:boolean,
      /**  Indicates the certificate is a system cert.  */  
   CertificateIsSystem:boolean,
      /**  Certificate expiration date.  */  
   CertExpiration:string,
      /**  Report Style status (from HealthCheck).It indicates if there are issues in the report style: 0 - OK, 1 - Missing RDL, etc.  */  
   Status:number,
      /**  Report Style status message (from HealthCheck).It is a more detailed message with  issues found, ie. the names of the missing RDL files.  */  
   StatusMessage:string,
   RptDefSystemFlag:boolean,
   LangNameIDDescription:string,
   IsBAQReport:boolean,
   StructuredOutputCertificateIsAllComp:boolean,
   StructuredOutputCertificateIsSystem:boolean,
   StructuredOutputCertificateExpirationDate:string,
   AllowGenerateEDI:boolean,
   BitFlag:number,
   ReportRptDescription:string,
   RptDefRptDescription:string,
   RptTypeRptTypeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ReportStyleRuleRow{
      /**  Company  */  
   Company:string,
      /**  ReportID  */  
   ReportID:string,
      /**  StyleNum  */  
   StyleNum:number,
      /**  RptDefID  */  
   RptDefID:string,
      /**  RptTableID  */  
   RptTableID:string,
      /**  SystemCode  */  
   SystemCode:string,
      /**  ZDataTableID  */  
   ZDataTableID:string,
      /**  RuleBody  */  
   RuleBody:string,
      /**  Thumbnail  */  
   Thumbnail:string,
      /**  IsEnabled  */  
   IsEnabled:boolean,
      /**  SysRevID  */  
   SysRevID:number,
      /**  SysRowID  */  
   SysRowID:string,
   BitFlag:number,
   ReportDataDefinitionRptDescription:string,
   ReportStyleStyleDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_ReportTableset{
   Report:Ice_Tablesets_ReportRow[],
   ReportStyle:Ice_Tablesets_ReportStyleRow[],
   RptStylePrinters:Ice_Tablesets_RptStylePrintersRow[],
   ReportStyleImage:Ice_Tablesets_ReportStyleImageRow[],
   ReportStyleRule:Ice_Tablesets_ReportStyleRuleRow[],
   ReportComp:Ice_Tablesets_ReportCompRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Ice_Tablesets_RptStylePrintersRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Report  ID  */  
   ReportID:string,
      /**  Report Style Number  */  
   StyleNum:number,
      /**  Printer Identifier. (PK)  */  
   PrinterID:string,
      /**  SystemFlag  */  
   SystemFlag:boolean,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Ice_Tablesets_UpdExtReportTableset{
   Report:Ice_Tablesets_ReportRow[],
   ReportStyle:Ice_Tablesets_ReportStyleRow[],
   RptStylePrinters:Ice_Tablesets_RptStylePrintersRow[],
   ReportStyleImage:Ice_Tablesets_ReportStyleImageRow[],
   ReportStyleRule:Ice_Tablesets_ReportStyleRuleRow[],
   ReportComp:Ice_Tablesets_ReportCompRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param exportDataSet
   */  
export interface ImportReportStyleImages_input{
      /**  The previously exported data set.  */  
   exportDataSet:any,      //schema had no properties on an object.
}

export interface ImportReportStyleImages_output{
}

   /** Required : 
      @param ds
      @param allCompanies
   */  
export interface ImportReportStyle_input{
   ds:Ice_Tablesets_ReportTableset[],
      /**  If true then import the report style to all companies. Otherwise import the report style only for the current company.  */  
   allCompanies:boolean,
}

export interface ImportReportStyle_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ReportTableset,
}
}

   /** Required : 
      @param reportPath
      @param rdlBytes
   */  
export interface ImportSsrsRdl_input{
      /**  The report path.  */  
   reportPath:string,
      /**  The RDL bytes.  */  
   rdlBytes:string,
}

export interface ImportSsrsRdl_output{
}

   /** Required : 
      @param reports
   */  
export interface ImportSsrsReports_input{
      /**  The report paths and contents.  */  
   reports:any,      //schema had no properties on an object.
}

export interface ImportSsrsReports_output{
}

   /** Required : 
      @param reportsZip
      @param previousImportInfos
   */  
export interface ImportZippedReports_input{
      /**  The zipped reports.  */  
   reportsZip:string,
      /**  The import information from the previous run. `null` or empty otherwise.  */  
   previousImportInfos:Ice_BO_Report_SsrsReportImportInfo[],
}

export interface ImportZippedReports_output{
      /**  The success and failure information for each of the reports imported.  */  
   returnObj:Ice_BO_Report_SsrsReportImportInfo[],
}

   /** Required : 
      @param fullReportPath
   */  
export interface LoadSsrsRdl_input{
      /**  The full path to the report (not the Display path).  */  
   fullReportPath:string,
}

export interface LoadSsrsRdl_output{
      /**  The SSRS RDL bytes.  */  
   returnObj:string,
}

   /** Required : 
      @param newRptTypeID
      @param ds
   */  
export interface OnChangeOutputEDI_input{
      /**  New Report Type.  */  
   newRptTypeID:string,
   ds:Ice_Tablesets_ReportTableset[],
}

export interface OnChangeOutputEDI_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ReportTableset,
}
}

   /** Required : 
      @param locations
   */  
export interface PrepareZipWithSsrsReports_input{
      /**  The report locations  */  
   locations:string,
}

export interface PrepareZipWithSsrsReports_output{
      /**  Server path to zip file  */  
   returnObj:string,
}

   /** Required : 
      @param reportId
      @param styleNumber
   */  
export interface RetrieveReportStyleImages_input{
      /**  The report identifier.  */  
   reportId:string,
      /**  The style number.  */  
   styleNumber:number,
}

export interface RetrieveReportStyleImages_output{
   returnObj:Ice_Tablesets_ReportTableset[],
}

   /** Required : 
      @param company
      @param reportid
      @param stylenum
   */  
export interface SynchronizeDataset_input{
      /**  Company code  */  
   company:string,
      /**  Report ID  */  
   reportid:string,
      /**  Style Number  */  
   stylenum:number,
}

export interface SynchronizeDataset_output{
      /**  synchronization results, i.e. RptTables status.  */  
   returnObj:any,      //schema had no properties on an object.
}

   /** Required : 
      @param ds
      @param continueProcessingOnError
      @param rollbackParentOnChildError
   */  
export interface UpdateExt_input{
   ds:Ice_Tablesets_UpdExtReportTableset[],
   continueProcessingOnError:boolean,
   rollbackParentOnChildError:boolean,
}

export interface UpdateExt_output{
   returnObj:Ice_BOUpdErrorTableset[],
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_UpdExtReportTableset,
   errorsOccurred:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Ice_Tablesets_ReportTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Ice_Tablesets_ReportTableset,
}
}

   /** Required : 
      @param customReportFolder
   */  
export interface ValidateFolderName_input{
      /**  Folder name entered by the user  */  
   customReportFolder:string,
}

export interface ValidateFolderName_output{
}

   /** Required : 
      @param certificateID
   */  
export interface VerifyCertCanBeUsedForReportSigning_input{
      /**  The certificate ID.  */  
   certificateID:string,
}

export interface VerifyCertCanBeUsedForReportSigning_output{
      /**  True if the certificate is OK to use, otherwise false.  */  
   returnObj:boolean,
}

export interface VerifyReportStyleRdls_output{
   returnObj:Ice_BO_Report_ReportHealthCheckMissingCatalogItems[],
}

   /** Required : 
      @param rptDefId
   */  
export interface VerifyRptDataDefHasBQAOrEI_input{
      /**  Report Data Definition Id  */  
   rptDefId:string,
}

export interface VerifyRptDataDefHasBQAOrEI_output{
      /**  True when report data definition has a data source with BAQ or EI. Otherwise false.  */  
   returnObj:boolean,
}

