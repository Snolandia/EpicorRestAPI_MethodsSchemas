import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.InvTransferSvc
// Description: Inventory Transfer
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/$metadata", {
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
   Summary: Invoke method ChangeFromBinRowMod
   Description: Kinetic client. This method will pull qty for the bin.
   OperationID: ChangeFromBinRowMod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFromBinRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromBinRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFromBinRowMod(requestBody:ChangeFromBinRowMod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFromBinRowMod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeFromBinRowMod", {
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
         resolve(data as ChangeFromBinRowMod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFromBin
   Description: This method will pull qty for the bin.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeFromBin", {
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
   Summary: Invoke method ChangeFromWhseRowMod
   Description: Kinetic client. This method validate from warehouse.
   OperationID: ChangeFromWhseRowMod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeFromWhseRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeFromWhseRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeFromWhseRowMod(requestBody:ChangeFromWhseRowMod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeFromWhseRowMod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeFromWhseRowMod", {
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
         resolve(data as ChangeFromWhseRowMod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeFromWhse
   Description: This method validate from warehouse.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeFromWhse", {
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
   Summary: Invoke method ChangeLotRowMod
   Description: kinetic client. Recalculates on hand qty when lot number changes.
   OperationID: ChangeLotRowMod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeLotRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLotRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLotRowMod(requestBody:ChangeLotRowMod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeLotRowMod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeLotRowMod", {
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
         resolve(data as ChangeLotRowMod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeLot
   Description: Recalculates on hand qty when lot number changes.
   OperationID: ChangeLot
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeLot(requestBody:ChangeLot_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeLot_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeLot", {
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
         resolve(data as ChangeLot_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeAttributeSetIDRowMod
   Description: Kinetic client. Recalculates on hand qty when attribute set changes.
   OperationID: ChangeAttributeSetIDRowMod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeAttributeSetIDRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeAttributeSetIDRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeAttributeSetIDRowMod(requestBody:ChangeAttributeSetIDRowMod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeAttributeSetIDRowMod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeAttributeSetIDRowMod", {
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
         resolve(data as ChangeAttributeSetIDRowMod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeAttributeSetID
   Description: Recalculates on hand qty when attribute set changes.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeAttributeSetID", {
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
   Summary: Invoke method ChangeToBinRowMod
   Description: Kinetic client. This method will pull qty for the TO bin.
   OperationID: ChangeToBinRowMod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeToBinRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToBinRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeToBinRowMod(requestBody:ChangeToBinRowMod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeToBinRowMod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeToBinRowMod", {
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
         resolve(data as ChangeToBinRowMod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeToBin
   Description: This method will pull qty for the TO bin.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeToBin", {
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
   Summary: Invoke method ChangeToWhseRowMod
   Description: Kinetic client
   OperationID: ChangeToWhseRowMod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeToWhseRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeToWhseRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeToWhseRowMod(requestBody:ChangeToWhseRowMod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeToWhseRowMod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeToWhseRowMod", {
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
         resolve(data as ChangeToWhseRowMod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeToWhse
   Description: This method validate to warehouse.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeToWhse", {
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
   Summary: Invoke method ChangeUOMRowMod
   Description: Kinetic client. Recalculates on hand qty and Num of Pieces when the inventory transfer UOM changes.
   OperationID: ChangeUOMRowMod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeUOMRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUOMRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUOMRowMod(requestBody:ChangeUOMRowMod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeUOMRowMod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeUOMRowMod", {
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
         resolve(data as ChangeUOMRowMod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeUOM
   Description: Recalculates on hand qty when the inventory transfer UOM changes.
   OperationID: ChangeUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUOM(requestBody:ChangeUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeUOM", {
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
         resolve(data as ChangeUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Call this method when the Nbr Of Pieces changes to calculate a new tran qty
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/OnChangingNumberOfPieces", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/OnChangingAttributeSet", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/OnChangingRevisionNum", {
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
   Summary: Invoke method OnChangingTransferQty
   Description: Call this method when the transferQty changes
   OperationID: OnChangingTransferQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingTransferQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTransferQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingTransferQty(requestBody:OnChangingTransferQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingTransferQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/OnChangingTransferQty", {
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
         resolve(data as OnChangingTransferQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingTransferQtyUOM
   Description: Call this method when the transferQtyUOM changes
   OperationID: OnChangingTransferQtyUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingTransferQtyUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingTransferQtyUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingTransferQtyUOM(requestBody:OnChangingTransferQtyUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingTransferQtyUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/OnChangingTransferQtyUOM", {
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
         resolve(data as OnChangingTransferQtyUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CommitTransfer
   Description: This method will commit the inventory transfer .
Serial numbers are passed from the serial number object through the
ttSelectedSerialNumbers temptable.
   OperationID: CommitTransfer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CommitTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CommitTransfer(requestBody:CommitTransfer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CommitTransfer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/CommitTransfer", {
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
         resolve(data as CommitTransfer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailBins
   Description: Based on the parameter AllBins, either all bins or only current bins will be
returned in the Bins Data table.
   OperationID: GetAvailBins
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetAvailBins_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailBins_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailBins(requestBody:GetAvailBins_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailBins_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/GetAvailBins", {
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
         resolve(data as GetAvailBins_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNewInventoryTransfer
   OperationID: GetNewInventoryTransfer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNewInventoryTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewInventoryTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNewInventoryTransfer(requestBody:GetNewInventoryTransfer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNewInventoryTransfer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/GetNewInventoryTransfer", {
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
         resolve(data as GetNewInventoryTransfer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePCID
   Description: Change PCID.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangePCID", {
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
   Summary: Invoke method ChangeTransferPartNum
   OperationID: ChangeTransferPartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTransferPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTransferPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTransferPartNum(requestBody:ChangeTransferPartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTransferPartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeTransferPartNum", {
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
         resolve(data as ChangeTransferPartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTransferQtyRowMod
   Description: Kinetic client. Change Transfer Qty.
   OperationID: ChangeTransferQtyRowMod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTransferQtyRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTransferQtyRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTransferQtyRowMod(requestBody:ChangeTransferQtyRowMod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTransferQtyRowMod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeTransferQtyRowMod", {
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
         resolve(data as ChangeTransferQtyRowMod_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeTransferQty
   Description: Change Transfer Qty.
   OperationID: ChangeTransferQty
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeTransferQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTransferQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeTransferQty(requestBody:ChangeTransferQty_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeTransferQty_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ChangeTransferQty", {
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
         resolve(data as ChangeTransferQty_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartXRefInfo
   Description: This method defaults PartAdvisor fields when the PartNum field changes
   OperationID: GetPartXRefInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartXRefInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartXRefInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartXRefInfo(requestBody:GetPartXRefInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartXRefInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/GetPartXRefInfo", {
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
         resolve(data as GetPartXRefInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPrimaryBin
   Description: Note: This method should be called when either the From or To Warehouse code changes.
Purpose: Get the Part (From or To) Warehouse's Primary Bin when the Warehouse is changed.
   OperationID: GetPrimaryBin
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPrimaryBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPrimaryBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPrimaryBin(requestBody:GetPrimaryBin_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPrimaryBin_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/GetPrimaryBin", {
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
         resolve(data as GetPrimaryBin_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetSelectSerialNumbersParamsRowMod
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: GetSelectSerialNumbersParamsRowMod
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetSelectSerialNumbersParamsRowMod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetSelectSerialNumbersParamsRowMod_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetSelectSerialNumbersParamsRowMod(requestBody:GetSelectSerialNumbersParamsRowMod_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetSelectSerialNumbersParamsRowMod_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/GetSelectSerialNumbersParamsRowMod", {
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
         resolve(data as GetSelectSerialNumbersParamsRowMod_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/GetSelectSerialNumbersParams", {
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
   Summary: Invoke method GetTransferRecord
   Description: This method creates a template transfer record . Gets defaults for the part to
be transfered  .
   OperationID: GetTransferRecord
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetTransferRecord_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTransferRecord_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetTransferRecord(requestBody:GetTransferRecord_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetTransferRecord_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/GetTransferRecord", {
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
         resolve(data as GetTransferRecord_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetNotSelectedInvTransferRecords
   OperationID: GetNotSelectedInvTransferRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetNotSelectedInvTransferRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNotSelectedInvTransferRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetNotSelectedInvTransferRecords(requestBody:GetNotSelectedInvTransferRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetNotSelectedInvTransferRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/GetNotSelectedInvTransferRecords", {
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
         resolve(data as GetNotSelectedInvTransferRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvTransferRecords
   OperationID: GetInvTransferRecords
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInvTransferRecords_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvTransferRecords_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvTransferRecords(requestBody:GetInvTransferRecords_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInvTransferRecords_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/GetInvTransferRecords", {
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
         resolve(data as GetInvTransferRecords_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreCommitTransfer
   Description: This method will return a record in the LegalNumberGenerate datatable if
a legal number is required for this transaction.  The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
   OperationID: PreCommitTransfer
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreCommitTransfer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreCommitTransfer_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreCommitTransfer(requestBody:PreCommitTransfer_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreCommitTransfer_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/PreCommitTransfer", {
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
         resolve(data as PreCommitTransfer_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method AttributeSetSplitPreLoadCheck
   Description: Specific checks related to Attribute Split to validate can load Inventory Attribute Entry form.
   OperationID: AttributeSetSplitPreLoadCheck
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AttributeSetSplitPreLoadCheck_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AttributeSetSplitPreLoadCheck_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AttributeSetSplitPreLoadCheck(requestBody:AttributeSetSplitPreLoadCheck_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AttributeSetSplitPreLoadCheck_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/AttributeSetSplitPreLoadCheck", {
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
         resolve(data as AttributeSetSplitPreLoadCheck_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ValidateSN", {
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

   /**  
   Summary: Invoke method AreSNumsAllocated
   Description: AreSNumsAllocated method.
   OperationID: AreSNumsAllocated
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/AreSNumsAllocated_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AreSNumsAllocated_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_AreSNumsAllocated(requestBody:AreSNumsAllocated_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<AreSNumsAllocated_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/AreSNumsAllocated", {
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
         resolve(data as AreSNumsAllocated_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailTranDocTypes
   Description: GetAvailTranDocTypes method.
   OperationID: GetAvailTranDocTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailTranDocTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailTranDocTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/GetAvailTranDocTypes", {
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
         resolve(data as GetAvailTranDocTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method NegativeInventoryTest
   Description: NegativeInventoryTest method.
   OperationID: NegativeInventoryTest
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/NegativeInventoryTest_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/NegativeInventoryTest_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_NegativeInventoryTest(requestBody:NegativeInventoryTest_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<NegativeInventoryTest_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/NegativeInventoryTest", {
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
         resolve(data as NegativeInventoryTest_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method MasterInventoryBinTests
   Description: Methods to check Negative Inventory and Contract bin.
   OperationID: MasterInventoryBinTests
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/MasterInventoryBinTests_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MasterInventoryBinTests_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_MasterInventoryBinTests(requestBody:MasterInventoryBinTests_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<MasterInventoryBinTests_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/MasterInventoryBinTests", {
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
         resolve(data as MasterInventoryBinTests_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartFromRowID
   Description: GetPartFromRowID method.
   OperationID: GetPartFromRowID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPartFromRowID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPartFromRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPartFromRowID(requestBody:GetPartFromRowID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPartFromRowID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/GetPartFromRowID", {
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
         resolve(data as GetPartFromRowID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvTransferRecordsForPCID
   Description: Get records for a list of PCIDs
   OperationID: GetInvTransferRecordsForPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInvTransferRecordsForPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvTransferRecordsForPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvTransferRecordsForPCID(requestBody:GetInvTransferRecordsForPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInvTransferRecordsForPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/GetInvTransferRecordsForPCID", {
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
         resolve(data as GetInvTransferRecordsForPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CommitTransferAndUpdateHistory
   Description: Used at the MetaFX. This method will commit the inventory transfer .
Serial numbers are passed from the serial number object through the
ttSelectedSerialNumbers temptable.
   OperationID: CommitTransferAndUpdateHistory
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CommitTransferAndUpdateHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CommitTransferAndUpdateHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CommitTransferAndUpdateHistory(requestBody:CommitTransferAndUpdateHistory_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CommitTransferAndUpdateHistory_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/CommitTransferAndUpdateHistory", {
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
         resolve(data as CommitTransferAndUpdateHistory_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method UpdateHistory
   Description: This method will update the InventoryTransfer history using the info in the dataset
   OperationID: UpdateHistory
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/UpdateHistory_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateHistory_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_UpdateHistory(requestBody:UpdateHistory_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<UpdateHistory_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/UpdateHistory", {
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
         resolve(data as UpdateHistory_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInvTransferRecordsForStandardPCIDList
   Description: Used at the MetaFX. Get records for a list of PCIDs delimited by '~'
   OperationID: GetInvTransferRecordsForStandardPCIDList
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInvTransferRecordsForStandardPCIDList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInvTransferRecordsForStandardPCIDList_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInvTransferRecordsForStandardPCIDList(requestBody:GetInvTransferRecordsForStandardPCIDList_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInvTransferRecordsForStandardPCIDList_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/GetInvTransferRecordsForStandardPCIDList", {
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
         resolve(data as GetInvTransferRecordsForStandardPCIDList_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckAdvancedMaterialAndPackageControl
   Description: Check Advanced Material and Package Control availability
   OperationID: CheckAdvancedMaterialAndPackageControl
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckAdvancedMaterialAndPackageControl_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckAdvancedMaterialAndPackageControl(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckAdvancedMaterialAndPackageControl_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/CheckAdvancedMaterialAndPackageControl", {
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
         resolve(data as CheckAdvancedMaterialAndPackageControl_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePartNum
   Description: Used at the MetaFX.Client logic transition
   OperationID: ValidatePartNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePartNum(requestBody:ValidatePartNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePartNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ValidatePartNum", {
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
         resolve(data as ValidatePartNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidatePCID
   Description: Used at the MetaFX.Client logic transition
   OperationID: ValidatePCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePCID(requestBody:ValidatePCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InvTransferSvc/ValidatePCID", {
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
         resolve(data as ValidatePCID_output)
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
      @param ipPartNum
   */  
export interface AreSNumsAllocated_input{
   ipPartNum:string,
}

export interface AreSNumsAllocated_output{
   returnObj:boolean,
}

   /** Required : 
      @param ds
   */  
export interface AttributeSetSplitPreLoadCheck_input{
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface AttributeSetSplitPreLoadCheck_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ipAttributeSetID
      @param ds
   */  
export interface ChangeAttributeSetIDRowMod_input{
   ipAttributeSetID:number,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeAttributeSetIDRowMod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ipAttributeSetID
      @param ds
   */  
export interface ChangeAttributeSetID_input{
   ipAttributeSetID:number,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeAttributeSetID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ipBinNum
      @param ds
   */  
export interface ChangeFromBinRowMod_input{
   ipBinNum:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeFromBinRowMod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ipBinNum
      @param ds
   */  
export interface ChangeFromBin_input{
   ipBinNum:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeFromBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ipwhseCode
      @param ds
   */  
export interface ChangeFromWhseRowMod_input{
   ipwhseCode:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeFromWhseRowMod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ipwhseCode
      @param ds
   */  
export interface ChangeFromWhse_input{
   ipwhseCode:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeFromWhse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ipLotNum
      @param ipFromTo
      @param ds
   */  
export interface ChangeLotRowMod_input{
   ipLotNum:string,
   ipFromTo:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeLotRowMod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
   message:string,
}
}

   /** Required : 
      @param ipLotNum
      @param ipFromTo
      @param ds
   */  
export interface ChangeLot_input{
   ipLotNum:string,
   ipFromTo:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeLot_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
   message:string,
}
}

   /** Required : 
      @param tranPCID
      @param ds
   */  
export interface ChangePCID_input{
      /**  Package Control ID  */  
   tranPCID:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ipToBinNum
      @param ds
   */  
export interface ChangeToBinRowMod_input{
   ipToBinNum:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeToBinRowMod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ipToBinNum
      @param ds
   */  
export interface ChangeToBin_input{
   ipToBinNum:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeToBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ipToWhse
      @param ds
   */  
export interface ChangeToWhseRowMod_input{
   ipToWhse:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeToWhseRowMod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ipToWhse
      @param ds
   */  
export interface ChangeToWhse_input{
   ipToWhse:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeToWhse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param tranPartNum
      @param ds
   */  
export interface ChangeTransferPartNum_input{
   tranPartNum:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeTransferPartNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param proposedValue
      @param ds
   */  
export interface ChangeTransferQtyRowMod_input{
   proposedValue:number,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeTransferQtyRowMod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param proposedValue
      @param ds
   */  
export interface ChangeTransferQty_input{
   proposedValue:number,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeTransferQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeUOMRowMod_input{
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeUOMRowMod_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeUOM_input{
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ChangeUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

export interface CheckAdvancedMaterialAndPackageControl_output{
parameters : {
      /**  output parameters  */  
   amAvailable:boolean,
   pcAvailable:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface CommitTransferAndUpdateHistory_input{
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface CommitTransferAndUpdateHistory_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
   LegalNumberMessage:string,
}
}

   /** Required : 
      @param ds
   */  
export interface CommitTransfer_input{
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface CommitTransfer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
   LegalNumberMessage:string,
   partTranPKs:string,
}
}

export interface Erp_Tablesets_InvTransRow{
   Company:string,
      /**  Date of transaction.  */  
   TranDate:string,
      /**  The Warehouse the part is being transferred From.  */  
   FromWarehouseCode:string,
   FromWarehouseDesc:string,
      /**  The Warehouse the part is being transferred To.  */  
   ToWarehouseCode:string,
   ToWarehouseDesc:string,
      /**  The Warehouse Bin the part is being transferred From.  */  
   FromBinNum:string,
   FromBinDesc:string,
      /**  The Warehouse Bin the part is being transferred To.  */  
   ToBinNum:string,
   ToBinDesc:string,
      /**  The Lot number that is being transferred.  */  
   FromLotNumber:string,
      /**  The Lot number that is being transferred to.  */  
   ToLotNumber:string,
   FromOnHandQty:number,
   ToOnHandQty:number,
   Plant:string,
   Plant2:string,
      /**  The Part Number selected for inventory transfer.  */  
   PartNum:string,
   TrackDimension:boolean,
   TrackSerialnumbers:boolean,
   TrackLots:boolean,
   PartDescription:string,
   SearchWord:string,
      /**  Transaction reference.  Can be used to hold a short comment.  */  
   TranReference:string,
      /**  Plant than owns the FromWarehouseCode  */  
   FromPlant:string,
      /**  If FromPlant is Full Serial Tracking  */  
   FromPlantTracking:boolean,
      /**  Plant that owns the ToWarehouseCode  */  
   ToPlant:string,
      /**  If ToPlant is Full Serial Tracking  */  
   ToPlantTracking:boolean,
   FromOnHandUOM:string,
      /**  Transfer Quantity entered for this inventory transfer.  */  
   TransferQty:number,
      /**  The unit of measure the quantify of this transfer is specified in.  */  
   TransferQtyUOM:string,
   ToOnHandUOM:string,
   TrackingUOM:string,
   TrackingQty:number,
      /**  Indicates the transaction document type for the record. A document type links a system transaction to a unique legal number.  */  
   TranDocTypeID:string,
   ToOrderNum:number,
   ToOrderLine:number,
   ToOrderRelNum:number,
      /**  Package Control Identification Number.  */  
   PCID:string,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  True if transaction is related to Epicor FSA  */  
   EpicorFSA:boolean,
      /**  Call Code from FSA  */  
   CallCode:string,
      /**  Contract Code from FSA  */  
   ContractCode:string,
      /**  Warranty Code from FSA  */  
   WarrantyCode:string,
      /**  Contract Num from FSA  */  
   ContractNum:number,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
   Source:string,
   SysRowID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
   PartAttrClassID:string,
   PartTrackInventoryAttributes:boolean,
   PartTrackDimension:boolean,
   EnableAttributeSetSearch:boolean,
   WarehouseFilterPartNum_Kinetic:string,
   WarehouseFilterPlant_Kinetic:string,
      /**  Contains PCID or PartNum. Use for Crumb bar items  */  
   Key_Kinetic:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   DispNumberOfPieces:number,
      /**  Unique SysRowID for the related part record.  */  
   PartSysRowID:string,
   PartTrackInventoryByRevision:boolean,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   PartTrackSerialNum:boolean,
   ToAttributeSetID:number,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InvTransferTableset{
   InvTrans:Erp_Tablesets_InvTransRow[],
   TransferHistory:Erp_Tablesets_TransferHistoryRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   Parts:Erp_Tablesets_PartsRow[],
   SelectedSerialNumbers:Erp_Tablesets_SelectedSerialNumbersRow[],
   SNFormat:Erp_Tablesets_SNFormatRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_LegalNumGenOptsRow{
   Company:string,
   LegalNumberID:string,
   TransYear:number,
   TransYearSuffix:string,
   DspTransYear:string,
      /**  Indicates if DspTransYear should be displayed when prompting for a manual number.  */  
   ShowDspTransYear:boolean,
   Prefix:string,
      /**  The list of prefixes that can be selected by the user for manual numbers.  */  
   PrefixList:string,
      /**  The suffix portion of the legal number.  */  
   NumberSuffix:string,
      /**  Indicates if the prefix can be entered by the user.  */  
   EnablePrefix:boolean,
      /**  Indicates if the suffix (number) can be entered by the user.  */  
   EnableSuffix:boolean,
   NumberOption:string,
   DocumentDate:string,
   GenerationType:string,
   Description:string,
   TransPeriod:number,
      /**  Prefix for the period  */  
   PeriodPrefix:string,
   ShowTransPeriod:boolean,
      /**  Used when the full legal number is entered  */  
   LegalNumber:string,
   TranDocTypeID:string,
   TranDocTypeID2:string,
   GenerationOption:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartsRow{
   Company:string,
   PartNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
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

export interface Erp_Tablesets_TransferHistoryRow{
      /**  Transfer history  */  
   History:string,
   PartNum:string,
   PartTranPKs:string,
   PCID:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

   /** Required : 
      @param PartNum
      @param AllBins
      @param WarehouseCode
      @param LotNum
      @param DimCode
   */  
export interface GetAvailBins_input{
      /**  Part Number  (current only).  */  
   PartNum:string,
      /**  A for all bins or C for current warehouse.  */  
   AllBins:string,
      /**  Warehouse code.  */  
   WarehouseCode:string,
      /**  Lot number  (current only).  */  
   LotNum:string,
      /**  UNIT OF MEASURE (old Dimension Code)  */  
   DimCode:string,
}

export interface GetAvailBins_output{
parameters : {
      /**  output parameters  */  
   BinList:string,
}
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   listAvailTranDocTypes:string,
}
}

   /** Required : 
      @param ipPCIDList
      @param fromPCIDContextSearch
      @param ds
   */  
export interface GetInvTransferRecordsForPCID_input{
   ipPCIDList:string,
   fromPCIDContextSearch:boolean,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface GetInvTransferRecordsForPCID_output{
   returnObj:Erp_Tablesets_InvTransferTableset[],
parameters : {
      /**  output parameters  */  
   errorMessages:string,
   PCIDList:string,
}
}

   /** Required : 
      @param ipPCIDList
      @param fromPCIDContextSearch
      @param ds
   */  
export interface GetInvTransferRecordsForStandardPCIDList_input{
   ipPCIDList:string,
   fromPCIDContextSearch:boolean,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface GetInvTransferRecordsForStandardPCIDList_output{
   returnObj:Erp_Tablesets_InvTransferTableset[],
parameters : {
      /**  output parameters  */  
   errorMessages:string,
}
}

   /** Required : 
      @param ipPartList
      @param ds
   */  
export interface GetInvTransferRecords_input{
   ipPartList:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface GetInvTransferRecords_output{
   returnObj:Erp_Tablesets_InvTransferTableset[],
}

   /** Required : 
      @param ipSourceType
      @param ds
   */  
export interface GetNewInventoryTransfer_input{
   ipSourceType:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface GetNewInventoryTransfer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ipPartList
      @param ds
   */  
export interface GetNotSelectedInvTransferRecords_input{
   ipPartList:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface GetNotSelectedInvTransferRecords_output{
   returnObj:Erp_Tablesets_InvTransferTableset[],
}

   /** Required : 
      @param ipRowType
      @param ipRowID
   */  
export interface GetPartFromRowID_input{
   ipRowType:string,
   ipRowID:string,
}

export interface GetPartFromRowID_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
}
}

   /** Required : 
      @param partNum
      @param uomCode
      @param SysRowID
      @param rowType
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
}

export interface GetPartXRefInfo_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   uomCode:string,
   serialWarning:string,
   questionString:string,
   multipleMatch:boolean,
}
}

   /** Required : 
      @param iPartNum
      @param iWarehouseCode
   */  
export interface GetPrimaryBin_input{
      /**  Part Number  */  
   iPartNum:string,
      /**  WarehouseCode  */  
   iWarehouseCode:string,
}

export interface GetPrimaryBin_output{
   returnObj:string,
parameters : {
      /**  output parameters  */  
   PrimaryBin:string,
}
}

   /** Required : 
      @param ds
   */  
export interface GetSelectSerialNumbersParamsRowMod_input{
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface GetSelectSerialNumbersParamsRowMod_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface GetSelectSerialNumbersParams_input{
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param iPartNum
      @param sysRowID
      @param iPCID
      @param uomCode
      @param ds
   */  
export interface GetTransferRecord_input{
      /**  Part Number  */  
   iPartNum:string,
      /**  row id  */  
   sysRowID:string,
      /**  Package Control ID  */  
   iPCID:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface GetTransferRecord_output{
parameters : {
      /**  output parameters  */  
   rowAdded:boolean,
   ds:Erp_Tablesets_InvTransferTableset,
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
      @param ds
   */  
export interface MasterInventoryBinTests_input{
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface MasterInventoryBinTests_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
   pcNeqQtyAction:string,
   pcNeqQtyMessage:string,
   pcFromPCBinAction:string,
   pcFromPCBinMessage:string,
   pcToPCBinAction:string,
   pcToPCBinMessage:string,
}
}

   /** Required : 
      @param pcPartNum
      @param pcWhseCode
      @param pcBinNum
      @param pcLotNum
      @param pcAttributeSetID
      @param pcPCID
      @param pcUOMCode
      @param pdTranQty
      @param pdDimConvFactor
   */  
export interface NegativeInventoryTest_input{
   pcPartNum:string,
   pcWhseCode:string,
   pcBinNum:string,
   pcLotNum:string,
   pcAttributeSetID:number,
   pcPCID:string,
   pcUOMCode:string,
   pdTranQty:number,
   pdDimConvFactor:number,
}

export interface NegativeInventoryTest_output{
parameters : {
      /**  output parameters  */  
   pcNeqQtyAction:string,
   pcMessage:string,
}
}

   /** Required : 
      @param attributeSetID
      @param ds
   */  
export interface OnChangingAttributeSet_input{
   attributeSetID:number,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface OnChangingAttributeSet_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param dispNumberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   dispNumberOfPieces:number,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param revisionNum
      @param ds
   */  
export interface OnChangingRevisionNum_input{
   revisionNum:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface OnChangingRevisionNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param transferQtyUOM
      @param ds
   */  
export interface OnChangingTransferQtyUOM_input{
   transferQtyUOM:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface OnChangingTransferQtyUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param transferQty
      @param ds
   */  
export interface OnChangingTransferQty_input{
   transferQty:number,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface OnChangingTransferQty_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface PreCommitTransfer_input{
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface PreCommitTransfer_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
   RequiresUserInput:boolean,
}
}

   /** Required : 
      @param ds
      @param partTransPKsParam
      @param tranQty
      @param tranQtyUOM
      @param fromWarehouseDesc
      @param fromBinDesc
      @param toWarehouseDesc
      @param toBinDesc
   */  
export interface UpdateHistory_input{
   ds:Erp_Tablesets_InvTransferTableset[],
      /**  partTransPKs value generated from transfer, if applicable  */  
   partTransPKsParam:string,
      /**  Transfer Quantity  */  
   tranQty:string,
      /**  Transfer Quantity UOM  */  
   tranQtyUOM:string,
      /**  From Warehouse Description  */  
   fromWarehouseDesc:string,
      /**  From Warehouse Bin Description  */  
   fromBinDesc:string,
      /**  To Warehouse Description  */  
   toWarehouseDesc:string,
      /**  To Warehouse Bin Description  */  
   toBinDesc:string,
}

export interface UpdateHistory_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
}
}

   /** Required : 
      @param proposedPCID
      @param uomCodePartXRef
      @param refreshMode
      @param pcidList
      @param ds
   */  
export interface ValidatePCID_input{
   proposedPCID:string,
   uomCodePartXRef:string,
   refreshMode:boolean,
   pcidList:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ValidatePCID_output{
   returnObj:Erp_Tablesets_InvTransferTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
   rowAdded:boolean,
}
}

   /** Required : 
      @param proposedPartNum
      @param uomCodePartXRef
      @param refreshMode
      @param partList
      @param ds
   */  
export interface ValidatePartNum_input{
   proposedPartNum:string,
   uomCodePartXRef:string,
   refreshMode:boolean,
   partList:string,
   ds:Erp_Tablesets_InvTransferTableset[],
}

export interface ValidatePartNum_output{
   returnObj:Erp_Tablesets_InvTransferTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
   rowAdded:boolean,
}
}

   /** Required : 
      @param ds
      @param serialNumber
   */  
export interface ValidateSN_input{
   ds:Erp_Tablesets_InvTransferTableset[],
      /**  Serial number to validate.  */  
   serialNumber:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InvTransferTableset,
   isVoided:boolean,
}
}

