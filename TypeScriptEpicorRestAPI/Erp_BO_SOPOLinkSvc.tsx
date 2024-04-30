import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.SOPOLinkSvc
// Description: 
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/$metadata", {
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
      200 Desc: OK => reference #/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.IMOrderHedListRow
   */  
export function get_List(select?:string, filter?:string, orderby?:string, top?:string, skip?:string, inlinecount?:string, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IMOrderHedListRow>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/List", {
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
         resolve(data as Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IMOrderHedListRow)
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
   OperationID: GetRows
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetRows_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetRows(requestBody:GetRows_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetRows_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/GetRows", {
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
         resolve(data as GetRows_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOrderHedIntQueID
   Description: Get the IntQueID associated with this ICPONum
   OperationID: GetOrderHedIntQueID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetOrderHedIntQueID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderHedIntQueID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrderHedIntQueID(requestBody:GetOrderHedIntQueID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetOrderHedIntQueID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/GetOrderHedIntQueID", {
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
         resolve(data as GetOrderHedIntQueID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeMiscCode
   Description: Update PO Link Misc Charge information when the MiscCode is changed.
   OperationID: ChangeMiscCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeMiscCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeMiscCode(requestBody:ChangeMiscCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeMiscCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/ChangeMiscCode", {
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
         resolve(data as ChangeMiscCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePartNum
   Description: Update PO Link information with values from the Part Number when the Part Number is changed.
   OperationID: ChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePartNum(requestBody:ChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/ChangePartNum", {
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
         resolve(data as ChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSoldToID
   Description: Update PO Link information with values from the Sold To when the Sold To is changed.
   OperationID: ChangeSoldToID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSoldToID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSoldToID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSoldToID(requestBody:ChangeSoldToID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSoldToID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/ChangeSoldToID", {
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
         resolve(data as ChangeSoldToID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckCustomerCreditLimit
   Description: This method should be called before the Update method is called for a detail record.
The method returns a character string if the customer will go over their credit limit
and the user is given the choice of continuing or not.
   OperationID: CheckCustomerCreditLimit
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckCustomerCreditLimit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckCustomerCreditLimit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckCustomerCreditLimit(requestBody:CheckCustomerCreditLimit_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckCustomerCreditLimit_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/CheckCustomerCreditLimit", {
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
         resolve(data as CheckCustomerCreditLimit_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckPartChange
   Description: The method is to be run on leave of the PartNum and Revision fields
before the ChangePart or Update methods are run.
This returns all the questions that need to be asked before a part can be changed.
   OperationID: CheckPartChange
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckPartChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckPartChange(requestBody:CheckPartChange_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckPartChange_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/CheckPartChange", {
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
         resolve(data as CheckPartChange_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckReadyForOrder
   Description: Validate/return questions to ask the user before marking a record ReadyForOrder.
   OperationID: CheckReadyForOrder
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckReadyForOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckReadyForOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckReadyForOrder(requestBody:CheckReadyForOrder_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckReadyForOrder_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/CheckReadyForOrder", {
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
         resolve(data as CheckReadyForOrder_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckSOPODifferences
   Description: Return text of messages to present to the user informing them unit prices differ
on detail lines or miscellaneous charges, or the currencies are different on the SO and PO.
   OperationID: CheckSOPODifferences
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckSOPODifferences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSOPODifferences_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSOPODifferences(requestBody:CheckSOPODifferences_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckSOPODifferences_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/CheckSOPODifferences", {
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
         resolve(data as CheckSOPODifferences_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateConfigKits
   Description: Loops through the input ttOrderDtl records which should be configured kit parts and generates the
components for each kit. This method is called after processing the ICPO Suggestions and once that the
order has been created and the user had already answered the Configuration Q-A
   OperationID: CreateConfigKits
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateConfigKits_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateConfigKits_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateConfigKits(requestBody:CreateConfigKits_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateConfigKits_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/CreateConfigKits", {
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
         resolve(data as CreateConfigKits_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOrder
   Description: Populates SOPOOrderTableset for a given Order.
   OperationID: GetOrder
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrder(requestBody:GetOrder_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetOrder_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/GetOrder", {
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
         resolve(data as GetOrder_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOrderDtl
   Description: Get the OrderDtl record related to the IMOrderDtl record.
   OperationID: GetOrderDtl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetOrderDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrderDtl(requestBody:GetOrderDtl_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetOrderDtl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/GetOrderDtl", {
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
         resolve(data as GetOrderDtl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOrderMsc
   Description: Get the OrderMsc record related to the IMOrderMsc record.
   OperationID: GetOrderMsc
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetOrderMsc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderMsc_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrderMsc(requestBody:GetOrderMsc_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetOrderMsc_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/GetOrderMsc", {
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
         resolve(data as GetOrderMsc_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetOrderRel
   Description: Get the OrderRel record related to the IMOrderRel record.
   OperationID: GetOrderRel
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetOrderRel_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetOrderRel_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetOrderRel(requestBody:GetOrderRel_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetOrderRel_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/GetOrderRel", {
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
         resolve(data as GetOrderRel_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreRejectICPOLink
   Description: Checks to see if the po link can be rejected and returns a question to be asked
of the user if necessary.
   OperationID: PreRejectICPOLink
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreRejectICPOLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreRejectICPOLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreRejectICPOLink(requestBody:PreRejectICPOLink_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreRejectICPOLink_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/PreRejectICPOLink", {
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
         resolve(data as PreRejectICPOLink_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessSuggestions
   Description: ProcessSuggestions
   OperationID: ProcessSuggestions
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessSuggestions_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessSuggestions(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessSuggestions_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/ProcessSuggestions", {
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
         resolve(data as ProcessSuggestions_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReadyForOrderAll
   Description: Mark a list of records as ready to order.
   OperationID: ReadyForOrderAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReadyForOrderAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReadyForOrderAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReadyForOrderAll(requestBody:ReadyForOrderAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReadyForOrderAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/ReadyForOrderAll", {
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
         resolve(data as ReadyForOrderAll_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateReadyForOrderAll
   Description: Validation for marking all orders as Ready For Order.  This method should be
called before method ReadyForOrderAll is called.
   OperationID: ValidateReadyForOrderAll
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateReadyForOrderAll_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateReadyForOrderAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateReadyForOrderAll(requestBody:ValidateReadyForOrderAll_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateReadyForOrderAll_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/ValidateReadyForOrderAll", {
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
         resolve(data as ValidateReadyForOrderAll_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetList
   Description: GetList
   OperationID: Get_GetList
   Required: True   Allow empty value : True
   Required: True
   Required: True
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/GetList" + params, {
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
   Summary: Invoke method CustomGetByID
   OperationID: CustomGetByID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CustomGetByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CustomGetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CustomGetByID(requestBody:CustomGetByID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CustomGetByID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/CustomGetByID", {
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
         resolve(data as CustomGetByID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetByIDIncoming
   Description: Invokes CustomGetByID with an incomingOutgoing value of "I".  Throws RecordNotFoundException if no IMOrderHed record found.
   OperationID: GetByIDIncoming
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetByIDIncoming_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByIDIncoming_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetByIDIncoming(requestBody:GetByIDIncoming_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetByIDIncoming_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/GetByIDIncoming", {
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
         resolve(data as GetByIDIncoming_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Update
   Description: Since this is a 'simple' BO we must manually code the Update
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SOPOLinkSvc/Update", {
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
export interface Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_IMOrderHedListRow{
   "odatametadata":string,
   "value":Erp_Tablesets_IMOrderHedListRow,
}

export interface Erp_Tablesets_IMOrderHedListRow{
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   "OpenOrder":boolean,
      /**   Indicates that the Order item was closed before any shipments were made against it. Normally the Orders are closed as part of the Shipping process when all the releases have been closed.  By using the "Close Order" menu option the user can close the Order manually, to provide the function to "Cancel"  the order when the customer cancels there request.  If the Order item had no shipments made it is then marked as "voided". Regardless of shipment activity the Order is always marked as closed (OpenOrder = No).
When an OrderHed record is 'voided/closed' all of it's related OrderDtl and OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   "VoidOrder":boolean,
      /**  Company Identifier.  */  
   "Company":string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   "OrderNum":number,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   "CustNum":number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  */  
   "PONum":string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in shipping entry. It does not prevent shipments from being entered for this order.  */  
   "OrderHeld":boolean,
      /**   This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.

On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   "EntryPerson":string,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   "ShipToNum":string,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  */  
   "RequestDate":string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   "OrderDate":string,
      /**  An optional field that describes the FOB policy.  */  
   "FOB":string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   "ShipViaCode":string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of ORDERHED.CUSTNUM use the CUSTOMER.TERMS

field as the default.  */  
   "TermsCode":string,
      /**  Used to establish a discount percent value which will be used as a default during order detail line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever ORDERHED.CUSTOMER field changes.  */  
   "DiscountPercent":number,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   "PrcConNum":number,
      /**  Establishes the Shipping Contact to be used as default on the Order release records. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   "ShpConNum":number,
      /**  Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   "DepositBal":number,
      /**  Display value contains the deposit balance in the customer's currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   "DocDepositBal":number,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   "NeedByDate":string,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   "ExchangeRate":number,
      /**  A unique code that identifies the currency.  */  
   "CurrencyCode":string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   "LockRate":boolean,
      /**  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  */  
   "AllocPriorityCode":string,
      /**  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  */  
   "ShipOrderComplete":boolean,
      /**  Indicates if this order header is linked to an inter-company PO header.  */  
   "Linked":boolean,
      /**  Inter-Company Purchase order number that uniquely identifies the purchase order.  */  
   "ICPONum":number,
      /**  External Trading Company Identifier.  */  
   "ExtCompany":string,
      /**  Indicates if order based discounting needs to be applied to the order.  */  
   "ApplyOrderBasedDisc":boolean,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   "AutoOrderBasedDisc":boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   "SysRowID":string,
   "DisplayAction":string,
   "DisplayDescription":string,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   "IntQueID":number,
   "IncomingOutgoing":string,
   "Action":string,
   "BaseCurrencyCode":string,
   "CustID":string,
   "IntComplete":boolean,
   "IntError":boolean,
   "IntStatus":string,
   "InvalidData":boolean,
   "OverridePOPrice":boolean,
   "POBaseCurrencyCode":string,
   "POCurrencyCode":string,
   "ReadyForOrder":boolean,
   "Reject":boolean,
   "Translated":boolean,
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
      @param ds
   */  
export interface ChangeMiscCode_input{
   ds:Erp_Tablesets_SOPOLinkTableset[],
}

export interface ChangeMiscCode_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SOPOLinkTableset,
}
}

   /** Required : 
      @param ds
      @param lUsePartDefaults
   */  
export interface ChangePartNum_input{
   ds:Erp_Tablesets_SOPOLinkTableset[],
      /**  Use part defaults  */  
   lUsePartDefaults:boolean,
}

export interface ChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SOPOLinkTableset,
   cReturnMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeSoldToID_input{
   ds:Erp_Tablesets_SOPOLinkTableset[],
}

export interface ChangeSoldToID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SOPOLinkTableset,
   cReturnMessage:string,
}
}

   /** Required : 
      @param iCustNum
   */  
export interface CheckCustomerCreditLimit_input{
      /**  The Customer Number  */  
   iCustNum:number,
}

export interface CheckCustomerCreditLimit_output{
parameters : {
      /**  output parameters  */  
   cCreditLimitMessage:string,
   lContinue:boolean,
}
}

   /** Required : 
      @param cPartNum
      @param cGlbPartNum
      @param cAction
   */  
export interface CheckPartChange_input{
      /**  The new PartNum if a substitute part is found, partNum will be the substitute part  */  
   cPartNum:string,
      /**  The global part number  */  
   cGlbPartNum:string,
      /**  The action field from IMOrderDtl  */  
   cAction:string,
}

export interface CheckPartChange_output{
parameters : {
      /**  output parameters  */  
   cPartNum:string,
   cSubPartMessage:string,
   lSubAvail:boolean,
   cGlbPartMessage:string,
   cUsingPODefaultsMessage:string,
   cMsgType:string,
}
}

   /** Required : 
      @param dIntQueID
      @param lChildUnitPricesDiffer
   */  
export interface CheckReadyForOrder_input{
      /**  The IntQueID of the IMOrderHed record  */  
   dIntQueID:number,
      /**  Flag from IMOrderHed to indicate if the unit prices
            on the detail lines or miscellaneous charges differ  */  
   lChildUnitPricesDiffer:boolean,
}

export interface CheckReadyForOrder_output{
parameters : {
      /**  output parameters  */  
   cGlbPartQuestionText:string,
   cPricesDifferQuestionText:string,
}
}

   /** Required : 
      @param lChildUnitPricesDiffer
      @param dIntQueID
   */  
export interface CheckSOPODifferences_input{
      /**  Flag from IMOrderHed to indicate if detail or misc charges
            unit prices differ  */  
   lChildUnitPricesDiffer:boolean,
      /**  IntQueID from the IMOrderHed record  */  
   dIntQueID:number,
}

export interface CheckSOPODifferences_output{
parameters : {
      /**  output parameters  */  
   cUnitPricesDifferMessage:string,
   cCurrenciesDifferMessage:string,
   cUOMDifferMessage:string,
}
}

   /** Required : 
      @param regenerateKit
      @param ds
   */  
export interface CreateConfigKits_input{
      /**  If true this will cause the previous loaded components to be deleted  */  
   regenerateKit:boolean,
   ds:Erp_Tablesets_SOPOOrderDtlTableset[],
}

export interface CreateConfigKits_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SOPOOrderDtlTableset,
}
}

   /** Required : 
      @param incomingOutgoing
      @param iCPONum
      @param intQueID
   */  
export interface CustomGetByID_input{
   incomingOutgoing:string,
   iCPONum:number,
   intQueID:number,
}

export interface CustomGetByID_output{
   returnObj:Erp_Tablesets_SOPOLinkTableset[],
}

export interface Erp_Tablesets_IMOrderDtlRow{
      /**   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   VoidLine:boolean,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   OpenLine:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   OrderNum:number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   OrderLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  EDI Reference  */  
   Reference:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLine:string,
      /**  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  */  
   Commissionable:boolean,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   DocUnitPrice:number,
      /**  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  */  
   OrderQty:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Discount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   DocDiscount:number,
      /**   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  */  
   RequestDate:string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  */  
   OrderComment:string,
      /**  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  */  
   ShipComment:string,
      /**  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  */  
   InvoiceComment:string,
      /**  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  */  
   PickListComment:string,
      /**  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  */  
   TaxCatID:string,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  */  
   AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   DocAdvanceBillBal:number,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  */  
   QuoteNum:number,
      /**  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  */  
   QuoteLine:number,
      /**  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  */  
   TMBilling:boolean,
      /**  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  */  
   OrigWhyNoTax:string,
      /**   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  */  
   NeedByDate:string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  */  
   CustNum:number,
      /**   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  */  
   Rework:boolean,
      /**   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  */  
   RMANum:number,
      /**  The line item of the RMA detail that this order line item is fulfilling.  */  
   RMALine:number,
      /**  Project ID of the Project table record that this OrderDtl record. Can be blank.  */  
   ProjectID:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  Indicate that the item or the product group has a warranty.  */  
   Warranty:boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  The # of days, months, years the material is covered by warranty  */  
   MaterialDuration:number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   LaborDuration:number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   MiscDuration:number,
      /**  Whether the duration of warranty  is for "Days"," Months", "Years".  */  
   MaterialMod:string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   LaborMod:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  This warranty covers On site visits  */  
   Onsite:boolean,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  */  
   SellingQuantity:number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   SalesCatID:string,
      /**  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  */  
   ShipLineComplete:boolean,
      /**  Quantity from last EDI update.  */  
   CumeQty:number,
      /**  Date of last update  */  
   CumeDate:string,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   MktgCampaignID:string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   MktgEvntSeq:number,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Indicates if this order line is linked to an inter-company PO line.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   ConfigUnitPrice:number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   ConfigBaseUnitPrice:number,
      /**  This is the Price List used to determine the starting base price.  */  
   PriceListCode:string,
      /**  This is the Price List used to determine the break % or amount.  */  
   BreakListCode:string,
      /**  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  */  
   PricingQty:number,
      /**  Indicates if the price of the order line can be changed.  */  
   LockPrice:boolean,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   ListPrice:number,
      /**   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  */  
   DocOrdBasedPrice:number,
      /**  This is the Price Group ID used to price the order line with.  */  
   PriceGroupCode:string,
      /**  Indicates if the user selected a price list different from the default.  */  
   OverridePriceList:boolean,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  */  
   PricingValue:number,
      /**  This field controls the order in which Sales Order lines are displayed.  Display Seq is a decimal number where the whole number portion is used to sequence normal sales order lines and the decimal portion is used to sequence kit components under their associated kit parent.  */  
   DisplaySeq:number,
      /**  The sales order line number of the parent kit item.  This is only relevent for sales order lines which are kit parent or component lines.  If the KitParentLine equals the OrderLine then this is a kit parent line.  */  
   KitParentLine:number,
      /**  Indicates if component lines can be added, deleted and modified during Sales Order entry.  This field is only relevant for sales order lines which are kit parents.  */  
   KitAllowUpdate:boolean,
      /**  Indicates if the parent kit part must be shipped complete of if kit components can be shippped in varying degrees of completeness.  This field is only relevant for sales order lines which are kit parents. If this field is set to "No" then KitPricing must be set to "P".  */  
   KitShipComplete:boolean,
      /**  Indicates if all components are to be backflushed when a kit parent part is shipped.  This field is only relevant for sales order lines which are kit parents.  */  
   KitBackFlush:boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "YES" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   KitPrintCompsPS:boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   KitPrintCompsInv:boolean,
      /**  Indicates how kits will be priced.  Values are P = Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for sales order lines which are kit parents.  */  
   KitPricing:string,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a sales order line which is a kit component.  */  
   KitQtyPer:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate1:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate2:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate3:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate4:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate5:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit1:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit2:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit3:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit4:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit5:number,
      /**  The Demand Contract Detail record this OrderDtl is related to.  */  
   DemandContractLine:number,
      /**  Create New Job flag  */  
   CreateNewJob:boolean,
      /**  The date before which the order cannot be shipped.  */  
   DoNotShipBeforeDate:string,
      /**  Get Details flag  */  
   GetDtls:boolean,
      /**  The date after which the order cannot be shipped.  */  
   DoNotShipAfterDate:string,
      /**  Schedule Job flag  */  
   SchedJob:boolean,
      /**  Release Job flag  */  
   RelJob:boolean,
      /**  Enable New Job flag  */  
   EnableCreateNewJob:boolean,
      /**  Enable Get Details flag  */  
   EnableGetDtls:boolean,
      /**  Enable Schedule Job flag  */  
   EnableSchedJob:boolean,
      /**  Enable Release Job flag  */  
   EnableRelJob:boolean,
      /**  Indicates the warehouse selected for a counter sale order line.  */  
   CounterSaleWarehouse:string,
      /**  Identifies the Bin selected for a counter sale order line.  */  
   CounterSaleBinNum:string,
      /**  Indicates the lot number selected for a counter sale order line.  */  
   CounterSaleLotNum:string,
      /**  Indicates the dimension code selected for a counter sales order line.  */  
   CounterSaleDimCode:string,
      /**  Indicates if the demand detail that created/updated this order line has been rejected.  */  
   DemandDtlRejected:boolean,
      /**   A character flag field used to differentiate between regular sales order line, Sales Kit parent order line and Sales Kit component order line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   KitFlag:string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new order line.  */  
   KitsLoaded:boolean,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   DemandHeadSeq:number,
      /**  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  */  
   DemandDtlSeq:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Total Number of releases for the line  */  
   TotalReleases:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt1UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt2UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt3UnitPrice:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt1Discount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt2Discount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt3Discount:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt1AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt2AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt3AdvanceBillBal:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1ListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2ListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3ListPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3OrdBasedPrice:number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule  */  
   ExtPriceDtl:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPriceDtl:number,
      /**  Status of Order Line  */  
   LineStatus:string,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table. Assumed to include taxes  */  
   InUnitPrice:number,
      /**  Same as DocUnit price except that this field contains the unit price including taxes  */  
   DocInUnitPrice:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed.  - includes taxes  */  
   InDiscount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed. - includes taxes  */  
   DocInDiscount:number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied. including taxes  */  
   InListPrice:number,
      /**   Same as List price except that this field contains the list price in
the customer currency -including taxes.  */  
   DocInListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied. including taxes  */  
   InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency - including taxes.  */  
   DocInOrdBasedPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt1InUnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt2InUnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt3InUnitPrice:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt1InDiscount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt2InDiscount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt3InDiscount:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1InListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2InListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3InListPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3InOrdBasedPrice:number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule - Taxes are Included  */  
   InExtPriceDtl:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule - Taxes Included  */  
   DocInExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtPriceDtl:number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   OldOurOpenQty:number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   OldSellingOpenQty:number,
      /**  Used to store open value setting assigned in product configuration programs  */  
   OldOpenValue:number,
      /**  Used to store prod code value assigned in product configuration programs  */  
   OldProdCode:string,
      /**  Previous Selling Quantity  */  
   PrevSellQty:number,
      /**  Previous Part Number  */  
   PrevPartNum:string,
      /**  Previous Customer Part Number  */  
   PrevXPartNum:string,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   KitCompOrigSeq:number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   KitCompOrigPart:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
   DiscBreakListCode:string,
   DiscListPrice:number,
   LockDisc:boolean,
   OverrideDiscPriceList:boolean,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  ECCOrderNum  */  
   ECCOrderNum:string,
      /**  ECCOrderLine  */  
   ECCOrderLine:number,
      /**  DupOnJobCrt  */  
   DupOnJobCrt:boolean,
      /**  UndersPct  */  
   UndersPct:number,
      /**  Overs  */  
   Overs:number,
      /**  Unders  */  
   Unders:number,
      /**  OversUnitPrice  */  
   OversUnitPrice:number,
      /**  PlanUserID  */  
   PlanUserID:string,
      /**  PlanGUID  */  
   PlanGUID:string,
      /**  MOMsourceType  */  
   MOMsourceType:string,
      /**  MOMsourceEst  */  
   MOMsourceEst:string,
      /**  DefaultOversPricing  */  
   DefaultOversPricing:string,
      /**  ECCPlant  */  
   ECCPlant:string,
      /**  ECCQuoteNum  */  
   ECCQuoteNum:string,
      /**  ECCQuoteLine  */  
   ECCQuoteLine:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MfgJobType  */  
   MfgJobType:string,
      /**  ProFormaInvComment  */  
   ProFormaInvComment:string,
      /**  CreateJob  */  
   CreateJob:boolean,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   LinkToContract:boolean,
      /**  DocInAdvanceBillBal  */  
   DocInAdvanceBillBal:number,
      /**  InAdvanceBillBal  */  
   InAdvanceBillBal:number,
      /**  Rpt1InAdvanceBillBal  */  
   Rpt1InAdvanceBillBal:number,
      /**  Rpt2InAdvanceBillBal  */  
   Rpt2InAdvanceBillBal:number,
      /**  Rpt3InAdvanceBillBal  */  
   Rpt3InAdvanceBillBal:number,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  CommodityCode  */  
   CommodityCode:string,
      /**  Base price before any price breaks and discounts  */  
   MSRP:number,
      /**  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   DocMSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   Rpt1MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   Rpt2MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   Rpt3MSRP:number,
      /**  Distributor end customer price.  */  
   EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   DocEndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   Rpt1EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   Rpt2EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   Rpt3EndCustomerPrice:number,
      /**  Promotional Price offered to Dealer and Distributors.  */  
   PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   DocPromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   Rpt1PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   Rpt2PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   Rpt3PromotionalPrice:number,
      /**  Current status of line.  This is a maintainable status through Order Line Status maintenance.  Depending on the setting can control is line is updatable from the web.  */  
   OrderLineStatusCode:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  */  
   AttributeSetID:number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  The unique identifier of the related original CPQ Configured Quote Product.  */  
   KBOriginalConfigProdID:number,
      /**  TotalCovenantDiscount  */  
   TotalCovenantDiscount:number,
      /**  DocCovenantDiscount  */  
   DocCovenantDiscount:number,
      /**  Rpt1CovenantDiscount  */  
   Rpt1CovenantDiscount:number,
      /**  Rpt2CovenantDiscount  */  
   Rpt2CovenantDiscount:number,
      /**  Rpt3CovenantDiscount  */  
   Rpt3CovenantDiscount:number,
      /**  TotalInCovenantDiscount  */  
   TotalInCovenantDiscount:number,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
   Action:string,
   AvailableQuantity:number,
   BaseCurrencyID:string,
   BaseCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
   DispInvalidData:string,
   DisplayAction:string,
   DocExtPrice:number,
   DocMiscCharge:number,
   DocTotalPrice:number,
   ExtPrice:number,
   GlbPartNum:string,
   IncomingOutgoing:string,
   IntComplete:boolean,
   IntError:boolean,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
   IntStatus:string,
   InvalidData:boolean,
   MiscCharge:number,
   POLineInteger:number,
   PUM:string,
   QuantityOnHand:number,
   ReadyForOrder:boolean,
   Reject:boolean,
   Rpt1ExtPrice:number,
   Rpt1MiscCharge:number,
   Rpt1SOUnitPrice:number,
   Rpt1TotalPrice:number,
   Rpt2ExtPrice:number,
   Rpt2MiscCharge:number,
   Rpt2SOUnitPrice:number,
   Rpt2TotalPrice:number,
   Rpt3ExtPrice:number,
   Rpt3MiscCharge:number,
   Rpt3SOUnitPrice:number,
   Rpt3TotalPrice:number,
   SODocUnitPrice:number,
   SOPricePerCode:string,
   SOUnitPrice:number,
   TotalPrice:number,
   TotalShipped:number,
   Translated:boolean,
   UnitPricesDiffer:boolean,
   CurrencyID:string,
   InActivePart:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMOrderHedListRow{
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**   Indicates that the Order item was closed before any shipments were made against it. Normally the Orders are closed as part of the Shipping process when all the releases have been closed.  By using the "Close Order" menu option the user can close the Order manually, to provide the function to "Cancel"  the order when the customer cancels there request.  If the Order item had no shipments made it is then marked as "voided". Regardless of shipment activity the Order is always marked as closed (OpenOrder = No).
When an OrderHed record is 'voided/closed' all of it's related OrderDtl and OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   VoidOrder:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   OrderNum:number,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  */  
   PONum:string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in shipping entry. It does not prevent shipments from being entered for this order.  */  
   OrderHeld:boolean,
      /**   This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.

On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  */  
   RequestDate:string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   OrderDate:string,
      /**  An optional field that describes the FOB policy.  */  
   FOB:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of ORDERHED.CUSTNUM use the CUSTOMER.TERMS

field as the default.  */  
   TermsCode:string,
      /**  Used to establish a discount percent value which will be used as a default during order detail line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever ORDERHED.CUSTOMER field changes.  */  
   DiscountPercent:number,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Establishes the Shipping Contact to be used as default on the Order release records. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**  Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   DepositBal:number,
      /**  Display value contains the deposit balance in the customer's currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   DocDepositBal:number,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   NeedByDate:string,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  */  
   AllocPriorityCode:string,
      /**  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  */  
   ShipOrderComplete:boolean,
      /**  Indicates if this order header is linked to an inter-company PO header.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number that uniquely identifies the purchase order.  */  
   ICPONum:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Indicates if order based discounting needs to be applied to the order.  */  
   ApplyOrderBasedDisc:boolean,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   AutoOrderBasedDisc:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   DisplayAction:string,
   DisplayDescription:string,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
   IncomingOutgoing:string,
   Action:string,
   BaseCurrencyCode:string,
   CustID:string,
   IntComplete:boolean,
   IntError:boolean,
   IntStatus:string,
   InvalidData:boolean,
   OverridePOPrice:boolean,
   POBaseCurrencyCode:string,
   POCurrencyCode:string,
   ReadyForOrder:boolean,
   Reject:boolean,
   Translated:boolean,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMOrderHedListTableset{
   IMOrderHedList:Erp_Tablesets_IMOrderHedListRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_IMOrderHedRow{
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**   Indicates that the Order item was closed before any shipments were made against it. Normally the Orders are closed as part of the Shipping process when all the releases have been closed.  By using the "Close Order" menu option the user can close the Order manually, to provide the function to "Cancel"  the order when the customer cancels there request.  If the Order item had no shipments made it is then marked as "voided". Regardless of shipment activity the Order is always marked as closed (OpenOrder = No).
When an OrderHed record is 'voided/closed' all of it's related OrderDtl and OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   VoidOrder:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  When creating a new order the user is prompted for an order number. If the field is left blank, the next available # is assigned by the system. The system generates a number by finding the order # of the last record on file and then adding 1 to it.  */  
   OrderNum:number,
      /**  Contains the Customer number that the sales order is for.  This must be valid in the Customer table.  */  
   CustNum:number,
      /**  This is an optional field used to enter the customers Purchase Order Number.  This will be used as an alternate index for searching Orders by PO number.  */  
   PONum:string,
      /**  Indicates if an order is flagged as being "HELD" , this  is primarily used as a visual indicator in shipping entry. It does not prevent shipments from being entered for this order.  */  
   OrderHeld:boolean,
      /**   This is used as one of the selection parameters on the Order entry edit reports. The intent is for users to be able to select orders that they have entered for hard copy edit.

On new orders use the users login ID as the default. They can override this if they wish to enter something more meaningful.  */  
   EntryPerson:string,
      /**  Indicates which customer ship to is to be used as the default for the Order release records for this order. It  can be blank or it must be valid in the SHIPTO table. Use the CUSTOMER.SHIPTONUM as the default on new orders or when the ORDERHED.CUSTNUM is changed.  */  
   ShipToNum:string,
      /**  Date that the items need to be shipped by to meet the customers NeedByDate.  This can be left blank, it is only used to supply a default for OrderDtl.RequestDate.  */  
   RequestDate:string,
      /**  Mandatory entry and must be valid. Default as the system date.  */  
   OrderDate:string,
      /**  An optional field that describes the FOB policy.  */  
   FOB:string,
      /**  Contains the key value of the record in the "SHIPVIA" table. It can be left blank or must be valid in the 'SHIPTO"  table.
Use the CUSTOMER.SHIPVIA as the default when the ORDER.CUSTNUM field is changed and the ORDERHED.SHIPTO is blank. Use SHIPTO.SHIPVIA when ORDER.CUSTNUM or ORDERHED.SHIPTO fields are changed and the ORDERHED.SHIPTO is not blank.  */  
   ShipViaCode:string,
      /**   Contains the key value of the record in the TERMS table which indicates the sales terms established for this order. On change of ORDERHED.CUSTNUM use the CUSTOMER.TERMS

field as the default.  */  
   TermsCode:string,
      /**  Used to establish a discount percent value which will be used as a default during order detail line entry. It can be left as zero.  Use the CUSTOMER.DISCOUNTPERCENT field as a default. Refreshed whenever ORDERHED.CUSTOMER field changes.  */  
   DiscountPercent:number,
      /**  Contains the key  value for the Purchasing Contact. This can be blank or it must be valid in the CUSTCNT  table. Use the CUSTOMER.PRIMPCON as the default.  */  
   PrcConNum:number,
      /**  Establishes the Shipping Contact to be used as default on the Order release records. Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Use the Customer.PrimScon as a default.  */  
   ShpConNum:number,
      /**  Stores the Sales Rep Codes for the order. Up to five codes can be  established. This field is not directly maintainable. Instead temp widgets are used for entry of each individual code and then put together as one comma delimited string field and assigned to this field.  This field will have a Word index, it then will make reporting and data base integrity checking much easier through the use of the "contains phrase" when retrieving records. These codes can be left blank or must be valid in the SalesRep master. The first one is defaulted from the Customer master if ship to is blank; otherwise, from the Ship To.  */  
   SalesRepList:string,
      /**  Contains comments about the overall order. These will be printed on the Sales Acknowledgements.  */  
   OrderComment:string,
      /**  Used to establish shipping comments about the overall order. These will copied into the packing slip header file as defaults.  */  
   ShipComment:string,
      /**  Used to establish invoice comments about the overall order. These will copied into the Invoice detail file as defaults.  */  
   InvoiceComment:string,
      /**  Contains picking  comments about the overall order. These will be printed on the picking lists.  */  
   PickListComment:string,
      /**  Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   DepositBal:number,
      /**  Display value contains the deposit balance in the customer's currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   DocDepositBal:number,
      /**  Date customer needs the items on this order to arrive.  This is used only as the default value for the NeedByDate when creating order detail line items.  This can be left blank.  */  
   NeedByDate:string,
      /**  Indicates that the credit hold was overridden for this order.  */  
   CreditOverride:boolean,
      /**  The USERID of the user that overrode an order credit hold (system set).  */  
   CreditOverrideUserID:string,
      /**  The date that the user last overrode the customer credit hold (system set).  */  
   CreditOverrideDate:string,
      /**  The time that the user last overrode the customer credit hold in HH:MM:SS format (system set).  */  
   CreditOverrideTime:string,
      /**  The authorized maximum dollar limit that an order for a credit held customer is approved for.  Initially defaulted to the current order amount when the order is credit hold overridden.  The order amount is calculated by using line information only (i.e. extended amount and discounts) - deposits, advance billings, shipments and miscellaneous charges are NOT considered.  */  
   CreditOverrideLimit:number,
      /**  Controls if an alert is to be sent when shipments are made for this order.  */  
   SndAlrtShp:boolean,
      /**   Exchange rate that will be used for this order.  Defaults from
CurrRate.CurrentRate. Conversion rates will be calculated as System Base = Foreign value * rate, Foreign value = system base * (1/rate). This is the dollar in foreign currency from the exchange rate tables in the newspapers.  */  
   ExchangeRate:number,
      /**  A unique code that identifies the currency.  */  
   CurrencyCode:string,
      /**  Used with the currency module.  When TRUE the currency rate can be changed by the user and cannot be changed by the system.  This will also be the default for the invoice.  */  
   LockRate:boolean,
      /**  The member's name on the credit card.  */  
   CardMemberName:string,
      /**  The credit card account identifier.  */  
   CardNumber:string,
      /**  A code assigned by the user to uniquely identify a Credit Card Type master. This can't be blank.  */  
   CardType:string,
      /**  The expiration month of the credit card.  */  
   ExpirationMonth:number,
      /**  The expiration year of the credit card.  */  
   ExpirationYear:number,
      /**  Optional field, a 4-digit, non-embossed code on face of American Express Card assigned for fraud prevention.  */  
   CardID:string,
      /**  Up to 17 alphnumeric characters provided by customer. This is used to track information on customer spending (e.g., cost center, project code). This field is especially critical, since inaccurate information will affect the general ledger. If no reference number is provided, leave this field blank.  */  
   CardmemberReference:string,
      /**  Code used to relate a AllocPri record to the order.  Defaulted from Customer.AllocPriorityCode.  */  
   AllocPriorityCode:string,
      /**  Code used to relate a ReservePri record to the order.  Defaulted from Customer.ReservePriorityCode.  */  
   ReservePriorityCode:string,
      /**  Indicates if the order must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases with a ship date <= the given cutoff date alos have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "O" (Ship Order 100% complete)  */  
   ShipOrderComplete:boolean,
      /**  Not editable, When SF Synch creates orders, this flag is set to YES.  */  
   WebOrder:boolean,
      /**  Updated Via SF Synch.  This is the authorization number from a third party credit card validation service.  */  
   CCApprovalNum:string,
      /**  Order created from EDI interfaced module.  */  
   EDIOrder:boolean,
      /**  Updated from EDI module if 855 or 865 created.  */  
   EDIAck:boolean,
      /**  Indicates if this order header is linked to an inter-company PO header.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number that uniquely identifies the purchase order.  */  
   ICPONum:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  This is the web-login-id (email address) of the person that placed the order.  */  
   WebEntryPerson:string,
      /**  Indicates whether the email acknowledgement of the order has been sent.  (For web orders)  */  
   AckEmailSent:boolean,
      /**  Indicates if order based discounting needs to be applied to the order.  */  
   ApplyOrderBasedDisc:boolean,
      /**  Indicates if order based discounting should be applied automatically or manually triggered by user as menu option.  */  
   AutoOrderBasedDisc:boolean,
      /**   Indicates Entry method program that used to create the order.
S = Standard, Q = Quick Entry,  C = Counter Sales, D = Demand/EDI  */  
   EntryMethod:string,
      /**  The help desk case that created this order.  */  
   HDCaseNum:number,
      /**  Flag used in sales order entry for counter sales orders.  */  
   CounterSale:boolean,
      /**  Create AR Invoice for counter sales order.  */  
   CreateInvoice:boolean,
      /**  Create Packing Slip for counter sale.  */  
   CreatePackingSlip:boolean,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Stores the encrypted credit card number  */  
   ProcessCard:string,
      /**  Credit Transaction Amount, makes up part of CCTotal  */  
   CCAmount:number,
      /**  Credit Card transaction freight amount, part of CCTotal  */  
   CCFreight:number,
      /**  Credit Card Transaction Tax amount, part of CCTotal  */  
   CCTax:number,
      /**  Total amount being sent to the credit card processor  */  
   CCTotal:number,
      /**  See CCAmount  */  
   CCDocAmount:number,
      /**  See CCFreight  */  
   CCDocFreight:number,
      /**  See CCTax  */  
   CCDocTax:number,
      /**  See CCTotal  */  
   CCDocTotal:number,
      /**  Address used during AVS validation for credit transactions  */  
   CCStreetAddr:string,
      /**  Zip used during AVS validation in credit transactions  */  
   CCZip:string,
      /**  Bill To Customer Number  */  
   BTCustNum:number,
      /**  New database field as it can be changed by user.  Default is set to BTCustNum?s primary billing contact.  If a primary billing contact is not set, default is ?None Selected?.  Keep in mind the BTCustNum field may be the same as CustNum (SoldTo) but the default would still be this customer?s primary billing contact where the ConNum field (Contact for sold to) is defaulting the primary purchasing contact.  */  
   BTConNum:number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   RepRate4:number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   RepRate5:number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   RepSplit1:number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   RepSplit2:number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   RepSplit3:number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   RepSplit4:number,
      /**  Split percent is used to calculate the "commissionable"  dollar amount. This field is used to establish the default split percent used in detail line entry. Should be zero if the corresponding SalesRep code is blank. Default as 100 percent  */  
   RepSplit5:number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   RepRate1:number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   RepRate2:number,
      /**  Establishes the defaults sales rep commission rates to be used during entry of order detail lines. Must be zero if the ORDERHED.SALEREPCODE is blank. Default is the SALESREP.COMMISSIONPERCENT.  */  
   RepRate3:number,
      /**  Incremented whenever an outbound sales document is generated from the order, i.e. Sales Order Acknowledgement, Response to Change, etc.  */  
   OutboundSalesDocCtr:number,
      /**  Incremented whenever an outbound shipping document is generated from the order, i.e. ASN.  */  
   OutboundShipDocsCtr:number,
      /**  The demand contract this OrderHed is related to.  */  
   DemandContractNum:number,
      /**  The date before which the order cannot be shipped.  */  
   DoNotShipBeforeDate:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  The date after which the order cannot be shipped.  */  
   DoNotShipAfterDate:string,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  The date after which the sales order should be canceled.  */  
   CancelAfterDate:string,
      /**  Indicates if the demand that created/updated this order has been rejected.  */  
   DemandRejected:boolean,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   OverrideService:boolean,
      /**  Indicates if the Order is a credit card order  */  
   CreditCardOrder:boolean,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   DemandHeadSeq:number,
      /**  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  */  
   PayFlag:string,
      /**  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  */  
   PayAccount:string,
      /**  Shipping Bill To. The first line of the Payers main address. Required when Pay Flag is Third party.  */  
   PayBTAddress1:string,
      /**  Shipping Bill To.  The second line of the Payers main address. An address is required when Pay Flag is Third party  */  
   PayBTAddress2:string,
      /**  Shipping, The city portion of the Payer main address.  */  
   PayBTCity:string,
      /**  The state or province portion of the shipment payer main address.  */  
   PayBTState:string,
      /**  The zip or postal code portion of the shipping payers main address.  */  
   PayBTZip:string,
      /**  The country of the main shipping payers address.  */  
   PayBTCountry:string,
      /**  Freight charges will not be returned if 'yes'  */  
   DropShip:boolean,
      /**  Added for international shipping  */  
   CommercialInvoice:boolean,
      /**  Added for international shipping. Shipper's Export Declaration  */  
   ShipExprtDeclartn:boolean,
      /**  For International shipping.  Certificate of Orgin.  */  
   CertOfOrigin:boolean,
      /**  For International shipping.  Shipper's Letter of Instruction.  */  
   LetterOfInstr:boolean,
      /**  International Shipping. Frieght Forwarder ID  */  
   FFID:string,
      /**  International Shipping. The first line of the Frieght Forwarder main address.  */  
   FFAddress1:string,
      /**  International Shipping. The second line of the Frieght Forwarder main address.  */  
   FFAddress2:string,
      /**  Shipping, The city portion of the Frieght Forwarder main address.  */  
   FFCity:string,
      /**  International Shipping. The state or province portion of the shipment Frieght Forwarder main address.  */  
   FFState:string,
      /**  International Shipping. The zip or postal code portion of the shipping Frieght Forwarder main address.  */  
   FFZip:string,
      /**  International shipping. The country of the Frieght Forwarder .  */  
   FFCountry:string,
      /**  International Shipping. Frieght Forwarder Contact  */  
   FFContact:string,
      /**  International Shipping. Frieght Forwarder company name  */  
   FFCompName:string,
      /**  International Shipping. Frieght Forwarder Phone number  */  
   FFPhoneNum:string,
      /**  Is this an International shipment  */  
   IntrntlShip:boolean,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Field to use for the BAM to Auto-Print the Crystal Report or Bartender Labels associated to this table.  */  
   AutoPrintReady:boolean,
      /**  Defines if this document is marked as EDI Ready  */  
   EDIReady:boolean,
      /**  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  */  
   IndividualPackIDs:boolean,
      /**  Freight Forwarder third address line.  */  
   FFAddress3:string,
      /**   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  */  
   DeliveryConf:number,
      /**  Additional Handling Required flag  */  
   AddlHdlgFlag:boolean,
      /**  Non Standard Package flag.  */  
   NonStdPkg:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Freight Forwarder country portion of the address  */  
   FFCountryNum:number,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Payer Bill To  third address line  */  
   PayBTAddress3:string,
      /**  Payer Bill To country portion of the address  */  
   PayBTCountryNum:number,
      /**  Payer Bill To phone number  */  
   PayBTPhone:string,
      /**  UPS Quantity View  */  
   UPSQuantumView:boolean,
      /**  UPS Quantum View Ship from Nam  */  
   UPSQVShipFromName:string,
      /**  UPS Quantity View Memo  */  
   UPSQVMemo:string,
      /**  This flag will be used to indicate if the order is ready for calculations. When set to true, tax calculations will take place whenever a save takes place for any tables tied to the order which could affect taxes (OrderDtl, OrderHed, OrderMisc, etc). It defaults from XASyst.SOReadyToCalcDflt field when an order is created.  */  
   ReadyToCalc:boolean,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalCharges:number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalMisc:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalDiscount:number,
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   TotalComm:number,
      /**  Total Advance Billable Balance  */  
   TotalAdvBill:number,
      /**  Total number of lines on the order  */  
   TotalLines:number,
      /**  Total Number of releases on order  */  
   TotalReleases:number,
      /**  Total number of distinct release dates on order  */  
   TotalRelDates:number,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   DocTotalCharges:number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   DocTotalMisc:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   DocTotalDiscount:number,
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   DocTotalComm:number,
      /**   Order Total Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalTax:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   DocTotalTax:number,
      /**  Total Advance Billable Balance  */  
   DocTotalAdvBill:number,
      /**  Total Shipped amount  */  
   TotalShipped:number,
      /**  Total amount of order that has been invoiced  */  
   TotalInvoiced:number,
      /**  Total number of lines that were commissionable  */  
   TotalCommLines:number,
      /**  Commission earned for first sales rep  */  
   SRCommAmt1:number,
      /**  Commission earned for second sales rep  */  
   SRCommAmt2:number,
      /**  Commission earned for third sales rep  */  
   SRCommAmt3:number,
      /**  Commission earned for fourth sales rep  */  
   SRCommAmt4:number,
      /**  Commission earned for fifth sales rep  */  
   SRCommAmt5:number,
      /**  Total Commissionable Amount for first salesrep  */  
   SRCommableAmt1:number,
      /**  Total Commissionable Amount for second salesrep  */  
   SRCommableAmt2:number,
      /**  Total Commissionable Amount for third salesrep  */  
   SRCommableAmt3:number,
      /**  Total Commissionable Amount for fourth salesrep  */  
   SRCommableAmt4:number,
      /**  Total Commissionable Amount for fifth salesrep  */  
   SRCommableAmt5:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   Rounding:number,
      /**  Display value contains the deposit balance in a reporting currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   Rpt1DepositBal:number,
      /**  Rounding is occurred if multiplier or rule for Total amount is different with multiplier or rule for Total line amount, it is included in the 'Amount to Pay' and it is booked to the rounding account specified in the company setup when the invoice is posted  */  
   DocRounding:number,
      /**  Display value contains the deposit balance in a report currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   Rpt2DepositBal:number,
      /**  Display value contains the deposit balance in a report currency when the currency module is used; otherwise it is equal to the DepositBal. customer. Contains the current outstanding (liability) deposits that have been made for the sales order. This value is increased via cash receipts or "deposit" type invoices. It is supplied as a default to invoice entry (InvcHead.DepositCredit) at which time it is decreased.  */  
   Rpt3DepositBal:number,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt1TotalCharges:number,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt2TotalCharges:number,
      /**   Total Line Amount
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt3TotalCharges:number,
      /**  Total Advance Billable Balance  */  
   Rpt1TotalAdvBill:number,
      /**  Total Advance Billable Balance  */  
   Rpt2TotalAdvBill:number,
      /**  Total Advance Billable Balance  */  
   Rpt3TotalAdvBill:number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt1TotalMisc:number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt2TotalMisc:number,
      /**   Total Miscellaneous charges
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt3TotalMisc:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt1TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt2TotalDiscount:number,
      /**   Total Line Discounts
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt3TotalDiscount:number,
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt1TotalComm:number,
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt2TotalComm:number,
      /**   Total Commissions for Order
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes
Net Total = Order Total - TotalComm  */  
   Rpt3TotalComm:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax +TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt1TotalTax:number,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt2TotalTax:number,
      /**  Reporting currency value of this field  */  
   Rpt1Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt2Rounding:number,
      /**  Reporting currency value of this field  */  
   Rpt3Rounding:number,
      /**  Unique identifier  */  
   RateGrpCode:string,
      /**   Total Order Invoice Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt3TotalTax:number,
      /**  See CCAmount  */  
   Rpt1CCAmount:number,
      /**  See CCAmount  */  
   Rpt2CCAmount:number,
      /**  See CCAmount  */  
   Rpt3CCAmount:number,
      /**  See CCFreight  */  
   Rpt1CCFreight:number,
      /**  See CCFreight  */  
   Rpt2CCFreight:number,
      /**  See CCFreight  */  
   Rpt3CCFreight:number,
      /**  See CCTax  */  
   Rpt1CCTax:number,
      /**  See CCTax  */  
   Rpt2CCTax:number,
      /**  See CCTax  */  
   Rpt3CCTax:number,
      /**  See CCTotal  */  
   Rpt1CCTotal:number,
      /**  See CCTotal  */  
   Rpt2CCTotal:number,
      /**  See CCTotal  */  
   Rpt3CCTotal:number,
      /**  Total order Amount. This field is an accumulation of the extended net amounts of the detail line items  */  
   OrderAmt:number,
      /**  Total order Amount in customer currency. This field is an accumulation of the extended net amounts of the detail line items and rounded according to the Doc currency Round rule  */  
   DocOrderAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1OrderAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2OrderAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3OrderAmt:number,
      /**  Tax Point  */  
   TaxPoint:string,
      /**  Date Used to calculate Tax Rates  */  
   TaxRateDate:string,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**   Indicates if the One Time Shipto information is to be used.
Note: This can only be true when if the OTSName is not blank. 
UI disables this when Customer.AllowQTS = False,  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipment country  */  
   OTSCountryNum:number,
      /**   Order Total Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   DocTotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt1TotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt2TotalWHTax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt3TotalWHTax:number,
      /**   Order Total Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   TotalSATax:number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   DocTotalSATax:number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt1TotalSATax:number,
      /**   Total Order Self Assessed Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt2TotalSATax:number,
      /**   Total Order Withholding Taxes
Order Total = TotalCharges + TotalMisc - TotalDiscount + TotalTaxes + TotalWHTax + TotalSATax
Net Total = Order Total - TotalComm  */  
   Rpt3TotalSATax:number,
      /**  Indicates if/how the OTS is saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   OTSSaveAs:string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   OTSSaveCustID:string,
      /**  True if Customer or ShipTo record was created using the  OTS info.  */  
   OTSCustSaved:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**  Status of Order  */  
   OrderStatus:string,
      /**  Hold Set by Demand  */  
   HoldSetByDemand:boolean,
      /**  Indicates that the tax is included in the unit price  */  
   InPrice:boolean,
      /**  Reserved for future use  */  
   InTotalCharges:number,
      /**  Reserved for future use  */  
   InTotalMisc:number,
      /**  Reserved for future use  */  
   InTotalDiscount:number,
      /**  Reserved for future use  */  
   DocInTotalCharges:number,
      /**  Reserved for future use  */  
   DocInTotalMisc:number,
      /**  Reserved for future use  */  
   DocInTotalDiscount:number,
      /**  Reserved for future use  */  
   Rpt1InTotalCharges:number,
      /**  Reserved for future use  */  
   Rpt2InTotalCharges:number,
      /**  Reserved for future use  */  
   Rpt3InTotalCharges:number,
      /**  Reserved for future use  */  
   Rpt1InTotalMisc:number,
      /**  Reserved for future use  */  
   Rpt2InTotalMisc:number,
      /**  Reserved for future use  */  
   Rpt3InTotalMisc:number,
      /**  Reserved for future use  */  
   Rpt1InTotalDiscount:number,
      /**  Reserved for future use  */  
   Rpt2InTotalDiscount:number,
      /**  Reserved for future use  */  
   Rpt3InTotalDiscount:number,
      /**  Letter of Credit ID.  */  
   ARLOCID:string,
      /**  Bank for Cash Receipts. Default is from Customer(Bill To).  */  
   OurBank:string,
      /**  It will be used to identify SO that will generate an invoice at the shipment.  If the order is created manually the default for this order will be taken from the customer master file. If the order is created via DM, the default will be taken from the value in the DM records.  */  
   ERSOrder:boolean,
      /**  Indicates that order is on hold due to amount exceeding value on Letter of Credit.  */  
   LOCHold:boolean,
      /**  Currency code used in further packing slips.  */  
   PSCurrCode:string,
      /**  Currency code used in further AR invoices.  */  
   InvCurrCode:string,
      /**  Legal Number for the record.  */  
   LegalNumber:string,
      /**  Transaction Document for the record.  */  
   TranDocTypeID:string,
      /**  Cross Reference Contract Number.  */  
   XRefContractNum:string,
      /**  Cross Reference Contract Date.  */  
   XRefContractDate:string,
      /**  Date in which the related demand was last processed.  */  
   DemandProcessDate:string,
      /**  System Time when demand was last processed.  */  
   DemandProcessTime:number,
      /**  Last Schedule Number in which the demand was processed.  */  
   LastScheduleNumber:string,
      /**  EDI Transaction Control Number  */  
   LastTCtrlNum:string,
      /**  EDI Batch Control Number  */  
   LastBatchNum:string,
      /**  ECCOrderNum  */  
   ECCOrderNum:string,
      /**  ECCPONum  */  
   ECCPONum:string,
      /**  WIOrder  */  
   WIOrder:string,
      /**  WIApplication  */  
   WIApplication:string,
      /**  WIUsername  */  
   WIUsername:string,
      /**  WIUserID  */  
   WIUserID:string,
      /**  WICreditCardorder  */  
   WICreditCardorder:boolean,
      /**  OrderCSR  */  
   OrderCSR:string,
      /**  UserChar1  */  
   UserChar1:string,
      /**  UserChar2  */  
   UserChar2:string,
      /**  UserChar3  */  
   UserChar3:string,
      /**  UserChar4  */  
   UserChar4:string,
      /**  UserDate1  */  
   UserDate1:string,
      /**  UserDate2  */  
   UserDate2:string,
      /**  UserDate3  */  
   UserDate3:string,
      /**  UserDate4  */  
   UserDate4:string,
      /**  UserDecimal1  */  
   UserDecimal1:number,
      /**  UserDecimal2  */  
   UserDecimal2:number,
      /**  UserInteger1  */  
   UserInteger1:number,
      /**  UserInteger2  */  
   UserInteger2:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  IsCSRSet  */  
   IsCSRSet:boolean,
      /**  ECCPaymentMethod  */  
   ECCPaymentMethod:string,
      /**  AGUseGoodDefaultMark  */  
   AGUseGoodDefaultMark:boolean,
      /**  OTSShipToNum  */  
   OTSShipToNum:string,
      /**  ProFormaInvComment  */  
   ProFormaInvComment:string,
      /**  ccToken  */  
   ccToken:string,
      /**  InvcOrderCmp  */  
   InvcOrderCmp:boolean,
      /**  ReprintSOAck  */  
   ReprintSOAck:boolean,
      /**  CounterSOAck  */  
   CounterSOAck:number,
      /**  DispatchReason  */  
   DispatchReason:string,
      /**  Plant  */  
   Plant:string,
      /**  This flag will be used to indicate if the sales order is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
      /**  Ship the good by this time  */  
   ShipByTime:number,
      /**  Taiwan GUI Calendar Fiscal Year  */  
   TWFiscalYear:number,
      /**  Taiwan GUI Calendar Fiscal Year Suffix  */  
   TWFiscalYearSuffix:string,
      /**  Taiwan GUI Calendar Fiscal Period  */  
   TWFiscalPeriod:number,
      /**  GUI Group of Legal Numbers  */  
   TWGUIGroup:string,
      /**  Seller GUI Code  */  
   TWGUIRegNumSeller:string,
      /**  Buyer GUI Code  */  
   TWGUIRegNumBuyer:string,
      /**  OrderOpenCredit  */  
   OrderOpenCredit:number,
      /**  ClosedNotShipped  */  
   ClosedNotShipped:number,
      /**  InvCurrDepositBal  */  
   InvCurrDepositBal:number,
      /**  Article. 106c  */  
   PLArticle106c:boolean,
      /**  Invoices are issued by a taxpayer's representative  */  
   PLInvIssuedByTaxpayer:boolean,
      /**  Invoices issued by the second taxpayer  */  
   PLInvIssuedBySecondTaxpayer:boolean,
      /**  Tourist Services  */  
   PLTouristService:boolean,
      /**  Second hand goods, works of art, collectibles or antiques  */  
   PLSecondHandOrArts:boolean,
      /**  Appropriate Legal Article of the Act  */  
   PLLegalArticleAct:string,
      /**  Appropriate Legal Article of 2006/112/WE Directive  */  
   PLLegalArticleWEDirective:string,
      /**  Other Legal Article  */  
   PLLegalArticleOther:string,
      /**  Name of the Enforcement Authority or the Name of the Judicial Officer  */  
   PLEnforcementAuthName:string,
      /**  Address of the Enforcement Authority or Judicial Officer  */  
   PLEnforcementAuthAddr:string,
      /**  Tax Representative Name  */  
   PLTaxRepresentativeName:string,
      /**  Tax Representative Address  */  
   PLTaxRepresentativeAddr:string,
      /**  Tax ID of the Tax Representative  */  
   PLTaxRepresentativeTaxID:string,
      /**  Margin Scheme  */  
   PLMarginScheme:number,
      /**  Goods or Service VAT exempt  */  
   PLGoodsOrServiceVATExempt:boolean,
      /**  Credit Card Holder City  */  
   CCCity:string,
      /**  Credit Card Holder State  */  
   CCState:string,
      /**  ExtAOEUserID  */  
   ExtAOEUserID:string,
      /**  ExtAOE  */  
   ExtAOE:string,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
      /**  FSMSendTo  */  
   FSMSendTo:boolean,
      /**  Incoterm Code  */  
   IncotermCode:string,
      /**  Incoterm Location  */  
   IncotermLocation:string,
      /**  CovenantDiscPercent  */  
   CovenantDiscPercent:number,
      /**  TotalCovenantDiscount  */  
   TotalCovenantDiscount:number,
      /**  DocCovenantDiscount  */  
   DocCovenantDiscount:number,
      /**  Rpt1CovenantDiscount  */  
   Rpt1CovenantDiscount:number,
      /**  Rpt2CovenantDiscount  */  
   Rpt2CovenantDiscount:number,
      /**  Rpt3CovenantDiscount  */  
   Rpt3CovenantDiscount:number,
      /**  TotalInCovenantDiscount  */  
   TotalInCovenantDiscount:number,
   CustomerName:string,
   Action:string,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
   CustID:string,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
   CustOnCreditHold:boolean,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
   DispInvalidData:string,
   DisplayAction:string,
   DisplayDescription:string,
   EnableFOB:boolean,
   EnableShipVia:boolean,
   EnableSoldTo:boolean,
   EnableTerms:boolean,
   FOBDescription:string,
   IncomingOutgoing:string,
   IntComplete:boolean,
   IntError:boolean,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
   IntStatus:string,
   InvalidData:boolean,
   InvalidShipTo:boolean,
   OverridePOPrice:boolean,
   POBaseCurrencyCode:string,
   POCurrencyCode:string,
   ReadyForOrder:boolean,
   Reject:boolean,
   ShipToAddressList:string,
   ShipToContactFaxNum:string,
   ShipToContactName:string,
   ShipToContactPhoneNum:string,
   ShipViaDescription:string,
   SoldToAddressList:string,
   SoldToContactFaxNum:string,
   SoldToContactName:string,
   SoldToContactPhoneNum:string,
   TermsDescription:string,
   Translated:boolean,
   BaseCurrencyCode:string,
   ChildUnitPricesDiffer:boolean,
   ChildInActivePart:boolean,
      /**  The formatted sold to address  */  
   SoldToAddressFormat:string,
      /**  The formatted ship to address  */  
   ShipToAddressFormat:string,
   BitFlag:number,
   BaseCurrencyCurrName:string,
   BaseCurrencyDocumentDesc:string,
   BaseCurrencyCurrDesc:string,
   BaseCurrencyCurrencyID:string,
   BaseCurrencyCurrSymbol:string,
   POBaseCurrencyCurrName:string,
   POBaseCurrencyDocumentDesc:string,
   POBaseCurrencyCurrDesc:string,
   POBaseCurrencyCurrencyID:string,
   POBaseCurrencyCurrSymbol:string,
   ReservePriDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMOrderMscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Order line number that this miscellaneous record is related to. If related to the Order then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when miscellaneous maintenance was requested.  */  
   OrderLine:number,
      /**  Sequence Number  */  
   SeqNum:number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing. The default is provided by MiscChrg.Description, but it's overridable by the user. This can't be blank.  */  
   Description:string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   MiscAmt:number,
      /**  The amount of the Miscellaneous Charge/Credit(display value). Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   DocMiscAmt:number,
      /**  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  */  
   FreqCode:string,
      /**  An internally used flag which indicates that this record was created from a Quote via the "Get Quote" function. "Q" = related to the QuoteQty record, "L" = related to the overall QuoteDtl record. This flag is used so that the OrderMsc file can be refreshed from the QuoteMsc when Quantity or Quote/Line # changes occur. The logic is that if a change in order quantity of a order line that is linked to a quote causes a different price break to be selected then all the existing all OrderMsc records where Quoting = "Q" are deleted and then re-pulled in based on the new qty. If the Quote # or QuoteLine are changed then all OrderMsc records where Quoting is either a "Q" or "L" are deleted then re-pulled in from the newly referenced quote.  */  
   Quoting:string,
      /**  Indicates if this order miscellaneous charge is linked to an inter-company PO misc charge.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  Inter Company PO Sequence Number  */  
   ICPOSeqNum:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default. - Includes taxes  */  
   InMiscAmt:number,
      /**  The amount of the Miscellaneous Charge/Credit(display value). Can't be zero. Use MiscChrg.MiscAmt as a default. - includes taxes  */  
   DocInMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InMiscAmt:number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  ChangeTrackApproved  */  
   ChangeTrackApproved:boolean,
      /**  ChangeTrackAmount  */  
   ChangeTrackAmount:number,
      /**  ChangeTrackMemoDesc  */  
   ChangeTrackMemoDesc:string,
      /**  ChangeTrackMemoText  */  
   ChangeTrackMemoText:string,
      /**  ChangeTrackStatus  */  
   ChangeTrackStatus:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   Action:string,
   BaseCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
   DispInvalidData:string,
   DisplayAction:string,
   DocSOMiscAmt:number,
   EnableMiscCode:boolean,
   IncomingOutgoing:string,
   IntComplete:boolean,
   IntError:boolean,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
   IntStatus:string,
   InvalidData:boolean,
   MiscAmtsDiffer:boolean,
   ReadyForOrder:boolean,
   Reject:boolean,
   Rpt1SOMiscAmt:number,
   Rpt2SOMiscAmt:number,
   Rpt3SOMiscAmt:number,
   SOMiscAmt:number,
   Translated:boolean,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_IMOrderRelRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Sales order Line number that this order release is linked to.  */  
   OrderLine:number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   OrderRelNum:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  */  
   ReqDate:string,
      /**  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   OurReqQty:number,
      /**  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  */  
   ShipViaCode:string,
      /**  Indicates if this release is open.  This is normally set to closed via the shipping program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   OpenRelease:boolean,
      /**  Indicates if this release is  "FIRM". The opposite is an uncommitted release, that is when the customer gives releases that are just 'Best Guesses' of what they will require in the future, such as in blanket order situations. This type of  releases is no different to the system, except that the FirmRelease field will be printed on reports such as TimePhase requirements.  */  
   FirmRelease:boolean,
      /**   Indicates if this requirement or any part of it will be manufactured. Default the setting to "No" if valid Part and the Part.Type is "S" or "P".

Default the setting to "Yes" if the part is not found in Part master or the Part.Type = "J".  This flag also gets set if this release gets linked to a Job via Job Entry. There is an Index on this field so that we can display releases that need have a job assigned to them. This display is part of Job Entry.  */  
   Make:boolean,
      /**  The planned production quantity, using Our U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   OurJobQty:number,
      /**  Actual quantity, using our U/M, shipped from the Job.  Updated via the shipping process.  */  
   OurJobShippedQty:number,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.

When an OrderRel record is 'voided' any outstanding inventory allocations are relieved, OrderRel.OpenRelease is set to "no" and records are created/updated in the OrdJobMsg file for all the related  open OrderRel records if the OrderDtl that was tied to a Job to indicate that the line item was voided.  */  
   VoidRelease:boolean,
      /**  Quantity, using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   OurStockQty:number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   WarehouseCode:string,
      /**  Actual quantity, using our U/M, shipped from Stock.  Updated via the shipping process.  */  
   OurStockShippedQty:number,
      /**  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  */  
   PartNum:string,
      /**  Part Revision number.  Mirror image of OrderDtl.RevisionNum.  Not directly maintainable.  */  
   RevisionNum:string,
      /**  Indicates if this customer/shipto  is exempt from sales tax for this line item. If field is non-blank it is considered exempt. Defaults from the Customer/Shipto file.  This code is totally user definable and no validation is required. This field will be printed on the Tax report if this item is reportable .  */  
   TaxExempt:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Enter via a DDSL fill-in for contact name. Use OrderHed.ShpConNum when the OrderRel.ShipToNum = OrderHed.ShipToNum else use ShipTo.PrimScon as a default.  */  
   ShpConNum:number,
      /**  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  */  
   NeedByDate:string,
      /**  EDI Reference  */  
   Reference:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Quantity ,using Selling U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   SellingReqQty:number,
      /**  The planned production quantity, using selling U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   SellingJobQty:number,
      /**  Actual quantity, using selling U/M, shipped from the Job.  Updated via the shipping process.  */  
   SellingJobShippedQty:number,
      /**  Quantity, using selling U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   SellingStockQty:number,
      /**  Actual quantity, using selling U/M, shipped from Stock.  Updated via the shipping process.  */  
   SellingStockShippedQty:number,
      /**  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The shipping "Staging" warehouse for the release.  Defaults from the system default shipping area (Site.DefShippingWhse). This is maintainable in the Sales Allocation program.  */  
   StagingWarehouseCode:string,
      /**  The shipping "Staging" bin for the release.  Defaults from the system default shipping area (Site.DefShippingBin). This is maintainable in the Sales Allocation program.  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**  Quantity from last EDI update.  */  
   CumeQty:number,
      /**  Date of last update  */  
   CumeDate:string,
      /**  Indicates if this order release is linked to an inter-company PO release.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   ICPORelNum:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  A link to the demand schedule that created/updated this OrderRel.  */  
   ScheduleNumber:string,
      /**  The Mark For to be used for this order release record. This MUST BE VALID IN THE SHIPTO file.  */  
   MarkForNum:string,
      /**  Full name for the drop shipment.  */  
   DropShipName:string,
      /**  RAN Number.  Used for informational purposes.  Supplied by EDI.  */  
   RAN:string,
      /**  Demand Reference.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  */  
   DemandReference:string,
      /**  Indicates if the demand schedule that created/updated this order release has been rejected.  */  
   DemandSchedRejected:boolean,
      /**  The last date that the Material Queue Report was run for this release.  This field will be null until the Material Queue Report is run.  */  
   DatePickTicketPrinted:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Verbal Confirmation required  */  
   VerbalConf:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Is a Service Saturday delivery acceptable  */  
   ServSatDelivery:boolean,
      /**  Is a Service Saturday pickup available  */  
   ServSatPickup:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Auto POD flag  */  
   ServPOD:boolean,
      /**  AOD  */  
   ServAOD:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   OverrideService:boolean,
      /**  The dockingstation of the shipto address.  For future use.  */  
   DockingStation:string,
      /**  The location within the customer shipto address.  For future use.  */  
   Location:string,
      /**  The code of the transport routing/time. For future use.  */  
   TransportID:string,
      /**  Ship the good by this time.  */  
   ShipbyTime:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  If true, the OrderRelTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the release before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  Indicates that the One Time ShipTO information defined for this release should be used.  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipment country  */  
   OTSCountryNum:number,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a store description.
Will be printed on the packing slip  */  
   SubShipTo:string,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a routing description.
Will be printed on the packing slip  */  
   ShipRouting:string,
      /**  This field identifies Buy To Order releases.  */  
   BuyToOrder:boolean,
      /**  The value for this field will be defaulted from the Supplier defined in the Part Site sub tab at the Part form. Used only for Buy To Order releases.  */  
   VendorNum:number,
      /**  Supplier Purchase Point. Used only for Buy To Order releases.  */  
   PurPoint:string,
      /**  This field identifies Drop Ship releases. Used only for Buy To Order releases.  */  
   DropShip:boolean,
      /**  Purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   PONum:number,
      /**  The line number of the purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   POLine:number,
      /**  The release number of the purchase order line related to this Buy To Order release. Used only for Buy To Order releases.  */  
   PORelNum:number,
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**  Indicates if/how the OTS can be saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   OTSSaveAs:string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   OTSSaveCustID:string,
      /**  True if Customer or ShipTo record was created using the OTS info.  */  
   OTSCustSaved:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**   Unit of Measure that qualifies the "our" quantity fields.
If a valid part then it is the Base Stocking UOM (Part.IUM).
A mirror image of OrderDtl.IUM. Not directly maintainable  */  
   IUM:string,
      /**   Selling Unit of measure. Qualifies the "Selling" quantity fields.
A mirror image of OrderDtl.SalesUM. Not directly maintainable.  */  
   SalesUM:string,
      /**  Status of Order Release  */  
   RelStatus:string,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  Previous Selling Quantity  */  
   PrevSellQty:number,
      /**  Previous Part Number  */  
   PrevPartNum:string,
      /**  Previous Customer Part Number  */  
   PrevXPartNum:string,
      /**  Previous Need By Date  */  
   PrevNeedByDate:string,
      /**  Previous Require Date  */  
   PrevReqDate:string,
      /**  Previous Ship To Num  */  
   PrevShipToNum:string,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   MFCustNum:number,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   UseOTMF:boolean,
      /**  One Time Mark For Name of the ShipTo.  */  
   OTMFName:string,
      /**  One Time Mark For first line of the ShipTo address.  */  
   OTMFAddress1:string,
      /**  One Time Mark For second line of the ShipTo address.  */  
   OTMFAddress2:string,
      /**  One Time Mark For third line of the ShipTo address.  */  
   OTMFAddress3:string,
      /**  City portion of the One Time Mark For address.  */  
   OTMFCity:string,
      /**  The state or province portion of the One Time Mark For address.  */  
   OTMFState:string,
      /**  The zip or postal code portion of the One Time Mark For address.  */  
   OTMFZIP:string,
      /**  One Time Mark For Contact Name  */  
   OTMFContact:string,
      /**  Fax number for the One Time Mark For.  */  
   OTMFFaxNum:string,
      /**  Phone number for the One Time Mark For  */  
   OTMFPhoneNum:string,
      /**  Country number for the One Time Mark For  */  
   OTMFCountryNum:number,
      /**  ECCPlant  */  
   ECCPlant:string,
      /**  WIOrderLine  */  
   WIOrderLine:string,
      /**  WIOrder  */  
   WIOrder:string,
      /**  WebSKU  */  
   WebSKU:string,
      /**  ShipOvers  */  
   ShipOvers:boolean,
      /**  WIItemPrice  */  
   WIItemPrice:number,
      /**  WIItemShipCost  */  
   WIItemShipCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  PhaseID  */  
   PhaseID:string,
      /**  OTSShipToNum  */  
   OTSShipToNum:string,
      /**  WasRecInvoiced  */  
   WasRecInvoiced:boolean,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   LinkToContract:boolean,
      /**  This flag indicates if the sales order release is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
      /**  One Time ShipTo email address.  */  
   OTSEMailAddress:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Unit of measure for the NumberOfPieces.  */  
   NumberOfPiecesUOM:string,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  Indicates if the release should be added or removed from the fulfillment queue.  */  
   PartAllocQueueAction:string,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
   Action:string,
   DisplayAction:string,
   IncomingOutgoing:string,
   IntComplete:boolean,
   IntError:boolean,
      /**  Unique identifier of related IntQueIn/IntQueOut record  */  
   IntQueID:number,
   IntStatus:string,
   InvalidData:boolean,
   ReadyForOrder:boolean,
   ReleaseStatus:string,
   Translated:boolean,
   WarehouseDesc:string,
   DispInvalidData:string,
   AttributeSetIDDescription:string,
   AttributeSetIDShortDescription:string,
   BitFlag:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderDtlRow{
      /**   Indicates that the line item was closed before any shipments were made against it. Normally line items are closed as part of the Shipping process. By using the "Close Line" menu option the user can close the line manually, to provide the function to close the line when the customer cancels there request.  If the line item had no shipments made it is then marked as "voided". Regardless of shipment activity the line is also marked as closed (OpenLine = No).
When an OrderDtl record is 'voided/closed' all of it's related OrderRel records are also Closed/Voided thereby removing  any outstanding inventory allocations, if the OrderRel records were related to Jobs then they are flagged (OrderRel.OpenChg = Yes) to show up in the Job "Change Order List".  */  
   VoidLine:boolean,
      /**  Indicates if the OrderDtl record is in a "open or closed" status.  This field is not directly maintainable. It can be set to "closed" via the "Close-Line" menu option,  the "Close-Order" menu option, or when all the related OrderRel records are closed, OrderRel records are closed via shipping or by the "Close Release" button within Order Entry. (See VoidLine also).  */  
   OpenLine:boolean,
      /**  Company Identifier.  */  
   Company:string,
      /**  Contains the Order Number that ties this detail record back to an OrderHed record.  */  
   OrderNum:number,
      /**  This field along with Company and OrderNum make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the OrderDtl record for the Order and the adding 1 to it.  The user can override this number if they wish.  */  
   OrderLine:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**   The user's Internal Part number used to identify line item part. It cannot  be blank. It does not have to exist in the Part table.

A default should be made when the OrderDtl.XPartNum is changed.  The PartNum and XPartNum fields work together in providing defaults for each other. Default when a valid record is found in the PartXRef table. NOTE THE PART CROSS REFERENCE LOGIC IS NOT INCLUDED IN RELEASE 1.0 ... PLAN FOR FUTURE  */  
   PartNum:string,
      /**  Line Item description. The Part.Description can be used as a default.  */  
   LineDesc:string,
      /**  EDI Reference  */  
   Reference:string,
      /**  Unit Of Measure (how it is sold/issued). Use the default Part.IUM if it's a valid Part.  */  
   IUM:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLine:string,
      /**  Controls if line is commissionable. Note if all the OrderHed.SalesRep are blank then this should be "No", also the user should not even see this field when there are no sales reps for the order.  */  
   Commissionable:boolean,
      /**  The line item discount percent. It has nothing to do with price break discounts. It is a flat discount percent that defaults from the OrderHed.DiscountPercent, which was originally defaulted from the Customer.DiscountPercent.  */  
   DiscountPercent:number,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in
the customer currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   DocUnitPrice:number,
      /**  Total Order Quantity for the line item. This quantity must always be kept in sync with the scheduled ship quantities stored in the OrderRel table. Normally this field is directly maintainable. However when multiple shipping releases have been established for this line ( more than one OrderRel record) the OrderQty is not maintainable. As the user modifies the quantities in the individual release lines the OrderQty field will get adjusted. This ensures that Order quantity and scheduled ship quantity are always in sync.  */  
   OrderQty:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Discount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   DocDiscount:number,
      /**   Date that the first release needs be shipped by in order to meet the customers due date for the first delivery. Defaulted as OrderHed.RequestDate.
Not directly maintainable when more than one delivery record exists, in which case it gets refreshed as the earliest ReqDate of the related OrderRel records.  */  
   RequestDate:string,
      /**  Product Group Code. Use the Part.ProdCode as a default.  This can be blank or must be valid in the ProdGrup table.  */  
   ProdCode:string,
      /**  An optional field that is used if the customer has a different  Part number  than the users internal part number.  The XPartNum and PartNum can provide defaults for each other via the PartXref table.. The XPartNum can be blank, does not have to exist in the PartXref table.  */  
   XPartNum:string,
      /**  Optional field that contains the customers revision. Default from the CustXPrt.RevisionNum field.  */  
   XRevisionNum:string,
      /**  Indicates the pricing per quantity. It can be "E" = per each, "C" = per hundred,  "M" = per thousand. Used to calculate the extended unit price for the line item. The logic is to divide the OrderDtl.OrderQty by the appropriate "per" value and then multiply by unit price.  Use the  Part.PricePerCode as a default. If Part record does not exist then default as "E".  */  
   PricePerCode:string,
      /**  Contains comments about the detail order line item. These will be printed on the Sales Acknowledgements.  */  
   OrderComment:string,
      /**  Used to establish shipping comments about the order line item. These will copied into the packing slip detail  file as defaults.  */  
   ShipComment:string,
      /**  Used to establish invoice comments about the order line item. These will copied into the Invoice detail  file as defaults.  */  
   InvoiceComment:string,
      /**  Contains comments for pick list or job about the order line item. These will be printed on the picking lists or copied to the job during the link process.  */  
   PickListComment:string,
      /**  Indicates the Tax Category for this record. Defaults from the the or from the Part Master.  */  
   TaxCatID:string,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs. This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering amount in the InvcDetl.  */  
   AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   DocAdvanceBillBal:number,
      /**  Quote number to which this line item detail record is associated with. This is part of the foreign key to QuoteHed file. This field is updated via the "get quote" function within Order Entry.  */  
   QuoteNum:number,
      /**  Quote Line number from which this order line was created. Updated via the Get Quote function within Order Entry. This field along with Company and QuoteNum make up the link to the QuoteDtl file.  */  
   QuoteLine:number,
      /**  Indicates if the Order line item is billed based on Time & Material. This flag is copied into the ShipDtl record during the Shipping Entry process. See ShipDtl.TMBilling description for further details.  */  
   TMBilling:boolean,
      /**  This field is no longer active. It has been replaced by OrderRel.Exempt. The contents were copied into OrderRel.Exempt during the release conversion process. This will be removed in the next release.  */  
   OrigWhyNoTax:string,
      /**   Date the customer needs the first release to be delivered.
Defaulted as OrderHed.NeedByDate. Not directly maintainable when more than one delivery record exists. In which case it is kept in sync with the OrderRel record which has the earliest ReqDate which are maintained in the shipping release dialog boxes.  */  
   NeedByDate:string,
      /**  Customer number that the sales order is for. Duplicated from OrderHed.CustNum.  Used to allow efficient browsing of the OrderDtl records for a specific customer.  */  
   CustNum:number,
      /**   Used to indicate that line item is to be "Reworked" instead of manufactured.  It is shown in the Job Entry Order Activity screens.
When Yes then all related OrderRel records are Make=Yes.  */  
   Rework:boolean,
      /**   Return Authorization Number that OrderDtl is fulfilling.
If entered, must be valid in RMAHead.  */  
   RMANum:number,
      /**  The line item of the RMA detail that this order line item is fulfilling.  */  
   RMALine:number,
      /**  Project ID of the Project table record that this OrderDtl record. Can be blank.  */  
   ProjectID:string,
      /**  Contract Number of the related Service Contract when the LineType field is "CONTRACT"  */  
   ContractNum:number,
      /**  A unique code that identifies the Service Contract when the Line Type is "CONTRACT"  */  
   ContractCode:string,
      /**  The part number used to identify the configured part number initially entered on the line.  */  
   BasePartNum:string,
      /**  Indicate that the item or the product group has a warranty.  */  
   Warranty:boolean,
      /**  Unique code for the Warranty that ties this record to a type of warranty.  Found on either the Part or ProdGrup table.  */  
   WarrantyCode:string,
      /**  The # of days, months, years the material is covered by warranty  */  
   MaterialDuration:number,
      /**  The # of days, months, years the Labor is covered by warranty  */  
   LaborDuration:number,
      /**  The # of days, months, years the Misc. Charges are covered by warranty  */  
   MiscDuration:number,
      /**  Whether the duration of warranty  is for "Days"," Months", "Years".  */  
   MaterialMod:string,
      /**  Whether the duration of warranty  is "Days"," Months"," years".  */  
   LaborMod:string,
      /**  Editor widget for Warranty comments.  */  
   WarrantyComment:string,
      /**  This warranty covers On site visits  */  
   Onsite:boolean,
      /**  Are Material cost covered  */  
   MatCovered:boolean,
      /**  Is Labor Cost Covered  */  
   LabCovered:boolean,
      /**  Are misc. Costs Covered  */  
   MiscCovered:boolean,
      /**  Unit of measure (how it is sold/issued).  Use the default Part.SUM if its a valid Part else use the global variable Def-UM which is established from XaSyst.DefaultUM.  */  
   SalesUM:string,
      /**   This value is used to convert quantity when there is a difference in the customers unit of measure and how it is stocked in inventory. Example is sold in pounds, stocked in sheets.

Formula: Inventory Qty * Conversion Factor = Selling Qty.  */  
   SellingFactor:number,
      /**  Represents one of the requested Order Quantities for the line item using OrderDtl.SUM.  */  
   SellingQuantity:number,
      /**  A Cod which uniquely identfies SalesCat record. Can't be blank.  */  
   SalesCatID:string,
      /**  Indicates if the order line must be shipped complete.  That is, as an orders release are selected for picking during the Auto Pick process of the Order Allocation program, the all releases of the line with a ship date <= the given cutoff date also have to be picked complete otherwise they will not be selected. This is defaulted to Yes when Customer.ShippingQualifier = "L" (Ship Order line 100% complete) and OrderHed.ShipOrderComplete = No. This field is disabled and set to No if the OrderHed.ShipOrderComplete = Yes.  */  
   ShipLineComplete:boolean,
      /**  Quantity from last EDI update.  */  
   CumeQty:number,
      /**  Date of last update  */  
   CumeDate:string,
      /**  The related Marketing Campaign ID. Mirror image of the QuoteHed.MkthCampaignID. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   MktgCampaignID:string,
      /**   Link to the marketing event associated with this record.
The related Marketing Event Sequence. Mirror image of the QuoteHed.MktgEventSeq. Maintainable via order entry if not related to a quote and the CRM module is installed.  */  
   MktgEvntSeq:number,
      /**   increase/decrease when releases are changed.
When locked changes to releases does not change the order quantity.
NOTE: This feature is not implemented with the initial 5.2 release. Intended to be available in a later patch.  */  
   LockQty:boolean,
      /**  Indicates if this order line is linked to an inter-company PO line.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  The date when the configuration was completed for the assembly.  */  
   LastConfigDate:string,
      /**  The system time when the configuration was completed for the assembly.  */  
   LastConfigTime:number,
      /**  The User ID of the last user to complete the configuration of the assembly.  */  
   LastConfigUserID:string,
      /**   Same as Unit price except that this field contains the unit price computed from the input based pricing in a configuration.
If price breaks exist this price should be used as the base price instead of the one found in the part table.  */  
   ConfigUnitPrice:number,
      /**  This is the base price for inputs based pricing of a configuration.  The price of inputs are added to this price to get the ConfigUnitPrice.  */  
   ConfigBaseUnitPrice:number,
      /**  This is the Price List used to determine the starting base price.  */  
   PriceListCode:string,
      /**  This is the Price List used to determine the break % or amount.  */  
   BreakListCode:string,
      /**  The Order Quantity (total qty of related order lines) used to find price when quantity based discounting is applied.  */  
   PricingQty:number,
      /**  Indicates if the price of the order line can be changed.  */  
   LockPrice:boolean,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied.  */  
   ListPrice:number,
      /**   Same as List price except that this field contains the list price in
the customer currency (converted using the exchange rate on OrderHed).  */  
   DocListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied.  */  
   OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency (converted using the exchange rate on OrderHed).  */  
   DocOrdBasedPrice:number,
      /**  This is the Price Group ID used to price the order line with.  */  
   PriceGroupCode:string,
      /**  Indicates if the user selected a price list different from the default.  */  
   OverridePriceList:boolean,
      /**  The revision number used to identify the configured part/revision number initially entered on the line.  */  
   BaseRevisionNum:string,
      /**  The Order Value (total extended price of related order lines) used to find order value break when value based discounting is applied.  */  
   PricingValue:number,
      /**  This field controls the order in which Sales Order lines are displayed.  Display Seq is a decimal number where the whole number portion is used to sequence normal sales order lines and the decimal portion is used to sequence kit components under their associated kit parent.  */  
   DisplaySeq:number,
      /**  The sales order line number of the parent kit item.  This is only relevent for sales order lines which are kit parent or component lines.  If the KitParentLine equals the OrderLine then this is a kit parent line.  */  
   KitParentLine:number,
      /**  Indicates if component lines can be added, deleted and modified during Sales Order entry.  This field is only relevant for sales order lines which are kit parents.  */  
   KitAllowUpdate:boolean,
      /**  Indicates if the parent kit part must be shipped complete of if kit components can be shippped in varying degrees of completeness.  This field is only relevant for sales order lines which are kit parents. If this field is set to "No" then KitPricing must be set to "P".  */  
   KitShipComplete:boolean,
      /**  Indicates if all components are to be backflushed when a kit parent part is shipped.  This field is only relevant for sales order lines which are kit parents.  */  
   KitBackFlush:boolean,
      /**  Indicates if kit components are to be printed on packing slips.  If KitShipComplete is "Yes", then this field must be set to "YES" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   KitPrintCompsPS:boolean,
      /**  Indicates if kit components are to be printed on invoices.  If KitShipComplete is "Yes", then this field must be set to "Yes" as well.  This field is only relevant for sales order lines which are kit parents.  */  
   KitPrintCompsInv:boolean,
      /**  Indicates how kits will be priced.  Values are P = Parent Pricing (The price is obtained from the sales price for the kit parent item), C = Component Pricing (The price is obtained from a rollup of kit component items).  This field is only relevant for sales order lines which are kit parents.  */  
   KitPricing:string,
      /**  Component quantity required to fulfill one kit parent.  This field is only relevant on a sales order line which is a kit component.  */  
   KitQtyPer:number,
      /**  Indicates how Factor is used in calculations.  If M (multiply), the Factor is multiplied, if  D (divide) the factor is divided.  */  
   SellingFactorDirection:string,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate1:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate2:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate3:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate4:number,
      /**  Commission Pay rates for the line item associated to the possible 5 sales reps for the order. Use the OrderHed.RepRate as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y".  */  
   RepRate5:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit1:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit2:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit3:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit4:number,
      /**  Use the OrderHed.RepSplit as the default. These fields are not accessible if the OrderDtl.Commissionable is not "Y"  */  
   RepSplit5:number,
      /**  The Demand Contract Detail record this OrderDtl is related to.  */  
   DemandContractLine:number,
      /**  Create New Job flag  */  
   CreateNewJob:boolean,
      /**  The date before which the order cannot be shipped.  */  
   DoNotShipBeforeDate:string,
      /**  Get Details flag  */  
   GetDtls:boolean,
      /**  The date after which the order cannot be shipped.  */  
   DoNotShipAfterDate:string,
      /**  Schedule Job flag  */  
   SchedJob:boolean,
      /**  Release Job flag  */  
   RelJob:boolean,
      /**  Enable New Job flag  */  
   EnableCreateNewJob:boolean,
      /**  Enable Get Details flag  */  
   EnableGetDtls:boolean,
      /**  Enable Schedule Job flag  */  
   EnableSchedJob:boolean,
      /**  Enable Release Job flag  */  
   EnableRelJob:boolean,
      /**  Indicates the warehouse selected for a counter sale order line.  */  
   CounterSaleWarehouse:string,
      /**  Identifies the Bin selected for a counter sale order line.  */  
   CounterSaleBinNum:string,
      /**  Indicates the lot number selected for a counter sale order line.  */  
   CounterSaleLotNum:string,
      /**  Indicates the dimension code selected for a counter sales order line.  */  
   CounterSaleDimCode:string,
      /**  Indicates if the demand detail that created/updated this order line has been rejected.  */  
   DemandDtlRejected:boolean,
      /**   A character flag field used to differentiate between regular sales order line, Sales Kit parent order line and Sales Kit component order line.
P = Sales Kit Parent line
C = Sales Kit Component Line
Null = regular line  */  
   KitFlag:string,
      /**  Indicates if the kit components have been automatically loaded.  If set to false the user interface will attempt to load the kit components after the user saves a new order line.  */  
   KitsLoaded:boolean,
      /**  The demand contract this demand is for.  */  
   DemandContractNum:number,
      /**  This field along with Company and DemandContractNum make up the unique key to the table. The system should generate this number during entry of new header records. The system determines next available number by finding the last DemandHead for the DemandContractNum and adding 1.  */  
   DemandHeadSeq:number,
      /**  This field along with Company, DemandContractNum and DemandHeadSeq make up the unique key to the table. The system should generate this number during entry of new detail records. The system determines next available number by finding the last DemandDetail record for the DemandHead and the adding 1 to it.  */  
   DemandDtlSeq:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reverse Charge.  */  
   ReverseCharge:boolean,
      /**  Total Number of releases for the line  */  
   TotalReleases:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt1UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt2UnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt3UnitPrice:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt1Discount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt2Discount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt3Discount:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt1AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt2AdvanceBillBal:number,
      /**  Tracks the "Balance" of Advance billings which are to be used to reduce the invoice when actual shipment occurs( in the customer's currency). This value is increased via the "Advance Bill" invoice type. It is reduced when the shipment invoice is created by entering the amount in the InvcDetl.  */  
   Rpt3AdvanceBillBal:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1ListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2ListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3ListPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2OrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3OrdBasedPrice:number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule  */  
   ExtPriceDtl:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2ExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3ExtPriceDtl:number,
      /**  Status of Order Line  */  
   LineStatus:string,
      /**   If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table. Assumed to include taxes  */  
   InUnitPrice:number,
      /**  Same as DocUnit price except that this field contains the unit price including taxes  */  
   DocInUnitPrice:number,
      /**  A flat discount amount for the line item. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed.  - includes taxes  */  
   InDiscount:number,
      /**  A flat discount amount for the line item Converted to the customers currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * InUnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, InUnitPrice or OrderQty fields are changed. - includes taxes  */  
   DocInDiscount:number,
      /**  This is the price returned by the price list before quantity based or order value based discounts are applied. including taxes  */  
   InListPrice:number,
      /**   Same as List price except that this field contains the list price in
the customer currency -including taxes.  */  
   DocInListPrice:number,
      /**  This is the unit price after quantity based or order value based discounts are applied. including taxes  */  
   InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in the customer currency - including taxes.  */  
   DocInOrdBasedPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt1InUnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt2InUnitPrice:number,
      /**   Same as Unit price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed.
If it's a valid item in the Part table the unit price is defaulted using the following logic:
- Determine if a price break is effective. The basic idea is to see if you can find a record in the OPrice table and then adjust the unit price retrieved from the Part table. 
Price breaks can exist with the following configurations:

 1. Part/Customer
 2. Part/Price level
 3. Part 
 4. Product group/Customer
 5. Product group/level
 6. Product Group 
The search logic is done in the above order. If a OPrice is found and it has an EndDate of zeros or the EndDate is >= OrderDate then consider that a price break has been found and the search quits. Use the Order quantity to determine which element of the QtyBreak array should be used. Then either a fixed unit price is selected (unitprices) or a discount percent is selected (discountPercents) and applied to the Unit Price retrieved from the Part table.  */  
   Rpt3InUnitPrice:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt1InDiscount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt2InDiscount:number,
      /**  A flat discount amount for the line item Converted to a report currency. It can be left zero. This is calculated using the OrderDtl.DiscountPercent * (OrderQty * UnitPrice). This field can also be directly updated by the user, However it is refreshed whenever the DiscountPercent, UnitPrice or OrderQty fields are changed.  */  
   Rpt3InDiscount:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1InListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2InListPrice:number,
      /**   Same as List price except that this field contains the list price in
a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3InListPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt1InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt2InOrdBasedPrice:number,
      /**  Same as Order Based price except that this field contains the unit price in a report currency (converted using the exchange rate on OrderHed).  */  
   Rpt3InOrdBasedPrice:number,
      /**  Extended Price for the order line item, rounded according to the Base currency Round rule - Taxes are Included  */  
   InExtPriceDtl:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule - Taxes Included  */  
   DocInExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt1InExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt2InExtPriceDtl:number,
      /**  Reporting currency value of this field  */  
   Rpt3InExtPriceDtl:number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   OldOurOpenQty:number,
      /**  Used to store selling open quantity value setting assigned in product configuration programs  */  
   OldSellingOpenQty:number,
      /**  Used to store open value setting assigned in product configuration programs  */  
   OldOpenValue:number,
      /**  Used to store prod code value assigned in product configuration programs  */  
   OldProdCode:string,
      /**  Previous Selling Quantity  */  
   PrevSellQty:number,
      /**  Previous Part Number  */  
   PrevPartNum:string,
      /**  Previous Customer Part Number  */  
   PrevXPartNum:string,
      /**  The original material sequence of this kit component under the kit parent part.  */  
   KitCompOrigSeq:number,
      /**  The original kit component part number prior to processing any configurator rule programs  */  
   KitCompOrigPart:string,
      /**  If TRUE then this field will mean that the smart string has already been processed  */  
   SmartStringProcessed:boolean,
      /**  Original smart string passed in for configuration  */  
   SmartString:string,
      /**  Contract renewal number. If the value is zero then the contract is not for a renewal.  */  
   RenewalNbr:number,
   DiscBreakListCode:string,
   DiscListPrice:number,
   LockDisc:boolean,
   OverrideDiscPriceList:boolean,
      /**  GroupSeq  */  
   GroupSeq:number,
      /**  ECCOrderNum  */  
   ECCOrderNum:string,
      /**  ECCOrderLine  */  
   ECCOrderLine:number,
      /**  DupOnJobCrt  */  
   DupOnJobCrt:boolean,
      /**  UndersPct  */  
   UndersPct:number,
      /**  Overs  */  
   Overs:number,
      /**  Unders  */  
   Unders:number,
      /**  OversUnitPrice  */  
   OversUnitPrice:number,
      /**  PlanUserID  */  
   PlanUserID:string,
      /**  PlanGUID  */  
   PlanGUID:string,
      /**  MOMsourceType  */  
   MOMsourceType:string,
      /**  MOMsourceEst  */  
   MOMsourceEst:string,
      /**  DefaultOversPricing  */  
   DefaultOversPricing:string,
      /**  ECCPlant  */  
   ECCPlant:string,
      /**  ECCQuoteNum  */  
   ECCQuoteNum:string,
      /**  ECCQuoteLine  */  
   ECCQuoteLine:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  MfgJobType  */  
   MfgJobType:string,
      /**  ProFormaInvComment  */  
   ProFormaInvComment:string,
      /**  CreateJob  */  
   CreateJob:boolean,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   LinkToContract:boolean,
      /**  DocInAdvanceBillBal  */  
   DocInAdvanceBillBal:number,
      /**  InAdvanceBillBal  */  
   InAdvanceBillBal:number,
      /**  Rpt1InAdvanceBillBal  */  
   Rpt1InAdvanceBillBal:number,
      /**  Rpt2InAdvanceBillBal  */  
   Rpt2InAdvanceBillBal:number,
      /**  Rpt3InAdvanceBillBal  */  
   Rpt3InAdvanceBillBal:number,
      /**  PCLinkRemoved  */  
   PCLinkRemoved:boolean,
      /**  CommodityCode  */  
   CommodityCode:string,
      /**  Base price before any price breaks and discounts  */  
   MSRP:number,
      /**  Same as MSRP except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   DocMSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   Rpt1MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   Rpt2MSRP:number,
      /**  Same as MSRP except that this field contains the price in a report currency.  */  
   Rpt3MSRP:number,
      /**  Distributor end customer price.  */  
   EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   DocEndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   Rpt1EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   Rpt2EndCustomerPrice:number,
      /**  Same as end customer price except that this field contains the price in a report currency.  */  
   Rpt3EndCustomerPrice:number,
      /**  Promotional Price offered to Dealer and Distributors.  */  
   PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in the customer currency converted using the exchange rate on OrderHed.  */  
   DocPromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   Rpt1PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   Rpt2PromotionalPrice:number,
      /**  Same as Promotional Price except that this field contains the price in a report currency converted using the exchange rate on OrderHed.  */  
   Rpt3PromotionalPrice:number,
      /**  Current status of line.  This is a maintainable status through Order Line Status maintenance.  Depending on the setting can control is line is updatable from the web.  */  
   OrderLineStatusCode:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  Used specifically for Deal Portal and Location Inventory, not for Inventory Tracked Attributes.  */  
   AttributeSetID:number,
      /**  The unique identifier of the related CPQ Configured Quote Product.  */  
   KBConfigProdID:number,
      /**  The unique identifier of the related original CPQ Configured Quote Product.  */  
   KBOriginalConfigProdID:number,
      /**  TotalCovenantDiscount  */  
   TotalCovenantDiscount:number,
      /**  DocCovenantDiscount  */  
   DocCovenantDiscount:number,
      /**  Rpt1CovenantDiscount  */  
   Rpt1CovenantDiscount:number,
      /**  Rpt2CovenantDiscount  */  
   Rpt2CovenantDiscount:number,
      /**  Rpt3CovenantDiscount  */  
   Rpt3CovenantDiscount:number,
      /**  TotalInCovenantDiscount  */  
   TotalInCovenantDiscount:number,
      /**  DocInCovenantDiscount  */  
   DocInCovenantDiscount:number,
      /**  Rpt1InCovenantDiscount  */  
   Rpt1InCovenantDiscount:number,
      /**  Rpt2InCovenantDiscount  */  
   Rpt2InCovenantDiscount:number,
      /**  Rpt3InCovenantDiscount  */  
   Rpt3InCovenantDiscount:number,
   AvailableQuantity:number,
      /**  Available Price Lists  */  
   AvailPriceLists:string,
   AvailUMFromQuote:string,
   BaseCurrencyID:string,
   BaseCurrSymbol:string,
      /**  Default calculated unit price for a particular part/customer.  Used with integrations for pre-order price validations.  */  
   CalcUnitPrice:number,
   ConfigType:string,
   Configured:string,
   CounterSale:boolean,
      /**  The message text returned by the credit check process.  */  
   CreditLimitMessage:string,
      /**  The source that put the customer on credit hold.  */  
   CreditLimitSource:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencyID:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
   DemandQuantity:number,
   DimCode:string,
   DimConvFactor:number,
      /**  Document currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DocDspDiscount:number,
      /**  Document currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DocDspUnitPrice:number,
      /**  Extended Price for the order line item in Customer currency, rounded according to the Doc currency Round rule  */  
   DocExtPrice:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in document currency  */  
   DocInMiscCharges:number,
      /**  The amount of discount for display in document currency which does not include taxes  */  
   DocLessDiscount:number,
   DocMiscCharges:number,
      /**  Total tax in Doc currency. The sum of all the tax details for the line (OrderRelTax).  */  
   DocTaxAmt:number,
   DocTotalPrice:number,
      /**  Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DspDiscount:number,
      /**  To display the type of job this is: MFG = Manufacturing, PRJ = Project  */  
   DspJobType:string,
      /**  Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   DspUnitPrice:number,
   DUM:string,
      /**  Web basket configuration related SysRowID  */  
   ECCConfigSysRowId:string,
      /**  Additional discount calculated by ECC  */  
   ECCDiscount:number,
      /**  Prevents Epicor repricing the unit price coming from ECC.  This usually would be a result of Epicor going off-line and order pricing was performed by ECC.  */  
   ECCPreventRepricing:boolean,
      /**  Allow enable/disable for the button Attibutes in Order Line  */  
   EnableDynAttrButton:boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   EnableKitUnitPrice:boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   EnableRenewalNbr:boolean,
      /**  This field is used for a row rule on the UIApp, it is set on the AfterGetRows for this table  */  
   EnableSellingQty:boolean,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   EntryProcess:string,
   ExtPrice:number,
   FromQuoteLineFlag:boolean,
      /**  Installation price of an equipment that requires installation in Epicor FSA. This value by default is inherited from the part but it could be overridden for another value if it's necessary.  */  
   FSAInstallationCost:number,
   FSAInstallationOrderLine:number,
   FSAInstallationOrderNum:number,
      /**  Indicates if the equipment requires an installation prior being marked as “Installed” on a Location in Epicor FSA. If true, at shipment it will create a service order for the installation service in FSA.  */  
   FSAInstallationRequired:boolean,
      /**  Indicates the service order template ID that Epicor FSA will use to create the installation service order.  */  
   FSAInstallationType:string,
   FSAInstallationTypeDescription:string,
      /**  Indicates whether the part has at least one Complement  */  
   HasComplement:boolean,
      /**  Indicates whether the part has at least one Downgrade  */  
   HasDowngrade:boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   HasSubstitute:boolean,
      /**  Indicates whether the part has at least one Upgrade  */  
   HasUpgrade:boolean,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line  */  
   InMiscCharges:number,
      /**  The flag to indicate if the Order Header Tax Liability is Tax Inclusive Pricing.  */  
   InPrice:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  Inventory UOM that the Order Detail is allocated against.  */  
   InvtyUOM:string,
   JobTypeDesc:string,
      /**  If the Job has been already created against this line.  */  
   JobWasCreated:boolean,
      /**  If Kit Flag = P then sets this field to the value of the related PartPlant.KitAllowChangeParms. If KitFlag <> P then this will be FALSE.  */  
   KitChangeParms:boolean,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   KitDisable:boolean,
      /**  Kit Flag Description. "P" = Parent, "C" = Component.  */  
   KitFlagDescription:string,
   KitOrderQtyUOM:string,
      /**  If KitFlag = "C" and the parent kit line is configured OR if KitFlag = "P" and Configured = "On" then this field will be TRUE, otherwise it will be false.  */  
   KitStandard:boolean,
      /**  The amount of discount for display which does not include taxes  */  
   LessDiscount:number,
   LotNum:string,
   MiscCharges:number,
   MultipleReleases:boolean,
   OnHandQuantity:number,
   PartExists:boolean,
   PartTrackDimension:boolean,
   PartTrackLots:boolean,
      /**  Optional field used to enter the customers Purchase Order line item reference number.  */  
   POLineRef:string,
   PriceListCodeDesc:string,
   ProcessCounterSale:boolean,
   ProcessQuickEntry:boolean,
   QuoteQtyNum:number,
      /**  For this Detail line there is Release line that has Project and Phase and these Project or Phase was invoiced or used in revenue recognition.  */  
   RelWasRecInvoiced:boolean,
      /**  Pass Credit Limit check message to the UI  */  
   RespMessage:string,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt1DspDiscount:number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt1DspUnitPrice:number,
      /**  Extended Price for the Order Line in Rpt1 currency  */  
   Rpt1ExtPrice:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   Rpt1InMiscCharges:number,
      /**  The amount of discount for display which does not include taxes (report currency)  */  
   Rpt1LessDiscount:number,
      /**  Report currency misc charges  */  
   Rpt1MiscCharges:number,
      /**  Report currency line tax amount  */  
   Rpt1TaxAmt:number,
      /**  Report currency line total price  */  
   Rpt1TotalPrice:number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt2DspDiscount:number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt2DspUnitPrice:number,
      /**  Extended Price for the orderLine in Rpt2 currency.  */  
   Rpt2ExtPrice:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   Rpt2InMiscCharges:number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   Rpt2LessDiscount:number,
      /**  Report currency misc charges  */  
   Rpt2MiscCharges:number,
      /**  Report currency line tax amount  */  
   Rpt2TaxAmt:number,
      /**  Report currency line total price  */  
   Rpt2TotalPrice:number,
      /**  Report Currency Discount amount being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt3DspDiscount:number,
      /**  Report Currency Unit Price being displayed (if the tax option is Tax Inclusive Pricing this amount includes taxes)  */  
   Rpt3DspUnitPrice:number,
      /**  Extended price for the order line in Rpt3 currency  */  
   Rpt3ExtPrice:number,
      /**  Tax Inclusive Pricing - Total Misc Charges for the Order Line in report currency  */  
   Rpt3InMiscCharges:number,
      /**  The amount of discount for display in report currency which does not include taxes (report currency)  */  
   Rpt3LessDiscount:number,
      /**  Report Currency misc charges  */  
   Rpt3MiscCharges:number,
      /**  Report currency line tax amount  */  
   Rpt3TaxAmt:number,
      /**  Report currency line total price  */  
   Rpt3TotalPrice:number,
   SalesRepName1:string,
   SalesRepName2:string,
   SalesRepName3:string,
   SalesRepName4:string,
   SalesRepName5:string,
      /**  Total tax in base currency. The sum of all the tax details for the line.  */  
   TaxAmt:number,
      /**  The Sales Order Quantity expressed in the Inventory Unit of Measure  */  
   ThisOrderInvtyQty:number,
   TotalPrice:number,
   TotalShipped:number,
   WarehouseCode:string,
   WarehouseDesc:string,
   BinNum:string,
      /**  Attribute class is MRP Planned but AttributeSetID has not been set on releases.  */  
   AttributeMismatch:boolean,
      /**  A string containing the parameters needed to run Job Manager  */  
   JobManagerString:string,
      /**  Default calculated order value based discounts unit price for a particular part/customer.  Used with integrations for pre-order price validations.  */  
   CalcOrdBasedPrice:number,
      /**  At least 1 OrderRel for OrderDtl has a PONum assigned.  */  
   SalesOrderLinked:boolean,
      /**  This external column is to be used for the purpose of adding an OrderDtl for a part that has Track Inventory Attributes, allowing the AttributeSetID to be passed in with the line to be included on the OrderRel within the same update method call.  */  
   InventoryAttributeSetID:number,
   BitFlag:number,
   CommodityCodeDescription:string,
   ContractCodeContractDescription:string,
   CustNumSendToFSA:boolean,
   CustNumBTName:string,
   CustNumCustID:string,
   CustNumName:string,
   DiscBreakListCodeListDescription:string,
   DiscBreakListCodeEndDate:string,
   DiscBreakListCodeStartDate:string,
   MktgCampaignIDCampDescription:string,
   MktgEvntEvntDescription:string,
   OrderNumBTCustNum:number,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   PartNumSendToFSA:boolean,
   PartNumTrackInventoryByRevision:boolean,
   PartNumAttrClassID:string,
   PartNumSalesUM:string,
   PartNumPricePerCode:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumIUM:string,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumTrackDimension:boolean,
   PartNumDefaultAttributeSetID:number,
   PartNumFSAEquipment:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PriceBreakListDescription:string,
   PriceBreakStartDate:string,
   PriceBreakEndDate:string,
   ProdCodeDescription:string,
   ProjectIDDescription:string,
   QuoteNumCurrencyCode:string,
   SalesCatIDDescription:string,
   TaxCatIDDescription:string,
   WarrantyCodeWarrDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderMscRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Order line number that this miscellaneous record is related to. If related to the Order then this field is zero. This number is not directly entered by the user; rather it is carried through from the header or detail line that user was on when miscellaneous maintenance was requested.  */  
   OrderLine:number,
      /**  Sequence Number  */  
   SeqNum:number,
      /**  The Miscellaneous Charge Code. This must be valid in the MiscChrg master file.  */  
   MiscCode:string,
      /**  Description of the miscellaneous charge. This will be printed on the acknowledgment and transferred over to invoice processing. The default is provided by MiscChrg.Description, but it's overridable by the user. This can't be blank.  */  
   Description:string,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   MiscAmt:number,
      /**  The amount of the Miscellaneous Charge/Credit(display value). Can't be zero. Use MiscChrg.MiscAmt as a default.  */  
   DocMiscAmt:number,
      /**  Sets the frequency of when this miscellaneous charge should be applied. The options are F - First shipment, L = Last shipment, E = every shipment. This defaults from the MiscChrg.FreqCode.  */  
   FreqCode:string,
      /**  An internally used flag which indicates that this record was created from a Quote via the "Get Quote" function. "Q" = related to the QuoteQty record, "L" = related to the overall QuoteDtl record. This flag is used so that the OrderMsc file can be refreshed from the QuoteMsc when Quantity or Quote/Line # changes occur. The logic is that if a change in order quantity of a order line that is linked to a quote causes a different price break to be selected then all the existing all OrderMsc records where Quoting = "Q" are deleted and then re-pulled in based on the new qty. If the Quote # or QuoteLine are changed then all OrderMsc records where Quoting is either a "Q" or "L" are deleted then re-pulled in from the newly referenced quote.  */  
   Quoting:string,
      /**  Indicates if this order miscellaneous charge is linked to an inter-company PO misc charge.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  Inter Company PO Sequence Number  */  
   ICPOSeqNum:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  Reporting currency value of this field  */  
   Rpt1MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2MiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3MiscAmt:number,
      /**  The amount of the Miscellaneous Charge/Credit. Can't be zero. Use MiscChrg.MiscAmt as a default. - Includes taxes  */  
   InMiscAmt:number,
      /**  The amount of the Miscellaneous Charge/Credit(display value). Can't be zero. Use MiscChrg.MiscAmt as a default. - includes taxes  */  
   DocInMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt1InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt2InMiscAmt:number,
      /**  Reporting currency value of this field  */  
   Rpt3InMiscAmt:number,
      /**  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  */  
   Percentage:number,
      /**  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  */  
   Type:string,
      /**  ChangeTrackApproved  */  
   ChangeTrackApproved:boolean,
      /**  ChangeTrackAmount  */  
   ChangeTrackAmount:number,
      /**  ChangeTrackMemoDesc  */  
   ChangeTrackMemoDesc:string,
      /**  ChangeTrackMemoText  */  
   ChangeTrackMemoText:string,
      /**  ChangeTrackStatus  */  
   ChangeTrackStatus:string,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BaseCurrSymbol:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
   CurrencySwitch:boolean,
   CurrSymbol:string,
      /**  Misc charge amount on display in document currency (may or may not include taxes)  */  
   DocDspMiscAmt:number,
      /**  Misc charge amount on display (may or may not include taxes)  */  
   DspMiscAmt:number,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   EntryProcess:string,
   OpenLine:boolean,
      /**  Misc charge amount on display in report currency  (may or may not include taxes)  */  
   Rpt1DspMiscAmt:number,
      /**  Misc charge amount on display in report currency  (may or may not include taxes)  */  
   Rpt2DspMiscAmt:number,
      /**  Misc charge amount on display in document currency (may or may not include taxes)  */  
   Rpt3DspMiscAmt:number,
      /**  Pass Credit Limit check message to the UI  */  
   RespMessage:string,
   BitFlag:number,
   MiscCodeDescription:string,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_OrderRelRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Sales Order Number  */  
   OrderNum:number,
      /**  Sales order Line number that this order release is linked to.  */  
   OrderLine:number,
      /**  The release number assigned by the system.  The user never sees this field. It  is used as a foreign key in other files (such as ShipDtl) to tie those records back to the release record.  */  
   OrderRelNum:number,
      /**  Used to differentiate between standard lines which are for parts "PART"  and lines for service contracts "CONTRACT".  */  
   LineType:string,
      /**  Date which the item needs to be shipped by in order to meet the customers due date. Initially defaulted as OrderHed.ReqDate.  */  
   ReqDate:string,
      /**  Quantity ,using Our U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   OurReqQty:number,
      /**  The ShipTo ID to be used for this scheduled release record. This MUST BE VALID IN THE SHIPTO file. Use the OrderHead.ShiptoNum as the default when creating new records.  */  
   ShipToNum:string,
      /**  Ship Via ID that is used for this shipment release. THIS CAN BE BLANK or MUST BE VALID IN THE SHIPVIA master file. Use the OrderHead.ShipViaCode as the default.  */  
   ShipViaCode:string,
      /**  Indicates if this release is open.  This is normally set to closed via the shipping program. But can be changed indirectly  by the user during order entry when they "Void" the release..  */  
   OpenRelease:boolean,
      /**  Indicates if this release is  "FIRM". The opposite is an uncommitted release, that is when the customer gives releases that are just 'Best Guesses' of what they will require in the future, such as in blanket order situations. This type of  releases is no different to the system, except that the FirmRelease field will be printed on reports such as TimePhase requirements.  */  
   FirmRelease:boolean,
      /**   Indicates if this requirement or any part of it will be manufactured. Default the setting to "No" if valid Part and the Part.Type is "S" or "P".

Default the setting to "Yes" if the part is not found in Part master or the Part.Type = "J".  This flag also gets set if this release gets linked to a Job via Job Entry. There is an Index on this field so that we can display releases that need have a job assigned to them. This display is part of Job Entry.  */  
   Make:boolean,
      /**  The planned production quantity, using Our U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   OurJobQty:number,
      /**  Actual quantity, using our U/M, shipped from the Job.  Updated via the shipping process.  */  
   OurJobShippedQty:number,
      /**   Indicates if the release was voided. Voided releases items are not maintainable, can't "unvoid". This field is not directly maintainable. Instead the void function will be performed via a "Void Release" button. Which then presents a verification dialog box.

When an OrderRel record is 'voided' any outstanding inventory allocations are relieved, OrderRel.OpenRelease is set to "no" and records are created/updated in the OrdJobMsg file for all the related  open OrderRel records if the OrderDtl that was tied to a Job to indicate that the line item was voided.  */  
   VoidRelease:boolean,
      /**  Quantity, using Our U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   OurStockQty:number,
      /**  Indicates the inventory warehouse. This field is only relevant if this line references a valid Part record. Use the PrimWhse in the Part table as a default.  */  
   WarehouseCode:string,
      /**  Actual quantity, using our U/M, shipped from Stock.  Updated via the shipping process.  */  
   OurStockShippedQty:number,
      /**  The part number the release quantity is currently allocated to (if it exists in the part master file).  This is a duplicate of the OrderDtl part number and is not user maintainable.  */  
   PartNum:string,
      /**  Part Revision number.  Mirror image of OrderDtl.RevisionNum.  Not directly maintainable.  */  
   RevisionNum:string,
      /**  Indicates if this customer/shipto  is exempt from sales tax for this line item. If field is non-blank it is considered exempt. Defaults from the Customer/Shipto file.  This code is totally user definable and no validation is required. This field will be printed on the Tax report if this item is reportable .  */  
   TaxExempt:string,
      /**  Contains the key value for the shipping contact in the CUSTCNT table. Can be blank or must be valid in the CUSTCNT table. Enter via a DDSL fill-in for contact name. Use OrderHed.ShpConNum when the OrderRel.ShipToNum = OrderHed.ShipToNum else use ShipTo.PrimScon as a default.  */  
   ShpConNum:number,
      /**  Date customer needs the item to be delivered. Defaulted as OrderHed.NeedByDate.  */  
   NeedByDate:string,
      /**  EDI Reference  */  
   Reference:string,
      /**  Site Identifier.  */  
   Plant:string,
      /**  Quantity ,using Selling U/M, that is requested to be shipped for this release. This MUST BE > ZERO.  */  
   SellingReqQty:number,
      /**  The planned production quantity, using selling U/M, for the Job. This is not maintainable in order entry. It gets updated via Job Entry.  */  
   SellingJobQty:number,
      /**  Actual quantity, using selling U/M, shipped from the Job.  Updated via the shipping process.  */  
   SellingJobShippedQty:number,
      /**  Quantity, using selling U/M, of the Sales Order release that is planned to be filled (pulled) from stock. This quantity is assigned = to the ReqQty when this item is not manufactured (Make = No).  For manufactured items this quantity can be updated by job entry when the user decides to pull some from stock and manufacture some. This value is used to  allocate to the designated warehouse.  */  
   SellingStockQty:number,
      /**  Actual quantity, using selling U/M, shipped from Stock.  Updated via the shipping process.  */  
   SellingStockShippedQty:number,
      /**  Indicates if the release is selected to be submitted to the picking queue. When submitted for picking a record is written to the MtlQueue table and then SelectForPicking is reset to NO.  */  
   SelectForPicking:boolean,
      /**  The shipping "Staging" warehouse for the release.  Defaults from the system default shipping area (Site.DefShippingWhse). This is maintainable in the Sales Allocation program.  */  
   StagingWarehouseCode:string,
      /**  The shipping "Staging" bin for the release.  Defaults from the system default shipping area (Site.DefShippingBin). This is maintainable in the Sales Allocation program.  */  
   StagingBinNum:string,
      /**   A non blank character indicates that the release could not be picked by the Auto Pick process.
The possible values are;
"L" - Order Line can't be shipped complete.
"O" - Order can't be shipped complete.
"I" - Insufficient quantity reserved
"Z" - Zero quantity reserved.  */  
   PickError:string,
      /**  Quantity from last EDI update.  */  
   CumeQty:number,
      /**  Date of last update  */  
   CumeDate:string,
      /**  Indicates if this order release is linked to an inter-company PO release.  */  
   Linked:boolean,
      /**  Inter-Company Purchase order number  that the detail line item is linked to.  */  
   ICPONum:number,
      /**  The line number of the detail record on the inter-company purchase order.  This number uniquely identifies the record within the Purchase Order number.  The number not directly maintainable, it's assigned by the system when records are created. The user references this item during PO receipt process.  */  
   ICPOLine:number,
      /**  Purchase order release number uniquely identifies a purchase release requirement record for a specific line item on an order. This is assigned by the system.  */  
   ICPORelNum:number,
      /**  External Trading Company Identifier.  */  
   ExtCompany:string,
      /**  A link to the demand schedule that created/updated this OrderRel.  */  
   ScheduleNumber:string,
      /**  The Mark For to be used for this order release record. This MUST BE VALID IN THE SHIPTO file.  */  
   MarkForNum:string,
      /**  Full name for the drop shipment.  */  
   DropShipName:string,
      /**  RAN Number.  Used for informational purposes.  Supplied by EDI.  */  
   RAN:string,
      /**  Demand Reference.  Used for informational purposes and to aide in matching demand schedules with existing OrderRel records.  Supplied by EDI.  */  
   DemandReference:string,
      /**  Indicates if the demand schedule that created/updated this order release has been rejected.  */  
   DemandSchedRejected:boolean,
      /**  The last date that the Material Queue Report was run for this release.  This field will be null until the Material Queue Report is run.  */  
   DatePickTicketPrinted:string,
      /**  Is this a residential delivery  */  
   ResDelivery:boolean,
      /**  Is a Saturday delivery acceptable  */  
   SatDelivery:boolean,
      /**  Is a Saturday pickup available  */  
   SatPickup:boolean,
      /**  Verbal Confirmation required  */  
   VerbalConf:boolean,
      /**  Hazmat or Dangerous Goods delivery  */  
   Hazmat:boolean,
      /**  Documents Only delivery  */  
   DocOnly:boolean,
      /**  Reference Notes for the delivery  */  
   RefNotes:string,
      /**  Apply Handling Charge to shipment  */  
   ApplyChrg:boolean,
      /**  Handling Charge Amount  */  
   ChrgAmount:number,
      /**  Prefer COD delivery  */  
   COD:boolean,
      /**  Add Freight COD Amount owed  */  
   CODFreight:boolean,
      /**  Cashier's Check or Money order is required on COD Delivery  */  
   CODCheck:boolean,
      /**  Amount due on Cashier's check or money order  */  
   CODAmount:number,
      /**  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  */  
   GroundType:string,
      /**  Indicates whether to send an email notification of delivery  */  
   NotifyFlag:boolean,
      /**  The list of email address to notify about a delivery  */  
   NotifyEMail:string,
      /**  Flag to indicate that an insurance value was declared on delivery  */  
   DeclaredIns:boolean,
      /**  Declared Insurance Amount  */  
   DeclaredAmt:number,
      /**  Is a Service Saturday delivery acceptable  */  
   ServSatDelivery:boolean,
      /**  Is a Service Saturday pickup available  */  
   ServSatPickup:boolean,
      /**  Service delivery requires signature  */  
   ServSignature:boolean,
      /**  Service Priority Alert flag  */  
   ServAlert:boolean,
      /**  Service Auto POD flag  */  
   ServPOD:boolean,
      /**  AOD  */  
   ServAOD:boolean,
      /**  Service Home Delivery allowed  */  
   ServHomeDel:boolean,
      /**  Service Home Delivery Type Code  */  
   DeliveryType:string,
      /**  Service Home Delivery date  */  
   ServDeliveryDate:string,
      /**  Home delivery phone number  */  
   ServPhone:string,
      /**  Service Delivery Instructions  */  
   ServInstruct:string,
      /**  Service Signature release is on file  */  
   ServRelease:boolean,
      /**  Service Signature Release authorization number  */  
   ServAuthNum:string,
      /**  Service Reference 1  */  
   ServRef1:string,
      /**  Service Reference 2  */  
   ServRef2:string,
      /**  Service Reference 3  */  
   ServRef3:string,
      /**  Service Reference 4  */  
   ServRef4:string,
      /**  Service Reference 5  */  
   ServRef5:string,
      /**  Override Carrier Defaults.  If not checked then the Site values will be used  */  
   OverrideCarrier:boolean,
      /**  Override Service Options.  If not checked then the Site values will be used  */  
   OverrideService:boolean,
      /**  The dockingstation of the shipto address.  For future use.  */  
   DockingStation:string,
      /**  The location within the customer shipto address.  For future use.  */  
   Location:string,
      /**  The code of the transport routing/time. For future use.  */  
   TransportID:string,
      /**  Ship the good by this time.  */  
   ShipbyTime:number,
      /**  Userid of user who made the last change to this record.  */  
   ChangedBy:string,
      /**  The date that the record was last changed  */  
   ChangeDate:string,
      /**  The time that the record was last change (seconds since midnight)  */  
   ChangeTime:number,
      /**  If true, the OrderRelTax records tied to this release are calculated using Tax Connect logic. If  false, taxes are calculated using the standard calc methods.  */  
   TaxConnectCalc:boolean,
      /**  If set to true, the tax calculation logic will retrieve the default SalesTax ids for the release before calculating taxes. It will also be reset to true if the TaxConnectCalc flag switches from true to false.  */  
   GetDfltTaxIds:boolean,
      /**  Unique identifier of the Tax Region assigned by the user.  */  
   TaxRegionCode:string,
      /**  Indicates that the One Time ShipTO information defined for this release should be used.  */  
   UseOTS:boolean,
      /**  One Time Shipto Name of the ShipTo.  */  
   OTSName:string,
      /**  One Time Shipto first line of the ShipTo address.  */  
   OTSAddress1:string,
      /**  One Time Shipto  second line of the ShipTo address.  */  
   OTSAddress2:string,
      /**  One Time Shipto  third line of the ShipTo address.  */  
   OTSAddress3:string,
      /**  City portion of the One Time Shipto  address.  */  
   OTSCity:string,
      /**  The state or province portion of the One Time Shipto  address.  */  
   OTSState:string,
      /**  The zip or postal code portion of the One Time ShipTo  address.  */  
   OTSZIP:string,
      /**  The State Tax Identification Number of the One Time Shipto.  */  
   OTSResaleID:string,
      /**  One Time Ship To Contact Name  */  
   OTSContact:string,
      /**  Fax number for the One Time ShipTo.  */  
   OTSFaxNum:string,
      /**  Phone number for the One Time ShipTo  */  
   OTSPhoneNum:string,
      /**  One Time Shipment country  */  
   OTSCountryNum:number,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a store description.
Will be printed on the packing slip  */  
   SubShipTo:string,
      /**   Free form. Can be used to further identify the shipping destination. Example, ship to a distribution site, this could contain a routing description.
Will be printed on the packing slip  */  
   ShipRouting:string,
      /**  This field identifies Buy To Order releases.  */  
   BuyToOrder:boolean,
      /**  The value for this field will be defaulted from the Supplier defined in the Part Site sub tab at the Part form. Used only for Buy To Order releases.  */  
   VendorNum:number,
      /**  Supplier Purchase Point. Used only for Buy To Order releases.  */  
   PurPoint:string,
      /**  This field identifies Drop Ship releases. Used only for Buy To Order releases.  */  
   DropShip:boolean,
      /**  Purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   PONum:number,
      /**  The line number of the purchase order related to this Buy To Order release. Used only for Buy To Order releases.  */  
   POLine:number,
      /**  The release number of the purchase order line related to this Buy To Order release. Used only for Buy To Order releases.  */  
   PORelNum:number,
      /**  Indicates if this order is in an "open" status. Open orders appear in the browses, open order reports. This field is not directly maintainable. Instead it is set to "no" if order is cancelled or if there are no open line details. If the order has no OrderDtl records, then it is still considered as "open". An order that is not open, is not accessible by order entry.  */  
   OpenOrder:boolean,
      /**  Indicates if/how the OTS can be saved. Valid values blank = None, C = Customer, P = Prospect, S = Suspect T = Ship To  */  
   OTSSaveAs:string,
      /**  CustID to be used if the OTS is used to create a customer record.  */  
   OTSSaveCustID:string,
      /**  True if Customer or ShipTo record was created using the OTS info.  */  
   OTSCustSaved:boolean,
      /**  Ship To Customer Number. This along with ShipToNum provides the foreign key field to a given ShipTo. Normally this has the same value as the CustNum field. However, if the customer allows 3rd party shipto (Customer.AllowShipTo3) then this could be a different custnum.  */  
   ShipToCustNum:number,
      /**   Unit of Measure that qualifies the "our" quantity fields.
If a valid part then it is the Base Stocking UOM (Part.IUM).
A mirror image of OrderDtl.IUM. Not directly maintainable  */  
   IUM:string,
      /**   Selling Unit of measure. Qualifies the "Selling" quantity fields.
A mirror image of OrderDtl.SalesUM. Not directly maintainable.  */  
   SalesUM:string,
      /**  Status of Order Release  */  
   RelStatus:string,
      /**  Displays the cause why the item is not compliant.  */  
   ComplianceMsg:string,
      /**  Previous Selling Quantity  */  
   PrevSellQty:number,
      /**  Previous Part Number  */  
   PrevPartNum:string,
      /**  Previous Customer Part Number  */  
   PrevXPartNum:string,
      /**  Previous Need By Date  */  
   PrevNeedByDate:string,
      /**  Previous Require Date  */  
   PrevReqDate:string,
      /**  Previous Ship To Num  */  
   PrevShipToNum:string,
      /**  Mark For Customer Number. This along with Mark For ShipToNum provides the foreign key field to a given ShipTo.  */  
   MFCustNum:number,
      /**  Indicates that the One Time Mark For information defined for this record should be used.  */  
   UseOTMF:boolean,
      /**  One Time Mark For Name of the ShipTo.  */  
   OTMFName:string,
      /**  One Time Mark For first line of the ShipTo address.  */  
   OTMFAddress1:string,
      /**  One Time Mark For second line of the ShipTo address.  */  
   OTMFAddress2:string,
      /**  One Time Mark For third line of the ShipTo address.  */  
   OTMFAddress3:string,
      /**  City portion of the One Time Mark For address.  */  
   OTMFCity:string,
      /**  The state or province portion of the One Time Mark For address.  */  
   OTMFState:string,
      /**  The zip or postal code portion of the One Time Mark For address.  */  
   OTMFZIP:string,
      /**  One Time Mark For Contact Name  */  
   OTMFContact:string,
      /**  Fax number for the One Time Mark For.  */  
   OTMFFaxNum:string,
      /**  Phone number for the One Time Mark For  */  
   OTMFPhoneNum:string,
      /**  Country number for the One Time Mark For  */  
   OTMFCountryNum:number,
      /**  ECCPlant  */  
   ECCPlant:string,
      /**  WIOrderLine  */  
   WIOrderLine:string,
      /**  WIOrder  */  
   WIOrder:string,
      /**  WebSKU  */  
   WebSKU:string,
      /**  ShipOvers  */  
   ShipOvers:boolean,
      /**  WIItemPrice  */  
   WIItemPrice:number,
      /**  WIItemShipCost  */  
   WIItemShipCost:number,
      /**  Revision identifier for this row. It is incremented upon each write.  */  
   SysRevID:number,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
      /**  EntityUseCode  */  
   EntityUseCode:string,
      /**  PhaseID  */  
   PhaseID:string,
      /**  OTSShipToNum  */  
   OTSShipToNum:string,
      /**  WasRecInvoiced  */  
   WasRecInvoiced:boolean,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  When a demand is flagged as Link to Contract, MRP will take the demand as part of the planning of the Contract.  */  
   LinkToContract:boolean,
      /**  This flag indicates if the sales order release is ready to be fulfilled.  */  
   ReadyToFulfill:boolean,
      /**  One Time ShipTo email address.  */  
   OTSEMailAddress:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  Number of pieces for this attribute set.  */  
   NumberOfPieces:number,
      /**  Unit of measure for the NumberOfPieces.  */  
   NumberOfPiecesUOM:string,
      /**  Planning number of pieces for this attribute set.  */  
   PlanningNumberOfPieces:number,
      /**  Indicates if the release should be added or removed from the fulfillment queue.  */  
   PartAllocQueueAction:string,
      /**  OTSTaxValidationStatus  */  
   OTSTaxValidationStatus:number,
      /**  OTSTaxValidationDate  */  
   OTSTaxValidationDate:string,
   AvailableQuantity:number,
      /**  BuyOverride  */  
   BuyOverride:boolean,
      /**  The message returned when checking a customer credit limit.  */  
   CreditLimitMessage:string,
      /**  The source that put the customer on credit hold.  */  
   CreditLimitSource:string,
      /**  Currency Code of the related record  */  
   CurrencyCode:string,
      /**  Is OTS allowed by the Sold to Customer?  */  
   CustAllowOTS:boolean,
      /**  True when Customer allows shipping to a Third-Party  */  
   CustomerAllowShipTo3:boolean,
   CustomerCustID:string,
   CustomerName:string,
   DisablePlantWhse:boolean,
   DocSelfAssessTax:number,
   DocTotalTax:number,
   DocWithholdTax:number,
      /**  DropShipOverride  */  
   DropShipOverride:boolean,
      /**   Invoicing Method. If advanced billing is not licensed the only options are CS and MB. Code/Desc: CS = Customer Shipment, MB = Milestone Billing, PB = Progress Billing, TM = Time and aterials
'CP' = Cost Plus
The default is Customer Shipment.  */  
   DspInvMeth:string,
      /**  Revenue Recognition Method has system list of the following options: LBR = Labor Booking Recognition, MAN = Manual Recognition, BDN = Actual Burden Recognition, PCC = POC-Cost-to-Cost, PCE = POC-Efforts, PCU = POC-Units-of-Delivery  */  
   DspRevMethod:string,
   EnableBuyToOrder:boolean,
   EnableMake:boolean,
      /**  this is used in order entry to ignore afterGetRows logic (logic that just refreshes external fields).  */  
   EntryProcess:string,
      /**  ExistPOSugg, external field to show/hide an epishape  */  
   ExistPOSugg:boolean,
   HdrOTS:boolean,
      /**  Unique identifier of related integration record.  */  
   IntExternalKey:string,
      /**  Inventory UOM that the Order Release is allocated against. It is the similare column to the OrderDtl InvtyUOM and should always has the same value as in OrderDtl  */  
   InvtyUOM:string,
      /**  Will be set to true if the current OrderDtl record is KitFlag = 'C' and the KitParent of this record is KitAllowUpdate = NO  */  
   KitDisable:boolean,
      /**  LinkToPONum, external field to show/hide an epishape  */  
   LinkToPONum:boolean,
   MakeOverride:boolean,
      /**  The formatted mark for address  */  
   MarkForAddrFormatted:string,
      /**  Contains the Mark For Address  */  
   MarkForAddrList:string,
   MFCustID:string,
      /**  The flag based on the user anwer if Ship To of the release is supposed be changed but Tax info is not changed because of the conflict in tax pricing  */  
   NoRelTaxRgnChange:boolean,
      /**  Indicates if the item on the line is not compliant on its source, that can be Inventory, PO or Job.  */  
   NotCompliant:boolean,
   OnHandQuantity:number,
   OTSSaved:boolean,
      /**  OTS Tax Liability Code (Order Release)  */  
   OTSTaxRegionCode:string,
   PartExists:boolean,
      /**  If the phase has been recognized or invoiced.  */  
   PhaseWasRecInvoiced:boolean,
   ProjectID:string,
   ReleaseStatus:string,
      /**  the flag to indicate if all previously creaded manually added and manual tax relcords related to Order line release should be deleted if the user populates Tax Exempt field.  */  
   RemoveManAdTax:boolean,
   Rpt1SelfAssessTax:number,
   Rpt1TotalTax:number,
   Rpt1WithholdTax:number,
   Rpt2SelfAssessTax:number,
   Rpt2TotalTax:number,
   Rpt2WithholdTax:number,
   Rpt3SelfAssessTax:number,
   Rpt3TotalTax:number,
   Rpt3WithholdTax:number,
      /**  SalesOrderLinked  */  
   SalesOrderLinked:boolean,
      /**  Self-Assessed Tax  */  
   SelfAssessTax:number,
      /**  Selling Factor for display only  */  
   SellingFactor:number,
      /**  Selling Factor Direction for display oly  */  
   SellingFactorDirection:string,
      /**  The formatted ship to address  */  
   ShipToAddressFormatted:string,
   ShipToAddressList:string,
   ShipToContactEMailAddress:string,
   ShipToContactName:string,
   ShipToSelected:boolean,
   SNEnable:boolean,
   ThisRelInvtyQty:number,
   TotalJobStockShipped:number,
      /**  Invoice Tax  */  
   TotalTax:number,
   UpdateMarkForRecords:boolean,
   VoidOrder:boolean,
      /**  Withholding Tax  */  
   WithholdTax:number,
   AllowTaxCodeUpd:boolean,
      /**  Allow enable/disable for the button Attibutes in Order Release  */  
   EnableDynAttrButton:boolean,
      /**  Attribute class is MRP Planned but AttributeSetID has not been set on release.  */  
   AttributeMismatch:boolean,
      /**  The total allocated quantity for this release.  */  
   AllocatedQuantity:number,
      /**  Error Status Display  */  
   ErrorStatusDisplay:string,
      /**  True if this release is in the fulfillment queue.  */  
   InPartAllocQueue:boolean,
      /**  Show Fulfillment Queue Actions  */  
   ShowAllocationQueueActions:boolean,
   BitFlag:number,
   DynAttrValueSetShortDescription:string,
   DynAttrValueSetDescription:string,
   MarkForNumInactive:boolean,
   MFCustNumInactive:boolean,
   OrderLineLineDesc:string,
   OrderNumCurrencyCode:string,
   OrderNumCardMemberName:string,
   OTMFCountryDescription:string,
   OTSCntryISOCode:string,
   OTSCntryEUMember:boolean,
   OTSCntryDescription:string,
   PartNumTrackInventoryByRevision:boolean,
   PartNumTrackInventoryAttributes:boolean,
   PartNumAttrClassID:string,
   PartNumPricePerCode:string,
   PartNumTrackDimension:boolean,
   PartNumIUM:string,
   PartNumTrackSerialNum:boolean,
   PartNumPartDescription:string,
   PartNumTrackLots:boolean,
   PartNumSellingFactor:number,
   PartNumSalesUM:string,
   PlantName:string,
   PurPointAddress3:string,
   PurPointZip:string,
   PurPointName:string,
   PurPointCountry:string,
   PurPointAddress1:string,
   PurPointState:string,
   PurPointCity:string,
   PurPointAddress2:string,
   PurPointPrimPCon:number,
   ShipToNumInactive:boolean,
   ShipViaCodeWebDesc:string,
   ShipViaCodeDescription:string,
   TaxRegionCodeDescription:string,
   TPShipToName:string,
   TPShipToBTName:string,
   TPShipToCustID:string,
   VendorNumState:string,
   VendorNumZIP:string,
   VendorNumName:string,
   VendorNumAddress2:string,
   VendorNumCountry:string,
   VendorNumCurrencyCode:string,
   VendorNumCity:string,
   VendorNumAddress3:string,
   VendorNumVendorID:string,
   VendorNumDefaultFOB:string,
   VendorNumTermsCode:string,
   VendorNumAddress1:string,
   WarehouseCodeDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SOPOLinkTableset{
   IMOrderDtl:Erp_Tablesets_IMOrderDtlRow[],
   IMOrderHed:Erp_Tablesets_IMOrderHedRow[],
   IMOrderMsc:Erp_Tablesets_IMOrderMscRow[],
   IMOrderRel:Erp_Tablesets_IMOrderRelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SOPOOrderDtlTableset{
   OrderDtl:Erp_Tablesets_OrderDtlRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SOPOOrderMscTableset{
   OrderMsc:Erp_Tablesets_OrderMscRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SOPOOrderRelTableset{
   OrderRel:Erp_Tablesets_OrderRelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SOPOOrderTableset{
   OrderDtl:Erp_Tablesets_OrderDtlRow[],
   OrderMsc:Erp_Tablesets_OrderMscRow[],
   OrderRel:Erp_Tablesets_OrderRelRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param iCPONum
      @param intQueID
   */  
export interface GetByIDIncoming_input{
      /**  PO Number  */  
   iCPONum:number,
      /**  IntQueID value.  Can be 0.  */  
   intQueID:number,
}

export interface GetByIDIncoming_output{
   returnObj:Erp_Tablesets_SOPOLinkTableset[],
}

   /** Required : 
      @param whereClause
      @param pageSize
      @param absolutePage
   */  
export interface GetList_input{
   whereClause:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetList_output{
   returnObj:Erp_Tablesets_IMOrderHedListTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param iOrderNum
      @param iOrderLine
      @param pageSize
      @param absolutePage
   */  
export interface GetOrderDtl_input{
      /**  The Order Number  */  
   iOrderNum:number,
      /**  The Order Line Number  */  
   iOrderLine:number,
      /**  The Page Size  */  
   pageSize:number,
      /**  The Absolute Page  */  
   absolutePage:number,
}

export interface GetOrderDtl_output{
   returnObj:Erp_Tablesets_SOPOOrderDtlTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param iCPONum
   */  
export interface GetOrderHedIntQueID_input{
      /**  iCPONum  */  
   iCPONum:string,
}

export interface GetOrderHedIntQueID_output{
   returnObj:number,
}

   /** Required : 
      @param iOrderNum
      @param iOrderLine
      @param iSeqNum
      @param pageSize
      @param absolutePage
   */  
export interface GetOrderMsc_input{
      /**  The Order Number  */  
   iOrderNum:number,
      /**  The Order Line Number  */  
   iOrderLine:number,
      /**  The Order Misc Sequence Number  */  
   iSeqNum:number,
      /**  The Page Size  */  
   pageSize:number,
      /**  The Absolute Page  */  
   absolutePage:number,
}

export interface GetOrderMsc_output{
   returnObj:Erp_Tablesets_SOPOOrderMscTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param iOrderNum
      @param iOrderLine
      @param iOrderRelNum
      @param pageSize
      @param absolutePage
   */  
export interface GetOrderRel_input{
      /**  The Order Number  */  
   iOrderNum:number,
      /**  The Order Line Number  */  
   iOrderLine:number,
      /**  The Order Release Number  */  
   iOrderRelNum:number,
      /**  The Page Size  */  
   pageSize:number,
      /**  The Absolute Page  */  
   absolutePage:number,
}

export interface GetOrderRel_output{
   returnObj:Erp_Tablesets_SOPOOrderRelTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
}

   /** Required : 
      @param orderNum
   */  
export interface GetOrder_input{
   orderNum:number,
}

export interface GetOrder_output{
   returnObj:Erp_Tablesets_SOPOOrderTableset[],
}

   /** Required : 
      @param whereClauseIMOrderHed
      @param whereClauseIMOrderDtl
      @param whereClauseIMOrderRel
      @param whereClauseIMOrderMsc
      @param pageSize
      @param absolutePage
   */  
export interface GetRows_input{
   whereClauseIMOrderHed:string,
   whereClauseIMOrderDtl:string,
   whereClauseIMOrderRel:string,
   whereClauseIMOrderMsc:string,
   pageSize:number,
   absolutePage:number,
}

export interface GetRows_output{
   returnObj:Erp_Tablesets_SOPOLinkTableset[],
parameters : {
      /**  output parameters  */  
   morePages:boolean,
}
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
      @param dIntQueID
   */  
export interface PreRejectICPOLink_input{
      /**  The IntQueID of the record to reject  */  
   dIntQueID:number,
}

export interface PreRejectICPOLink_output{
parameters : {
      /**  output parameters  */  
   cMessageText:string,
}
}

export interface ProcessSuggestions_output{
   returnObj:Erp_Tablesets_SOPOOrderDtlTableset[],
parameters : {
      /**  output parameters  */  
   needsConfig:boolean,
}
}

   /** Required : 
      @param cIntQueIDList
   */  
export interface ReadyForOrderAll_input{
      /**  A delimited list of IntQueIDs of the IMOrderHed records
            to mark as ReadyForOrder  */  
   cIntQueIDList:string,
}

export interface ReadyForOrderAll_output{
   returnObj:Erp_Tablesets_IMOrderHedListTableset[],
}

   /** Required : 
      @param ds
   */  
export interface Update_input{
   ds:Erp_Tablesets_SOPOLinkTableset[],
}

export interface Update_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SOPOLinkTableset,
}
}

   /** Required : 
      @param cIntQueIDList
   */  
export interface ValidateReadyForOrderAll_input{
      /**  A delimited list of IntQueIDs of the IMOrderHed records
            to mark as ReadyForOrder  */  
   cIntQueIDList:string,
}

export interface ValidateReadyForOrderAll_output{
}

