import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.ReportQtySvc
// Description: Quantity Reporting from MES menu
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/$metadata", {
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
   Summary: Invoke method CheckInspResults
   Description: This method validates if InspResults has been entered when the Inspection Data is allowed for the current OprSeq.
   OperationID: CheckInspResults
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckInspResults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckInspResults_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckInspResults(requestBody:CheckInspResults_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckInspResults_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/CheckInspResults", {
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
         resolve(data as CheckInspResults_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DeleteLaborEquip
   Description: This method should call when EquipID is changed
   OperationID: DeleteLaborEquip
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DeleteLaborEquip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLaborEquip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DeleteLaborEquip(requestBody:DeleteLaborEquip_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DeleteLaborEquip_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/DeleteLaborEquip", {
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
         resolve(data as DeleteLaborEquip_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewLaborEquip
   Description: This method returns the new Labor Equipment
   OperationID: GetNewLaborEquip
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewLaborEquip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborEquip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewLaborEquip(requestBody:GetNewLaborEquip_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewLaborEquip_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/GetNewLaborEquip", {
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
         resolve(data as GetNewLaborEquip_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewReportQty
   Description: This method returns the new ReportQty dataset in place of the standard GetNew method.
   OperationID: GetNewReportQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewReportQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewReportQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewReportQty(requestBody:GetNewReportQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewReportQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/GetNewReportQty", {
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
         resolve(data as GetNewReportQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAsmSeq
   Description: This method validates the Assembly sequence.
   OperationID: OnChangeAsmSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAsmSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAsmSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAsmSeq(requestBody:OnChangeAsmSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAsmSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/OnChangeAsmSeq", {
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
         resolve(data as OnChangeAsmSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeEquipID
   Description: This method should call when EquipID is changed
   OperationID: OnChangeEquipID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeEquipID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeEquipID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeEquipID(requestBody:OnChangeEquipID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeEquipID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/OnChangeEquipID", {
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
         resolve(data as OnChangeEquipID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeJobNum
   Description: This method validates the Operation sequence.
   OperationID: OnChangeJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeJobNum(requestBody:OnChangeJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/OnChangeJobNum", {
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
         resolve(data as OnChangeJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeNextOprSeq
   Description: This method validates the Next Operation sequence.
   OperationID: OnChangeNextOprSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeNextOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeNextOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeNextOprSeq(requestBody:OnChangeNextOprSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeNextOprSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/OnChangeNextOprSeq", {
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
         resolve(data as OnChangeNextOprSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeOprSeq
   Description: This method validates the Operation sequence.
   OperationID: OnChangeOprSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeOprSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOprSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeOprSeq(requestBody:OnChangeOprSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeOprSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/OnChangeOprSeq", {
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
         resolve(data as OnChangeOprSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCID
   Description: This method validates the PCID
   OperationID: OnChangePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePCID(requestBody:OnChangePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/OnChangePCID", {
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
         resolve(data as OnChangePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeResource
   Description: This method validates the ResourceID.
   OperationID: OnChangeResource
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeResource_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeResource_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeResource(requestBody:OnChangeResource_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeResource_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/OnChangeResource", {
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
         resolve(data as OnChangeResource_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ReportQuantity
   Description: This method reports the quantity changes to the database
   OperationID: ReportQuantity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ReportQuantity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReportQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ReportQuantity(requestBody:ReportQuantity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ReportQuantity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/ReportQuantity", {
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
         resolve(data as ReportQuantity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateLaborEquip
   Description: This method should call when EquipID is changed
   OperationID: UpdateLaborEquip
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateLaborEquip_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateLaborEquip_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateLaborEquip(requestBody:UpdateLaborEquip_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateLaborEquip_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/UpdateLaborEquip", {
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
         resolve(data as UpdateLaborEquip_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSerialBeforeSelect
   Description: Call before allowing the select of serial numbers
   OperationID: ValidateSerialBeforeSelect
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSerialBeforeSelect_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSerialBeforeSelect_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSerialBeforeSelect(requestBody:ValidateSerialBeforeSelect_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSerialBeforeSelect_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/ValidateSerialBeforeSelect", {
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
         resolve(data as ValidateSerialBeforeSelect_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSelectSerialNumbersParams
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParams
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParams_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParams_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectSerialNumbersParams(requestBody:GetSelectSerialNumbersParams_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSelectSerialNumbersParams_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/GetSelectSerialNumbersParams", {
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
         resolve(data as GetSelectSerialNumbersParams_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number is valid for this transaction
   OperationID: ValidateSN
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSN(requestBody:ValidateSN_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSN_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.ReportQtySvc/ValidateSN", {
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
         resolve(data as ValidateSN_output)
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
      @param ipJobNum
      @param ipAssemblySeq
      @param ipOprSeq
   */  
export interface CheckInspResults_input{
      /**  Current Job  */  
   ipJobNum:string,
      /**  Current AssembleSeq  */  
   ipAssemblySeq:number,
      /**  Current OprSeq  */  
   ipOprSeq:number,
}

export interface CheckInspResults_output{
parameters : {
      /**  output parameters  */  
   inspectionOK:boolean,
}
}

   /** Required : 
      @param empID
      @param equipID
      @param hedSeq
      @param dtlSeq
      @param ds
   */  
export interface DeleteLaborEquip_input{
      /**  Current Employee ID  */  
   empID:string,
      /**  Current Labor Equipment ID  */  
   equipID:string,
      /**  Current LaborDtl.LaborHedSeq value  */  
   hedSeq:number,
      /**  Current LaborDtl.LaborDtlSeq value  */  
   dtlSeq:number,
   ds:Erp_Tablesets_ReportQtyTableset[],
}

export interface DeleteLaborEquip_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReportQtyTableset,
}
}

export interface Erp_Tablesets_ReportQtyEquipRow{
   EmpID:string,
   EquipID:string,
   CurrentMeter:number,
   Hours:number,
   MeterUOM:string,
   Qty:number,
      /**  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  */  
   LaborDtlSeq:number,
      /**  Used as the foreign key to the LaborHed record.  */  
   LaborHedSeq:number,
      /**   Indicate if/how equipment meter values can be updated from labor entry.
Valid options are; "No"  "Hrs" (Hours), "Qty" (Quantity), "Mtr" (Current Meter Value)
	No - Labor does NOT update Equipment Meter values.
	Qty  - Quantity is +/- against Equip.CurrentMeter  ( no uom conversion, just straight usage of field value)
	Hrs  -Hours are +/- against Equip.CurrentMeter
	Mtr  - Meter value is entered directly 
                           Only updates the Equipment when the Labor Date/Time is > latest Meter Reading Date/Time.  */  
   LaborMeterOpt:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReportQtyPartRow{
   EmpID:string,
   PartNum:string,
   CurrentQty:number,
   PrevQty:number,
   TotalQty:number,
   RequestMove:boolean,
      /**  Unit of measure for CurrentQty  */  
   CurrentUOM:string,
      /**  Unit of measure for PrevQty  */  
   PrevUOM:string,
      /**  Unit of measure for TotalQty  */  
   TotalUOM:string,
   PartDescription:string,
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReportQtyRow{
   JobNum:string,
   AssemblySeq:number,
   OprSeq:number,
   ResourceID:string,
   CurrentQty:number,
   TotalQty:number,
   NextAssemblySeq:number,
   NextOprSeq:number,
   ResourceGrpDesc:string,
   OprDescription:string,
   EmpID:string,
   ResourceGrpID:string,
   RequestMove:boolean,
      /**  Indicates whether to enable/disable the RequestMove,NextOprSeq or Tag button  */  
   EnableReqOprTag:boolean,
   TagType:string,
   TagPart:string,
   TagRevisionNum:string,
   TagDescription:string,
   TagIUM:string,
   TagInputWhse:string,
   TagInputBinNum:string,
   PrevQty:number,
   ResourceIDDesc:string,
      /**  Determines if CurrentQty is available for input.  Is set to false when ReportQtyPart records exist because the quantities will be entered at the part level.  */  
   EnableCurrentQty:boolean,
      /**  Determines if RequestMove is available for input.  */  
   EnableRequestMove:boolean,
      /**  Unit of measure for CurrentQty  */  
   CurrentUOM:string,
      /**  Unit of measure for PrevQty  */  
   PrevUOM:string,
      /**  Unit of measure for TotalQty  */  
   TotalUOM:string,
      /**  Enable input Inspection Data  */  
   EnableInspection:boolean,
   Company:string,
   EnableSN:boolean,
   EnablePrintTagsList:boolean,
   ClockInDate:string,
   ClockinTime:number,
   EnableNextOprSeq:boolean,
      /**  Display the quantity completed for this operation in general.  */  
   CompletedQty:number,
      /**  Unit of measure for CompletedQty  */  
   CompletedQtyUOM:string,
      /**  Package Control Identification Number  */  
   PCID:string,
      /**  Internal flag used for the row rules to control whether the PCID columns should be enabled.  */  
   EnablePCID:boolean,
      /**  BinNum  */  
   OutputBin:string,
      /**  The output warehouse from the resource  */  
   OutputWarehouse:string,
      /**  Internal flag used for the row rules to control whether the Lot columns should be enabled.  */  
   EnableLot:boolean,
      /**  Lot number that is to be added to the PCID  */  
   LotNum:string,
      /**  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  */  
   PrintPCIDContents:boolean,
   AssemblySeqDescription:string,
   OprSeqDescription:string,
      /**  ID of related Attribute Class.  */  
   AttrClassID:string,
      /**  The Full Description of the Attribute Set for CurrentQty  */  
   CurrentAttributeSetDescription:string,
      /**  he unique identifier of the related Dynamic Attribute Set for the Current Quantity.  */  
   CurrentAttributeSetID:number,
      /**  The Short Description of the Attribute Set for CurrentQty  */  
   CurrentAttributeSetShortDescription:string,
   CurrentRevisionNum:string,
   CurrentTrackInventoryByRevision:boolean,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_ReportQtyTableset{
   ReportQty:Erp_Tablesets_ReportQtyRow[],
   ReportQtyEquip:Erp_Tablesets_ReportQtyEquipRow[],
   ReportQtyPart:Erp_Tablesets_ReportQtyPartRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SNFormatRow{
      /**  Company Identifier.  */  
   Company:string,
      /**  Site Identifier. This field cannot be blank.  */  
   Plant:string,
      /**  The PartNum field identifies the Part and is used in the primary key.  */  
   PartNum:string,
      /**  Number of digits in the serial number  */  
   NumberOfDigits:number,
      /**  If the SNBaseDataType is Mask this is the Serial Mask ID assigned for format validation/generation.  */  
   SNMask:string,
      /**   Current setting for Data type of the Base Serial Number field to be used as new serial numbers are generated. Valid values; Character, Integer, Mask
Code/desc required:
CHARACTER`Alphanumeric
INTEGER`NumericOnly
MASK`Serial Mask
This field should be flagged as Include = true in Object Designer.  */  
   SNBaseDataType:string,
      /**   Current setting for Format of the Base serial number that will be used as new serial numbers are generated. Expressed in progress syntax. Ex: X(30), 99999999 for Character or Integer, or as a Serial Mask defined in SerialMask table.
This field should be flagged as ReadOnly and Include = true in Object Designer.  */  
   SNFormat:string,
      /**  Whether or not to have leading zeroes  */  
   LeadingZeroes:boolean,
      /**   Current setting for the prefix that will be attached to all new Serial Numbers as they are generated for Character and Integer format types.
This field should be flagged as Include = true in Object Designer.  */  
   SNPrefix:string,
      /**  A standard suffix that will be attached to all serial numbers generated for the PartSite currently used only by SNBaseStructure Mask types  */  
   SNMaskSuffix:string,
      /**  The prefix that was used to construct the serial number currently used only by SNBaseStructure Mask types  */  
   SNMaskPrefix:string,
      /**  This is the last used serial sequence. It is used only for the Mask Generate type to determine the next logical serial number to generate for this part/Site. It can be altered by the user and several PartSites can have the same counter values defined, but  */  
   SNLastUsedSeq:string,
   HasSerialNumbers:boolean,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   BitFlag:number,
   PartPricePerCode:string,
   PartTrackLots:boolean,
   PartTrackSerialNum:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartIUM:string,
   PartSellingFactor:number,
   PartPartDescription:string,
   SerialMaskMaskType:number,
   SerialMaskMask:string,
   SerialMaskExample:string,
   SerialMaskDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsRow{
      /**  The part number to which the serial numbers have been assigned.  */  
   partNum:string,
      /**  The quantity of serial numbers that need to be selected.  */  
   quantity:number,
      /**  whereClause for filtering available serial numbers  */  
   whereClause:string,
      /**  transType of this transaction  */  
   transType:string,
      /**  Include when filtering a set of SN's for BL processing is necessary.  It may be null if not needed.  */  
   sourceRowID:string,
      /**  Determines if serial numbers can be created.  */  
   enableCreate:boolean,
      /**  Determines if serial numbers can be selected.  */  
   enableSelect:boolean,
      /**  Determines if serial numbers can be retrieved.  */  
   enableRetrieve:boolean,
      /**  Specifies whether Voided serial numbers can be manually selected.  */  
   allowVoided:boolean,
      /**  The Plant associated with this transaction  */  
   plant:string,
   xrefPartNum:string,
   xrefPartType:string,
   xrefCustNum:number,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   attributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   attributeSetShortDescription:string,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   revisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_SelectSerialNumbersParamsTableset{
   SelectSerialNumbersParams:Erp_Tablesets_SelectSerialNumbersParamsRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SelectedSerialNumbersRow{
      /**  Company  */  
   Company:string,
      /**  SerialNumber  */  
   SerialNumber:string,
      /**  Scrapped flag  */  
   Scrapped:boolean,
      /**  Scrapped reason code  */  
   ScrappedReasonCode:string,
      /**  Voided flag  */  
   Voided:boolean,
      /**  Reference field  */  
   Reference:string,
      /**  Reason code type = s  */  
   ReasonCodeType:string,
      /**  Reason code description  */  
   ReasonCodeDesc:string,
      /**  PartNumber  */  
   PartNum:string,
      /**  Serial number prefix  */  
   SNPrefix:string,
      /**  Base number used to create the serial number  */  
   SNBaseNumber:string,
      /**  RowID of the source record for this serial number  */  
   SourceRowID:string,
      /**  TransType of the record that created this serial number  */  
   TransType:string,
      /**  True if this serial numbered part passed inspection  */  
   PassedInspection:boolean,
      /**  Used to flag previously selected serial numbers as deselected  */  
   Deselected:boolean,
   KitWhseList:string,
      /**  This will be the raw serial number as it was scanned or entered into the system. This would only differ from the SerialNumber field if a validate type mask was being used where characters were stripped (using ~ in the mask).  */  
   RawSerialNum:string,
      /**  Action type field used for Kanban receipts to indicate if the new serial number status is Inventory, Scrapped or NonConf.  This requires Code/desc:  1 ` inventory 2 ` Scrapped 3 ` Nonconformance  */  
   KBLbrAction:number,
      /**  Description field for KBLbrAction ? holds the translated description for the KBLbrAction code for UI display and combo box.  */  
   KBLbrActionDesc:string,
      /**  If true, then users can not deselect this serial number.  This is used by applications that allow maintenance to the Selected Serial Numbers after update.  */  
   PreventDeselect:boolean,
      /**  Used only by SN Assignment  */  
   XRefPartNum:string,
      /**  Used only by SN Assignment: C = Customer Part / I = Internal Part XRef  */  
   XRefPartType:string,
   PreDeselected:boolean,
      /**  temporary field used to link the packout lines to ship detail lines  */  
   poLinkValues:string,
      /**  The mask the was used to generate the serial number  */  
   SNMask:string,
      /**  Flag to indicate that the SelectedSerialNumbers entry has not yet been saved to the DB for the related transaction. Used to keep track of which deselected serial numbers need to be passed to the transaction update logic.  */  
   NotSavedToDB:boolean,
   RowSelected:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param empID
      @param ds
   */  
export interface GetNewLaborEquip_input{
      /**  Current Employee ID  */  
   empID:string,
   ds:Erp_Tablesets_ReportQtyTableset[],
}

export interface GetNewLaborEquip_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReportQtyTableset,
}
}

   /** Required : 
      @param empID
      @param DtlLaborHedSeq
      @param DtlLaborDtlSeq
   */  
export interface GetNewReportQty_input{
      /**  Current Employee ID  */  
   empID:string,
      /**  Current LaborDtl.LaborHedSeq value if record is available  */  
   DtlLaborHedSeq:number,
      /**  Current LaborDtl.LaborDtlSeq value if record is available  */  
   DtlLaborDtlSeq:number,
}

export interface GetNewReportQty_output{
   returnObj:Erp_Tablesets_ReportQtyTableset[],
}

   /** Required : 
      @param hedSeq
      @param dtlSeq
      @param ds
   */  
export interface GetSelectSerialNumbersParams_input{
      /**  Current LaborDtl.LaborHedSeq value  */  
   hedSeq:number,
      /**  Current LaborDtl.LaborDtlSeq value  */  
   dtlSeq:number,
   ds:Erp_Tablesets_ReportQtyTableset[],
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReportQtyTableset,
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
      @param assemblySeq
      @param ds
   */  
export interface OnChangeAsmSeq_input{
      /**  Assembly Sequence  */  
   assemblySeq:number,
   ds:Erp_Tablesets_ReportQtyTableset[],
}

export interface OnChangeAsmSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReportQtyTableset,
}
}

   /** Required : 
      @param equipID
      @param DtlLaborHedSeq
      @param DtlLaborDtlSeq
      @param ds
   */  
export interface OnChangeEquipID_input{
      /**  equipID  */  
   equipID:string,
      /**  Current LaborDtl.LaborHedSeq value  */  
   DtlLaborHedSeq:number,
      /**  Current LaborDtl.LaborDtlSeq value  */  
   DtlLaborDtlSeq:number,
   ds:Erp_Tablesets_ReportQtyTableset[],
}

export interface OnChangeEquipID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReportQtyTableset,
}
}

   /** Required : 
      @param jobNum
      @param ds
   */  
export interface OnChangeJobNum_input{
      /**  Job Number  */  
   jobNum:string,
   ds:Erp_Tablesets_ReportQtyTableset[],
}

export interface OnChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReportQtyTableset,
}
}

   /** Required : 
      @param nextOprSeq
      @param ds
   */  
export interface OnChangeNextOprSeq_input{
      /**  Next Operation Sequence  */  
   nextOprSeq:number,
   ds:Erp_Tablesets_ReportQtyTableset[],
}

export interface OnChangeNextOprSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReportQtyTableset,
}
}

   /** Required : 
      @param oprSeq
      @param ds
   */  
export interface OnChangeOprSeq_input{
      /**  Operation Sequence  */  
   oprSeq:number,
   ds:Erp_Tablesets_ReportQtyTableset[],
}

export interface OnChangeOprSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReportQtyTableset,
}
}

   /** Required : 
      @param pcid
      @param ds
   */  
export interface OnChangePCID_input{
      /**  PCID to validate  */  
   pcid:string,
   ds:Erp_Tablesets_ReportQtyTableset[],
}

export interface OnChangePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReportQtyTableset,
}
}

   /** Required : 
      @param resourceID
      @param ds
   */  
export interface OnChangeResource_input{
      /**  Resource ID  */  
   resourceID:string,
   ds:Erp_Tablesets_ReportQtyTableset[],
}

export interface OnChangeResource_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReportQtyTableset,
}
}

   /** Required : 
      @param hedSeq
      @param dtlSeq
      @param ds
   */  
export interface ReportQuantity_input{
      /**  Current LaborDtl.LaborHedSeq value  */  
   hedSeq:number,
      /**  Current LaborDtl.LaborDtlSeq value  */  
   dtlSeq:number,
   ds:Erp_Tablesets_ReportQtyTableset[],
}

export interface ReportQuantity_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_ReportQtyTableset,
}
}

   /** Required : 
      @param empID
      @param equipID
      @param hedSeq
      @param dtlSeq
      @param ds
   */  
export interface UpdateLaborEquip_input{
      /**  Current Employee ID  */  
   empID:string,
      /**  Current Labor Equipment ID  */  
   equipID:string,
      /**  Current LaborDtl.LaborHedSeq value  */  
   hedSeq:number,
      /**  Current LaborDtl.LaborDtlSeq value  */  
   dtlSeq:number,
   ds:Erp_Tablesets_ReportQtyTableset[],
}

export interface UpdateLaborEquip_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReportQtyTableset,
}
}

   /** Required : 
      @param ds
      @param serialNumber
      @param hedSeq
      @param dtlSeq
   */  
export interface ValidateSN_input{
   ds:Erp_Tablesets_ReportQtyTableset[],
      /**  Serial number to validate.  */  
   serialNumber:string,
      /**  Current LaborDtl.LaborHedSeq value  */  
   hedSeq:number,
      /**  Current LaborDtl.LaborDtlSeq value  */  
   dtlSeq:number,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReportQtyTableset,
   isVoided:boolean,
}
}

   /** Required : 
      @param ds
      @param dtlLaborHedSeq
      @param dtlLaborDtlSeq
   */  
export interface ValidateSerialBeforeSelect_input{
   ds:Erp_Tablesets_ReportQtyTableset[],
      /**  Labor Head Sequence  */  
   dtlLaborHedSeq:number,
      /**  Labor Dtl Sequence  */  
   dtlLaborDtlSeq:number,
}

export interface ValidateSerialBeforeSelect_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_ReportQtyTableset,
   notEnoughSerials:string,
   totSNReq:number,
   totNewSNReq:number,
}
}

