import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.UnpickTransactionSvc
// Description: BO for Unpick screens
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/$metadata", {
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
   Summary: Invoke method Init
   Description: Init
   OperationID: Init
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Init_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Init(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Init_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/Init", {
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
         resolve(data as Init_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFromBin
   Description: Validate the bin and populate description
   OperationID: ChangeFromBin
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFromBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFromBin(requestBody:ChangeFromBin_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFromBin_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeFromBin", {
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
         resolve(data as ChangeFromBin_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFromWhse
   Description: Validate the warehouse and populate description
   OperationID: ChangeFromWhse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFromWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFromWhse(requestBody:ChangeFromWhse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFromWhse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeFromWhse", {
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
         resolve(data as ChangeFromWhse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeJobAsm
   Description: Validate the job assembly
   OperationID: ChangeJobAsm
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeJobAsm_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobAsm_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJobAsm(requestBody:ChangeJobAsm_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeJobAsm_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeJobAsm", {
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
         resolve(data as ChangeJobAsm_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeJobMtlSeq
   Description: Validate the job mtl seqr and populate mtl data
   OperationID: ChangeJobMtlSeq
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeJobMtlSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobMtlSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJobMtlSeq(requestBody:ChangeJobMtlSeq_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeJobMtlSeq_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeJobMtlSeq", {
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
         resolve(data as ChangeJobMtlSeq_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeJobNum
   Description: Validate the job number
   OperationID: ChangeJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeJobNum(requestBody:ChangeJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeJobNum", {
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
         resolve(data as ChangeJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeLotNum
   Description: Validate the part and set the description
   OperationID: ChangeLotNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLotNum(requestBody:ChangeLotNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeLotNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeLotNum", {
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
         resolve(data as ChangeLotNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOrderLine
   Description: Validate the order line
   OperationID: ChangeOrderLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOrderLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOrderLine(requestBody:ChangeOrderLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOrderLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeOrderLine", {
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
         resolve(data as ChangeOrderLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOrderNum
   Description: Validate the order number
   OperationID: ChangeOrderNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOrderNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOrderNum(requestBody:ChangeOrderNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOrderNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeOrderNum", {
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
         resolve(data as ChangeOrderNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeOrderRelNum
   Description: Validate the order release number and populate release data
   OperationID: ChangeOrderRelNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeOrderRelNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeOrderRelNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeOrderRelNum(requestBody:ChangeOrderRelNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeOrderRelNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeOrderRelNum", {
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
         resolve(data as ChangeOrderRelNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePartNum
   Description: Validate the part and set the description
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangePartNum", {
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
   Summary: Invoke method ChangeAttributeSetID
   Description: Validate the attribute set and set the description
   OperationID: ChangeAttributeSetID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAttributeSetID(requestBody:ChangeAttributeSetID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeAttributeSetID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeAttributeSetID", {
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
         resolve(data as ChangeAttributeSetID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRevisionNum
   Description: Validate revision num
   OperationID: ChangeRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRevisionNum(requestBody:ChangeRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeRevisionNum", {
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
         resolve(data as ChangeRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeSupplyJobNum
   Description: Validate the supply job number
   OperationID: ChangeSupplyJobNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeSupplyJobNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSupplyJobNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeSupplyJobNum(requestBody:ChangeSupplyJobNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeSupplyJobNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeSupplyJobNum", {
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
         resolve(data as ChangeSupplyJobNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeUnpickQty
   Description: Call this method when the UnpickQty changes
   OperationID: ChangeUnpickQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeUnpickQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnpickQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUnpickQty(requestBody:ChangeUnpickQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeUnpickQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeUnpickQty", {
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
         resolve(data as ChangeUnpickQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeUnpickUOM
   Description: Call this method when the unpickQtyUOM changes
   OperationID: ChangeUnpickUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeUnpickUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUnpickUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUnpickUOM(requestBody:ChangeUnpickUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeUnpickUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeUnpickUOM", {
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
         resolve(data as ChangeUnpickUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
   OperationID: ChangeNumberOfPieces
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeNumberOfPieces_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeNumberOfPieces_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeNumberOfPieces(requestBody:ChangeNumberOfPieces_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeNumberOfPieces_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeNumberOfPieces", {
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
         resolve(data as ChangeNumberOfPieces_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePCID
   Description: Validate the PCID
   OperationID: ChangePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePCID(requestBody:ChangePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangePCID", {
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
         resolve(data as ChangePCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFOrdLine
   Description: Validate the transfer order line number and populate line data
   OperationID: ChangeTFOrdLine
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFOrdLine(requestBody:ChangeTFOrdLine_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTFOrdLine_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeTFOrdLine", {
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
         resolve(data as ChangeTFOrdLine_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTFOrdNum
   Description: Validate the transfer order number
   OperationID: ChangeTFOrdNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTFOrdNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTFOrdNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTFOrdNum(requestBody:ChangeTFOrdNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTFOrdNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeTFOrdNum", {
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
         resolve(data as ChangeTFOrdNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeToBin
   Description: Validate the bin and populate description
   OperationID: ChangeToBin
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeToBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeToBin(requestBody:ChangeToBin_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeToBin_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeToBin", {
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
         resolve(data as ChangeToBin_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeToWhse
   Description: Validate the whse and populate description
   OperationID: ChangeToWhse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeToWhse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToWhse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeToWhse(requestBody:ChangeToWhse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeToWhse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/ChangeToWhse", {
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
         resolve(data as ChangeToWhse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewUnpickTransaction
   Description: Gets a new ttUnpickTransaction record
   OperationID: GetNewUnpickTransaction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewUnpickTransaction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewUnpickTransaction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewUnpickTransaction(requestBody:GetNewUnpickTransaction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewUnpickTransaction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/GetNewUnpickTransaction", {
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
         resolve(data as GetNewUnpickTransaction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreUnpickTransaction
   Description: PreUnpickTransaction - Validates unpick before any changes happen
   OperationID: PreUnpickTransaction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreUnpickTransaction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreUnpickTransaction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreUnpickTransaction(requestBody:PreUnpickTransaction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreUnpickTransaction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/PreUnpickTransaction", {
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
         resolve(data as PreUnpickTransaction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method _UnpickTransaction
   Description: Unpicks a transaction
1) Validates Unpick
2) Updates PartAlloc for Transfer Orders
3) Updates Picked Orders for Sales Orders
   OperationID: _UnpickTransaction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/_UnpickTransaction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/_UnpickTransaction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UnpickTransaction(requestBody:_UnpickTransaction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<_UnpickTransaction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/_UnpickTransaction", {
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
         resolve(data as _UnpickTransaction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailTranDocTypes
   Description: Method to call to get available tran doc types.
   OperationID: GetAvailTranDocTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAvailTranDocTypes_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTranDocTypes(requestBody:GetAvailTranDocTypes_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailTranDocTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/GetAvailTranDocTypes", {
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
         resolve(data as GetAvailTranDocTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method HandheldPCID
   Description: Validate that the current Transfer Order/Line is not attached to a PCID
   OperationID: HandheldPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/HandheldPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/HandheldPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_HandheldPCID(requestBody:HandheldPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<HandheldPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.UnpickTransactionSvc/HandheldPCID", {
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
         resolve(data as HandheldPCID_output)
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
      @param ipProposedValue
      @param ds
   */  
export interface ChangeAttributeSetID_input{
      /**  Proposed Value  */  
   ipProposedValue:number,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeAttributeSetID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeFromBin_input{
      /**  Proposed Value  */  
   ipProposedValue:string,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeFromBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeFromWhse_input{
      /**  Proposed Value  */  
   ipProposedValue:string,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeFromWhse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeJobAsm_input{
      /**  Proposed Value  */  
   ipProposedValue:number,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeJobAsm_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeJobMtlSeq_input{
      /**  Proposed Value  */  
   ipProposedValue:number,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeJobMtlSeq_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeJobNum_input{
      /**  Proposed Value  */  
   ipProposedValue:string,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeLotNum_input{
      /**  Proposed Value  */  
   ipProposedValue:string,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param dispNumberOfPieces
      @param ds
   */  
export interface ChangeNumberOfPieces_input{
   dispNumberOfPieces:number,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeOrderLine_input{
      /**  Proposed Value  */  
   ipProposedValue:number,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeOrderLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeOrderNum_input{
      /**  Proposed Value  */  
   ipProposedValue:number,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeOrderNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeOrderRelNum_input{
      /**  Proposed Value  */  
   ipProposedValue:number,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeOrderRelNum_output{
parameters : {
      /**  output parameters  */  
   opMessage:string,
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipPCID
      @param ds
   */  
export interface ChangePCID_input{
      /**  Proposed PCID value  */  
   ipPCID:string,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangePCID_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangePartNum_input{
      /**  Proposed Value  */  
   ipProposedValue:string,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangePartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface ChangeRevisionNum_input{
      /**  Proposed Value  */  
   revisionNum:string,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeSupplyJobNum_input{
      /**  Proposed Value  */  
   ipProposedValue:string,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeSupplyJobNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeTFOrdLine_input{
      /**  Proposed Value  */  
   ipProposedValue:number,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeTFOrdLine_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeTFOrdNum_input{
      /**  Proposed Value  */  
   ipProposedValue:string,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeTFOrdNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeToBin_input{
      /**  Proposed Value  */  
   ipProposedValue:string,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeToBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param ipProposedValue
      @param ds
   */  
export interface ChangeToWhse_input{
      /**  Proposed Value  */  
   ipProposedValue:string,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeToWhse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param unpickQty
      @param ds
   */  
export interface ChangeUnpickQty_input{
   unpickQty:number,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeUnpickQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param unpickUOM
      @param ds
   */  
export interface ChangeUnpickUOM_input{
   unpickUOM:string,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface ChangeUnpickUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

export interface Erp_Tablesets_UnpickTransactionRow{
   OrderNum:number,
   OrderLine:number,
   OrderRelNum:number,
   JobNum:string,
   AssemblySeq:number,
   MtlSeq:number,
   TFOrdNum:string,
   TFOrdLine:number,
   PartNum:string,
   LotNum:string,
   UnpickQty:number,
   UnpickUOM:string,
   FromWhse:string,
   ToWhse:string,
   FromBin:string,
   ToBin:string,
   AvailQty:number,
   AvailUOM:string,
   FromBinDesc:string,
   ToBinDesc:string,
   FromWhseDesc:string,
   ToWhseDesc:string,
   PartDesc:string,
   LotTracked:boolean,
   SerialTracked:boolean,
      /**  Valid values are "O" for sales order, "J" for job, or "T" for transfer order.  */  
   UnpickType:string,
      /**  PCID to Unpick From  */  
   PCID:string,
   EnablePCID:boolean,
   TranDocTypeID:string,
      /**  Indicates if a PkgControlHeader record was deleted during the Unpick Transaction.  */  
   PkgControlHeaderDeleted:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   PartAttrClassID:string,
   EnableAttributeSetSearch:boolean,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
   PartTrackInventoryByRevision:boolean,
   RevisionNum:string,
   SupplyJobNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_UnpickTransactionTableset{
   UnpickTransaction:Erp_Tablesets_UnpickTransactionRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

   /** Required : 
      @param unpickType
   */  
export interface GetAvailTranDocTypes_input{
      /**  The unpick type of the transaction  */  
   unpickType:string,
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   AvailTypes:string,
}
}

   /** Required : 
      @param ipType
      @param ds
   */  
export interface GetNewUnpickTransaction_input{
      /**  Type (O=Order/J=Job/T=TO)  */  
   ipType:string,
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface GetNewUnpickTransaction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

   /** Required : 
      @param TFOrdNum
      @param TFOrdLine
      @param LotNum
      @param UOM
   */  
export interface HandheldPCID_input{
      /**  Transfer Order Number  */  
   TFOrdNum:string,
      /**  Transfer Order Line  */  
   TFOrdLine:number,
      /**  Part Lot Number  */  
   LotNum:string,
      /**  Available Unit of Measure  */  
   UOM:string,
}

export interface HandheldPCID_output{
   returnObj:boolean,
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

export interface Init_output{
}

   /** Required : 
      @param ds
   */  
export interface PreUnpickTransaction_input{
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface PreUnpickTransaction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
   msg:string,
}
}

   /** Required : 
      @param ds
   */  
export interface _UnpickTransaction_input{
   ds:Erp_Tablesets_UnpickTransactionTableset[],
}

export interface _UnpickTransaction_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_UnpickTransactionTableset,
}
}

