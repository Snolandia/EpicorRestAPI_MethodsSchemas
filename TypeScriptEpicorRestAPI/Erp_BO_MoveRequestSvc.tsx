import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.MoveRequestSvc
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/$metadata", {
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
   Summary: Invoke method CheckEmployee
   Description: This method needs to be called from the main menu only.  if the object
is being called from the shop floor menu then the employee id has already been determined
and validated and is passed in
   OperationID: CheckEmployee
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckEmployee_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckEmployee_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckEmployee(requestBody:CheckEmployee_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckEmployee_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/CheckEmployee", {
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
         resolve(data as CheckEmployee_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewMoveRequest
   Description: Call this method to create a new Epicor.Mfg.BO.MoveRequestDataSet with the RequestType
   OperationID: GetNewMoveRequest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewMoveRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewMoveRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewMoveRequest(requestBody:GetNewMoveRequest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewMoveRequest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/GetNewMoveRequest", {
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
         resolve(data as GetNewMoveRequest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeAssembly
   Description: Call this method when the AssemblySeq field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeAssembly
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeAssembly_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeAssembly_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeAssembly(requestBody:OnChangeAssembly_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeAssembly_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangeAssembly", {
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
         resolve(data as OnChangeAssembly_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFromBin
   Description: Call this method when the FromBin field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeFromBin
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFromBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromBin(requestBody:OnChangeFromBin_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFromBin_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangeFromBin", {
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
         resolve(data as OnChangeFromBin_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFromWhse
   Description: Call this method when the FromWhse field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeFromWhse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFromWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromWhse(requestBody:OnChangeFromWhse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFromWhse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangeFromWhse", {
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
         resolve(data as OnChangeFromWhse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeJobNum
   Description: Call this method when the JobNum field changes
RowMod must be "A" or "U" for this method to work
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangeJobNum", {
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
   Summary: Invoke method OnChangeLot
   Description: Call this method when the lotNum field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeLot
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLot(requestBody:OnChangeLot_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLot_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangeLot", {
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
         resolve(data as OnChangeLot_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeMtlSeq
   Description: Call this method when the MtlSeq field changes
if RequestType = "MW":U then MtlSeq is actually the JobOper.OprSeq
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeMtlSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeMtlSeq(requestBody:OnChangeMtlSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeMtlSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangeMtlSeq", {
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
         resolve(data as OnChangeMtlSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePartNum
   Description: Call this method when the PartNum field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangePartNum(requestBody:OnChangePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangePartNum", {
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
         resolve(data as OnChangePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeFromPCID
   Description: Validates that PCID exists
   OperationID: OnChangeFromPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeFromPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFromPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeFromPCID(requestBody:OnChangeFromPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeFromPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangeFromPCID", {
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
         resolve(data as OnChangeFromPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeToPCID
   Description: Validates that PCID exists
   OperationID: OnChangeToPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeToPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeToPCID(requestBody:OnChangeToPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeToPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangeToPCID", {
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
         resolve(data as OnChangeToPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetWarehouses
   Description: Returns a list of warehouses
   OperationID: GetWarehouses
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetWarehouses_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetWarehouses(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetWarehouses_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/GetWarehouses", {
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
         resolve(data as GetWarehouses_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartWarehouses
   Description: Returns a list of warehouses that are valid for a part
   OperationID: GetPartWarehouses
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartWarehouses_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartWarehouses_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartWarehouses(requestBody:GetPartWarehouses_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartWarehouses_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/GetPartWarehouses", {
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
         resolve(data as GetPartWarehouses_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeReqDirection
   Description: Call this method when the ReqDirection field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeReqDirection
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeReqDirection_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeReqDirection_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeReqDirection(requestBody:OnChangeReqDirection_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeReqDirection_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangeReqDirection", {
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
         resolve(data as OnChangeReqDirection_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeToBin
   Description: Call this method when the ToBin field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeToBin
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeToBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeToBin(requestBody:OnChangeToBin_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeToBin_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangeToBin", {
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
         resolve(data as OnChangeToBin_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeToWhse
   Description: Call this method when the ToWhse field changes
RowMod must be "A" or "U" for this method to work
   OperationID: OnChangeToWhse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeToWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeToWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeToWhse(requestBody:OnChangeToWhse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeToWhse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangeToWhse", {
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
         resolve(data as OnChangeToWhse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new request qty
   OperationID: OnChangingNumberOfPieces
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingNumberOfPieces(requestBody:OnChangingNumberOfPieces_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingNumberOfPieces_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangingNumberOfPieces", {
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
         resolve(data as OnChangingNumberOfPieces_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingRevisionNum
   Description: Call this method when the Revision changes to maintain inventory tracking
   OperationID: OnChangingRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingRevisionNum(requestBody:OnChangingRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangingRevisionNum", {
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
         resolve(data as OnChangingRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeRequestQty
   Description: Call this method when the value of Epicor.Mfg.BO.MoveRequestDataSet.RequestQty changes.
   OperationID: OnChangeRequestQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeRequestQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeRequestQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeRequestQty(requestBody:OnChangeRequestQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeRequestQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangeRequestQty", {
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
         resolve(data as OnChangeRequestQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeUOM
   Description: Call this method when the value of Epicor.Mfg.BO.MoveRequestDataSet.UOM changes.
   OperationID: OnChangeUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeUOM(requestBody:OnChangeUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangeUOM", {
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
         resolve(data as OnChangeUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAttributeSet
   Description: Call this method when the attribute set changes
   OperationID: OnChangingAttributeSet
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingAttributeSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAttributeSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAttributeSet(requestBody:OnChangingAttributeSet_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingAttributeSet_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/OnChangingAttributeSet", {
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
         resolve(data as OnChangingAttributeSet_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessRequest
   Description: Must set the MoveRequest RowMod to "U" or "A" for this method to work
The method updates the Mtl Queue record when the user is done inputing data
   OperationID: ProcessRequest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessRequest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessRequest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessRequest(requestBody:ProcessRequest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessRequest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/ProcessRequest", {
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
         resolve(data as ProcessRequest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeDetailPartNum
   OperationID: ChangeDetailPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeDetailPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDetailPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeDetailPartNum(requestBody:ChangeDetailPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeDetailPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/ChangeDetailPartNum", {
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
         resolve(data as ChangeDetailPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method VerifyEmpID
   Description: Verify Employee ID and return name if valid.
   OperationID: VerifyEmpID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/VerifyEmpID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VerifyEmpID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_VerifyEmpID(requestBody:VerifyEmpID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<VerifyEmpID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.MoveRequestSvc/VerifyEmpID", {
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
         resolve(data as VerifyEmpID_output)
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
      @param NewPartNum
      @param SysRowID
      @param rowType
      @param ds
   */  
export interface ChangeDetailPartNum_input{
   NewPartNum:string,
   SysRowID:string,
   rowType:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface ChangeDetailPartNum_output{
parameters : {
      /**  output parameters  */  
   NewPartNum:string,
   multipleMatch:boolean,
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param empID
   */  
export interface CheckEmployee_input{
      /**  Employee ID  */  
   empID:string,
}

export interface CheckEmployee_output{
parameters : {
      /**  output parameters  */  
   empName:string,
}
}

export interface Erp_Tablesets_MoveRequestRow{
   RequestType:string,
   ReqDirection:string,
   RequestQty:number,
   JobNum:string,
   JobPartNum:string,
   JobPartDesc:string,
   AssemblySeq:number,
   AsmPartNum:string,
   AsmPartDesc:string,
   MtlSeq:number,
   MtlPartNum:string,
   MtlPartDesc:string,
   PartNum:string,
   PartDesc:string,
   LotNumber:string,
   FromWhse:string,
   FromWhseDesc:string,
   FromBin:string,
   FromBinDesc:string,
   ToWhse:string,
   ToWhseDesc:string,
   ToBin:string,
   ToBinDesc:string,
   DummyKeyField:string,
   EmpId:string,
   EmpName:string,
      /**  If yes, ToBin should be enabled, otherwise diable tobin  */  
   ToMultiBin:boolean,
      /**  if true then enable FromBin otherwise disable from bin  */  
   FromMultiBin:boolean,
   TrackLot:boolean,
   LotDesc:string,
      /**  Unit of measure for the Part (JobPartNum) being moved  */  
   UOM:string,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Used by EpicorFSA. Set to true to delete related MtlQueue.  */  
   FSADelete:boolean,
      /**  The optional NeedByDate the generated MtlQueue should use.  */  
   NeedByDate:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AsmAttributeSetID:number,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   MtlAttributeSetID:number,
      /**  The Full Description of the Material Attribute Set.  */  
   MtlAttributeSetDescription:string,
      /**  The Short Description of the Material Attribute Set.  */  
   MtlAttributeSetShortDescription:string,
   AttrClassID:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   EnableAttributeSetSearch:boolean,
      /**  The Full Description of the Inventory Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Inventory Attribute Set.  */  
   AttributeSetShortDescription:string,
   Plant:string,
   ToPCID:string,
   FromPCID:string,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   RevisionNum:string,
      /**  Indicates if inventory for this part is tracked by revision number.  */  
   TrackInventoryByRevision:boolean,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   MtlRevisionNum:string,
   PlantConfCtrlEnablePackageControl:boolean,
      /**  Optional field that contains the customers revision. Default from the PartRev.RevisionNum field.  */  
   AsmRevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_MoveRequestTableset{
   MoveRequest:Erp_Tablesets_MoveRequestRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param requestType
      @param ds
   */  
export interface GetNewMoveRequest_input{
      /**  Request Type  */  
   requestType:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface GetNewMoveRequest_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param partNum
   */  
export interface GetPartWarehouses_input{
   partNum:string,
}

export interface GetPartWarehouses_output{
   returnObj:string,
}

export interface GetWarehouses_output{
   returnObj:string,
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
      @param asmSeq
      @param ds
   */  
export interface OnChangeAssembly_input{
      /**  Assembly Sequence  */  
   asmSeq:number,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangeAssembly_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param fromBin
      @param ds
   */  
export interface OnChangeFromBin_input{
      /**  From Bin Number  */  
   fromBin:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangeFromBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param pcid
      @param pCallProcess
      @param ds
   */  
export interface OnChangeFromPCID_input{
   pcid:string,
   pCallProcess:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangeFromPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
   warehousesList:string,
}
}

   /** Required : 
      @param fromWhse
      @param ds
   */  
export interface OnChangeFromWhse_input{
      /**  From Warehouse  */  
   fromWhse:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangeFromWhse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param jobNum
      @param ds
   */  
export interface OnChangeJobNum_input{
      /**  Job Number  */  
   jobNum:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param lotNum
      @param ds
   */  
export interface OnChangeLot_input{
      /**  Lot Number  */  
   lotNum:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangeLot_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param mtlSeq
      @param ds
   */  
export interface OnChangeMtlSeq_input{
      /**  Material Sequence  */  
   mtlSeq:number,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangeMtlSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param partNum
      @param ds
   */  
export interface OnChangePartNum_input{
      /**  Part Number  */  
   partNum:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
   warehousesList:string,
}
}

   /** Required : 
      @param reqDirection
      @param ds
   */  
export interface OnChangeReqDirection_input{
      /**  Request Direction  */  
   reqDirection:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangeReqDirection_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param pdRequestQty
      @param ds
   */  
export interface OnChangeRequestQty_input{
      /**  Request Qty  */  
   pdRequestQty:number,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangeRequestQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param toBin
      @param ds
   */  
export interface OnChangeToBin_input{
      /**  To Bin Number  */  
   toBin:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangeToBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param pcid
      @param pCallProcess
      @param ds
   */  
export interface OnChangeToPCID_input{
   pcid:string,
   pCallProcess:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangeToPCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
   warehousesList:string,
}
}

   /** Required : 
      @param toWhse
      @param ds
   */  
export interface OnChangeToWhse_input{
      /**  To Warehouse  */  
   toWhse:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangeToWhse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param pUOM
      @param ds
   */  
export interface OnChangeUOM_input{
      /**  UOM  */  
   pUOM:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangeUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
      /**  attributeSetID  */  
   attributeSetID:number,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ProcessRequest_input{
   ds:Erp_Tablesets_MoveRequestTableset[],
}

export interface ProcessRequest_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_MoveRequestTableset,
}
}

   /** Required : 
      @param empID
   */  
export interface VerifyEmpID_input{
   empID:string,
}

export interface VerifyEmpID_output{
parameters : {
      /**  output parameters  */  
   empName:string,
}
}

