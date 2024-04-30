import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.InventoryQtyAdjSvc
// Description: Temporary datatables allow the user to enter data for
the quantity adjustments, serial numbers selected and
serial number formats.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/$metadata", {
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
   Summary: Invoke method CheckSN
   Description: Determines if serial numbers are required for this transaction
   OperationID: CheckSN
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckSN_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSN_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSN(requestBody:CheckSN_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckSN_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/CheckSN", {
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
         resolve(data as CheckSN_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckSNFSA
   OperationID: CheckSNFSA
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckSNFSA_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSNFSA_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckSNFSA(requestBody:CheckSNFSA_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckSNFSA_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/CheckSNFSA", {
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
         resolve(data as CheckSNFSA_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPCIDAdjustmentInfo
   Description: Gets the InventoryQtyAdj and InventoryQtyAdjBrw datasets for the specified PCID.
   OperationID: GetPCIDAdjustmentInfo
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetPCIDAdjustmentInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPCIDAdjustmentInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetPCIDAdjustmentInfo(requestBody:GetPCIDAdjustmentInfo_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetPCIDAdjustmentInfo_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetPCIDAdjustmentInfo", {
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
         resolve(data as GetPCIDAdjustmentInfo_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInventoryQtyAdjForPCID
   Description: Gets the default InventoryQtyAdj values for the PCID and the Warehouse Bins (InventoryQtyAdjBrw)
   OperationID: GetInventoryQtyAdjForPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjForPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjForPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryQtyAdjForPCID(requestBody:GetInventoryQtyAdjForPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInventoryQtyAdjForPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetInventoryQtyAdjForPCID", {
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
         resolve(data as GetInventoryQtyAdjForPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInventoryQtyAdjPCID
   Description: Gets the default values for the InventoryQtyAdj data table based on the PCID entered.
   OperationID: GetInventoryQtyAdjPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryQtyAdjPCID(requestBody:GetInventoryQtyAdjPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInventoryQtyAdjPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetInventoryQtyAdjPCID", {
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
         resolve(data as GetInventoryQtyAdjPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInventoryQtyAdj
   Description: Gets the default values for the InventoryQtyAdj data table based on the part
number entered.
   OperationID: GetInventoryQtyAdj
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryQtyAdj(requestBody:GetInventoryQtyAdj_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInventoryQtyAdj_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetInventoryQtyAdj", {
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
         resolve(data as GetInventoryQtyAdj_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInventoryQtyAdjForPart
   Description: Gets the default InventoryQtyAdj values for the Part and the Warehouse Bins (InventoryQtyAdjBrw)
   OperationID: GetInventoryQtyAdjForPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjForPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjForPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryQtyAdjForPart(requestBody:GetInventoryQtyAdjForPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInventoryQtyAdjForPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetInventoryQtyAdjForPart", {
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
         resolve(data as GetInventoryQtyAdjForPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInventoryQtyAdjBrwInclManaged
   Description: Gets the default values for the browse section of the adjustment screen (including SMI inventory)
   OperationID: GetInventoryQtyAdjBrwInclManaged
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrwInclManaged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrwInclManaged_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryQtyAdjBrwInclManaged(requestBody:GetInventoryQtyAdjBrwInclManaged_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInventoryQtyAdjBrwInclManaged_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetInventoryQtyAdjBrwInclManaged", {
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
         resolve(data as GetInventoryQtyAdjBrwInclManaged_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInventoryQtyAdjBrwInclPCID
   Description: Gets the default values for the browse section of the adjustment screen (excluding SMI inventory and including PCID)
   OperationID: GetInventoryQtyAdjBrwInclPCID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrwInclPCID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrwInclPCID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryQtyAdjBrwInclPCID(requestBody:GetInventoryQtyAdjBrwInclPCID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInventoryQtyAdjBrwInclPCID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetInventoryQtyAdjBrwInclPCID", {
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
         resolve(data as GetInventoryQtyAdjBrwInclPCID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInventoryQtyAdjBrwInclPCIDInventoryTracking
   Description: Gets the default values for the browse section of the adjustment screen (excluding SMI inventory and including PCID)
   OperationID: GetInventoryQtyAdjBrwInclPCIDInventoryTracking
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrwInclPCIDInventoryTracking_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrwInclPCIDInventoryTracking_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryQtyAdjBrwInclPCIDInventoryTracking(requestBody:GetInventoryQtyAdjBrwInclPCIDInventoryTracking_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInventoryQtyAdjBrwInclPCIDInventoryTracking_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetInventoryQtyAdjBrwInclPCIDInventoryTracking", {
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
         resolve(data as GetInventoryQtyAdjBrwInclPCIDInventoryTracking_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInventoryQtyAdjBrw
   Description: Gets the default values for the browse section of the adjustment screen (excluding SMI inventory)
   OperationID: GetInventoryQtyAdjBrw
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrw_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrw_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryQtyAdjBrw(requestBody:GetInventoryQtyAdjBrw_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInventoryQtyAdjBrw_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetInventoryQtyAdjBrw", {
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
         resolve(data as GetInventoryQtyAdjBrw_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetInventoryQtyAdjBrwInventoryTracking
   Description: Gets the default values for the browse section of the adjustment screen (excluding SMI inventory)
   OperationID: GetInventoryQtyAdjBrwInventoryTracking
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/GetInventoryQtyAdjBrwInventoryTracking_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetInventoryQtyAdjBrwInventoryTracking_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetInventoryQtyAdjBrwInventoryTracking(requestBody:GetInventoryQtyAdjBrwInventoryTracking_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetInventoryQtyAdjBrwInventoryTracking_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetInventoryQtyAdjBrwInventoryTracking", {
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
         resolve(data as GetInventoryQtyAdjBrwInventoryTracking_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetPartXRefInfo", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetSelectSerialNumbersParams", {
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
   Summary: Invoke method KitPartStatus
   Description: Checks Part's type and returns warning message if the part is a Sales Kit.
   OperationID: KitPartStatus
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/KitPartStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/KitPartStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KitPartStatus(requestBody:KitPartStatus_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<KitPartStatus_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/KitPartStatus", {
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
         resolve(data as KitPartStatus_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreSetInventoryQtyAdj
   Description: This method performs multiple functions:
This method will return a record in the LegalNumGenOpts datatable if
a legal number is required for this transaction.
The RequiresUserInput
flag will indicate if this legal number requires input from the user.  If
it does, the LegalNumberPrompt business objects needs to be called to
gather that information.  This method should be called when the user
saves the record but before the Update method is called.
            
And will auto select serial numbers if the adjustment is from a PCID and the entire PCID PartBin qty is being adjusted out.
   OperationID: PreSetInventoryQtyAdj
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreSetInventoryQtyAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreSetInventoryQtyAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreSetInventoryQtyAdj(requestBody:PreSetInventoryQtyAdj_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreSetInventoryQtyAdj_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/PreSetInventoryQtyAdj", {
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
         resolve(data as PreSetInventoryQtyAdj_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetInventoryQtyAdj
   Description: Create Part Tran records from the Inventory QtyAdj dataset. If Serial numbers
are entered, SerialNo records and SNTran records are created.  If the Serial
number format is changed, the Part table will be updated with the information
provided in the SNFormat data table.
   OperationID: SetInventoryQtyAdj
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetInventoryQtyAdj_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetInventoryQtyAdj_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetInventoryQtyAdj(requestBody:SetInventoryQtyAdj_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetInventoryQtyAdj_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/SetInventoryQtyAdj", {
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
         resolve(data as SetInventoryQtyAdj_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/ValidateSN", {
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
   Summary: Invoke method GetAvailTranDocTypes
   Description: Method to call to get available tran doc types.
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetAvailTranDocTypes", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/NegativeInventoryTest", {
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
   Summary: Invoke method FindPart
   OperationID: FindPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/FindPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/FindPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_FindPart(requestBody:FindPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<FindPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/FindPart", {
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
         resolve(data as FindPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetPartFromRowID
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/GetPartFromRowID", {
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
   Summary: Invoke method ChangeUOM
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/ChangeUOM", {
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
   Summary: Invoke method OnChangeBinNum
   Description: Validates that the bin entered is valid
   OperationID: OnChangeBinNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeBinNum(requestBody:OnChangeBinNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeBinNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/OnChangeBinNum", {
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
         resolve(data as OnChangeBinNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeWareHseCode
   Description: Validates that the warehouse entered is valid
   OperationID: OnChangeWareHseCode
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeWareHseCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeWareHseCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeWareHseCode(requestBody:OnChangeWareHseCode_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeWareHseCode_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/OnChangeWareHseCode", {
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
         resolve(data as OnChangeWareHseCode_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeUnitOfMeasure
   Description: Validates that the unit of measure entered is valid
   OperationID: OnChangeUnitOfMeasure
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeUnitOfMeasure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeUnitOfMeasure_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeUnitOfMeasure(requestBody:OnChangeUnitOfMeasure_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeUnitOfMeasure_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/OnChangeUnitOfMeasure", {
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
         resolve(data as OnChangeUnitOfMeasure_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangeLotNum
   Description: Validates that the lotNum entered is valid
   OperationID: OnChangeLotNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeLotNum(requestBody:OnChangeLotNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeLotNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/OnChangeLotNum", {
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
         resolve(data as OnChangeLotNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangePCID
   Description: Validates that the PCID entered is valid
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/OnChangePCID", {
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
   Summary: Invoke method OnChangeSelectionAttributeSetID
   Description: Validates that the selectionAttributeSetID entered is valid
   OperationID: OnChangeSelectionAttributeSetID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangeSelectionAttributeSetID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeSelectionAttributeSetID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangeSelectionAttributeSetID(requestBody:OnChangeSelectionAttributeSetID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangeSelectionAttributeSetID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/OnChangeSelectionAttributeSetID", {
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
         resolve(data as OnChangeSelectionAttributeSetID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingSelectionRevisionNum
   Description: Call this method when the Revision changes.  Will select related bins.
   OperationID: OnChangingSelectionRevisionNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingSelectionRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingSelectionRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingSelectionRevisionNum(requestBody:OnChangingSelectionRevisionNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingSelectionRevisionNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/OnChangingSelectionRevisionNum", {
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
         resolve(data as OnChangingSelectionRevisionNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingAdjustQuantity
   Description: Logic for when the adjust quantity is changing
   OperationID: OnChangingAdjustQuantity
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingAdjustQuantity_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingAdjustQuantity_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingAdjustQuantity(requestBody:OnChangingAdjustQuantity_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingAdjustQuantity_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/OnChangingAdjustQuantity", {
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
         resolve(data as OnChangingAdjustQuantity_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingUnitOfMeasure
   Description: Logic for when the unit of measure is changing
   OperationID: OnChangingUnitOfMeasure
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/OnChangingUnitOfMeasure_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangingUnitOfMeasure_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_OnChangingUnitOfMeasure(requestBody:OnChangingUnitOfMeasure_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<OnChangingUnitOfMeasure_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/OnChangingUnitOfMeasure", {
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
         resolve(data as OnChangingUnitOfMeasure_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method OnChangingNumberOfPieces
   Description: Logic for when the number of pieces is changing
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.InventoryQtyAdjSvc/OnChangingNumberOfPieces", {
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



//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////
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
      @param UOM
      @param ds
   */  
export interface ChangeUOM_input{
   UOM:string,
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface ChangeUOM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
}
}

   /** Required : 
      @param partNum
      @param warehouseCode
      @param binNum
      @param ipPCID
   */  
export interface CheckSNFSA_input{
   partNum:string,
   warehouseCode:string,
   binNum:string,
      /**  PCID  */  
   ipPCID:string,
}

export interface CheckSNFSA_output{
parameters : {
      /**  output parameters  */  
   serialNumbersRequired:boolean,
}
}

   /** Required : 
      @param partNum
      @param warehouseCode
      @param ipPCID
   */  
export interface CheckSN_input{
      /**  Part Number  */  
   partNum:string,
      /**  Warehouse Code  */  
   warehouseCode:string,
      /**  PCID  */  
   ipPCID:string,
}

export interface CheckSN_output{
parameters : {
      /**  output parameters  */  
   serialNumbersRequired:boolean,
}
}

export interface Erp_Tablesets_InventoryQtyAdjBrwRow{
      /**  Company  */  
   Company:string,
      /**  Bin number  */  
   BinNum:string,
      /**  On hand quantity  */  
   OnHandQty:number,
      /**  Non nettable flag  */  
   NonNettable:boolean,
      /**  Ware house code  */  
   WareHseCode:string,
      /**  Lot number  */  
   LotNum:string,
      /**  WareHouse Bin description.  */  
   WhseBinDesc:string,
   StkUOMCode:string,
   StkUOMDesc:string,
      /**  The PartBin.OnHandQty expressed in Part Base UOM  */  
   BaseOnHandQty:number,
      /**  Unit of Measure to qualifiy BaseOnHandQty. This is the Part Base UOM.  */  
   BaseOnHandUOM:string,
   BinType:string,
      /**  Translated description string of Bin Type  */  
   BinTypeDesc:string,
      /**  Determines if the Part Bin has to be synchronized with Epicor FSA application.  */  
   SendToFSA:boolean,
      /**  The parent PCID for the bin or child PCID record.  */  
   PCID:string,
      /**  PartNum for the bin record.  */  
   PartNum:string,
      /**  The PCID of the child in the parent PCID.  */  
   ItemPCID:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
   PartAttrClassID:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InventoryQtyAdjBrwTableset{
   InventoryQtyAdjBrw:Erp_Tablesets_InventoryQtyAdjBrwRow[],
   ExtensionTables:Ice_Extensions_ExtensionTableData[],
}

export interface Erp_Tablesets_InventoryQtyAdjRow{
   Company:string,
   PartNum:string,
   WareHseCode:string,
   OnHandQty:number,
   BinNum:string,
   AdjustQuantity:number,
   ReasonCode:string,
   LotNum:string,
   Reference:string,
   UnitOfMeasure:string,
   TransDate:string,
   ReasonType:string,
      /**  Total Serial number quantity  */  
   SerialNoQty:number,
      /**  Temporary serial number  */  
   TempSerialNo:number,
      /**  Reason code required flag  */  
   ReasonCodeReq:boolean,
      /**  Determines if inventory level can be driven below zero.  */  
   AllowNegQty:boolean,
   LegalNumberMessage:string,
   StkUOMCode:string,
      /**  True/False flag that determines if serial numbers are required for this transaction.  */  
   EnableSN:boolean,
      /**  Unit of Measure that qualifies the OnHandQty.  */  
   OnHandUOM:string,
   TranDocTypeID:string,
   PCID:string,
      /**  Unique identifier for this row. The value is a GUID.  */  
   SysRowID:string,
   ReasonCodeDescription:string,
   MYImportNum:string,
      /**  Related to an Epicor FSA transaction  */  
   EpicorFSA:boolean,
      /**  Used by Epicor FSA  */  
   ContractCode:string,
      /**  Used by Epicor FSA  */  
   WarrantyCode:string,
      /**  Used by Epicor FSA  */  
   CallCode:string,
      /**  Service Order number generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderNum:number,
      /**  Service Order Resource generated on FSA, stored on FSAExtData db table.  */  
   FSAServiceOrderResourceNum:number,
      /**  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  */  
   FSAAction:string,
      /**  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  */  
   FSAEquipmentPartNum:string,
      /**  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  */  
   FSAEquipmentInstallID:number,
      /**  FSA ContractNum  */  
   ContractNum:number,
   TrackSerialNo:boolean,
   FSABin:boolean,
      /**  PCID used to populate the selection criteria.  This value is not used for update.  */  
   SelectionPCID:string,
      /**  PartNum used to populate the selection criteria.  This value is not used for update.  */  
   SelectionPartNum:string,
      /**  The description of the selection part number.  */  
   SelectionPartDescription:string,
      /**  True/False that determines if Advanced Package Control is allowed.  */  
   AdvancedPackageControl:boolean,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   AttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   AttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   AttributeSetShortDescription:string,
      /**  The unique identifier of the related Dynamic Attribute Set.  */  
   SelectionAttributeSetID:number,
      /**  The Full Description of the Attribute Set.  */  
   SelectionAttributeSetDescription:string,
      /**  The Short Description of the Attribute Set.  */  
   SelectionAttributeSetShortDescription:string,
      /**  Number of pieces for inventory attribute tracked parts.  */  
   NumberOfPieces:number,
      /**  Revision number which is used to uniquely identify the revision of the part.  */  
   RevisionNum:string,
   SelectionRevisionNum:string,
   PartTrackInventoryByRevision:boolean,
   PartTrackInventoryAttributes:boolean,
   PartTrackLots:boolean,
   PartTrackDimension:boolean,
   PartSalesUM:string,
   PartPricePerCode:string,
   PartSellingFactor:number,
   PartTrackSerialNum:boolean,
   PartIUM:string,
   PartPartDescription:string,
   PartAttrClassID:string,
   WareHseDescription:string,
   WhseBinDescription:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_InventoryQtyAdjTableset{
   InventoryQtyAdj:Erp_Tablesets_InventoryQtyAdjRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
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
      @param ipPartNum
   */  
export interface FindPart_input{
   ipPartNum:string,
}

export interface FindPart_output{
parameters : {
      /**  output parameters  */  
   opPartNum:string,
   opUOM:string,
   opMatchType:string,
}
}

export interface GetAvailTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   AvailTypes:string,
}
}

   /** Required : 
      @param partNum
      @param wareHouseCode
   */  
export interface GetInventoryQtyAdjBrwInclManaged_input{
      /**  Part number for the adjustment.  */  
   partNum:string,
      /**  Warehouse code used to get bin information.  */  
   wareHouseCode:string,
}

export interface GetInventoryQtyAdjBrwInclManaged_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
parameters : {
      /**  output parameters  */  
   primaryBin:string,
}
}

   /** Required : 
      @param partNum
      @param revisionNum
      @param attributeSetID
      @param wareHouseCode
   */  
export interface GetInventoryQtyAdjBrwInclPCIDInventoryTracking_input{
      /**  Part number for the adjustment.  */  
   partNum:string,
      /**  Revision Number used to get bin information. Bins are not filtered by Revision Number if no value is sent.  */  
   revisionNum:string,
      /**  Attribute Set ID used to get bin information. Bins are not filtered by Attribute Set ID if a zero is sent.  */  
   attributeSetID:number,
      /**  Warehouse code used to get bin information.  */  
   wareHouseCode:string,
}

export interface GetInventoryQtyAdjBrwInclPCIDInventoryTracking_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
parameters : {
      /**  output parameters  */  
   primaryBin:string,
}
}

   /** Required : 
      @param partNum
      @param attributeSetID
      @param wareHouseCode
   */  
export interface GetInventoryQtyAdjBrwInclPCID_input{
      /**  Part number for the adjustment.  */  
   partNum:string,
      /**  Attribute Set ID used to get bin information. Bins are not filtered by Attribute Set ID if a zero is sent  */  
   attributeSetID:number,
      /**  Warehouse code used to get bin information.  */  
   wareHouseCode:string,
}

export interface GetInventoryQtyAdjBrwInclPCID_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
parameters : {
      /**  output parameters  */  
   primaryBin:string,
}
}

   /** Required : 
      @param partNum
      @param revisionNum
      @param attributeSetID
      @param wareHouseCode
   */  
export interface GetInventoryQtyAdjBrwInventoryTracking_input{
      /**  Part number for the adjustment.  */  
   partNum:string,
      /**  Revision Number used to get bin information. Bins are not filtered by Revision Number if no value is sent.  */  
   revisionNum:string,
      /**  Attribute Set ID used to get bin information. Bins are not filtered by Attribute Set ID if a zero is sent  */  
   attributeSetID:number,
      /**  Warehouse code used to get bin information.  */  
   wareHouseCode:string,
}

export interface GetInventoryQtyAdjBrwInventoryTracking_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
parameters : {
      /**  output parameters  */  
   primaryBin:string,
}
}

   /** Required : 
      @param partNum
      @param attributeSetID
      @param wareHouseCode
   */  
export interface GetInventoryQtyAdjBrw_input{
      /**  Part number for the adjustment.  */  
   partNum:string,
      /**  Attribute Set ID used to get bin information. Bins are not filtered by Attribute Set ID if a zero is sent  */  
   attributeSetID:number,
      /**  Warehouse code used to get bin information.  */  
   wareHouseCode:string,
}

export interface GetInventoryQtyAdjBrw_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
parameters : {
      /**  output parameters  */  
   primaryBin:string,
}
}

   /** Required : 
      @param pcid
      @param doStatusValidation
      @param ds
   */  
export interface GetInventoryQtyAdjForPCID_input{
      /**  The PCID to adjust  */  
   pcid:string,
      /**  Validate the PCID Status  */  
   doStatusValidation:boolean,
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface GetInventoryQtyAdjForPCID_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
}
}

   /** Required : 
      @param partnumber
      @param uomCode
      @param ds
   */  
export interface GetInventoryQtyAdjForPart_input{
      /**  The part to adjust  */  
   partnumber:string,
      /**  UOM code if selected from part cross reference  */  
   uomCode:string,
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface GetInventoryQtyAdjForPart_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
}
}

   /** Required : 
      @param partnumber
      @param uomCode
      @param pcid
   */  
export interface GetInventoryQtyAdjPCID_input{
      /**  Part number to adjust.  */  
   partnumber:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
      /**  The parent PCID  */  
   pcid:string,
}

export interface GetInventoryQtyAdjPCID_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjTableset[],
}

   /** Required : 
      @param partnumber
      @param uomCode
   */  
export interface GetInventoryQtyAdj_input{
      /**  Part number to adjust.  */  
   partnumber:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
}

export interface GetInventoryQtyAdj_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjTableset[],
}

   /** Required : 
      @param pcid
      @param doStatusValidations
      @param inventoryQtyAdj
      @param inventoryQtyAdjBrw
   */  
export interface GetPCIDAdjustmentInfo_input{
      /**  A PCID that has parts to be adjusted  */  
   pcid:string,
      /**  True if the status of the PCID should be validated  */  
   doStatusValidations:boolean,
   inventoryQtyAdj:Erp_Tablesets_InventoryQtyAdjTableset[],
   inventoryQtyAdjBrw:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
}

export interface GetPCIDAdjustmentInfo_output{
parameters : {
      /**  output parameters  */  
   inventoryQtyAdj:Erp_Tablesets_InventoryQtyAdjTableset,
   inventoryQtyAdjBrw:Erp_Tablesets_InventoryQtyAdjBrwTableset,
}
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
      @param sysRowID
      @param rowType
      @param uomCode
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   sysRowID:string,
      /**  RowType of the selected record. Only used with sysRowID.  */  
   rowType:string,
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
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
      @param ipCompany
      @param ipWareHseCode
      @param ipPartNum
      @param ipAttributeSetID
      @param ipAdjustQuantity
      @param ipBinNum
      @param ipUnitOfMeasure
      @param ipSysRowID
      @param ipPCID
      @param ipLotNum
   */  
export interface GetSelectSerialNumbersParams_input{
   ipCompany:string,
   ipWareHseCode:string,
   ipPartNum:string,
   ipAttributeSetID:number,
   ipAdjustQuantity:number,
   ipBinNum:string,
   ipUnitOfMeasure:string,
   ipSysRowID:string,
   ipPCID:string,
   ipLotNum:string,
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
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
   */  
export interface KitPartStatus_input{
      /**  Part number.  */  
   partNum:string,
}

export interface KitPartStatus_output{
parameters : {
      /**  output parameters  */  
   kitMessage:string,
}
}

   /** Required : 
      @param pcPartNum
      @param pcWhseCode
      @param pcBinNum
      @param pcLotNum
      @param pcAttributeSetID
      @param pcPCID
      @param pcDimCode
      @param pdDimConvFactor
      @param ipSellingQuantity
   */  
export interface NegativeInventoryTest_input{
   pcPartNum:string,
   pcWhseCode:string,
   pcBinNum:string,
   pcLotNum:string,
   pcAttributeSetID:number,
   pcPCID:string,
   pcDimCode:string,
   pdDimConvFactor:number,
   ipSellingQuantity:number,
}

export interface NegativeInventoryTest_output{
parameters : {
      /**  output parameters  */  
   pcNeqQtyAction:string,
   pcMessage:string,
}
}

   /** Required : 
      @param binNum
      @param ds
   */  
export interface OnChangeBinNum_input{
      /**  The proposed bin  */  
   binNum:string,
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface OnChangeBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
}
}

   /** Required : 
      @param lotNum
      @param ds
   */  
export interface OnChangeLotNum_input{
      /**  The proposed lot number  */  
   lotNum:string,
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface OnChangeLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
}
}

   /** Required : 
      @param pcid
      @param ds
   */  
export interface OnChangePCID_input{
      /**  The proposed PCID number  */  
   pcid:string,
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface OnChangePCID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
}
}

   /** Required : 
      @param selectionAttributeSetID
      @param ds
   */  
export interface OnChangeSelectionAttributeSetID_input{
      /**  The proposed attribute set id  */  
   selectionAttributeSetID:number,
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface OnChangeSelectionAttributeSetID_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
}
}

   /** Required : 
      @param ium
      @param ds
   */  
export interface OnChangeUnitOfMeasure_input{
      /**  The proposed unit of measure  */  
   ium:string,
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface OnChangeUnitOfMeasure_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
}
}

   /** Required : 
      @param wareHseCode
      @param ds
   */  
export interface OnChangeWareHseCode_input{
      /**  The proposed warehouse  */  
   wareHseCode:string,
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface OnChangeWareHseCode_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
}
}

   /** Required : 
      @param adjustQuantity
      @param ds
   */  
export interface OnChangingAdjustQuantity_input{
   adjustQuantity:number,
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface OnChangingAdjustQuantity_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
}
}

   /** Required : 
      @param numberOfPieces
      @param ds
   */  
export interface OnChangingNumberOfPieces_input{
   numberOfPieces:number,
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface OnChangingNumberOfPieces_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
}
}

   /** Required : 
      @param selectionRevisionNum
      @param ds
   */  
export interface OnChangingSelectionRevisionNum_input{
      /**  The proposed Revision Number  */  
   selectionRevisionNum:string,
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface OnChangingSelectionRevisionNum_output{
   returnObj:Erp_Tablesets_InventoryQtyAdjBrwTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
}
}

   /** Required : 
      @param unitOfMeasure
      @param ds
   */  
export interface OnChangingUnitOfMeasure_input{
   unitOfMeasure:string,
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface OnChangingUnitOfMeasure_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface PreSetInventoryQtyAdj_input{
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface PreSetInventoryQtyAdj_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
   requiresUserInput:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface SetInventoryQtyAdj_input{
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
}

export interface SetInventoryQtyAdj_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
   partTranPKs:string,
}
}

   /** Required : 
      @param ds
      @param serialNumber
   */  
export interface ValidateSN_input{
   ds:Erp_Tablesets_InventoryQtyAdjTableset[],
      /**  Serial number to validate.  */  
   serialNumber:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_InventoryQtyAdjTableset,
   isVoided:boolean,
}
}

