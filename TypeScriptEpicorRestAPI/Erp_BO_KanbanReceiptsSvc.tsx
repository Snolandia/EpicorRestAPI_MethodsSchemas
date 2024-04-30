import * as configEpicorSchemas from "./configEpicorSchemas"


/** 
// Title: Erp.BO.KanbanReceiptsSvc
// Description: Kanban Receipts Business Object
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/$metadata", {
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
   Summary: Invoke method CalculateLotPartSelectedQuantities
   Description: Calculate the correct quantities when selecting quantity for a Lot Bin part.
   OperationID: CalculateLotPartSelectedQuantities
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalculateLotPartSelectedQuantities_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateLotPartSelectedQuantities_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateLotPartSelectedQuantities(requestBody:CalculateLotPartSelectedQuantities_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalculateLotPartSelectedQuantities_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/CalculateLotPartSelectedQuantities", {
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
         resolve(data as CalculateLotPartSelectedQuantities_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeProposedBinNum
   Description: Set proposed bin num when binnum is changing
   OperationID: ChangeProposedBinNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeProposedBinNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProposedBinNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeProposedBinNum(requestBody:ChangeProposedBinNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeProposedBinNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeProposedBinNum", {
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
         resolve(data as ChangeProposedBinNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeBin
   Description: Update default information based on the bin changing
   OperationID: ChangeBin
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeBin_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBin_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeBin(requestBody:ChangeBin_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeBin_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeBin", {
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
         resolve(data as ChangeBin_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeEmployee
   Description: Update default information based on the employee changing
   OperationID: ChangeEmployee
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeEmployee_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeEmployee_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeEmployee(requestBody:ChangeEmployee_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeEmployee_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeEmployee", {
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
         resolve(data as ChangeEmployee_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeInventoryUM
   Description: Procedure for changing KanbanReceipts.InventoryUM field
   OperationID: ChangeInventoryUM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeInventoryUM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeInventoryUM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeInventoryUM(requestBody:ChangeInventoryUM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeInventoryUM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeInventoryUM", {
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
         resolve(data as ChangeInventoryUM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeProposedLotNum
   Description: Set proposed lot num when lot num is changing
   OperationID: ChangeProposedLotNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeProposedLotNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProposedLotNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeProposedLotNum(requestBody:ChangeProposedLotNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeProposedLotNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeProposedLotNum", {
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
         resolve(data as ChangeProposedLotNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeLotNum
   Description: Update default information based on the lot changing
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeLotNum", {
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
   Summary: Invoke method ChangeNonConfReason
   Description: Update default information based on the bin changing
   OperationID: ChangeNonConfReason
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeNonConfReason_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeNonConfReason_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeNonConfReason(requestBody:ChangeNonConfReason_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeNonConfReason_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeNonConfReason", {
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
         resolve(data as ChangeNonConfReason_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeProposedPart
   Description: Set a proposed part num when part number is changing
   OperationID: ChangeProposedPart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeProposedPart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProposedPart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeProposedPart(requestBody:ChangeProposedPart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeProposedPart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeProposedPart", {
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
         resolve(data as ChangeProposedPart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangePart
   Description: Update default information based on the part number changing
   OperationID: ChangePart
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangePart_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangePart_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangePart(requestBody:ChangePart_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangePart_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangePart", {
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
         resolve(data as ChangePart_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeRevision
   Description: Update default information based on the revision number changing
   OperationID: ChangeRevision
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeRevision_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRevision_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeRevision(requestBody:ChangeRevision_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeRevision_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeRevision", {
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
         resolve(data as ChangeRevision_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeContractID
   Description: Update information based on the ContractID changed.
   OperationID: ChangeContractID
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeContractID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeContractID_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeContractID(requestBody:ChangeContractID_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeContractID_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeContractID", {
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
         resolve(data as ChangeContractID_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeScrapReason
   Description: Update default information based on the scrap reason changing
   OperationID: ChangeScrapReason
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeScrapReason_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeScrapReason_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeScrapReason(requestBody:ChangeScrapReason_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeScrapReason_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeScrapReason", {
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
         resolve(data as ChangeScrapReason_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeUsePartNumForLot
   Description: Update lot number and description if the value is changed to true.
   OperationID: ChangeUsePartNumForLot
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeUsePartNumForLot_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeUsePartNumForLot_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeUsePartNumForLot(requestBody:ChangeUsePartNumForLot_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeUsePartNumForLot_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeUsePartNumForLot", {
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
         resolve(data as ChangeUsePartNumForLot_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeProposedWarehosue
   Description: Set a proposed part num when part number is changing
   OperationID: ChangeProposedWarehosue
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeProposedWarehosue_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeProposedWarehosue_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeProposedWarehosue(requestBody:ChangeProposedWarehosue_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeProposedWarehosue_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeProposedWarehosue", {
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
         resolve(data as ChangeProposedWarehosue_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ChangeWarehouse
   Description: Update default information based on the warehouse changing
   OperationID: ChangeWarehouse
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ChangeWarehouse_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeWarehouse_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ChangeWarehouse(requestBody:ChangeWarehouse_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ChangeWarehouse_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ChangeWarehouse", {
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
         resolve(data as ChangeWarehouse_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CheckProcessRunning
   Description: Verify if a similar process is running for the same part.
   OperationID: CheckProcessRunning
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CheckProcessRunning_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckProcessRunning_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CheckProcessRunning(requestBody:CheckProcessRunning_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CheckProcessRunning_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/CheckProcessRunning", {
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
         resolve(data as CheckProcessRunning_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ConvertUOM
   Description: This procedure will update the OnhandQty for the LotPartBin record where the qty is retrived and also will update the Total Selected Qty
from LotPartMtl in the correct UOM.
   OperationID: ConvertUOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ConvertUOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ConvertUOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ConvertUOM(requestBody:ConvertUOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ConvertUOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ConvertUOM", {
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
         resolve(data as ConvertUOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method DoesMtlsMatch
   Description: Validates if the Total Selected Qty for Each Part Mtl match with Required Qty. If not
a message is returned to used to inform that case.
   OperationID: DoesMtlsMatch
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/DoesMtlsMatch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DoesMtlsMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_DoesMtlsMatch(requestBody:DoesMtlsMatch_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<DoesMtlsMatch_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/DoesMtlsMatch", {
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
         resolve(data as DoesMtlsMatch_output)
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/GetPartXRefInfo", {
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/GetSelectSerialNumbersParams", {
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
   Summary: Invoke method KanbanReceiptsGetNew
   Description: Creates a temporary record to store information needed for the receipt process.
   OperationID: KanbanReceiptsGetNew
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/KanbanReceiptsGetNew_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_KanbanReceiptsGetNew(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<KanbanReceiptsGetNew_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/KanbanReceiptsGetNew", {
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
         resolve(data as KanbanReceiptsGetNew_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method PreProcessKanbanReceipts
   Description: This method will return a record in the LegalNumGenOpts datatable if
a WIPStock / NonConf / StockWIP legal number is required for this transaction.
The promptWIPStock / promptNonConf flags will indicate whether these legal number types require user input
the LegalNumberPrompt business objects needs to be called to gather that information.
Note - You cannot currently cater for manual StockWIP LN's as this will generate multiple PartTransactions
This method should be called when the user saves the record but before the Update method is called.
   OperationID: PreProcessKanbanReceipts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/PreProcessKanbanReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreProcessKanbanReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_PreProcessKanbanReceipts(requestBody:PreProcessKanbanReceipts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<PreProcessKanbanReceipts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/PreProcessKanbanReceipts", {
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
         resolve(data as PreProcessKanbanReceipts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ProcessKanbanReceipts
   Description: Processes the Kanban Receipt.
   OperationID: ProcessKanbanReceipts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ProcessKanbanReceipts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessKanbanReceipts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ProcessKanbanReceipts(requestBody:ProcessKanbanReceipts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ProcessKanbanReceipts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ProcessKanbanReceipts", {
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
         resolve(data as ProcessKanbanReceipts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method SetActionToSelSerNum
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: SetActionToSelSerNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/SetActionToSelSerNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetActionToSelSerNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_SetActionToSelSerNum(requestBody:SetActionToSelSerNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<SetActionToSelSerNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/SetActionToSelSerNum", {
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
         resolve(data as SetActionToSelSerNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method Submit
   Description: Submit the Kanban Receipt Process.
   OperationID: Submit
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/Submit_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Submit_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_Submit(requestBody:Submit_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<Submit_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/Submit", {
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
         resolve(data as Submit_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateNegQtyAction
   Description: Checks if the Selected Qty from PartBin will result into a negative Onhand Quantity and returns this value to UI
   OperationID: ValidateNegQtyAction
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateNegQtyAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateNegQtyAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateNegQtyAction(requestBody:ValidateNegQtyAction_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateNegQtyAction_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ValidateNegQtyAction", {
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
         resolve(data as ValidateNegQtyAction_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateLowerLevelLotTrackedParts
   Description: Validates if there are Lot Tracked Part Materials. If there are at least one, ttKanbanPartLotBin table
is filled with those records and returned to UI to prompt the user to select form which lot he wants to
get the Required Qty.
   OperationID: ValidateLowerLevelLotTrackedParts
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateLowerLevelLotTrackedParts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateLowerLevelLotTrackedParts_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateLowerLevelLotTrackedParts(requestBody:ValidateLowerLevelLotTrackedParts_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateLowerLevelLotTrackedParts_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ValidateLowerLevelLotTrackedParts", {
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
         resolve(data as ValidateLowerLevelLotTrackedParts_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSelectedSerNum
   Description: Gets parameters required for launching Select Serial Numbers
   OperationID: ValidateSelectedSerNum
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateSelectedSerNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateSelectedSerNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateSelectedSerNum(requestBody:ValidateSelectedSerNum_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateSelectedSerNum_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ValidateSelectedSerNum", {
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
         resolve(data as ValidateSelectedSerNum_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateSN
   Description: Validates that a single serial number manually entered is valid for this transaction
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ValidateSN", {
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
   Summary: Invoke method RestoreKanbanReceipt
   Description: This procedure will reset the KanbanRecetips fields related with process of Lot Tracked Mtl feature.
   OperationID: RestoreKanbanReceipt
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/RestoreKanbanReceipt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RestoreKanbanReceipt_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_RestoreKanbanReceipt(requestBody:RestoreKanbanReceipt_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<RestoreKanbanReceipt_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/RestoreKanbanReceipt", {
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
         resolve(data as RestoreKanbanReceipt_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method FindPart
   Description: Find Part
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/FindPart", {
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
   Description: GetPartFromRowID
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
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/GetPartFromRowID", {
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
   Summary: Invoke method ValidatePartMOM
   Description: This method validates status of the MOM before proceed to generate the Kanban Job
More validations can be added here.
   OperationID: ValidatePartMOM
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidatePartMOM_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePartMOM_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidatePartMOM(requestBody:ValidatePartMOM_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidatePartMOM_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ValidatePartMOM", {
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
         resolve(data as ValidatePartMOM_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method ValidateParts_Kit_NonStock_Phantom
   Description: This method validates NonStock Phantoms
   OperationID: ValidateParts_Kit_NonStock_Phantom
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/ValidateParts_Kit_NonStock_Phantom_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateParts_Kit_NonStock_Phantom_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_ValidateParts_Kit_NonStock_Phantom(requestBody:ValidateParts_Kit_NonStock_Phantom_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<ValidateParts_Kit_NonStock_Phantom_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/ValidateParts_Kit_NonStock_Phantom", {
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
         resolve(data as ValidateParts_Kit_NonStock_Phantom_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method GetAvailAutoTranDocTypes
   Description: Method to get available automatic tran doc types.
   OperationID: GetAvailAutoTranDocTypes
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailAutoTranDocTypes_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_GetAvailAutoTranDocTypes(epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<GetAvailAutoTranDocTypes_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/GetAvailAutoTranDocTypes", {
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
         resolve(data as GetAvailAutoTranDocTypes_output)
          })
      .catch((error) => {
          reject(error)
      })
   }))
}

   /**  
   Summary: Invoke method CalculateLotPartSelectedDecimalQuantities
   Description: Calculate the correct quantities with decimals when selecting quantity for a Lot Bin part.
   OperationID: CalculateLotPartSelectedDecimalQuantities
      @param epicorHeaders A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      @param requestBody Desc: Input parameters  => reference#/components/schemas/CalculateLotPartSelectedDecimalQuantities_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CalculateLotPartSelectedDecimalQuantities_output
      500 Desc: Internal server error. Server is unable to process the request.
   */  
export function post_CalculateLotPartSelectedDecimalQuantities(requestBody:CalculateLotPartSelectedDecimalQuantities_input, epicorHeaders?:Headers){

   var headers = configEpicorSchemas.epicorHeaders
   if(typeof epicorHeaders !== 'undefined'){
         headers = epicorHeaders
   }

   return (new Promise<CalculateLotPartSelectedDecimalQuantities_output>((resolve, reject) => {
      const request: RequestInfo = new Request(configEpicorSchemas.epicorURL + "Erp.BO.KanbanReceiptsSvc/CalculateLotPartSelectedDecimalQuantities", {
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
         resolve(data as CalculateLotPartSelectedDecimalQuantities_output)
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
      @param selectedConvQty
      @param proposedSelectedQtyForBin
      @param selectedQtyForMtl
      @param proposedSelectedQtyForMtl
      @param partNum
      @param lotNum
      @param warehouseCode
      @param binNum
   */  
export interface CalculateLotPartSelectedDecimalQuantities_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
      /**  The currently selected converted quantity  */  
   selectedConvQty:number,
      /**  The new quantity being selected from the bin  */  
   proposedSelectedQtyForBin:number,
      /**  The currently selected material quantity  */  
   selectedQtyForMtl:number,
      /**  The new quantity being selected for the material  */  
   proposedSelectedQtyForMtl:number,
      /**  The current row's part number  */  
   partNum:string,
      /**  The current row's lot number  */  
   lotNum:string,
      /**  The current row's warehouse code  */  
   warehouseCode:string,
      /**  The current row's bin number  */  
   binNum:string,
}

export interface CalculateLotPartSelectedDecimalQuantities_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
}
}

   /** Required : 
      @param ds
      @param selectedConvQty
      @param proposedSelectedQtyForBin
      @param selectedQtyForMtl
      @param proposedSelectedQtyForMtl
      @param partNum
      @param lotNum
      @param warehouseCode
      @param binNum
   */  
export interface CalculateLotPartSelectedQuantities_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
      /**  The currently selected converted quantity  */  
   selectedConvQty:number,
      /**  The new quantity being selected from the bin  */  
   proposedSelectedQtyForBin:number,
      /**  The currently selected material quantity  */  
   selectedQtyForMtl:number,
      /**  The new quantity being selected for the material  */  
   proposedSelectedQtyForMtl:number,
      /**  The current row's part number  */  
   partNum:string,
      /**  The current row's lot number  */  
   lotNum:string,
      /**  The current row's warehouse code  */  
   warehouseCode:string,
      /**  The current row's bin number  */  
   binNum:string,
}

export interface CalculateLotPartSelectedQuantities_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeBin_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
}

export interface ChangeBin_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   lValidBin:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeContractID_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
}

export interface ChangeContractID_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeEmployee_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
}

export interface ChangeEmployee_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   lValidEmployee:boolean,
}
}

   /** Required : 
      @param ds
      @param ipProposedIUM
   */  
export interface ChangeInventoryUM_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
      /**  The Proposed IUM  */  
   ipProposedIUM:string,
}

export interface ChangeInventoryUM_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeLotNum_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
}

export interface ChangeLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   lValidLot:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeNonConfReason_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
}

export interface ChangeNonConfReason_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   lValidNonConfReason:boolean,
}
}

   /** Required : 
      @param ds
      @param uomCode
   */  
export interface ChangePart_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
      /**  UOM Code (only used for Product Codes)  */  
   uomCode:string,
}

export interface ChangePart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   lValidPart:boolean,
}
}

   /** Required : 
      @param ds
      @param proposedBinNum
   */  
export interface ChangeProposedBinNum_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
   proposedBinNum:string,
}

export interface ChangeProposedBinNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   lValidLot:boolean,
}
}

   /** Required : 
      @param ds
      @param proposedLotNum
   */  
export interface ChangeProposedLotNum_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
   proposedLotNum:string,
}

export interface ChangeProposedLotNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   lValidLot:boolean,
}
}

   /** Required : 
      @param ds
      @param uomCode
      @param proposedPartNum
   */  
export interface ChangeProposedPart_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
   uomCode:string,
   proposedPartNum:string,
}

export interface ChangeProposedPart_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   lValidPart:boolean,
}
}

   /** Required : 
      @param ds
      @param proposedWhseCode
   */  
export interface ChangeProposedWarehosue_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
   proposedWhseCode:string,
}

export interface ChangeProposedWarehosue_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   lValidPart:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeRevision_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
}

export interface ChangeRevision_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeScrapReason_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
}

export interface ChangeScrapReason_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   lValidScrapReason:boolean,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeUsePartNumForLot_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
}

export interface ChangeUsePartNumForLot_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
}
}

   /** Required : 
      @param ds
   */  
export interface ChangeWarehouse_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
}

export interface ChangeWarehouse_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   lValidWarehouse:boolean,
}
}

   /** Required : 
      @param ip_partnum
   */  
export interface CheckProcessRunning_input{
      /**  The required PartNum to run the Kanban Receipt.  */  
   ip_partnum:string,
}

export interface CheckProcessRunning_output{
parameters : {
      /**  output parameters  */  
   oMsgText:string,
}
}

   /** Required : 
      @param ipPartNum
      @param ipFromUOM
      @param ipFromQty
      @param ipToUOM
      @param doRounding
   */  
export interface ConvertUOM_input{
      /**  The Unit of Measure of LotPartBin.  */  
   ipPartNum:string,
      /**  The Unit of Measure of LotPartBin.  */  
   ipFromUOM:string,
      /**  SelectedQty from LotPartBin.  */  
   ipFromQty:number,
      /**  The Unit of Measure of LotPartMtl.  */  
   ipToUOM:string,
      /**  Is set to false if rounding is not needed.  */  
   doRounding:boolean,
}

export interface ConvertUOM_output{
parameters : {
      /**  output parameters  */  
   opNewQty:number,
}
}

   /** Required : 
      @param ds
   */  
export interface DoesMtlsMatch_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
}

export interface DoesMtlsMatch_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   cMessageText:string,
}
}

export interface Erp_Tablesets_KanbanReceiptsRow{
   Company:string,
   EmployeeID:string,
   PartNum:string,
   RevisionNum:string,
   LotNum:string,
   Quantity:number,
   JobDate:string,
   ScrapQuantity:number,
   ScrapReason:string,
   NonConfQuantity:number,
   NonConfReason:string,
   DimCode:string,
   WarehouseCode:string,
   BinNum:string,
   CanReportScrapQty:boolean,
   CanReportNCQty:boolean,
   EmployeeName:string,
   PartDescription:string,
   ScrapReasonDesc:string,
   NonConfReasonDesc:string,
   TrackLots:boolean,
   TrackDimension:boolean,
   TrackSerialNum:boolean,
   JobFirm:boolean,
   JobEngineered:boolean,
   JobReleased:boolean,
   WarehouseDescription:string,
   BinDescription:string,
   LegalNumber:string,
   JobNum:string,
   SerialNoTempTranID:number,
   LotNumDescription:string,
      /**  Indicates if the job number should be used for the lot number  */  
   UseJobNumForLot:boolean,
   AltMethod:string,
      /**  Flag to be set to enable/disable a Revision's Alternate Method  */  
   DisableAltMethod:boolean,
   DimCodeDescription:string,
   InventoryUM:string,
      /**  Display only version of InventoryUM  */  
   InventoryUMDisp:string,
      /**  This field is used in BO program KanBan Receipts to validate issues regarding the serial numbers.  */  
   ValidateOK:boolean,
      /**  For serial processing, the number of serial numbers required for the KanbanReceipts.Quantity based on the Part.IUM.  */  
   SNQuantity:number,
   TotalReqQty:number,
   PartNumDisp:string,
   JobAlreadyCreated:boolean,
   BaseUOM:string,
   TranDocTypeID:string,
      /**  The identifier of the planning contract.  */  
   ContractID:string,
      /**  Legal number transaction document type used for backflushed components (StockWIP)  */  
   TranDocTypeIDStockWIP:string,
      /**  Legal number used for Non-Conformance  */  
   LegalNumberNonConf:string,
      /**  Transaction document type used for Non conformance  */  
   TranDocTypeIDNonConf:string,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_KanbanReceiptsTableset{
   KanbanReceipts:Erp_Tablesets_KanbanReceiptsRow[],
   LegalNumGenOpts:Erp_Tablesets_LegalNumGenOptsRow[],
   LotPartBin:Erp_Tablesets_LotPartBinRow[],
   LotPartMtl:Erp_Tablesets_LotPartMtlRow[],
   PartLotAttributes:Erp_Tablesets_PartLotAttributesRow[],
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

export interface Erp_Tablesets_LotPartBinRow{
   Company:string,
   PartNum:string,
   LotNum:string,
   BinNum:string,
   OnhandQty:number,
   SelectedQty:number,
   IsEnabled:boolean,
   WarehouseCode:string,
   InventoryUOM:string,
   ParentMtlSeq:number,
      /**  Group by criteria stored in one field (WH + Bin)  */  
   GrpWrhBin:string,
      /**  Selected Qty UOM  */  
   SelectedUOM:string,
      /**  Selected Qty converted to InventoryUOM  */  
   SelectedConvQty:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_LotPartMtlRow{
   PartNum:string,
   Company:string,
      /**  Mtl Part Num configured in Enginering Workbench  */  
   MtlPartNum:string,
   RequiredQty:number,
   QtyPer:number,
   TotSelectedQty:number,
   FixedQty:boolean,
   ScrapQty:number,
   ScrapType:string,
   UOMCode:string,
   LotTracked:boolean,
   MtlSeq:number,
   SysRowID:string,
      /**  RowMod  */  
   RowMod:string,
}

export interface Erp_Tablesets_PartLotAttributesRow{
   Company:string,
   PartNum:string,
   Batch:string,
   MfgBatch:string,
   MfgLot:string,
   HeatNum:string,
   FirmWare:string,
   BestBeforeDt:string,
   CureDt:string,
   ExpirationDate:string,
   ShipDocAvail:boolean,
   PartLotDescription:string,
   MfgDt:string,
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

export interface GetAvailAutoTranDocTypes_output{
parameters : {
      /**  output parameters  */  
   AvailTypes:string,
}
}

   /** Required : 
      @param rowType
      @param vSysRowID
   */  
export interface GetPartFromRowID_input{
   rowType:string,
   vSysRowID:string,
}

export interface GetPartFromRowID_output{
parameters : {
      /**  output parameters  */  
   partNum:string,
   xrUomCode:string,
}
}

   /** Required : 
      @param partNum
      @param SysRowID
      @param rowType
      @param uomCode
   */  
export interface GetPartXRefInfo_input{
      /**  Proposed PartNumber change  */  
   partNum:string,
      /**  RowID of the selected record. Skips find part logic if this has a value.  */  
   SysRowID:string,
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
      @param ds
   */  
export interface GetSelectSerialNumbersParams_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
}

export interface GetSelectSerialNumbersParams_output{
   returnObj:Erp_Tablesets_SelectSerialNumbersParamsTableset[],
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
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

export interface KanbanReceiptsGetNew_output{
   returnObj:Erp_Tablesets_KanbanReceiptsTableset[],
}

   /** Required : 
      @param ds
   */  
export interface PreProcessKanbanReceipts_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
}

export interface PreProcessKanbanReceipts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   promptWIPStock:boolean,
   promptNonConf:boolean,
}
}

   /** Required : 
      @param ds
      @param dSerialNoQty
   */  
export interface ProcessKanbanReceipts_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
      /**  The quantity of Serialized parts.  This value is returned by Serial # selector object.  */  
   dSerialNoQty:number,
}

export interface ProcessKanbanReceipts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   cMessageText:string,
}
}

   /** Required : 
      @param ds
   */  
export interface RestoreKanbanReceipt_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
}

export interface RestoreKanbanReceipt_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
}
}

   /** Required : 
      @param ds
      @param ipInventory
      @param ipScrapped
      @param ipNonconformance
   */  
export interface SetActionToSelSerNum_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
      /**  Is the quantity of serial numbers to inventory  */  
   ipInventory:number,
      /**  Is quantity of serial numbers to scrapped  */  
   ipScrapped:number,
      /**  Is the quantity of serial numbers nonconformance  */  
   ipNonconformance:number,
}

export interface SetActionToSelSerNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
}
}

   /** Required : 
      @param ds
      @param dSerialNoQty
   */  
export interface Submit_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
      /**  The quantity of Serialized parts.  This value is returned by Serial # selector object.  */  
   dSerialNoQty:number,
}

export interface Submit_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
}
}

   /** Required : 
      @param ds
      @param dSerialNoQty
   */  
export interface ValidateLowerLevelLotTrackedParts_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
      /**  The quantity of Serialized parts.  This value is returned by Serial # selector object.  */  
   dSerialNoQty:number,
}

export interface ValidateLowerLevelLotTrackedParts_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
   cMessageText:string,
   lLotTrackedMtlExist:boolean,
}
}

   /** Required : 
      @param ipPartNum
   */  
export interface ValidateNegQtyAction_input{
      /**  The quantity of Serialized parts.  This value is returned by Serial # selector object.  */  
   ipPartNum:string,
}

export interface ValidateNegQtyAction_output{
parameters : {
      /**  output parameters  */  
   opNegQtyAction:number,
}
}

   /** Required : 
      @param partNum
      @param revNum
      @param altMethod
   */  
export interface ValidatePartMOM_input{
      /**  Part Num to be Validated  */  
   partNum:string,
      /**  Revision Number  */  
   revNum:string,
      /**  Alternate Method  */  
   altMethod:string,
}

export interface ValidatePartMOM_output{
      /**  True if validation passes.  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   oMessage:string,
}
}

   /** Required : 
      @param partNum
   */  
export interface ValidateParts_Kit_NonStock_Phantom_input{
      /**  Part Num to be Validated  */  
   partNum:string,
}

export interface ValidateParts_Kit_NonStock_Phantom_output{
      /**  True if validation passes.  */  
   returnObj:boolean,
parameters : {
      /**  output parameters  */  
   oMessage:string,
}
}

   /** Required : 
      @param ds
      @param serialNumber
   */  
export interface ValidateSN_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
      /**  Serial number to validate.  */  
   serialNumber:string,
}

export interface ValidateSN_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
}
}

   /** Required : 
      @param ds
      @param ipInventory
      @param ipScrapped
      @param ipNonconf
   */  
export interface ValidateSelectedSerNum_input{
   ds:Erp_Tablesets_KanbanReceiptsTableset[],
      /**  Is the quantity of serial numbers to inventory  */  
   ipInventory:number,
      /**  Is quantity of serial numbers to scrapped  */  
   ipScrapped:number,
      /**  Is the quantity of serial numbers nonconformance  */  
   ipNonconf:number,
}

export interface ValidateSelectedSerNum_output{
parameters : {
      /**  output parameters  */  
   ds:Erp_Tablesets_KanbanReceiptsTableset,
}
}

