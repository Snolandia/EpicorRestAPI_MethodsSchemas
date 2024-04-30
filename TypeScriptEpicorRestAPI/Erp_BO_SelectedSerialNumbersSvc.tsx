import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.SelectedSerialNumbersSvc
// Description: New and existing serial numbers are added to the ttSelectedSerialNumbers
temp table when the user selects them.  Also allows update of the SNFormat
temp table.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/$metadata", {
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
   Summary: Invoke method AddSerialNum
   Description: This method is used for adding an existing SerialNo record to the Selected
Serial Numbers dataset.
   OperationID: AddSerialNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AddSerialNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AddSerialNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AddSerialNum(requestBody:AddSerialNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AddSerialNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/AddSerialNum", {
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
         resolve(data as AddSerialNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HHScanCheckSN
   Description: Determines whether the SN exists or not. Also performs other validation on the request.
   OperationID: HHScanCheckSN
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HHScanCheckSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HHScanCheckSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HHScanCheckSN(requestBody:HHScanCheckSN_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HHScanCheckSN_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/HHScanCheckSN", {
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
         resolve(data as HHScanCheckSN_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateSerialNum
   Description: Add a serial number temporary record to the Selected Serial Number dataset.
   OperationID: CreateSerialNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateSerialNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSerialNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateSerialNum(requestBody:CreateSerialNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateSerialNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/CreateSerialNum", {
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
         resolve(data as CreateSerialNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateSerialNumRange
   Description: Create multiple serial number temporary records in the Selected Serial Numbers dataset.
   OperationID: CreateSerialNumRange
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateSerialNumRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSerialNumRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateSerialNumRange(requestBody:CreateSerialNumRange_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateSerialNumRange_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/CreateSerialNumRange", {
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
         resolve(data as CreateSerialNumRange_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method KineticGetSerialNumFormat
   Description: Gets the next serial number format based on the part number passed in.
   OperationID: KineticGetSerialNumFormat
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/KineticGetSerialNumFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KineticGetSerialNumFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KineticGetSerialNumFormat(requestBody:KineticGetSerialNumFormat_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<KineticGetSerialNumFormat_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/KineticGetSerialNumFormat", {
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
         resolve(data as KineticGetSerialNumFormat_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNextSN
   Description: Gets the next serial number based on the format for the part number passed in.
   OperationID: GetNextSN
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNextSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNextSN(requestBody:GetNextSN_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNextSN_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/GetNextSN", {
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
         resolve(data as GetNextSN_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSerialNumFormat
   Description: Gets the next serial number format based on the part number passed in.
   OperationID: GetSerialNumFormat
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSerialNumFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSerialNumFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSerialNumFormat(requestBody:GetSerialNumFormat_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSerialNumFormat_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/GetSerialNumFormat", {
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
         resolve(data as GetSerialNumFormat_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method RetrieveSerialNumbers
   Description: Retrieve serial numbers
   OperationID: RetrieveSerialNumbers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RetrieveSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrieveSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RetrieveSerialNumbers(requestBody:RetrieveSerialNumbers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RetrieveSerialNumbers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/RetrieveSerialNumbers", {
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
         resolve(data as RetrieveSerialNumbers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessSelectedSerialNumbers
   Description: Process selected serial numbers
   OperationID: ProcessSelectedSerialNumbers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessSelectedSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessSelectedSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessSelectedSerialNumbers(requestBody:ProcessSelectedSerialNumbers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessSelectedSerialNumbers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/ProcessSelectedSerialNumbers", {
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
         resolve(data as ProcessSelectedSerialNumbers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateSingleSerialNumber
   Description: Add a serial number temporary record to the Selected Serial Number dataset.  The source data for this method is dataset SerialNumberSelection.
   OperationID: CreateSingleSerialNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateSingleSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSingleSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateSingleSerialNumber(requestBody:CreateSingleSerialNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateSingleSerialNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/CreateSingleSerialNumber", {
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
         resolve(data as CreateSingleSerialNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CreateSerialNumberRange
   Description: Create multiple serial number temporary records in the Serial Number Selection dataset.
   OperationID: CreateSerialNumberRange
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CreateSerialNumberRange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CreateSerialNumberRange_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CreateSerialNumberRange(requestBody:CreateSerialNumberRange_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CreateSerialNumberRange_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/CreateSerialNumberRange", {
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
         resolve(data as CreateSerialNumberRange_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNextSerialNumber
   Description: Gets the next serial number based on the format for the part number passed in.  The source
data for this method is the SerialNumberSelection dataset.
   OperationID: GetNextSerialNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNextSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNextSerialNumber(requestBody:GetNextSerialNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNextSerialNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/GetNextSerialNumber", {
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
         resolve(data as GetNextSerialNumber_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SelectSerialNumbers
   Description: Select/unselect all serial numbers in the SerialNumberSelection dataset.  When parameter select = true all
rows will be marked as selected; When parameter select = false all rows will be unselected.
   OperationID: SelectSerialNumbers
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SelectSerialNumbers_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SelectSerialNumbers_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SelectSerialNumbers(requestBody:SelectSerialNumbers_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SelectSerialNumbers_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/SelectSerialNumbers", {
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
         resolve(data as SelectSerialNumbers_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCreateSNStartAtQty
   OperationID: ValidateCreateSNStartAtQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateCreateSNStartAtQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCreateSNStartAtQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCreateSNStartAtQty(requestBody:ValidateCreateSNStartAtQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateCreateSNStartAtQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/ValidateCreateSNStartAtQty", {
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
         resolve(data as ValidateCreateSNStartAtQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateCreateSerialNumber
   OperationID: ValidateCreateSerialNumber
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateCreateSerialNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateCreateSerialNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateCreateSerialNumber(requestBody:ValidateCreateSerialNumber_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateCreateSerialNumber_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.SelectedSerialNumbersSvc/ValidateCreateSerialNumber", {
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
         resolve(data as ValidateCreateSerialNumber_output)
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
      @param ds
      @param PartNum
      @param xrefPartNum
      @param xrefPartType
      @param xrefCustNum
      @param SerialNum
      @param SourceRowID
      @param TransType
      @param plantID
   */  
export interface AddSerialNum_input{
   ds:Erp_Tablesets_SelectedSerialNumbersTableset[],
      /**  Part number for the serial number.  */  
   PartNum:string,
      /**  XRef Part Number.  */  
   xrefPartNum:string,
      /**  XRef Part Type (C=Customer/I=Internal Xref).  */  
   xrefPartType:string,
      /**  XRef Customer Number.  */  
   xrefCustNum:number,
      /**  Serial Number to be added.  */  
   SerialNum:string,
      /**  RowID from the source transaction record.  */  
   SourceRowID:string,
      /**  Transaction Type from the source transaction record.  */  
   TransType:string,
      /**  Plant associated with the transaction.  */  
   plantID:string,
}

export interface AddSerialNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SelectedSerialNumbersTableset,
}
}

   /** Required : 
      @param ds
      @param PartNum
      @param xrefPartNum
      @param xrefPartType
      @param xrefCustNum
      @param NumToAdd
      @param baseBeginNum
      @param SourceRowID
      @param TransType
      @param plantID
   */  
export interface CreateSerialNumRange_input{
   ds:Erp_Tablesets_SelectedSerialNumbersTableset[],
      /**  Part number for the serial number.  */  
   PartNum:string,
      /**  XRef Part Number.  */  
   xrefPartNum:string,
      /**  XRef Part Type (C=Customer/I=Internal Xref).  */  
   xrefPartType:string,
      /**  XRef Customer Number.  */  
   xrefCustNum:number,
      /**  Number of serial numbers to create.  */  
   NumToAdd:number,
      /**  The beginning base serial number.  */  
   baseBeginNum:string,
      /**  RowID from the source transaction record.  */  
   SourceRowID:string,
      /**  Transaction Type from the source transaction record.  */  
   TransType:string,
      /**  Plant associated with the transaction.  */  
   plantID:string,
}

export interface CreateSerialNumRange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SelectedSerialNumbersTableset,
}
}

   /** Required : 
      @param ds
      @param PartNum
      @param xrefPartNum
      @param xrefPartType
      @param xrefCustNum
      @param baseSerialNum
      @param SourceRowID
      @param transType
      @param plantID
      @param fullSerialNum
   */  
export interface CreateSerialNum_input{
   ds:Erp_Tablesets_SelectedSerialNumbersTableset[],
      /**  Part number for the serial number.  */  
   PartNum:string,
      /**  XRef Part Number.  */  
   xrefPartNum:string,
      /**  XRef Part Type (C=Customer/I=Internal Xref).  */  
   xrefPartType:string,
      /**  XRef Customer Number.  */  
   xrefCustNum:number,
      /**  Serial Number to be used as the base serial number.  */  
   baseSerialNum:string,
      /**  RowID from the source transaction record.  */  
   SourceRowID:string,
      /**  Transaction Type from the source transaction record.  */  
   transType:string,
      /**  Plant associated with the transaction.  */  
   plantID:string,
      /**  Full Serial Number including prefixs, suffix, subs, etc - used with generate masks  */  
   fullSerialNum:string,
}

export interface CreateSerialNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SelectedSerialNumbersTableset,
}
}

   /** Required : 
      @param ds
      @param PartNum
      @param attributeSetID
      @param xrefPartNum
      @param xrefPartType
      @param xrefCustNum
      @param NumToAdd
      @param baseBeginNum
      @param SourceRowID
      @param TransType
      @param plantID
   */  
export interface CreateSerialNumberRange_input{
   ds:Erp_Tablesets_SerialNumberSelectionTableset[],
      /**  Part number for the serial number.  */  
   PartNum:string,
      /**  ID of Attribute Set.  */  
   attributeSetID:number,
      /**  XRef Part Number.  */  
   xrefPartNum:string,
      /**  XRef Part Type (C=Customer/I=Internal Xref).  */  
   xrefPartType:string,
      /**  XRef Customer Number.  */  
   xrefCustNum:number,
      /**  Number of serial numbers to create.  */  
   NumToAdd:number,
      /**  The beginning base serial number.  */  
   baseBeginNum:string,
      /**  RowID from the source transaction record.  */  
   SourceRowID:string,
      /**  Transaction Type from the source transaction record.  */  
   TransType:string,
      /**  Plant associated with the transaction.  */  
   plantID:string,
}

export interface CreateSerialNumberRange_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNumberSelectionTableset,
   nextBaseSN:string,
   snPrefix:string,
   nextFullSN:string,
   snCounterMax:boolean,
   snFormat:string,
}
}

   /** Required : 
      @param ds
      @param PartNum
      @param attributeSetID
      @param xrefPartNum
      @param xrefPartType
      @param xrefCustNum
      @param baseSerialNum
      @param SourceRowID
      @param transType
      @param plantID
      @param fullSerialNum
   */  
export interface CreateSingleSerialNumber_input{
   ds:Erp_Tablesets_SerialNumberSelectionTableset[],
      /**  Part number for the serial number.  */  
   PartNum:string,
      /**  ID of Attribute Set.  */  
   attributeSetID:number,
      /**  XRef Part Number.  */  
   xrefPartNum:string,
      /**  XRef Part Type (C=Customer/I=Internal Xref).  */  
   xrefPartType:string,
      /**  XRef Customer Number.  */  
   xrefCustNum:number,
      /**  Serial Number to be used as the base serial number.  */  
   baseSerialNum:string,
      /**  RowID from the source transaction record.  */  
   SourceRowID:string,
      /**  Transaction Type from the source transaction record.  */  
   transType:string,
      /**  Plant associated with the transaction.  */  
   plantID:string,
      /**  Full Serial Number including prefixs, suffix, subs, etc - used with generate masks  */  
   fullSerialNum:string,
}

export interface CreateSingleSerialNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNumberSelectionTableset,
}
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

export interface Erp_Tablesets_SelectedSerialNumbersTableset{
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_SerialNumberSelectionRow{
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

export interface Erp_Tablesets_SerialNumberSelectionTableset{
   SerialNumberSelection:Erp_Tablesets_SerialNumberSelectionRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param ds
      @param snPartNum
      @param xrefPartNum
      @param xrefPartType
      @param xrefCustNum
      @param plantID
   */  
export interface GetNextSN_input{
   ds:Erp_Tablesets_SelectedSerialNumbersTableset[],
      /**  Part number to create serial numbers for.  */  
   snPartNum:string,
      /**  XRef Part Number.  */  
   xrefPartNum:string,
      /**  XRef Part Type (C=Customer/I=Internal Xref).  */  
   xrefPartType:string,
      /**  XRef Customer Number.  */  
   xrefCustNum:number,
      /**  Plant associated with the transaction.  */  
   plantID:string,
}

export interface GetNextSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SelectedSerialNumbersTableset,
   nextBaseSN:string,
   snPrefix:string,
   nextFullSN:string,
   snCounterMax:boolean,
}
}

   /** Required : 
      @param ds
      @param snPartNum
      @param xrefPartNum
      @param xrefPartType
      @param xrefCustNum
      @param plantID
   */  
export interface GetNextSerialNumber_input{
   ds:Erp_Tablesets_SerialNumberSelectionTableset[],
      /**  Part number to create serial numbers for.  */  
   snPartNum:string,
      /**  XRef Part Number.  */  
   xrefPartNum:string,
      /**  XRef Part Type (C=Customer/I=Internal Xref).  */  
   xrefPartType:string,
      /**  XRef Customer Number.  */  
   xrefCustNum:number,
      /**  Plant associated with the transaction.  */  
   plantID:string,
}

export interface GetNextSerialNumber_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNumberSelectionTableset,
   nextBaseSN:string,
   snPrefix:string,
   nextFullSN:string,
   snCounterMax:boolean,
   snFormat:string,
}
}

   /** Required : 
      @param ds
      @param partNum
      @param xrefPartNum
      @param xrefPartType
      @param xrefCustNum
      @param plantID
   */  
export interface GetSerialNumFormat_input{
   ds:Erp_Tablesets_SelectedSerialNumbersTableset[],
      /**  Part number to create serial numbers for.  */  
   partNum:string,
      /**  XRef Part Number.  */  
   xrefPartNum:string,
      /**  XRef Part Type (C=Customer/I=Internal Xref).  */  
   xrefPartType:string,
      /**  XRef Customer Number.  */  
   xrefCustNum:number,
      /**  Plant associated with the transaction.  */  
   plantID:string,
}

export interface GetSerialNumFormat_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SelectedSerialNumbersTableset,
}
}

   /** Required : 
      @param ds
      @param ipPartNum
      @param ipXrefPartNum
      @param ipXrefPartType
      @param ipXrefCustNum
      @param ipBaseSerialNum
      @param ipSourceRowID
      @param ipTransType
      @param ipPlantID
      @param ipFullSerialNum
   */  
export interface HHScanCheckSN_input{
   ds:Erp_Tablesets_SelectedSerialNumbersTableset[],
      /**  Part number for the serial number.  */  
   ipPartNum:string,
      /**  XRef Part Number.  */  
   ipXrefPartNum:string,
      /**  XRef Part Type (C=Customer/I=Internal Xref).  */  
   ipXrefPartType:string,
      /**  XRef Customer Number.  */  
   ipXrefCustNum:number,
      /**  Serial Number to be used as the base serial number.  */  
   ipBaseSerialNum:string,
      /**  RowID from the source transaction record.  */  
   ipSourceRowID:string,
      /**  Transaction Type from the source transaction record.  */  
   ipTransType:string,
      /**  Plant associated with the transaction.  */  
   ipPlantID:string,
      /**  Full Serial Number including prefixs, suffix, subs, etc - used with generate masks  */  
   ipFullSerialNum:string,
}

export interface HHScanCheckSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SelectedSerialNumbersTableset,
   opSNIsDeselected:boolean,
   opExists:boolean,
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
      @param partNum
      @param xrefPartNum
      @param xrefPartType
      @param xrefCustNum
      @param plantID
   */  
export interface KineticGetSerialNumFormat_input{
      /**  Part number to create serial numbers for.  */  
   partNum:string,
      /**  XRef Part Number.  */  
   xrefPartNum:string,
      /**  XRef Part Type (C=Customer/I=Internal Xref).  */  
   xrefPartType:string,
      /**  XRef Customer Number.  */  
   xrefCustNum:number,
      /**  Plant associated with the transaction.  */  
   plantID:string,
}

export interface KineticGetSerialNumFormat_output{
   returnObj:Erp_Tablesets_SelectedSerialNumbersTableset[],
parameters : {
      /**  output parameters  */  
   nextBaseSN:string,
   snPrefix:string,
   nextFullSN:string,
   snCounterMax:boolean,
}
}

   /** Required : 
      @param ds
      @param ds1
   */  
export interface ProcessSelectedSerialNumbers_input{
   ds:Erp_Tablesets_SerialNumberSelectionTableset[],
   ds1:Erp_Tablesets_SelectedSerialNumbersTableset[],
}

export interface ProcessSelectedSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNumberSelectionTableset,
   ds1:Erp_Tablesets_SelectedSerialNumbersTableset,
}
}

   /** Required : 
      @param whereClause
      @param startSerialNumber
      @param endSerialNumber
      @param forSelected
      @param sourceRowID
      @param transType
      @param ds
   */  
export interface RetrieveSerialNumbers_input{
      /**  The where clause  */  
   whereClause:string,
      /**  Starting serial number  */  
   startSerialNumber:string,
      /**  Ending serial number  */  
   endSerialNumber:string,
      /**  Mark retrieved as selected  */  
   forSelected:boolean,
      /**  Source rowid  */  
   sourceRowID:string,
      /**  Transaction type  */  
   transType:string,
   ds:Erp_Tablesets_SerialNumberSelectionTableset[],
}

export interface RetrieveSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_SerialNumberSelectionTableset,
}
}

   /** Required : 
      @param selected
      @param requiredQuantity
      @param selectedQuantity
      @param ds
   */  
export interface SelectSerialNumbers_input{
   selected:boolean,
   requiredQuantity:number,
   selectedQuantity:number,
   ds:Erp_Tablesets_SerialNumberSelectionTableset[],
}

export interface SelectSerialNumbers_output{
parameters : {
      /**  output parameters  */  
   deselectMessage:string,
   ds:Erp_Tablesets_SerialNumberSelectionTableset,
}
}

   /** Required : 
      @param startAtQty
      @param serialNumber
      @param nextFullSN
      @param nextBaseSN
      @param ds
   */  
export interface ValidateCreateSNStartAtQty_input{
   startAtQty:string,
   serialNumber:string,
   nextFullSN:string,
   nextBaseSN:string,
   ds:Erp_Tablesets_SelectedSerialNumbersTableset[],
}

export interface ValidateCreateSNStartAtQty_output{
parameters : {
      /**  output parameters  */  
   startAtQty:string,
   ds:Erp_Tablesets_SelectedSerialNumbersTableset,
}
}

   /** Required : 
      @param serialNumber
      @param nextFullSN
      @param nextBaseSN
      @param ds
   */  
export interface ValidateCreateSerialNumber_input{
   serialNumber:string,
   nextFullSN:string,
   nextBaseSN:string,
   ds:Erp_Tablesets_SelectedSerialNumbersTableset[],
}

export interface ValidateCreateSerialNumber_output{
parameters : {
      /**  output parameters  */  
   serialNumber:string,
   ds:Erp_Tablesets_SelectedSerialNumbersTableset,
}
}

